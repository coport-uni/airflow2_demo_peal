from datetime import datetime

from airflow import DAG
from airflow.decorators import task
from airflow.models.baseoperator import chain
from airflow.operators.bash import BashOperator
import time

# Sample simple class
class Counter:

    def __init__(self):
        print("")
    
    def counter(self, f_input):
        i=0
        for i in range(f_input):
            print(i)
            time.sleep(0.1)

# Initialize DAG
with DAG(dag_id="demo", start_date=datetime(2024, 4, 20), schedule_interval=None) as dag:

    # Wrapping each tasks
    @task()
    def count_10():
        cn = Counter()
        print("FastCount10")
        cn.counter(10)

    @task()
    def count_20():
        cn = Counter()
        print("FastCount20")
        cn.counter(20)
    
    @task()
    def count_30():
        cn = Counter()
        print("FastCount30")
        cn.counter(30)

    # count_10() >> count_20() >> count_30()
    i = 0
    for i in range(3): 
        count_10() >> count_20() >> count_30()
        print(f"\n loop_number: {i}")
        i = i + 1