from ..database import DatabaseConnection

class Category:
    def __init__(self, **kwargs) -> None:
        self.category_id = kwargs.get("category_id")
        self.category_name = kwargs.get("category_name")
    
    @classmethod
    def get_category(cls, category_id):
        query = "SELECT * FROM categories WHERE category_id = %s"
        category_data = DatabaseConnection.fetch_one("production", query, (category_id,))
        if category_data:
            return Category(
                category_id = category_data[0],
                category_name = category_data[1]
            )
        else:
            return None