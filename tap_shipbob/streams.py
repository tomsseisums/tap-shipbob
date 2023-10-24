"""Stream type classes for tap-shipbob."""

from singer_sdk import typing as th

from tap_shipbob.client import ShipBobStream


class ProductsStream(ShipBobStream):
    name = "products"
    path = "/product"
    primary_keys = ["id"]

    schema = th.PropertiesList(
        th.Property("id", th.IntegerType),
        th.Property("reference_id", th.StringType),
        th.Property(
            "bundle_root_information",
            th.ObjectType(
                th.Property("id", th.IntegerType),
                th.Property("name", th.StringType),
            ),
        ),
        th.Property("created_date", th.DateTimeType),
        th.Property(
            "channel",
            th.ObjectType(
                th.Property("id", th.IntegerType),
                th.Property("name", th.StringType),
            ),
        ),
        th.Property("sku", th.StringType),
        th.Property("name", th.StringType),
        th.Property("barcode", th.StringType),
        th.Property("gtin", th.StringType),
        th.Property("upc", th.StringType),
        th.Property("unit_price", th.NumberType),
        th.Property("total_fulfillable_quantity", th.IntegerType),
        th.Property("total_onhand_quantity", th.IntegerType),
        th.Property("total_committed_quantity", th.IntegerType),
        th.Property(
            "fulfillable_inventory_items",
            th.ArrayType(
                th.ObjectType(
                    th.Property("id", th.IntegerType),
                    th.Property("name", th.StringType),
                    th.Property("quantity", th.IntegerType),
                )
            ),
        ),
        th.Property(
            "fulfillable_quantity_by_fulfillment_center",
            th.ArrayType(
                th.ObjectType(
                    th.Property("id", th.IntegerType),
                    th.Property("name", th.StringType),
                    th.Property("fulfillable_quantity", th.IntegerType),
                    th.Property("onhand_quantity", th.IntegerType),
                    th.Property("committed_quantity", th.IntegerType),
                )
            ),
        ),
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
        th.Property(
            "dimensions",
            th.ObjectType(
                th.Property("weight", th.NumberType),
                th.Property("length", th.NumberType),
                th.Property("width", th.NumberType),
                th.Property("depth", th.NumberType),
            ),
        ),
        th.Property("total_fulfillable_quantity", th.IntegerType),
        th.Property("total_onhand_quantity", th.IntegerType),
        th.Property("total_committed_quantity", th.IntegerType),
        th.Property("total_sellable_quantity", th.IntegerType),
        th.Property("total_awaiting_quantity", th.IntegerType),
        th.Property("total_exception_quantity", th.IntegerType),
        th.Property("total_internal_transfer_quantity", th.IntegerType),
        th.Property("total_backordered_quantity", th.IntegerType),
        th.Property("is_active", th.BooleanType),
        th.Property(
            "fulfillable_quantity_by_fulfillment_center",
            th.ArrayType(
                th.ObjectType(
                    th.Property("id", th.IntegerType),
                    th.Property("name", th.StringType),
                    th.Property("fulfillable_quantity", th.IntegerType),
                    th.Property("onhand_quantity", th.IntegerType),
                    th.Property("committed_quantity", th.IntegerType),
                    th.Property("awaiting_quantity", th.IntegerType),
                    th.Property("internal_transfer_quantity", th.IntegerType),
                )
            ),
        ),
        th.Property(
            "fulfillable_quantity_by_lot",
            th.ArrayType(
                th.ObjectType(
                    th.Property("lot_number", th.StringType),
                    th.Property("expiration_date", th.DateTimeType),
                    th.Property("fulfillable_quantity", th.IntegerType),
                    th.Property("onhand_quantity", th.IntegerType),
                    th.Property("committed_quantity", th.IntegerType),
                    th.Property("awaiting_quantity", th.IntegerType),
                    th.Property("internal_transfer_quantity", th.IntegerType),
                    th.Property(
                        "fulfillable_quantity_by_fulfillment_center",
                        th.ArrayType(
                            th.ObjectType(
                                th.Property("id", th.IntegerType),
                                th.Property("name", th.StringType),
                                th.Property("fulfillable_quantity", th.IntegerType),
                                th.Property("onhand_quantity", th.IntegerType),
                                th.Property("committed_quantity", th.IntegerType),
                                th.Property("awaiting_quantity", th.IntegerType),
                                th.Property(
                                    "internal_transfer_quantity", th.IntegerType
                                ),
                            )
                        ),
                    ),
                )
            ),
        ),
        th.Property("packaging_attribute", th.StringType),
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
        th.Property(
            "services",
            th.ArrayType(
                th.ObjectType(
                    th.Property("service_type", th.StringType),
                    th.Property("enabled", th.BooleanType),
                    th.Property(
                        "address",
                        th.ObjectType(
                            th.Property("name", th.StringType),
                            th.Property("address1", th.StringType),
                            th.Property("address2", th.StringType),
                            th.Property("city", th.StringType),
                            th.Property("state", th.StringType),
                            th.Property("country", th.StringType),
                            th.Property("zip_code", th.StringType),
                            th.Property("phone_number", th.StringType),
                            th.Property("email", th.StringType),
                        ),
                    ),
                )
            ),
        ),
        th.Property(
            "region",
            th.ObjectType(
                th.Property("id", th.IntegerType), th.Property("name", th.StringType)
            ),
        ),
        th.Property(
            "fulfillment_center_type",
            th.ObjectType(
                th.Property("id", th.IntegerType),
                th.Property("name", th.StringType),
            ),
        ),
        th.Property(
            "fulfillment_center_attributes",
            th.ArrayType(
                th.ObjectType(
                    th.Property("id", th.IntegerType),
                    th.Property("name", th.StringType),
                )
            ),
        ),
    ).to_dict()


class FullfillmentCentersStream(ShipBobStream):
    name = "fulfillment_centers"
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


class MultipleWarehouseReceivingOrdersStream(ShipBobStream):
    name = "multiple_warehouse_receiving_orders"
    path = "/receiving"
    primary_keys = ["id"]

    schema = th.PropertiesList(
        th.Property("id", th.IntegerType),
        th.Property("status", th.StringType),
        th.Property("package_type", th.StringType),
        th.Property("box_packaging_type", th.StringType),
        th.Property("expected_arrival_date", th.DateTimeType),
        th.Property("insert_date", th.DateTimeType),
        th.Property("last_updated_date", th.DateTimeType),
        th.Property("box_labels_uri", th.StringType),
        th.Property(
            "fulfillment_center",
            th.ObjectType(
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
            ),
        ),
        th.Property("purchase_order_number", th.StringType),
        th.Property(
            "inventory_quantities",
            th.ArrayType(
                th.ObjectType(
                    th.Property("inventory_id", th.IntegerType),
                    th.Property("sku", th.StringType),
                    th.Property("expected_quantity", th.IntegerType),
                    th.Property("received_quantity", th.IntegerType),
                )
            ),
        ),
    ).to_dict()


class OrdersStream(ShipBobStream):
    name = "orders"
    path = "/order"
    primary_keys = ["id"]
    replication_key = "updated_date"

    schema = th.PropertiesList(
        th.Property("id", th.IntegerType),
        th.Property("created_date", th.DateTimeType),
        th.Property("updated_date", th.DateTimeType),
        th.Property("purchase_date", th.DateTimeType),
        th.Property("reference_id", th.StringType),
        th.Property("order_number", th.StringType),
        th.Property("status", th.StringType),
        th.Property("type", th.StringType),
        th.Property(
            "channel",
            th.ObjectType(
                th.Property("id", th.IntegerType),
                th.Property("name", th.StringType),
            ),
        ),
        th.Property("shipping_method", th.StringType),
        th.Property(
            "recipient",
            th.ObjectType(
                th.Property("name", th.StringType),
                th.Property("email", th.StringType),
                th.Property("phone_number", th.StringType),
                th.Property(
                    "address",
                    th.ObjectType(
                        th.Property("type", th.StringType),
                        th.Property("address1", th.StringType),
                        th.Property("address2", th.StringType),
                        th.Property("company_name", th.StringType),
                        th.Property("city", th.StringType),
                        th.Property("state", th.StringType),
                        th.Property("country", th.StringType),
                        th.Property("zip_code", th.StringType),
                    ),
                ),
            ),
        ),
        th.Property(
            "products",
            th.ArrayType(
                th.ObjectType(
                    th.Property("id", th.IntegerType),
                    th.Property("reference_id", th.StringType),
                    th.Property("quantity", th.IntegerType),
                    th.Property("quantity_unit_of_measure_code", th.StringType),
                    th.Property("sku", th.StringType),
                    th.Property("gtin", th.StringType),
                    th.Property("upc", th.StringType),
                    th.Property("unit_price", th.NumberType),
                    th.Property("external_line_id", th.IntegerType),
                )
            ),
        ),
        th.Property(
            "tags",
            th.ArrayType(
                th.ObjectType(
                    th.Property("name", th.StringType),
                    th.Property("value", th.StringType),
                )
            ),
        ),
        th.Property(
            "shipments",
            th.ArrayType(
                th.ObjectType(
                    th.Property("store_order_id", th.StringType),
                    th.Property("id", th.IntegerType),
                    th.Property("order_id", th.IntegerType),
                    th.Property("reference_id", th.StringType),
                    th.Property(
                        "recipient",
                        th.ObjectType(
                            th.Property("name", th.StringType),
                            th.Property("email", th.StringType),
                            th.Property("phone_number", th.StringType),
                            th.Property(
                                "address",
                                th.ObjectType(
                                    th.Property("type", th.StringType),
                                    th.Property("address1", th.StringType),
                                    th.Property("address2", th.StringType),
                                    th.Property("company_name", th.StringType),
                                    th.Property("city", th.StringType),
                                    th.Property("state", th.StringType),
                                    th.Property("country", th.StringType),
                                    th.Property("zip_code", th.StringType),
                                ),
                            ),
                        ),
                    ),
                    th.Property("created_date", th.DateTimeType),
                    th.Property("last_update_at", th.DateTimeType),
                    th.Property("last_tracking_update_at", th.DateTimeType),
                    th.Property("status", th.StringType),
                    th.Property(
                        "status_details",
                        th.ArrayType(
                            th.ObjectType(
                                th.Property("name", th.StringType),
                                th.Property("description", th.StringType),
                                th.Property("id", th.IntegerType),
                                th.Property("inventory_id", th.IntegerType),
                                th.Property(
                                    "exception_fulfillment_center_id", th.IntegerType
                                ),
                            )
                        ),
                    ),
                    th.Property(
                        "location",
                        th.ObjectType(
                            th.Property("id", th.IntegerType),
                            th.Property("name", th.StringType),
                        ),
                    ),
                    th.Property("invoice_amount", th.NumberType),
                    th.Property("insurance_value", th.NumberType),
                    th.Property("ship_option", th.StringType),
                    th.Property("package_material_type", th.StringType),
                    th.Property(
                        "tracking",
                        th.ObjectType(
                            th.Property("carrier", th.StringType),
                            th.Property("tracking_number", th.StringType),
                            th.Property("carrier_service", th.StringType),
                            th.Property("tracking_url", th.StringType),
                            th.Property("bol", th.StringType),
                            th.Property("shipping_date", th.DateTimeType),
                            th.Property("pro_number", th.StringType),
                            th.Property("scac", th.StringType),
                        ),
                    ),
                    th.Property(
                        "products",
                        th.ArrayType(
                            th.ObjectType(
                                th.Property("id", th.IntegerType),
                                th.Property("reference_id", th.StringType),
                                th.Property("name", th.StringType),
                                th.Property("sku", th.StringType),
                                th.Property(
                                    "inventory_items",
                                    th.ArrayType(
                                        th.ObjectType(
                                            th.Property("id", th.IntegerType),
                                            th.Property("name", th.StringType),
                                            th.Property("quantity", th.IntegerType),
                                            th.Property(
                                                "quantity_committed", th.IntegerType
                                            ),
                                            th.Property("lot", th.StringType),
                                            th.Property(
                                                "expiration_date", th.DateTimeType
                                            ),
                                            th.Property(
                                                "serial_numbers",
                                                th.ArrayType(th.StringType),
                                            ),
                                            th.Property(
                                                "is_dangerous_goods", th.BooleanType
                                            ),
                                        )
                                    ),
                                ),
                            )
                        ),
                    ),
                    th.Property(
                        "parent_cartons",
                        th.ArrayType(
                            th.ObjectType(
                                th.Property("type", th.StringType),
                                th.Property("barcode", th.StringType),
                                th.Property(
                                    "measurements",
                                    th.ObjectType(
                                        th.Property("total_weight_oz", th.NumberType),
                                        th.Property("length_in", th.NumberType),
                                        th.Property("width_in", th.NumberType),
                                        th.Property("depth_in", th.NumberType),
                                    ),
                                ),
                                th.Property(
                                    "cartons",
                                    th.ArrayType(
                                        th.ObjectType(
                                            th.Property("id", th.IntegerType),
                                            th.Property("type", th.StringType),
                                            th.Property("barcode", th.StringType),
                                            th.Property(
                                                "measurements",
                                                th.ObjectType(
                                                    th.Property(
                                                        "total_weight_oz",
                                                        th.NumberType,
                                                    ),
                                                    th.Property(
                                                        "length_in", th.NumberType
                                                    ),
                                                    th.Property(
                                                        "width_in", th.NumberType
                                                    ),
                                                    th.Property(
                                                        "depth_in", th.NumberType
                                                    ),
                                                ),
                                            ),
                                        )
                                    ),
                                ),
                            )
                        ),
                    ),
                    th.Property(
                        "measurements",
                        th.ObjectType(
                            th.Property("total_weight_oz", th.NumberType),
                            th.Property("length_in", th.NumberType),
                            th.Property("width_in", th.NumberType),
                            th.Property("depth_in", th.NumberType),
                        ),
                    ),
                    th.Property("require_signature", th.BooleanType),
                    th.Property("estimated_fulfillment_date", th.DateTimeType),
                    th.Property("actual_fulfillment_date", th.DateTimeType),
                    th.Property("estimated_fulfillment_date_status", th.StringType),
                    th.Property("is_tracking_uploaded", th.BooleanType),
                    th.Property("gift_message", th.StringType),
                )
            ),
        ),
        th.Property("gift_message", th.StringType),
        th.Property(
            "shipping_terms",
            th.ObjectType(
                th.Property("carrier_type", th.StringType),
                th.Property("payment_term", th.StringType),
            ),
        ),
        th.Property(
            "retailer_program_data",
            th.ObjectType(
                th.Property("purchase_order_number", th.StringType),
                th.Property("retailer_program_type", th.StringType),
                th.Property("mark_for_store", th.StringType),
                th.Property("department", th.StringType),
                th.Property("delivery_date", th.DateTimeType),
                th.Property(
                    "addresses",
                    th.ArrayType(
                        th.ObjectType(
                            th.Property("type", th.StringType),
                            th.Property("address1", th.StringType),
                            th.Property("address2", th.StringType),
                            th.Property("company_name", th.StringType),
                            th.Property("city", th.StringType),
                            th.Property("state", th.StringType),
                            th.Property("country", th.StringType),
                            th.Property("zip_code", th.StringType),
                        ),
                    ),
                ),
                th.Property("customer_ticket_number", th.StringType),
            ),
        ),
    ).to_dict()
