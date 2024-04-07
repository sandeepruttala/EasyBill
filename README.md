
# EasyBill: A Cost-Efficient Restaurant Management System

## Quick Start

- [Getting Started](#getting-started)

## Introduction

EasyBill is a comprehensive restaurant management system designed for efficient operation within dining establishments. Built with a Django backend and an HTML frontend, EasyBill facilitates a streamlined workflow for restaurant staff and administrators. It supports a local Wi-Fi network hosting solution, making it a cost-efficient choice for restaurants of all sizes.

### Features

- **User Role Management**: Distinct roles with tailored permissions for Admins and Staff.
- **Admin Features**:
  - Register and manage staff accounts.
  - Modify restaurant tables and menu items.
  - Overview of staff login status.
  - Full access to functionalities available to staff.
- **Staff Features**:
  - Manage orders and table service.
  - Access to view the menu.

## Getting Started

### Prerequisites

- Git
- Python 3.9 or later
- Other dependencies listed in `requirements.txt`

### Installation (Same for Windows, macOS, and Linux)

(Note: use `python3` and `pip3` if `python` and `pip` commands do not work)

1. Clone the repository:
   ```
   git clone https://github.com/sandeepruttala/EasyBill.git
   ```
2. Navigate to the project directory:
   ```
   cd easybill
   ```
3. Install the required dependencies:
   ```
   pip install -r requirements.txt
   ```
4. Initialize the database:
   ```
   python manage.py migrate
   ```
5. Create an admin account:
   ```
   python manage.py createsuperuser
   ```
6. Run the server:
   ```
   python manage.py runserver (for testing)
   ```
   ```
   python manage.py runserver 0.0.0.0:8000 (for local network hosting)
   ```

7. Access the admin panel at:
   ```
   `http://localhost:8000/` and log in with the admin credentials created in step 5.
   ```

## Usage

- Access the admin panel at `http://localhost:8000/admin` to start managing your restaurant.

- If you hosted the server on a local network, other devices can access the admin panel at `http://<your-ip-address>:8000/admin`.

- How to Find Your IP Address:
  - On Windows: Open Command Prompt and run `ipconfig` and find the IPv4 Address.
  - On macOS: Open Terminal and run `ipconfig getifaddr en0`.
  - Example Usage:
   if your IP address is `192.168.1.3`, other devices can access the admin panel at `http://192.168.1.3:8000/`


- As the project contains a streamlined set of features, everyone can understand the UI and functionalities easily.

- As an admin, you can add staff members, modify the menu, and check the status of your staff.

- Staff can log in to manage orders and view the menu, ensuring a smooth and efficient service for your customers.

## Demo

Will be updated soon.


## Contributing

We welcome contributions to EasyBill! If you have suggestions for improvements or bug fixes, please feel free to fork the repository and submit a pull request.

### Features that need to be implemented:
- **Permanent Record of Orders**: Currently, orders are only temporarily stored in the database. Implement a feature to store orders permanently.

- **Session Management**: Implement a feature to manage sessions for staff members so that after a certain period of inactivity, the staff member is automatically logged out.

## License

[MIT License](LICENSE.md)

## Contact
For any questions or comments about EasyBill, please 

mail to `itssandeepruttala@gmail.com`

### Feedback and Issues: 
We highly value your feedback and contributions to making EasyBill even better. If you encounter any issues or would like to suggest enhancements, please report them through our GitHub Issues page. This helps us track and address your concerns more efficiently. To report an issue, visit EasyBill Issues and click on the "New Issue" button. Please provide as much detail as possible to help us understand the context and address the issue promptly.

Your insights and feedback play a crucial role in improving EasyBill and ensuring it meets the needs of its users. Thank you for your support and contributions!

