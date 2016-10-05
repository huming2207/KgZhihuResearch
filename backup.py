from zhihu_oauth import ZhihuClient

# A simple backup tool (use the sample code from zhihu_oauth project) to backup ZhiHu SHSS question.
# Then backup to a safer place like GitHub or wherever.

client = ZhihuClient()
client.login_in_terminal()

question = client.question(51241029)

print(question.title)

for answer in question.answers:
    answer.save(answer.author.name + " - " +  str(answer.id))
    print("Saved the answer from\t" + answer.author.name + "\t\twith ID " + str(answer.id))
