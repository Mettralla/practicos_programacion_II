from ..database import DatabaseConnection

class Customer:
    def __init__(self, **kwargs) -> None:
        self.customer_id = kwargs.get("customer_id")
        self.first_name = kwargs.get("first_name")
        self.last_name = kwargs.get("last_name")
        self.email = kwargs.get("email")
        self.phone = kwargs.get("phone")
        self.street = kwargs.get("street")
        self.city = kwargs.get("city")
        self.state = kwargs.get("state")
        self.zip_code = kwargs.get("zip_code")
    
    
    @classmethod
    def get_customer(cls, customer_id):
        query = "SELECT * FROM customers WHERE customer_id = %s"
        customer_data = DatabaseConnection.fetch_one("sales", query, (customer_id,))
        if customer_data is not None:
            return Customer(
                customer_id = customer_id,
                first_name = customer_data[1],
                last_name = customer_data[2],
                phone = customer_data[3],
                email = customer_data[4],
                street = customer_data[5],
                city = customer_data[6],
                state = customer_data[7],
                zip_code = customer_data[8]
            )
        else:
            return None
    
    @classmethod
    def get_customers(cls, state = None) -> list:
        query = "SELECT * FROM customers WHERE state = %s" if state else "SELECT * FROM customers"
        
        params = (state,) if state else None

        customers = DatabaseConnection.fetch_all("sales", query, params)

        customers_list = []
        for customer in customers:
            customer_data = Customer(
                customer_id = customer[0],
                first_name = customer[1],
                last_name = customer[2],
                phone = customer[3],
                email = customer[4],
                street = customer[5],
                city = customer[6],
                state = customer[7],
                zip_code = customer[8]
            )
            customers_list.append(customer_data)
        
        return customers_list

    @classmethod
    def create_customer(cls, customer):
        query = "INSERT INTO customers (first_name, last_name, email, phone, street, city, state, zip_code) VALUES (%s, %s, %s, %s, %s, %s, %s, %s)"
        params = (customer.first_name, customer.last_name, customer.email, customer.phone, customer.street, customer.city, customer.state, customer.zip_code)
        DatabaseConnection.execute_query("sales", query, params)
    
    @classmethod
    def update_customer(cls, params):
        query = "UPDATE customers SET first_name = %s, last_name = %s, email = %s, phone = %s, street = %s, city = %s, state = %s, zip_code = %s WHERE customer_id = %s"
        DatabaseConnection.execute_query("sales", query, params)
    
    @classmethod
    def delete_customer(cls, customer_id):
        query = "DELETE FROM customers WHERE customer_id = %s"
        DatabaseConnection.execute_query("sales", query, (customer_id,))

    def serialize(self):
        return {
        "customer_id": self.customer_id,
        "first_name": self.first_name,
        "last_name": self.last_name,
        "email": self.email,
        "phone": self.phone,
        "street": self.street,
        "city": self.city,
        "state": self.state,
        "zip_code": self.zip_code
        }