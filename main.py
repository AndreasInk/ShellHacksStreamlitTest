import streamlit as st

from pydantic import BaseModel


if 'count' not in st.session_state:
	st.session_state.count = 0

class Question(BaseModel):
    id: int = 0
    a: str = ""
    b: str = ""
    c: str = ""
    correct: str = ""
    picked: str = ""

def study(question: Question()):
    st.button(question.a)
    st.button(question.b)
    st.button(question.c)

def loadQuestions():
    questions = [Question(id= 0, a= "a", b="b", c= "c", correct= "c", picked= "")]
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
        study(question=Question(id= question.id, a= question.a, b=question.b, c= question.c, correct= question.correct, picked= ""))
