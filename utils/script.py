import json

from hiredigital_ecom.models.product import Products
from hiredigital_ecom.models.category import Categories
from hiredigital_ecom.models.user_profile import UserProfile
from hiredigital_ecom.models.products_viewed import ProductsViewed
from hiredigital_ecom.models.following import Following


def SaveDataDB():
    """
        Save Products Data in DB
    """
    with open("utils/products.json", 'r') as file:
        json_data = json.loads(file.read())

    for entry in json_data:
        product_payload = {}
        product_id = entry.get("productId")
        category_data, _ = Categories.objects.get_or_create(name=entry.get("productCategory"), user_profile_id=1, is_active=True)
        product_payload["product_id"] = product_id
        product_payload["user_profile_id"] = 1
        product_payload["name"] = entry.get("productName")
        product_payload["image"] = entry.get("productImage")
        product_payload["stock"] = entry.get("productStock")
        product_payload["unit_price"] = entry.get("productPrice")
        product_payload["sale_price"] = entry.get("salePrice")
        product_payload["is_active"] = True
        product_payload["category_id"] = category_data.id
        product_data, _ = Products.objects.get_or_create(product_id=product_id, defaults=product_payload, is_active=True)


def createUsers():
    """
        Create User, Product Viewed, Following in DB
    """
    with open("utils/names.json", 'r') as file:
        json_data = json.loads(file.read())

    for entry in json_data:
        user_profile_payload = dict()
        user_profile_payload["name"] = entry.get("name")
        user_profile_payload["id"] = entry.get("name")
        user_data, _ = UserProfile.objects.get_or_create(pk=entry.get("id"), defaults=user_profile_payload)
        product_viewed_data, _ = ProductsViewed.objects.get_or_create(user_profile_id=user_data.id,
                                                                     defaults={"user_profile_id": user_data.id})
        Following.objects.get_or_create(user_profile_id=user_data.id, defaults={"user_profile_id": user_data.id})


def addFollowing():
    """
        Add Following in Users
    """
    with open("utils/users.json", 'r') as file:
        json_data = json.loads(file.read())

    for entry in json_data:
        following_data, _ = Following.objects.get_or_create(user_profile_id=entry.get("id"),
                                                            defaults={"user_profile_id": entry.get("id")})
        following_data.following.add(*entry.get("following"))

