import csv


def calculate_metrics(csv_filename, result_filename):
    # read from csv file
    with open(csv_filename, 'r') as file:
        reader = csv.reader(file)
        # Skip the header row
        header = next(reader)

        total_revenue = 0
        total_quantity = 0

        # Calculate total revenue and total quantity
        for row in reader:
            product_name, quantity, price = row
            quantity = int(quantity)
            price = float(price)
            total_revenue += quantity * price
            total_quantity += quantity

        average_price = total_revenue / total_quantity if total_quantity != 0 else 0

    # Save the results to a new CSV file
    with open(result_filename, 'w', newline='') as result_file:
        writer = csv.writer(result_file)

        # Write header
        writer.writerow(['Total Revenue', 'Average Price per Item'])

        # Write data
        writer.writerow([total_revenue, average_price])


if __name__ == "__main__":
    # Specify the input CSV file and the output result CSV file
    input_csv_filename = 'sales_data.csv'
    output_result_filename = 'result_metrics.csv'

    # Call the function to calculate metrics and save results
    calculate_metrics(input_csv_filename, output_result_filename)
