from numpy import product
import pandas as pd
from glob import glob
from os.path import join


def read_data(args):
    """读取数据

    Args:
        args (NameSpace): 命令行参数

    Returns:
        customer:pd.DataFrame 用户信息
        date:pd.DataFrame 日期信息
        order:pd.DataFrame 订单信息
        product:pd.DataFrame 商品信息
    """
    data_dir = args.data_dir
    customer = pd.read_csv(join(data_dir, "customer.csv"), encoding="gb2312")
    date = pd.read_csv(join(data_dir, "date.csv"), encoding="gb2312")
    order = pd.read_csv(join(data_dir, "order.csv"), encoding="gb2312")
    product = pd.read_csv(join(data_dir, "product.csv"), encoding="gb2312")

    return customer, date, order, product
