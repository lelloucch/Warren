# **Setup Instructions for Warren SDK**  

## **Prerequisites**  
Before setting up the Warren SDK, ensure you have the following installed:  

- Python 3.8+  
- `pip` (Python package manager)  
- PostgreSQL (if using a database)  
- `virtualenv` (optional but recommended)  

## **1. Clone the Repository**  
```bash
git clone https://github.com/your-repo/warren-sdk.git
cd warren-sdk
```

## **2. Create a Virtual Environment**  
It is recommended to use a virtual environment to manage dependencies.  
```bash
python -m venv venv
source venv/bin/activate  # On Windows use `venv\Scripts\activate`
```

## **3. Install Dependencies**  
```bash
pip install -r requirements.txt
```

## **4. Set Up Environment Variables**  
Create a `.env` file in the project root directory and add the required configurations:  
```ini
# Blockchain Wallet Keys
EVM_PRIVATE_KEY=your-evm-private-key
SOLANA_PRIVATE_KEY=your-solana-private-key

# API Keys
FLEXLEND_API_KEY=your-flexlend-api-key

# Database Config (Optional)
DATABASE_URL=postgresql://user:password@localhost:5432/warren
```

## **5. Run Database Migrations (If Applicable)**  
```bash
alembic upgrade head  # If using Alembic for database migrations
```

## **6. Running the Project**  
To start the SDK, run:  
```bash
python main.py
```

## **7. Running Tests**  
To execute the test suite:  
```bash
pytest
```

## **8. Linting & Formatting**  
Ensure code quality with:  
```bash
flake8  # For linting
black .  # For formatting
```

## **9. API Documentation**  
If applicable, generate API docs using:  
```bash
mkdocs serve  # If using MkDocs
```

## **10. Deploying the Project**  
If deploying the SDK as a package or service:  
```bash
# Example: Building a Python package
python setup.py sdist bdist_wheel
twine upload dist/*
```
