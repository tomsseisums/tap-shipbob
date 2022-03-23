"""Stream type classes for tap-shipbob."""

from pathlib import Path
from typing import Any, Dict, Optional, Union, List, Iterable

from singer_sdk import typing as th  # JSON Schema typing helpers

from tap_shipbob.client import ShipBobStream

# TODO: Delete this is if not using json files for schema definition
SCHEMAS_DIR = Path(__file__).parent / Path("./schemas")
# TODO: - Override `UsersStream` and `GroupsStream` with your own stream definition.
#       - Copy-paste as many times as needed to create multiple stream types.


class UsersStream(ShipBobStream):
    """Define custom stream."""
    name = "users"
    path = "/users"
    primary_keys = ["id"]
    replication_key = None
    # Optionally, you may also use `schema_filepath` in place of `schema`:
    # schema_filepath = SCHEMAS_DIR / "users.json"
    schema = th.PropertiesList(
        th.Property("name", th.StringType),
        th.Property(
            "id",
            th.StringType,
            description="The user's system ID"
        ),
        th.Property(
            "age",
            th.IntegerType,
            description="The user's age in years"
        ),
        th.Property(
            "email",
            th.StringType,
            description="The user's email address"
        ),
        th.Property("street", th.StringType),
        th.Property("city", th.StringType),
        th.Property(
            "state",
            th.StringType,
            description="State name in ISO 3166-2 format"
        ),
        th.Property("zip", th.StringType),
    ).to_dict()


class GroupsStream(ShipBobStream):
    """Define custom stream."""
    name = "groups"
    path = "/groups"
    primary_keys = ["id"]
    replication_key = "modified"
    schema = th.PropertiesList(
        th.Property("name", th.StringType),
        th.Property("id", th.StringType),
        th.Property("modified", th.DateTimeType),
    ).to_dict()

class ProductsStream(ShipBobStream):
    name = "products"
    path = "/product"
    primary_keys = ["id"]

    schema = th.PropertiesList(


             "id", integer,
        "reference_id", string,
        "bundle_root_information": null,
        "created_date": "2022-03-21T14:02:19.96+00:00",
        "channel": {
            "id": 121525,
            "name": "ShipBob Default"
        },
        "sku": "QIA0y1cv",
        "name": "Medium - Naruto Cat Shirt",
        "barcode": null,
        "gtin": null,
        "upc": null,
        "unit_price": null,
        "total_fulfillable_quantity": 5,
        "total_onhand_quantity": 5,
        "total_committed_quantity": 0,
        "fulfillable_inventory_items": [
            {
                "id": 10667456,
                "name": "Medium - Naruto Cat Shirt",
                "quantity": 1
            }
        ],
        "fulfillable_quantity_by_fulfillment_center": [
            {
                "id": 1,
                "name": "Chicago-Old",
                "fulfillable_quantity": 5,
                "onhand_quantity": 5,
                "committed_quantity": 0
            }
        ]
    )