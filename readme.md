# Apache Airflow
* 코드 기반으로 Workflow를 관리하고 자동화할 수 있는 도구
	* Step by step으로 실험 / 개발작업 진행, 시각화 가능
	* 잘 익혀두면 PM이나 화학 실험시 유리할 수 있음으로 판단됨
# Setup
* https://airflow.apache.org/docs/docker-stack/build.html
* https://airflow.apache.org/docs/apache-airflow/stable/howto/docker-compose/index.html
* https://95mkr.tistory.com/entry/airflow1
* https://velog.io/@hamdoe/Airflow-%EC%A1%B0%EA%B7%B8%EB%A7%A3%EA%B2%8C-%EC%8B%9C%EC%9E%91%ED%95%98%EA%B8%B0-Quick-start
* https://letzgorats.tistory.com/entry/Airflow-Python-operator-%EA%B8%B0%EB%B3%B8
```bash
conda create -n airflow python=3.8
conda activate airflow
apt update -y && sudo apt install -y python3-pip libmysqlclient-dev libssl-dev libffi-dev libxml2-dev libxslt1-dev zlib1g-dev
apt upgrade -y

pip install apache-airflow
pip list | grep airflow

airflow db init
airflow users create \
    		--role Admin \
    		--username peal \
    		--firstname y \
    		--lastname z \
    		--email m \
    		--password pass
    		
apt-get install graphviz
pip install graphviz, pandas
# airflow scheduler &
# airflow webserver --port 8080 &

```
# Example
```python title:smapleDAG
# dags 폴더안에 만들 것!
from datetime import datetime

from airflow import DAG
from airflow.decorators import task
from airflow.operators.bash import BashOperator
from airflow.models.baseoperator import chain
import time

class Counter:

    def __init__(self):
        print("")
    
    def counter(self, f_input):
        i=0
        for i in range(f_input):
            print(i)
            time.sleep(0.1)

with DAG(dag_id="demo", start_date=datetime(2024, 4, 20), schedule="0 0 * * *") as dag:

    # ② Tasks are represented as operators
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
        
	# Seequential
    # count_10() >> count_20() >> count_30()
    i = 0
    for i in range(3):
        [count_10(),count_30(),count_20()]
        print(f"\n loop_number: {i}")
        i = i + 1
```

```bash title:DAGRunner
# 코드 작동확인
python dags/examples/airflow_test.py

# 내용물 확인 후 실행
airflow db migrate
airflow dags list
airflow tasks list number_counting_dag
airflow dags test "demo"

# 시각화
airflow dags show demo --save demo.png
```

# 작동결과
* 코드 Graph 이미지 / 3번 Loop 버전
* ![demo.png](https://github.com/coport-uni/airflow2_demo_peal/blob/main/demo.png)
* ![demo_loop.png](https://github.com/coport-uni/airflow2_demo_peal/blob/main/demo_loop.png)
