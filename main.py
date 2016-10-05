import jieba
import csv
from zhihu_oauth import ZhihuClient
from joblib import Parallel

client = ZhihuClient()
client.login_in_terminal()

if __name__ == '__main__':
    me = client.me()

    # Put the question ID here:
    specified_question = client.question(51241029)
    answers_list = specified_question.answers
    content_list = []
    seg_list = []
    result = []

    file_handler = open('result.csv', 'w')
    field_range = ["Keyword", "Count"]
    writer = csv.DictWriter(file_handler, dialect="excel", extrasaction='ignore', fieldnames=field_range)



    print("Grabbing contents...\n")

    for specified_answer in specified_question.answers:
        content_list.append(specified_answer.content)
        print("... 1 answer added!")

    print("Got " + str(len(content_list)) + " answers!\n")
    print(content_list)

    jieba.load_userdict("phrase.txt")


    for content in content_list:
        seg_list.extend(jieba.cut(content, cut_all=False))

    writer.writeheader()

    for seg_str in seg_list:
        writer.writerow({'Keyword': seg_str, 'Count': str(seg_list.count(seg_str))})

    file_handler.flush()
    file_handler.close()


