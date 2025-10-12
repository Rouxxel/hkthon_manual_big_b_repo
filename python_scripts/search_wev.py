import weaviate
from weaviate.classes.init import Auth
import os, json

# Best practice: store your credentials in environment variables
weaviate_url = "8mf5bru6raov5pe7qbitw.c0.europe-west3.gcp.weaviate.cloud"
weaviate_api_key = "Q0ZSZmJTa0V3VDJ2YXZwNF8vZWRtRnhrcEw0bmhXV2pqdTE2d2N6QTJqZVBEM01qajBQUUZ5cEJudzVvPV92MjAw"


client = weaviate.connect_to_weaviate_cloud(
    cluster_url=weaviate_url,                                    # Replace with your Weaviate Cloud URL
    auth_credentials=Auth.api_key(weaviate_api_key),             # Replace with your Weaviate Cloud key
)

questions = client.collections.use("Inventory_products")

response = questions.query.near_text(
    query="motor",
    limit=2
)

for obj in response.objects:
    print(json.dumps(obj.properties, indent=2))

client.close()  # Free up resources