# SmartDuka

## Overview
A digital inventory and order management system for small shops

## Features and Functionality
* User management: Register, Login and role-based permissions
* Order management: create and track customer orders
* Inventory management: monitor stock levels and product details
* Reporting and Analytics: sales reports, stock trends and perfomance insight

## Stack
* Language: Python(Django)
* Database: MySQL
* Authentication: JWT
* API docs: Postman collections

## Endpoints
### User Endpoints
1. Register User 

*POST*  /users/register

*Request body*

```json
{
  "username": "user2",
  "email": "user2@gmail.com.com",
  "password": "userpassword123"
}
```

*Response*
```json
{
    "message": "user registered succesfully"
}
```
2. Login User

*POST* /users/login

*Request Body*

```json
{
  "email": "johndoe@example.com",
  "password": "strongpassword123"
}
```

*Response:* JWT Token for authentication.

### Inventory Endpoints
1. Create a new product
POST /products/


*Request Body*

```json
{
  "category": 1,
  "name": "Coca Cola 500ml",
  "sku": "CC500",
  "price": 60.00,
  "stock_quantity": 100,
  "description": "Soft drink"
}
```

*Response(201):*
```json
{
  "id": 1,
  "category": 1,
  "name": "Coca Cola 500ml",
  "sku": "CC500",
  "price": "60.00",
  "stock_quantity": 100,
  "description": "Soft drink"
}
```

2. List products
GET /api/products/

*Response (200):*
```json
[
  {
    "id": 1,
    "category": 1,
    "name": "Coca Cola 500ml",
    "sku": "CC500",
    "price": "60.00",
    "stock_quantity": 100,
    "description": "Soft drink"
  }
]
```

### Orders Endpoints
1. Create Order
POST /orders/

Request Body (JSON):
```json
{
  "items": [
    {
      "product_id": 1,
      "quantity": 2
    },
    {
      "product_id": 3,
      "quantity": 1
    }
  ]
}
```

2. List Orders for a User

GET /api/orders/

Response (200 OK):

```json
[
  {
    "id": 5,
    "status": "pending",
    "total_amount": 3500.00,
    "created_at": "2025-08-29T17:20:33Z"
  },
  {
    "id": 6,
    "status": "shipped",
    "total_amount": 2000.00,
    "created_at": "2025-08-28T10:15:03Z"
  }
]
```


