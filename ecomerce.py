import requests
import openai
import time
import streamlit as st


def get_all_products():
    shopify_url = "https://quickstart-91bd45a3.myshopify.com"
    api_version = "2021-07"
    endpoint = f"{shopify_url}/admin/api/{api_version}/products.json"

    # Replace with your API key and password
    api_key = "1a44f9ef89383f69054401a8d502305f"
    api_password = "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"

    # Make the request
    response = requests.get(endpoint, auth=(api_key, api_password))

    # Check if the request was successful (status code 200)
    if response.status_code == 200:
        product = response.json()["products"]
        return product
    else:
        print(f"Error: {response.status_code}, {response.text}")

 
def get_orders_detail():
    shopify_url = "https://quickstart-91bd45a3.myshopify.com"
    api_version = "2021-07"
    endpoint = f"{shopify_url}/admin/api/{api_version}/orders.json"

    # Replace with your API key and password
    api_key = "1a44f9ef89383f69054401a8d502305f"
    api_password = "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"

    # Make the request
    response = requests.get(endpoint, auth=(api_key, api_password))

    # Check if the request was successful (status code 200)
    if response.status_code == 200:
        order = response.json()["orders"]
        print(order)
        return order
    else:
        print(f"Error: {response.status_code}, {response.text}") 




def create_customer(First_name,Last_name,Email,Phone,Address1,City,Postal_Code):
# Replace with your actual values
    shopify_url = "https://your-shopify-store.myshopify.com"
    api_version = "2021-07"
    api_key = "1a44f9ef89383f69054401a8d502305f"
    api_password = "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"

# Customer data
    customer_data = {
        "customer": {
            "first_name": First_name,
            "last_name": Last_name,
            "email": Email,
            "phone": Phone,
            "addresses": [
                {
                    "address1": Address1,
                    "city": City,
                    "Postal_Code": Postal_Code,
                    "country": "PK"
                }
            ]
            
            # Add other necessary parameters
        }
    }

    # Create a customer
    customer_endpoint = f"{shopify_url}/admin/api/{api_version}/customers.json"
    customer_response = requests.post(customer_endpoint, json=customer_data, auth=(api_key, api_password))

    if customer_response.status_code == 201:
        print("Customer created successfully!")
    else:
        print(f"Error creating customer: {customer_response.status_code}, {customer_response.text}")
        # Handle error or exit
   
   
   
   
   
def get_customer():
# Replace with your actual values
    
    api_key = "1a44f9ef89383f69054401a8d502305f"
    api_password = "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"
    shopify_url = "https://quickstart-91bd45a3.myshopify.com"
    api_version = "2021-07"
    endpoint = f"{shopify_url}/admin/api/{api_version}/customers.json"

    response = requests.get(endpoint, auth=(api_key, api_password))

    if response.status_code == 200:
        customers = response.json()["customers"]
        print(customers)
        return customers
    else:
        print(f"Error: {response.status_code}, {response.text}")   




def place_order(Variant_id , Quantity , Price , Customer_id , Address1 , City  , Postal_Code , Email , Phone):
    api_key = "1a44f9ef89383f69054401a8d502305f"
    api_password = "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"
    shopify_url = "https://quickstart-91bd45a3.myshopify.com"
    api_version = "2021-07"
    endpoint = f"{shopify_url}/admin/api/{api_version}/orders.json"
    order_data = {
        "order": {
            "line_items": [
                {
                    "variant_id": Variant_id,  # Replace with the actual variant ID
                    "quantity": Quantity,
                    "price": Price
                }
            ],
            "customer": {
                "id": Customer_id,  # Replace with the actual customer ID
            },
            "addresses": [
                {
                    "address1": Address1,
                    "city": City,
                    "postal_code": Postal_Code,
                    "country": "PK"
                }
            ],
            "email": Email,
            "phone": Phone,
        }
    }

    # Make the POST request
    response = requests.post(endpoint, json=order_data, auth=(api_key, api_password))

    # Check the response
    if response.status_code == 201:
        print("Order created successfully")
    else:
        print(f"Error: {response.status_code}, {response.text}")



tools_list = [
    {
        "type": "function",
        "function": {
            "name": "get_orders_detail",
            "description": "Retrieve all orders",
            "parameters": {
                "type": "object",
                "properties": {},  # No parameters
            },
        }
    },
    {
        "type": "function",
        "function": {
            "name": "get_all_products",
            "description": "Retrieve all products",
            "parameters": {
                "type": "object",
                "properties": {},  # No parameters
            },
        }
    },
    {
        "type": "function",
        "function": {
            "name": "get_customer",
            "description": "Retrieve all customers",
            "parameters": {
                "type": "object",
                "properties": {},  # No parameters
            },
        }
    },
    {
    "type": "function",
    "function": {
        "name": "create_customer",
        "description": "Create a new customer. Ask for every parameter from the customer",
        "parameters": {
            "type": "object",
            "properties": {
                "First_name": {
                    "type": "string",
                    "description": "First name of the customer"
                },
                "Last_name": {
                    "type": "string",
                    "description": "Last name of the customer"
                },
                "Email": {
                    "type": "string",
                    "description": "Email of the customer. Note: Email should be valid. You have to validate it"
                },
                "Phone": {
                    "type": "number",
                    "description": "Phone number of the customer"
                },
                "Address1": {
                    "type": "string",
                    "description": "First address of the customer"
                },
                "City": {
                    "type": "string",
                    "description": "City of the customer"
                },
                "Postal_Code": {
                    "type": "string",
                    "description": "Postal Code for  address of the customer"
                }
            },
            "required": ["First_name", "Last_name", "Email", "Phone", "Address1", "City", "Postal_Code"]
        }
    }
},
    {
    "type": "function",
    "function": {
        "name": "place_order",
        "description": "Create a new order , ask every paramter from user",
        "parameters": {
            "type": "object",
            "properties": {
                "Variant_id": {  
                    "type": "string",
                    "description": "Id of the product which user wants to order."
                },
                "Quantity": {
                    "type": "number",
                    "description": "number of item user wants to order"
                },
                "Price": {
                    "type": "number",
                    "description": "Price of the product"
                },
                "Customer_id": {
                    "type": "string",
                    "description": "d of the customer"
                },
                "Email": {
                    "type": "string",
                    "description": "Email of the customer. Note: Email should be valid. You have to validate it"
                },
                "Phone": {
                    "type": "number",
                    "description": "Phone number of the customer"
                },
                "Address1": {
                    "type": "string",
                    "description": "First address of the customer"
                },
                "City": {
                    "type": "string",
                    "description": "City of the customer"
                },
                "Postal_Code": {
                    "type": "string",
                    "description": "Postal Code for  address of the customer"
                }
                
            },
            "required": ["Variant_id", "Quantity","Price","Customer_id", "Email", "Phone", "Address1", "City","Postal_Code"]
        }
    }
},
{"type": "code_interpreter"}
]
text = 'Please Wait .....'
st.title("Your Guide to Corporate Excellence")
user_input = st.text_input("Enter your prompt")
show = False
if st.button('Start'):
        show=True
        if show == True:
            st.text(text)
        else :
            st.text('')
            

# Initialize the client
client = openai.OpenAI(
    api_key='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'
)
assistant = client.beta.assistants.create(
    name="Personal Assistant",
    instructions="You are a personal asistant for my ecomerce website",
    tools=tools_list,
    model="gpt-3.5-turbo-1106",
)

# Step 2: Create a Thread
thread = client.beta.threads.create()    

# Step 3: Add a Message to a Thread
while show:
    message = client.beta.threads.messages.create(
    thread_id=thread.id,
    role="user",
    content=user_input
    )

# Step 4: Run the Assistant
    run = client.beta.threads.runs.create(
    thread_id=thread.id,
    assistant_id=assistant.id,
    instructions="Please address the user as abdul hadi."
    )

    print(run.model_dump_json(indent=4))

    while True:
    
    # Retrieve the run status
        run_status = client.beta.threads.runs.retrieve(
            thread_id=thread.id,
            run_id=run.id
        )
        print(run_status.model_dump_json(indent=4))

    # If run is completed, get messages
        if run_status.status == 'completed':
            messages = client.beta.threads.messages.list(
                thread_id=thread.id
            )
            show = False

        # Loop through messages and print content based on role
            for msg in messages.data:
                role = msg.role
                content = msg.content[0].text.value
                text=st.text(f"{content}")
                st.text(text)

            break
        elif run_status.status == 'requires_action':
            print("Function Calling")
            required_actions = run_status.required_action.submit_tool_outputs.model_dump()
            print(required_actions)
            tool_outputs = []
            import json
            for action in required_actions["tool_calls"]:
                func_name = action['function']['name']
                arguments = json.loads(action['function']['arguments'])
            
                if func_name == "get_orders_detail":
                    output = get_orders_detail()
                    output = str(output)
                    tool_outputs.append({
                        "tool_call_id":action['id'],
                        "output":output
                    })
                elif func_name == "get_all_products":
                    output = get_all_products()
                    output = str(output)
                    tool_outputs.append({
                        "tool_call_id":action['id'],
                        "output":output
                    })
                    
                elif func_name == "create_customer":
                    output = create_customer(
                        arguments['First_name'],
                        arguments['Last_name'],
                        arguments['Email'],
                        arguments['Phone'],
                        arguments['Address'],
                        arguments['City'],
                        arguments['Postal_Code']
                    )                    
                    output = str(output)
                    tool_outputs.append({
                        "tool_call_id":action['id'],
                        "output":output
                    })
                elif func_name == "place_order":
                    output = place_order(
                        arguments['Variant_id'],
                        arguments['Quantity'],
                        arguments['Price'],
                        arguments['Customer_id'],
                        arguments['Address1'],  # Corrected key to 'Address1'
                        arguments['City'],
                        arguments['Postal_Code'],
                        arguments['Email'],
                        arguments['Phone']
                    )                    
                    output = str(output)
                    tool_outputs.append({
                        "tool_call_id":action['id'],
                        "output":output
                    })
                    
                elif func_name == "get_customer":
                    output = get_customer()
                    output = str(output)
                    tool_outputs.append({
                        "tool_call_id":action['id'],
                        "output":output
                    })
                    
                    
                else:
                    raise ValueError(f"Unknown function: {func_name}")
            
            print("Submitting outputs back to the Assistant...")
            client.beta.threads.runs.submit_tool_outputs(
                thread_id=thread.id,
                run_id=run.id,
                tool_outputs=tool_outputs
            )
        else:
            print("Waiting for the Assistant to process...")
            time.sleep(2)