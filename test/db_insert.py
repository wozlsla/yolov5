import numpy as np
import psycopg2
import time
from datetime import datetime


# Database Access Info
db_inform = {
    "dbname": "test",
    "user": "jimin",
    "password": "1234",
    "host": "000.000.0.000",
    "port": "0000",
}


def get_data(db_inform):
    try:
        conn = psycopg2.connect(**db_inform)
        try:
            while 1:
                cur = conn.cursor()
                # dist = np.random.rand()
                # dist = str(np.random.randint(30, 500))         
                dist_rand = [np.random.randint(30, 500)]

                eqp_time = time.strftime("%Y-%m-%d %H:%M:%S.%03d", time.localtime(time.time()))[:-3] # Linux
                # eqp_time = (datetime.now()).strftime("%Y-%m-%d %H:%M:%S.%f")[:-3] # Windows

                # Linux
                query = f"INSERT INTO test.operation (node_id, id, class_name, eqp_time, bbox, distance) \
                    VALUES ('{node_id}', %s, %s, '{eqp_time}', ARRAY {box_list}, '{dist_rand}')" 
                cur.execute(query, (img_id, name))
                
                # Windows : syntax error at or near "%"
                query = f"INSERT INTO test.operation (node_id, id, class_name, eqp_time, bbox, distance) \
                    VALUES ('{node_id}', ARRAY {img_id}, ARRAY {name}, '{eqp_time}', ARRAY {box_list}, '{dist_rand}')" 
                cur.execute(query)

                # rows = cur.fetchall()

                conn.commit()
                time.sleep(2)

        finally:
            cur.close()
            conn.close()
            print("Conn Closed")

    # except Exception as e:
    except (psycopg2.OperationalError, psycopg2.DatabaseError) as e:
        print(f"Error getting data: {str(e)}")

get_data(db_inform)