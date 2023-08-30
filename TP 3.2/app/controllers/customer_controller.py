from ..models.customer_model import Customer
from flask import request, jsonify

class CustomerController:
    @classmethod
    def get_customer(cls, customer_id):
        customer = Customer.get_customer(customer_id)

        if customer:
            return jsonify(customer.serialize()), 200
        else:
            return jsonify({"message": "Customer not found"}), 404
    
    @classmethod
    def get_customers(cls):
        state = request.args.get('state')
        customers = Customer.get_customers(state)
        response = {}

        if customers:
            customers_list = []
            for customer in customers:
                customers_list.append(customer.serialize())

            response["customers"] = customers_list
            response["total"] = len(customers_list)
            return jsonify(response), 200
        else: 
            return jsonify(response), 200
    
    @classmethod
    def create_customer(cls):
        try:
            customer_data = request.json
            new_customer = Customer(
                first_name = customer_data.get('first_name'),
                last_name = customer_data.get('last_name'),
                email = customer_data.get('email'),
                phone = customer_data.get('phone'),
                street = customer_data.get('street'),
                city = customer_data.get('city'),
                state = customer_data.get('state'),
                zip_code = customer_data.get('zip_code')
            )
            Customer.create_customer(new_customer)
            return jsonify({'message': 'Customer created successfully'}), 201
        except Exception as e:
            return jsonify({'error': str(e)}), 400
    
    @classmethod
    def update_customer(cls, customer_id):
        try:
            update_data = request.json
            og_customer = Customer.get_customer(customer_id)

            if og_customer:
                Customer.update_customer((
                    update_data.get('first_name', og_customer.first_name),
                    update_data.get('last_name', og_customer.last_name),
                    update_data.get('email', og_customer.email),
                    update_data.get('phone', og_customer.phone),
                    update_data.get('street', og_customer.street),
                    update_data.get('city', og_customer.city),
                    update_data.get('state', og_customer.state),
                    update_data.get('zip_code', og_customer.zip_code),
                    customer_id
                ))
                return jsonify({'message': 'Customer updated successfully'}), 200
        except Exception as e:
            return jsonify({'error': str(e)}), 400
    
    @classmethod
    def delete_customer(cls, customer_id):
        try:
            Customer.delete_customer(customer_id)
            return jsonify({'message': 'Customer deleted successfully'}), 204
        except Exception as e:
            return jsonify({'error': str(e)}), 400

