[![Codacy Badge](https://api.codacy.com/project/badge/Grade/e9e6dd2c31b048a7a88316b75c3a8063)](https://www.codacy.com/app/Dianawats/store-manager?utm_source=github.com&amp;utm_medium=referral&amp;utm_content=Dianawats/store-manager&amp;utm_campaign=Badge_Grade)
[![Build Status](https://travis-ci.org/Dianawats/store-manager.svg?branch=develop)](https://travis-ci.org/Dianawats/store-manager)
[![Coverage Status](https://coveralls.io/repos/github/Dianawats/store-manager/badge.svg?branch=develop)](https://coveralls.io/github/Dianawats/store-manager?branch=develop)
# store-manager

### Project Overview
Store Manager is a web application that helps store owners manage sales and product inventory
records. This application is meant for use in a single store..


### Prerequisites

##Built with;
- `Python3.6` - Programming language that lets you work more quickly
- `Flask` - Python based web framework
- `Virtualenv` - A tool to create isolated virtual environment

## Project links:

Here is my link to the UI final branch:
(git clone: https://github.com/Dianawats/store-manager)

### API Endpoints
```
- Admin can add a product
- Admin/store attendant can get all products
- Admin/store attendant can get a specific product
- Store attendant can add a sale order
- Admin can get all sale order records
```

###Use the following endpoints to perform the specified tasks
HTTP Method|End point | Public Access|Action
-----------|----------|--------------|------
POST | /api/v1/products | False | Create a product
GET | /api/v1/products | False | Fetch all available products
GET | /api/v1/products/<product_id> | False | Fetch a single product
POST | /api/v1/sales | False | Create a sale order
GET | /api/v1/sales/<sale_id> | False | Fetch a single sale record
GET | /api/v1/sales | False | Fetch all sale records created


## Author

* **Diana Nakiwala**

## Acknowledgments

* Andela Software Development Community
* Inspiration
* Bootcamp 13 team-mates

