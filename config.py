
import os

class Config:
    def __init__(self):
        self.base_url_sever_product = os.getenv('URL_SEVER_PRODUCT', 'http://localhost:7777')
        self.base_url_orders = os.getenv('URL_ORDERS', 'http://localhost:8080/api')

        # Tạo các URL hoàn chỉnh
        self.URL_PRODUCT_GET = f"{self.base_url_sever_product}/product_get"
        self.URL_PRODUCT_GET_ID = f"{self.base_url_sever_product}/product_get_id"
        self.URL_PRODUCT_GET_LOAI = f"{self.base_url_sever_product}/product_get_loai"
        self.URL_PRODUCT_ALL_LOAI = f"{self.base_url_sever_product}/loai_rem"
        self.URL_PRODUCT_COMMENT = f"{self.base_url_sever_product}/comment"
        self.URL_PRODUCT_FIND = f"{self.base_url_sever_product}/find"
        self.URL_PRODUCT_ADD = f"{self.base_url_sever_product}/product_add"
        self.URL_PRODUCT_UPDATE = f"{self.base_url_sever_product}/product_update"
        self.URL_PRODUCT_DEL = f"{self.base_url_sever_product}/product_del"
        self.URL_PROMOTION_GET = f"{self.base_url_sever_product}/promotion_get"
        self.URL_PROMOTION_ADD = f"{self.base_url_sever_product}/promotion_add"
        self.URL_PROMOTION_GET_ID = f"{self.base_url_sever_product}/promotion_get_id"
        self.URL_PROMOTION_UPDATE = f"{self.base_url_sever_product}/promotion_update"
        self.URL_PROMOTION_DEL = f"{self.base_url_sever_product}/promotion_del"


        # Các URL khác với URL orders base khác
        self.URL_ORDERS_GET = f"{self.base_url_orders}/orders"
        self.URL_ORDERS_GET_ID = f"{self.base_url_orders}/orders/{{}}"
        self.URL_ORDERS_DETAIL_ORDER = f"{self.base_url_orders}/orders/{{}}/order/detail_order"
        self.URL_ORDERS_DETAIL_ORDER_ID = f"{self.base_url_orders}/orders/{{}}/order/detail_order/{{}}"
        self.URL_STATUS_GET = f"{self.base_url_orders}/status"
        self.URL_GET_SUM_ORDER = f"{self.base_url_orders}/orders/report/{{}}"