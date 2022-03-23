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


        th.Property("id", th.IntegerType),
        th.Property("reference_id", th.StringType),
        th.Property("bundle_root_information", th.CustomType({"type": ["null", "string"]})),
        th.Property("created_date", th.DateTimeType),
        th.Property("channel", th.ObjectType(
            th.Property("id", th.IntegerType),
            th.Property("name", th.StringType),
        )),
        th.Property("sku", th.StringType),
        th.Property("name", th.StringType),
        th.Property("barcode", th.CustomType({"type": ["null", "string"]})),
        th.Property("gtin", th.CustomType({"type": ["null", "string"]})),
        th.Property("upc", th.CustomType({"type": ["null", "string"]})),
        th.Property("unit_price", th.CustomType({"type": ["null", "string", "integer"]})),
        th.Property("total_fulfillable_quantity", th.IntegerType),
        th.Property("total_onhand_quantity", th.IntegerType),
        th.Property("total_committed_quantity", th.IntegerType),
        th.Property("fulfillable_inventory_items", th.ArrayType(
            th.ObjectType(
                th.Property("id", th.IntegerType),
                th.Property("name", th.StringType),
                th.Property("quantity", th.IntegerType),
            )
        )),
        th.Property("fulfillable_quantity_by_fulfillment_center", th.ArrayType(
            th.ObjectType(
                th.Property("id", th.IntegerType),
                th.Property("name", th.StringType),
                th.Property("fulfillable_quantity", th.IntegerType),
                th.Property("onhand_quantity", th.IntegerType),
                th.Property("committed_quantity", th.IntegerType),
            )
        ))
    ).to_dict()


class InventoryStream(ShipBobStream):
    name = "inventory"
    path = "/inventory"
    primary_keys = ["id"]

    schema = th.PropertiesList(
        
        th.Property("id", th.IntegerType),
        th.Property("name", th.StringType),
        th.Property("is_digital", th.BooleanType),
        th.Property("is_case_pick", th.BooleanType),
        th.Property("is_lot", th.BooleanType),
        th.Property("dimensions", th.ObjectType(
            th.Property("weight", th.IntegerType),
            th.Property("length", th.IntegerType),
            th.Property("width", th.IntegerType),
            th.Property("depth", th.IntegerType),
        )),
        th.Property("total_fulfillable_quantity", th.IntegerType),
        th.Property("total_onhand_quantity", th.IntegerType),
        th.Property("total_committed_quantity", th.IntegerType),
        th.Property("total_sellable_quantity", th.IntegerType),
        th.Property("total_awaiting_quantity", th.IntegerType),
        th.Property("total_exception_quantity", th.IntegerType),
        th.Property("total_internal_transfer_quantity", th.IntegerType),
        th.Property("total_backordered_quantity", th.IntegerType),
        th.Property("is_active", th.BooleanType),
        th.Property("fulfillable_quantity_by_fulfillment_center", th.ArrayType(
            th.ObjectType(
                th.Property("id", th.IntegerType),
                th.Property("name", th.StringType),
                th.Property("fulfillable_quantity", th.IntegerType),
                th.Property("onhand_quantity", th.IntegerType),
                th.Property("committed_quantity", th.IntegerType),
                th.Property("awaiting_quantity", th.IntegerType),
                th.Property("internal_transfer_quantity", th.IntegerType),
            )
        )),
        th.Property("fulfillable_quantity_by_lot", th.ArrayType(
            th.ObjectType(
                th.Property("lot_number", th.CustomType({"type": ["null", "string", "integer"]})),
                th.Property("expiration_date", th.CustomType({"type": ["null", "string", "integer"]})),
                th.Property("fulfillable_quantity", th.IntegerType),
                th.Property("onhand_quantity", th.IntegerType),
                th.Property("committed_quantity", th.IntegerType),
                th.Property("awaiting_quantity", th.IntegerType),
                th.Property("internal_transfer_quantity", th.IntegerType),
                th.Property("fulfillable_quantity_by_fulfillment_center", th.ArrayType(
                    th.ObjectType(
                        th.Property("id", th.IntegerType),
                        th.Property("name", th.StringType),
                        th.Property("fulfillable_quantity", th.IntegerType),
                        th.Property("onhand_quantity", th.IntegerType),
                        th.Property("committed_quantity", th.IntegerType),
                        th.Property("awaiting_quantity", th.IntegerType),
                        th.Property("internal_transfer_quantity", th.IntegerType),
                    )
                ))

            )
        )),
        th.Property("packaging_attribute",th.StringType)
    ).to_dict()


class LocationsStream(ShipBobStream):
    name = "locations"
    path = "/location"
    primary_keys = ["id"]

    schema = th.PropertiesList(
        th.Property("id", th.IntegerType),
        th.Property("name", th.StringType),
        th.Property("abbreviation", th.StringType),
        th.Property("timezone", th.StringType),
        th.Property("is_active", th.BooleanType),
        th.Property("is_receiving_enabled", th.BooleanType),
        th.Property("is_shipping_enabled", th.BooleanType),
        th.Property("access_granted", th.BooleanType),
        th.Property("attributes", th.ArrayType(th.StringType)),
        th.Property("services", th.ArrayType(
            th.CustomType({"type": ["null", "object"]})
        )),
        th.Property("region", th.ObjectType(
            th.Property("id", th.IntegerType),
            th.Property("name", th.StringType)
        ))
    ).to_dict()


class FullfillmentCentersStream(ShipBobStream):
    name = "fulfillmentCenters"
    path = "/fulfillmentCenter"
    primary_keys = ["id"]

    schema = th.PropertiesList(
         
        th.Property("id", th.IntegerType),
        th.Property("name", th.StringType),
        th.Property("timezone", th.StringType),
        th.Property("address1", th.StringType),
        th.Property("address2", th.StringType),
        th.Property("city", th.StringType),
        th.Property("state", th.StringType),
        th.Property("country", th.StringType),
        th.Property("zip_code", th.StringType),
        th.Property("phone_number", th.StringType),
        th.Property("email", th.StringType),
    
    ).to_dict()


class OrdersStream(ShipBobStream):
    name = "orders"
    path = "/order"
    primary_keys = ["id"]

    schema = th.PropertiesList(
        
        th.Property("id", th.IntegerType),
        th.Property("created_date", th.DateTimeType),
        th.Property("purchase_date", th.CustomType({"type": ["null", "datetime"]})),
        th.Property("reference_id", th.CustomType({"type": ["null", "string", "integer"]})),
        th.Property("order_number", th.CustomType({"type": ["null", "string", "integer"]})),
        th.Property("status", th.StringType),
        th.Property("type", th.StringType),
        th.Property("channel", th.ObjectType(
            th.Property("id", th.IntegerType),
            th.Property("name", th.StringType),
        )),
        th.Property("shipping_method", th.CustomType({"type": ["null", "string"]})),
        th.Property("recipient",  th.CustomType({"type": ["null", "object"]})),
        th.Property("products", th.ArrayType(th.StringType)),
        th.Property("tags", th.ArrayType(th.StringType)),
        th.Property("shipments", th.ArrayType(th.CustomType({"type": ["null", "object"]}))),
        th.Property("gift_message", th.CustomType({"type": ["null", "string"]})),
        th.Property("shipping_terms", th.ObjectType(
            th.Property("carrier_type", th.CustomType({"type": ["null", "string"]})),
            th.Property("payment_term", th.CustomType({"type": ["null", "string"]}))
        )),
        th.Property("retailer_program_data", th.CustomType({"type": ["null", "string"]}))
    ).to_dict()