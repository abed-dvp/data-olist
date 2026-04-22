from pathlib import Path
import pandas as pd


class Olist:
    """
    The Olist class provides methods to interact with Olist's e-commerce data.

    Methods:
        get_data():
            Loads and returns a dictionary where keys are dataset names (e.g., 'sellers', 'orders')
            and values are pandas DataFrames loaded from corresponding CSV files.

        ping():
            Prints "pong" to confirm the method is callable.
    """
    def get_data(self):
        """
        This function returns a Python dict.
        Its keys should be 'sellers', 'orders', 'order_items' etc...
        Its values should be pandas.DataFrames loaded from csv files
        """
        csv_path = Path("~/.lewagon/olist/data/csv").expanduser()
        csv_path
        file_paths = list(csv_path.iterdir())
        file_paths
        # Test your code below. We try to load the first csv in the directory
        import pandas as pd
        pd.read_csv(file_paths[0]).head()

        file_names = ['olist_customers_dataset.csv',
              'product_category_name_translation.csv',
              'olist_orders_dataset.csv',
              'olist_order_items_dataset.csv',
              'olist_geolocation_dataset.csv',
              'olist_order_reviews_dataset.csv',
              'olist_order_payments_dataset.csv',
              'olist_products_dataset.csv',
              'olist_sellers_dataset.csv']

        key_names=[]
        for names in file_names:
            key_names.append(names.replace('_dataset.csv','').replace('olist_','').replace('.csv',''))

        data = {}
        for key, path in zip(key_names, file_paths):
            data[key] = pd.read_csv(path)

        return data


    def ping(self):
        """
        You call ping I print pong.
        """
        print("pong")
