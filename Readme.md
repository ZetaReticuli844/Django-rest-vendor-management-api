# Vendor Management System with Performance Metrics

## Features

- **Vendor Profile Management**: Create, retrieve, update, and delete vendor profiles with details like name, contact information, address, and a unique vendor code.
- **Purchase Order Tracking**: Create, retrieve, update, and delete purchase orders, including details like PO number, vendor reference, order date, items, quantity, and status.
- **Vendor Performance Evaluation**: Calculate and retrieve performance metrics for vendors, including on-time delivery rate, quality rating, average response time, and fulfillment rate.
- **Historical Performance Data**: Store historical performance data for vendors, enabling trend analysis and tracking performance over time.
- **API Documentation with Swagger**: Access interactive API documentation through the `/swagger` endpoint.

## API Endpoints

### Vendor Endpoints

- `POST /api/vendors/`: Create a new vendor.
- `GET /api/vendors/`: List all vendors.
- `GET /api/vendors/{vendor_id}/`: Retrieve a specific vendor's details.
- `PUT /api/vendors/{vendor_id}/`: Update a vendor's details.
- `DELETE /api/vendors/{vendor_id}/`: Delete a vendor.
- `GET /api/performance/{vendor_id}/`: Retrieve a vendor's performance metrics.

### Purchase Order Endpoints

- `POST /api/purchase_orders/`: Create a purchase order.
- `GET /api/purchase_orders/`: List all purchase orders with an option to filter by vendor.
- `GET /api/purchase_orders/{po_id}/`: Retrieve details of a specific purchase order.
- `PUT /api/purchase_orders/{po_id}/`: Update a purchase order.
- `DELETE /api/purchase_orders/{po_id}/`: Delete a purchase order.


## Installation

1. Clone the repository:
    ```bash
    git clone https://github.com/ZetaReticuli844/Django-rest-vendor-management-api.git
    ```

2. Create a Python virtual environment:
    ```bash
    python3 -m venv myvenv
    ```
    ```bash
    source myvenv/bin/activate
    ```

3. Install the dependencies:
  
    ```bash
    pip install -r requirements.txt
    ```

4. Run the Django server:
    ```bash
    python manage.py runserver
    ```