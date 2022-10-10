import pyodbc

global server
global database
global cnn
global cursor


def make_connection():
    server = 'CD-TEST'
    database = 'PY'
    cnn = pyodbc.connect(
        "DRIVER={SQL Server};SERVER=" + server + ";DATABASE=" + database + ";Trusted_Connection=Yes")
    cursor = cnn.cursor()
    return cnn, cursor


def get_column_header(cn, cr, sql_text):
    query = f"EXEC {sql_text}"
    print(query)
    cr.execute(query)
    result = cr.fetchall()
    for col_name, ord_id, col_type in result:
        if col_type == int:
            print(f"\t{col_name:5}\t|", end="")
        else:
            print(f"\t{col_name:12}\t|", end="")

    if result[0]:
        how_long = len(result) * 25
        print("\n", "="*how_long)
    # cn.commit()
    return (len(result))


def call_find_column(table_name):
    return f"find_columns '{table_name}'"


def display_hearder(tname):
    # print("display_hearder")
    cnn, cursor = make_connection()
    fn_name = call_find_column(tname)
    get_column_header(cnn, cursor, fn_name)


# display_hearder()
