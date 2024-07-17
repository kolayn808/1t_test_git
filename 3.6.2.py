import random
from faker import Faker

from pyspark.sql import SparkSession
from pyspark.sql.functions import col, rand, round, when


spark = SparkSession.builder.appName("SyntheticPurchaseData").getOrCreate()

fake = Faker()

# Генерация случайных данных о покупках
def generate_purchase_data(num_rows):
    products = ['Laptop', 'Smartphone', 'Tablet', 'Headphones', 'Camera']

    data = []
    for _ in range(num_rows):
        date = fake.date_between(start_date='-1y', end_date='today')
        user_id = random.randint(1, 1000)
        product = random.choice(products)
        quantity = random.randint(1, 10)
        price = round(random.uniform(20.0, 1500.0), 2)
        data.append((date, user_id, product, quantity, price))
    return data


num_rows = 1000
purchase_data = generate_purchase_data(num_rows)

columns = ["Date", "UserID", "Product", "Quantity", "Price"]
purchase_df = spark.createDataFrame(purchase_data, columns)

output_path = "purchase_data.csv"
purchase_df.write.csv(output_path, header=True)


purchase_df.show(10)

spark.stop()