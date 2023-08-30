from ..database import DatabaseConnection
from .brand_model import Brand
from .category_model import Category

class Product:
    def __init__(self, **kwargs) -> None:
        self.product_id = kwargs.get("product_id")
        self.product_name = kwargs.get("product_name")
        self.brand = kwargs.get("brand")
        self.category = kwargs.get("category")
        self.model_year = kwargs.get("model_year")
        self.list_price = kwargs.get("list_price")
        
    @classmethod
    def get_product(cls, product_id):
        query = "SELECT * FROM products WHERE product_id = %s"
        product_data = DatabaseConnection.fetch_one("production", query, (product_id,))
        if product_data is not None:
            return Product(
                product_id = product_id,
                product_name = product_data[1],
                brand = Brand.get_brand(product_data[2]),
                category = Category.get_category(product_data[3]), 
                model_year = product_data[4],
                list_price = product_data[5]
            )
        else:
            return None
    
    @classmethod
    def get_products(cls, brand_id = None, category_id = None) -> list:
        query = "SELECT * FROM products"
        conditions = []
        params = []

        if brand_id:
            conditions.append("brand_id = %s")
            params.append(brand_id)
        if category_id:
            conditions.append("category_id = %s")
            params.append(category_id)
        
        if conditions:
            query += " WHERE " + " AND ".join(conditions)
        
        products = DatabaseConnection.fetch_all("production", query, params)
        
        products_list = []
        for product in products:
            product_data = Product(
                product_id = product[0],
                product_name = product[1],
                brand = Brand.get_brand(product[2]),
                category = Category.get_category(product[3]),
                model_year = product[4],
                list_price = product[5]
            )
            products_list.append(product_data)
        
        return products_list
    
    @classmethod
    def create_product(cls, product):
        query = "INSERT INTO products (product_name, brand_id, category_id, model_year, list_price) VALUES (%s, %s, %s, %s, %s)"
        params = (product.product_name, product.brand, product.category, product.model_year, product.list_price)
        DatabaseConnection.execute_query("production", query, params)
    
    @classmethod
    def update_product(cls, params):
        query = "UPDATE products SET product_name = %s, brand_id = %s, category_id = %s, model_year = %s, list_price = %s WHERE product_id = %s"
        DatabaseConnection.execute_query("production", query, params)
    
    @classmethod
    def delete_product(cls, product_id):
        query = "DELETE FROM products WHERE product_id = %s"
        DatabaseConnection.execute_query("production", query, (product_id,))
    
    def serialize(self):
        return {
            "brand": { 
                "brand_id": self.brand.brand_id, 
                "brand_name": self.brand.brand_name 
            }, 
            "category": { 
                "category_id": self.category.category_id, 
                "category_name": self.category.category_name
            }, 
            "list_price": self.list_price, 
            "model_year": self.model_year, 
            "product_id": self.product_id, 
            "product_name": self.product_name
        }
