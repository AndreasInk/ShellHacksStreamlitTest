import streamlit as st

from pydantic import BaseModel

from audio import playAudio
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
    st.header(str(question.id + 1) + ") "+ question.questionStr)
    a = st.button(question.a, key=str(question.id) + question.a)
    if str(question.id) not in st.session_state:
	    st.session_state[str(question.id)] = 0
    if a:
        question.picked  = 1
        st.session_state[str(question.id)] = question.picked

    b = st.button(question.b, key=str(question.id) + question.b)
    if b:
        question.picked  = 2
        st.session_state[str(question.id)] = question.picked

    c = st.button(question.c, key=str(question.id) + question.c)
    if c:
        question.picked  = 3
        st.session_state[str(question.id)] = question.picked
    if st.session_state[str(question.id)] == 3:
        st.write("Picked: " + "C")
    else:
        st.write("Picked: " + str("A" if  st.session_state[str(question.id)] == 1 else "B"))

def loadQuestions():
    questions = [Question(id= 0, questionStr = "___is the ability to use the same type pointer to point to pointers of different types.", a= "Overloading operators", b="Inheritance", c= "Polymorphism", correct= "Polymorphism", picked= 0), Question(id= 1, questionStr = "_____is the ability to create new data types from existing data types.", a= "Encapsulation", b="Inheritance", c= "Polymorphism", correct= "Inheritance", picked= 0)]
    ## Get Questions From JSON
    return questions
st.image("logo.png")
st.title("Remembear")

st.header("Reimagine Studying")

st.subheader("Studies suggest that when students hear the same music as they listened to while studying during sleep that they are are more likely to rememeber that study material.  Further research is required to solidify the results, Remembear is a platform to further research.")

start = st.button("Take The Test")
sleep = st.button("Test The App")
if sleep:
    playAudio()
if start:
    st.session_state.count += 1
if  st.session_state.count > 0:
    questions = loadQuestions()
    questionNum = 0
    for question in questions:

        study(question=Question(id= questionNum, questionStr = question.questionStr, a= question.a, b=question.b, c= question.c, correct= question.correct, picked= 0))
        questionNum += 1
