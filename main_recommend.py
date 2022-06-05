import argparse
import logging
import os
from datetime import datetime
from os.path import *

from utils import read_data, setup_logging


def get_args():
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "--method",
        type=str,
        default="usercf",
        help="recommend use usercf",
        choices=["usercf", "itemcf"],
    )
    parser.add_argument(
        "--data_dir", type=str, default="./data/", help="data directory"
    )

    return parser.parse_args()



def main(args):
    logging.info(f"reading data")
    
    customer, date, order, product = read_data(args)
    
    logging.info(f"sample data")
    logging.info(f"customer: {customer.head()}\n {customer.tail()} \n {customer.shape}")
    logging.info(f"date: {date.head()}\n {date.tail()} \n {date.shape}")
    logging.info(f"order: {order.head()}\n {order.tail()} \n {order.shape}")
    logging.info(f"product: {product.head()}\n {product.tail()} \n {product.shape}")
    
    
    logging.info(f"start recommend using model {args.method}")
    
    
    
        
    
    


if __name__ == "__main__":
    args = get_args()
    start_time = datetime.now()
    args.log_folder = join(
        "logs", split(__file__)[1][:-3], start_time.strftime("%Y-%m-%d_%H-%M-%S-%f")
    )
    setup_logging(args.log_folder)
    logging.info(f"args: {args}")

    main()
