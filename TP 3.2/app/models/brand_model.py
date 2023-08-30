from ..database import DatabaseConnection

class Brand:
    def __init__(self, **kwargs) -> None:
        self.brand_id = kwargs.get("brand_id")
        self.brand_name = kwargs.get("brand_name")
    
    @classmethod
    def get_brand(cls, brand_id):
        query = "SELECT * FROM brands WHERE brand_id = %s"
        brand_data = DatabaseConnection.fetch_one("production", query, (brand_id,))
        if brand_data:
            return Brand(
                brand_id = brand_data[0],
                brand_name = brand_data[1]
            )
        else:
            return None