import streamlit as st
import pandas as pd
import pickle
import requests
def fetch_poster(movie_id):

     url="https://api.themoviedb.org/3/movie/{}?api_key=8265bd1679663a7ea12ac168da84d2e8&language=en-US".format(movie_id)
     data=requests.get(url)
     data=data.json()
     poster_path=data['poster_path']
     return "https://image.tmdb.org/t/p/w500/" + poster_path

def movie_sel(m):
     l = []
     n_index_movie = movie[movie['title'] == m].index[0]
     sim = similarity[n_index_movie]
     l = sorted(list(enumerate(sim)), reverse=True, key=lambda x: x[1])[1:7]
     recommended_movie=[]
     recommended_movie_posters = []
     for i in l:
          movie_id = movie.iloc[i[0]].movie_id
          recommended_movie_posters.append(fetch_poster(movie_id))
          recommended_movie.append(movie.iloc[i[0]].title)
     return recommended_movie,recommended_movie_posters

movie = pickle.load(open('Movie.pkl','rb'))
st.title('Movie Recommendor System')
similarity = pickle.load(open('similarity.pkl','rb'))

option = st.selectbox(
     'Select the movie from list to get related movies',
     movie['title'].values)

st.write('You selected:', option)

if st.button('Top 6 Related Movies'):
     name,poster=movie_sel(option)
     col1, col2, col3,col4,col5,col6 = st.columns(6)

     with col1:
          st.image(poster[0])
          st.header(name[0])

     print(end="           ")
     with col2:
          st.image(poster[1])
          st.header(name[1])

     print(end="          ")
     with col3:
          st.image(poster[2])
          st.header(name[2])
     print(end="          ")
     with col4:
          st.image(poster[3])
          st.header(name[3])

     print(end="          ")
     with col5:
          st.image(poster[4])
          st.header(name[4])
     print(end="          ")

     with col6:
          st.image(poster[5])
          st.header(name[5])


else:
     st.write('Please press the button')

