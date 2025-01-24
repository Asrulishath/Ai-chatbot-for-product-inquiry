from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from chatbot.models import Product, Supplier
import logging

# Initialize logging
logger = logging.getLogger(__name__)

class ChatbotResponse(APIView):
    def post(self, request):
        user_input = request.data.get("message", "").strip().lower()
        
        # Log the received user input
        logger.info(f"Received input: {user_input}")
        
        if not user_input:
            return Response({"error": "No input provided"}, status=400)

        # Predefined responses for greetings
        greetings = ["hi", "hello", "hey"]
        if user_input in greetings:
            response_text = "Hello! How can I assist you today?"
            logger.info(f"Responding with: {response_text}")
            return Response({"response": response_text})

        # Handle queries about products under a specific brand
        if "products under brand" in user_input:
            brand_name = user_input.replace("show me all products under brand", "").strip()
            products = Product.objects.filter(brand__iexact=brand_name)
            if products.exists():
                product_list = [f"{product.name} ({product.category}): {product.description}" for product in products]
                response_text = f"Here are all the products under the brand '{brand_name}':\n" + "\n".join(product_list)
            else:
                response_text = f"Sorry, no products found under the brand '{brand_name}'."

        # Handle queries about specific products
        elif "details of" in user_input or "about" in user_input or "tell me details of" in user_input:
            product_name = user_input.replace("give me details of", "").replace("tell me about", "").replace("tell me details of", "").strip()
            product = Product.objects.filter(name__icontains=product_name).first()
            if product:
                response_text = (f"Product Name: {product.name}, Price: ${product.price}, "
                                 f"Category: {product.category}, Description: {product.description}")
            else:
                response_text = f"Sorry, I couldn't find any details for '{product_name}'."

        # Handle supplier queries
        elif "supplier" in user_input or "provides" in user_input:
            if "which suppliers provide" in user_input or "which suppliers have" in user_input:
                category = user_input.replace("which suppliers provide", "").replace("which suppliers have", "").strip()
                suppliers = Supplier.objects.filter(product_categories_offered__icontains=category)
                if suppliers.exists():
                    supplier_list = [f"{supplier.name} (Address: {supplier.contact_info})" for supplier in suppliers]
                    response_text = f"The following suppliers provide {category}:\n" + "\n".join(supplier_list)
                else:
                    response_text = f"Sorry, I couldn't find any suppliers for '{category}'."
            else:
                product_name = user_input.replace("who supplies", "").replace("tell me the supplier of", "").replace("which company provides", "").strip()
                product = Product.objects.filter(name__icontains=product_name).first()
                if product:
                    suppliers = Supplier.objects.filter(product_categories_offered__icontains=product.category)
                    if suppliers.exists():
                        supplier_list = [f"{supplier.name} (Address: {supplier.contact_info})" for supplier in suppliers]
                        response_text = f"The supplier(s) for {product.name} are:\n" + "\n".join(supplier_list)
                    else:
                        response_text = f"Sorry, no suppliers found for {product.name}."
                else:
                    response_text = f"Sorry, I couldn't find any supplier details for '{product_name}'."

        # Handle "show me all products"
        elif "show me all products" in user_input or "list all products" in user_input or "show all products" in user_input or "all products" in user_input:
            products = Product.objects.all()
            if products.exists():
                product_list = [f"{product.name} ({product.category}): {product.description}" for product in products]
                response_text = "Here are all the available products:\n" + "\n".join(product_list)
            else:
                response_text = "Sorry, no products are available."

        # Handle category-specific queries like "list all laptops"
        elif "list all" in user_input or "show all" in user_input:
            category = user_input.replace("list all", "").replace("show all", "").strip()
            products = Product.objects.filter(category__icontains=category)
            if products.exists():
                product_list = [f"{product.name} (${product.price}): {product.description}" for product in products]
                response_text = f"Here are all the {category}s:\n" + "\n".join(product_list)
            else:
                response_text = f"Sorry, no {category}s are available."

        else:
            # Fallback for unrecognized queries
            response_text = "I'm sorry, I couldn't understand your query. Could you please rephrase?"
        goodbye = ["bye", "goodbye", "thank you", "thankyou bye","thank you bye bye"]
        if user_input in goodbye:
            response_text = "Thank you for using our chatbot! Have a great day!"
            logger.info(f"Responding with: {response_text}")
            return Response({"response": response_text})

            

            
        
    

        # Log and return the response
        logger.info(f"Responding with: {response_text}")
        return Response({"response": response_text})
