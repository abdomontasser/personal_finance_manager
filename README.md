# Personal Finance Manager

A command-line application for managing personal finances, tracking expenses, and monitoring financial health.

## Features

### 👤 User Management

- Register new users with custom currency preferences
- Secure login system
- Multiple user support with isolated data

### 💰 Transaction Management

- Add income and expense transactions
- Categorize transactions
- Support multiple payment methods
- Custom date entry for transactions
- Transaction IDs for tracking

### 📊 Reports & Analytics

- **Dashboard Summary**
  - Total income
  - Total expenses
  - Current balance
- **Monthly Reports**
  - Filter transactions by month
  - View monthly spending patterns
- **Category Breakdown**
  - Expense totals by category
  - Spending pattern analysis
- **Financial Health Score (0-100)**
  - Savings Rate (40 points): % of income saved
  - Expense Stability (20 points): Monthly expense consistency
  - Income Stability (20 points): Monthly income consistency
  - Expense Diversity (20 points): Category distribution

### 🎯 Savings Goals

- Set target amounts
- Track progress towards goals
- Optional due dates
- Progress calculation based on savings

### 🔍 Search & Filter

- Filter transactions by:
  - Category
  - Date range
  - Amount range
- Sort transactions by amount (ascending/descending)

### 📥 Import/Export

- Import transactions from CSV files
- Export transactions to CSV
- Batch transaction processing
- Option to assign imported transactions to current user

## Installation

1. Clone the repository:

```bash
git clone https://github.com/abdomontasser/personal_finance_manager
cd personal_finance_manager
```

2. Ensure Python 3.x is installed
3. No additional dependencies required (uses standard library)

## Usage

### Starting the Application

```bash
python main.py
```

### User Management

1. **Register New User**

   ```
   Choose: 1
   Enter name: <username>
   Enter password: <password>
   Enter currency (default USD): <currency>
   ```

2. **Login**
   ```
   Choose: 2
   Username: <username>
   Password: <password>
   ```

### Transaction Management

1. **Add Transaction**

   ```
   Choose: 1
   Type (income/expense): <type>
   Amount: <amount>
   Category: <category>
   Description: <description>
   Payment method: <method>
   Date (YYYY-MM-DD): <date>
   ```

2. **View Transactions**
   - Lists all transactions chronologically
   - Shows date, type, category, amount, and description

### Reports

1. **Dashboard Summary**

   - View total income/expenses and balance

2. **Monthly Report**

   - Enter month (YYYY-MM)
   - View all transactions for that month

3. **Category Breakdown**

   - View expenses grouped by category
   - Total spent in each category

4. **Financial Health Score**
   - Overall score (0-100)
   - Detailed breakdown of scoring components

### Savings Goals

1. **Add Goal**

   ```
   Goal name: <name>
   Target amount: <amount>
   Due date (optional): <YYYY-MM-DD>
   ```

2. **View Goals**
   - List all goals with progress
   - Track savings against targets

### Search & Filter

1. **Category Filter**

   - Find transactions by category

2. **Date Range Filter**

   - Start date (YYYY-MM-DD)
   - End date (YYYY-MM-DD)

3. **Amount Range Filter**
   - Minimum amount
   - Maximum amount

### Import/Export

1. **Import CSV**

   - File must have headers:
     ```
     transaction_id,user_id,type,amount,category,date,description,payment_method
     ```
   - Option to assign to current user
   - Validates data before import

2. **Export CSV**
   - Export all transactions or filtered by user
   - Same format as import

## Data Storage

- User data: `Data/data.json`
- Transactions: `Data/transactions.csv`
- Automatic file creation on first run

## File Structure

- `main.py` - Application entry point
- `finance_manager.py` - Core business logic
- `User.py` - User management
- `Transaction.py` - Transaction handling
- `report_generator.py` - Reports and analytics
- `Search_filter.py` - Search functionality
- `users_data.py` - Data persistence

## Contributing

1. Fork the repository
2. Create feature branch
3. Commit changes
4. Push to branch
5. Create Pull Request

## License

MIT License

## Author

abdomontasser : https://github.com/abdomontasser
Elsayed-Elpna : https://github.com/Elsayed-Elpna

## Version

1.0.0
