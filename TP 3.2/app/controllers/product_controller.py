from ..models.product_model import Product
from flask import request, jsonify

class ProductController:
    @classmethod
    def get_product(cls, product_id):
        product = Product.get_product(product_id)
        
        if product:
            return jsonify(product.serialize()), 200
        else:
            return jsonify({"message": "Product not found"}), 404
    
    @classmethod
    def get_products(cls) -> list:
        brand_id = request.args.get("brand_id", None) 
        category_id = request.args.get("category_id", None)
        products = Product.get_products(brand_id, category_id)
        response = {}
        
        if products:
            products_list = []
            for product in products:
                products_list.append(product.serialize())
            
            response["products"] = products_list
            response["total"] = len(products_list)
            return jsonify(response), 200
        else: 
            return jsonify(response), 200
        
    @classmethod
    def create_product(cls):
        try:
            product_data = request.json
            new_product = Product(
                product_name = product_data.get('product_name'), 
                brand = product_data.get('brand_id'), 
                category = product_data.get('category_id'), 
                model_year = product_data.get('model_year'), 
                list_price = product_data.get('list_price')
            )
            Product.create_product(new_product)
            return jsonify({'message': 'Product created successfully'}), 201
        except Exception as e:
            return jsonify({'error': str(e)}), 400
    
    @classmethod
    def update_product(cls, product_id):
        try:
            update_data = request.json
            og_product = Product.get_product(product_id)
            
            if og_product:
                Product.update_product((
                    update_data.get('product_name', og_product.product_name),
                    update_data.get('brand_id', og_product.brand.brand_id),
                    update_data.get('category_id', og_product.category.category_id),
                    update_data.get('model_year', og_product.model_year),
                    update_data.get('list_price', og_product.list_price),
                    product_id 
                ))
                return jsonify({'message': 'Product updated successfully'}), 200
        except Exception as e:
            return jsonify({'error': str(e)}), 400
    
    @classmethod
    def delete_product(cls, product_id):
        try: 
            Product.delete_product(product_id)
            return jsonify({'message': 'Product deleted successfully'}), 204
        except Exception as e:
            return jsonify({'error': str(e)}), 400