products = [
    {
        "id": 1,
        "name": "...",
        "price": 150
    },
    {
        "id": 2,
        "name": "...",
        "price": 350
    },
    {
        "id": 3,
        "name": "...",
        "price": 150
    },
]

carts = [
  {
    "product": {
        "id": 1,
        "name": "...",
        "price": 150
      },
     "quantity": 1
  },
  {
    "product": {
        "id": 2,
        "name": "...",
        "price": 350
      },
     "quantity": 1
  }
]

def add(id):
    product = [item for item in carts if item["product"]["id"] == id]
    
    if len(product) > 0:
        product[0]["quantity"] += 1
        return
    
    for product in products:
        if product['id'] == id:
            carts.append({
                "product": product,
                "quantity": 1
            })

def total():
    return sum([item["quantity"] * item["product"]["price"]  for item in carts ])

def total2():
    return sum(map(lambda item: item["quantity"] * item["product"]["price"], carts))
            
# add(2)
add(2)
print(total2())