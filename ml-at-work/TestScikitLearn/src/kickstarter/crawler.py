import json
import os
import time
import traceback
import glob

import urllib.request
import pandas as pd
import pandas.io.json

result_dir_path = r"result"


def fetch_data_and_output():
    search_term = ""
    sort_key = "newest"
    category_list = [16, 331, 332, 333, 334, 335, 336, 337, 52, 362, 338, 51, 339, 340, 341, 342]  # technology category
    query_base = "https://www.kickstarter.com/projects/search.json?term={}&category_id={}&page={}&sort={}"
    for category_id in category_list:
        for page_id in range(1, 201):
            try:
                query = query_base.format(search_term, category_id, page_id, sort_key)
                print(query)
                data = urllib.request.urlopen(query).read().decode("utf-8")
                response_json = json.loads(data)
            except:
                traceback.print_exc()
                break
            # 1ページあたり、20件の結果が返ってくるので、1件ずつ保存する。
            for project in response_json["projects"]:
                file_path = result_dir_path + os.sep + str(project["id"]) + ".json"
                print("file_path = {}".format(file_path))
                with open(file_path, "w") as fp:
                    fp.write(json.dumps(project, sort_keys=True, indent=2))
            # urllib.requestする前にsleepし過剰アクセスを防止
            time.sleep(1)


def convert_result_json_to_csv():
    project_list = []
    # globでresultフォルダにあるファイルを読み込む
    for file_name in glob.glob(result_dir_path + os.sep + "*.json"):
        with open(file_name, "r") as fp:
            project = json.loads(fp.read())
            project_list.append(project)
    # json_normalizeでDataFrameに変換
    df = pd.io.json.json_normalize(project_list)
    # 末尾が"_at"で終わるunixtimeのカラムをdatetimeに変換
    datetime_columns = filter(lambda a: a[-3:] == "_at", df.columns)
    for column in datetime_columns:
        df[column] = pd.to_datetime(df[column], unit="s")
    # DataFrameからCSV形式のstrに変換
    csv_data = df.to_csv()
    # WindowsのExcelに読み込ませるのでCP932(Shift-JIS)にする
    csv_data = csv_data.encode("cp932", "ignore")
    # 結果を書き込む
    with open("kickstarter_result.csv", "wb") as fp:
        fp.write(csv_data)
    pass


def main():
    os.makedirs(result_dir_path, exist_ok=True)
    # fetch_data_and_output()
    convert_result_json_to_csv()


if __name__ == "__main__":
    main()
