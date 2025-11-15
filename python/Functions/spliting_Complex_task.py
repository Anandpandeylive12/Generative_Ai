def fech_sales():
    sales_data = {
        'Monday': 150,
        'Tuesday': 200,
        'Wednesday': 250,
        'Thursday': 300,
        'Friday': 350
    }
    return sales_data
def calculate_total_sales(sales):
    total = sum(sales.values())
    return total

def sumarize_sales():
   print("Fetching sales data...")


def Generate_report():
    sales = fech_sales()
    total_sales = calculate_total_sales(sales)
    print("Total sales for the week:", total_sales)
    print("Calculating total sales...")
    sumarize_sales()
Generate_report()