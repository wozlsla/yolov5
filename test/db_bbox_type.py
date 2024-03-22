import itertools
import psycopg2
import pandas as pd


# Database Access Info
db_inform = {
    "dbname": "test",
    "user": "jimin",
    "password": "1234",
    "host": "000.000.0.000",
    "port": "0000",
} 


def connect_to_database(db_inform):
    global conn, cur
    try:
        conn = psycopg2.connect(**db_inform)
        cur = conn.cursor()
        print("Database connection established successfully!")
    except (psycopg2.OperationalError, psycopg2.DatabaseError) as error:
        print(f"Error connecting to the database: {error}")
        print(f"Database Unconnected")



connect_to_database(db_inform)

try:
    # line = ["tv", 62, [0.3789, 0.8806, 0.0797, 0.0944]]
    lines = [["tv", 62, [0.3789, 0.8806, 0.0797, 0.0944]], ["tv", 6, [0.3234, 0.3958, 0.0688, 0.1806]]]

    name, id, box = [], [], []
    for line in lines:
        name.append(line[0])
        id.append(line[1])
        box.append(line[2])

    boxes = list(itertools.chain(*box))

    box_list = []
    box_list_2 = []
    
    step_size = 4 # 4개씩 묶음
    for i in range(0, len(boxes), step_size):
        box_float = boxes[i : i + step_size]  # float
        box_str = ", ".join(map(str, box_float))  # str
        # box_str_2 = ",".join(map(str, box_float))  # 공백 있어야 "" 로 들어감.. 이유는?
        box_list.append(box_str)
        # box_list_2.append(box_str_2)


    box_list = ['0.3789, 0.8806, 0.0797, 0.0944', '0.3234, 0.3958, 0.0688, 0.1806']
    box_list_2 = ['0.3789, 0.8806,0.0797,0.0944', '0.3234,0.3958,0.0688,0.1806']

    # ['0,0', ''0,0']
    query = f"INSERT INTO test.operation (node_id, img_id, class_name, eqp_time, bbox)\
          VALUES ('test', '00', %s, '2023-10-06 00:00:00.000', ARRAY ['0.3789, 0.8806, 0.0797, 0.0944', '0.3234, 0.3958, 0.0688, 0.1806'])"
    # ['0,0', 0,0]
    query = f"INSERT INTO test.operation (node_id, img_id, class_name, eqp_time, bbox)\
          VALUES ('test', '00', %s, '2023-10-06 00:00:00.000', ARRAY ['0.3789, 0.8806,0.0797,0.0944', '0.3234,0.3958,0.0688,0.1806'])"
    # [0,0,0,0]
    query = f"INSERT INTO test.operation (node_id, img_id, class_name, eqp_time, bbox)\
          VALUES ('test', '00', %s, '2023-10-06 00:00:00.000', ARRAY ['0.3789,0.8806,0.0797,0.0944', '0.3234,0.3958,0.0688,0.1806'])"
    
    query = f"INSERT INTO test.operation (node_id, img_id, class_name, eqp_time, bbox)\
          VALUES ('test', '00', %s, '2023-10-06 00:00:00.000', ARRAY {box_list})"
    
    cur.execute(query, (name))
    conn.commit()
    

    # Select
    # query = f"SELECT * FROM test.operation ORDER BY regtimestamp DESC LIMIT 6"
    # cur.execute(query)
    # rows = cur.fetchall()
    # col = [column[0] for column in cur.description]
    # data = pd.DataFrame(rows, columns=col)

finally:
    cur.close()
    conn.close()