"""REST client handling, including ShipBobStream base class."""

from typing import Any, Dict, Optional

from memoization import cached
import requests
from singer_sdk.authenticators import BearerTokenAuthenticator
from singer_sdk.streams import RESTStream
from pendulum import parse

class ShipBobStream(RESTStream):
    """ShipBob stream class."""

    url_base = "https://api.shipbob.com/1.0"

    records_jsonpath = "$[*]"
    _page_size = 250

    @cached
    def get_starting_time(self, context):
        start_date = parse(self.config.get("start_date"))
        rep_key = self.get_starting_timestamp(context)
        return rep_key or start_date

    @property
    def authenticator(self) -> BearerTokenAuthenticator:
        """Return a new authenticator object."""
        return BearerTokenAuthenticator.create_for_stream(
            self, token=self.config.get("access_token")
        )

    @property
    def http_headers(self) -> dict:
        """Return the http headers needed."""
        headers = {}
        if "user_agent" in self.config:
            headers["User-Agent"] = self.config.get("user_agent")
        return headers

    def get_next_page_token(
        self, response: requests.Response, previous_token: Optional[Any]
    ) -> Optional[Any]:
        """Return a token for identifying next page or None if no more pages."""
        total_pages = response.headers.get("total-pages")
        if not total_pages:
            return None
        page_number = int(response.headers["page-number"])
        next_page_token = page_number + 1
        if next_page_token > int(total_pages):
            return None
        return next_page_token

    def get_url_params(
        self, context: Optional[dict], next_page_token: Optional[Any]
    ) -> Dict[str, Any]:
        """Return a dictionary of values to be used in URL parameterization."""
        params: dict = {}
        params["Limit"] = self._page_size
        if next_page_token:
            params["Page"] = next_page_token
        if self.replication_key:
            start_date = self.get_starting_time(context)
            params["LastUpdateStartDate"] = start_date.isoformat()
        return params

    def post_process(self, row: dict, context: Optional[dict]) -> dict:
        """As needed, append or transform raw data to match expected structure."""
        updated_date = row["created_date"]
        shipments = row["shipments"]
        if shipments:
            shipment_dates = [parse(d["last_update_at"]) for d in shipments if d.get("last_update_at")]
            if not shipment_dates:
                shipment_dates = [parse(d["created_date"]) for d in shipments if d.get("created_date")]
            updated_date = max(shipment_dates).isoformat()
        row["updated_date"] = updated_date
        return row
