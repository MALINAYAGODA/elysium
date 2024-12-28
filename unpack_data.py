import pandas as pd

def get_all_questions():
    df = pd.read_csv("D:\danila_prj_my\mock_interview\questions.csv")
    df = df[df["Тема"]=="ML"]
    id_to_list = {}
    question_to_id = {}
    ind = 1
    for i in df.iterrows():
        id_to_list[ind] = (i[1]["Вопрос"], i[1]["Ответ"], i[1]["Ресурсы"])
        question_to_id[i[1]["Вопрос"]] = ind
        ind += 1
    return id_to_list, question_to_id

get_all_questions()