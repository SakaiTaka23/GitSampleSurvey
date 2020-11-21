import csv

def write_result(result):
    with open("result.csv","a") as f:
        writer = csv.writer(f)
        writer.writerow(result)

# result = ("SakaiTaka23",300,0,14)
# write_result(result)