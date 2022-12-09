"""ShipBob tap class."""

from typing import List

from singer_sdk import Stream, Tap
from singer_sdk import typing as th

from tap_shipbob.streams import (
    FullfillmentCentersStream,
    InventoryStream,
    LocationsStream,
    OrdersStream,
    ProductsStream,
)

STREAM_TYPES = [
    ProductsStream,
    InventoryStream,
    LocationsStream,
    FullfillmentCentersStream,
    OrdersStream,
]


class TapShipBob(Tap):
    """ShipBob tap class."""

    name = "tap-shipbob"

    config_jsonschema = th.PropertiesList(
        th.Property(
            "access_token",
            th.StringType,
            required=True,
            description="The token to authenticate against the API service",
        ),
        th.Property(
            "start_date",
            th.DateTimeType,
            description="The earliest record date to sync",
        ),
    ).to_dict()

    def discover_streams(self) -> List[Stream]:
        """Return a list of discovered streams."""
        return [stream_class(tap=self) for stream_class in STREAM_TYPES]


if __name__ == "__main__":
    TapShipBob.cli()
