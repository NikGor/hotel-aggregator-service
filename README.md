[![Github Actions Status](https://github.com/NikGor/hotel-aggregator-service/workflows/Python%20CI/badge.svg)](https://github.com/NikGor/hotel-aggregator-service/actions)

# 🏨 Hotel Aggregator Service

Manage hotels, create meta-hotels, and more with this Python-based API service.

## 📋 Description

The Hotel Aggregator Service is a versatile Python-based API for hotel management and aggregation. Whether you need to create hotels, merge multiple supplier hotels into a single meta-hotel, retrieve lists of meta-hotels and their associated hotels, reassign hotels, or track the history of hotel assignments, this service has you covered.

## 🔧 Features

- 🏢 Hotel Creation: Create supplier hotels.
- 🔄 Aggregation: Merge multiple hotels into meta-hotels.
- 🏨 Meta-Hotel Listing: Get lists of meta-hotels and their associated hotels.
- 🔄 Reassignment: Reassign hotels to different meta-hotels.
- 📅 History Tracking: Track the history of hotel assignments.

No authentication or authorization required.
[]()

## 🚀 Getting Started

1. Clone the repository.

```bash
git clone
```

2. Install the required dependencies.

```bash
make install
```

3. Configure the database settings. See the .env.example file for an example.

```bash
# Create a .env file
touch .env
```

4. Apply the database migrations.

```bash
make migrate
```

5. Run the tests.

```bash
make test
```

6. Start the service.

```bash
make start
```

7. Create a superuser to access the admin panel.

```bash
make superuser
```

8. Access the admin panel at http://localhost:8000/admin.
9. Access the API documentation at http://localhost:8000/docs.


## 🤖 Contributing

Contributions are welcome! Please follow our Contribution Guidelines.

## 📄 License

This project is licensed under the MIT License. See the LICENSE file for details.