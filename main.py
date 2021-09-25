import streamlit as st

from pydantic import BaseModel





if 'count' not in st.session_state:
	st.session_state.count = 0

class Question(BaseModel):
    id: int = 0
    questionStr: str = ""
    a: str = ""
    b: str = ""
    c: str = ""
    correct: str = ""
    picked: int = 0

def study(question: Question()):
    st.header(str(question.id) + ") "+ question.questionStr)
    a = st.button(question.a)
    if str(question.id) not in st.session_state:
	    st.session_state[str(question.id)] = 0
    if a:
        question.picked  = 1
        st.session_state[str(question.id)] = question.picked

    b = st.button(question.b)
    if b:
        question.picked  = 2
        st.session_state[str(question.id)] = question.picked

    c = st.button(question.c)
    if c:
        question.picked  = 3
        st.session_state[str(question.id)] = question.picked
    if st.session_state[str(question.id)] == 3:
        st.write("Picked: " + "C")
    else:
        st.write("Picked: " + str("A" if  st.session_state[str(question.id)] == 1 else "B"))

def loadQuestions():
    questions = [Question(id= 0, questionStr = "Hello World", a= "a", b="b", c= "c", correct= "c", picked= 0)]
    ## Get Questions From JSON
    return questions
st.image("logo.png")
st.title("Remembear")

st.header("Reimagine Studying")

st.subheader("Studies suggest that when students hear the same music as they listened to while studying during sleep that they are are more likely to rememeber that study material.  Further research is required to solidify the results, Remembear is a platform to further research.")

start = st.button("Participate In Preliminary Study")
if start:
    st.session_state.count += 1
if  st.session_state.count > 0:
    questions = loadQuestions()
    for question in questions:
        study(question=Question(id= question.id, questionStr = question.questionStr, a= question.a, b=question.b, c= question.c, correct= question.correct, picked= 0))

# currLinesPosition = 0
# with open('TestQuizlet.txt') as f:
#     lines = f.readlines()
#     for line in  lines:
#         st.subheader(line)
#         for answers in range (2):
#             st.text(line)

questionNumCount = 1
with open('TestQuizlet.txt') as f:
    line = f.readline()
    while line:
        if line[0] != 'a' and line[0]!='b' and line[0]!='\n':
            st.subheader(str(questionNumCount)+").  " + line) 
            questionNumCount = questionNumCount + 1
        else:
            st.text(line)
            
        line = f.readline()
