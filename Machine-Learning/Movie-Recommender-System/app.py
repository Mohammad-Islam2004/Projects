import streamlit as st
import requests
import pickle

st.set_page_config(
    page_title="Movie Recommender",
    page_icon="🎬"
)

st.sidebar.title("🎥 About")
st.sidebar.info(
    """
    This is a **content-based movie recommender system**
    built by **Mohammad Islam**.
    
    Check my other projects below :
    """
)
st.sidebar.markdown(
    "[🔗 **My Website**](https://mohammad-islam2004.github.io/Portfolio/)"
)

st.markdown(
    "<h1 style='text-align: center;'>🎬 Movie Recommender System</h1>",
    unsafe_allow_html=True
)
st.markdown(
    "<p style='text-align: center; color: gray;'>Find movies similar to your taste</p>",
    unsafe_allow_html=True
)
def movie_card(title, poster):
    st.markdown(
        f"""
        <div style="
            text-align:center;
            background-color:#1c1c1c;
            padding:10px;
            border-radius:12px;
            box-shadow:0px 4px 10px rgba(0,0,0,0.4);
        ">
            <img src="{poster}" style="width:100%; border-radius:10px;">
            <h4 style="color:white;">{title}</h4>
        </div>
        """,
        unsafe_allow_html=True
    )



movies = pickle.load(open("movies.pkl", "rb"))

similarity = pickle.load(open("similarity.pkl", "rb"))

def fetch_poster(movie_id):
    response = requests.get('https://api.themoviedb.org/3/movie/{}?api_key=8265bd1679663a7ea12ac168da84d2e8&language=en-US'.format(movie_id))
    data = response.json()
    return  "https://image.tmdb.org/t/p/w500" + data['poster_path']

def recommend(movie):
    movie_index = movies[movies['title'] == movie].index[0]
    distances = similarity[movie_index]
    movies_list= sorted(list(enumerate(distances)), reverse=True, key=lambda x: x[1])[1:6]

    recommended_movies = []
    recommended_movies_posters = []
    for i in movies_list:
        movie_id = movies.iloc[i[0]].movie_id
        recommended_movies.append(movies.iloc[i[0]].title)
        recommended_movies_posters.append(fetch_poster(movie_id))
    return recommended_movies, recommended_movies_posters

selected_movie_name = st.selectbox('', movies['title'].values)

if st.button('Recommend'):
    names, posters = recommend(selected_movie_name)

    col1, col2, col3, col4, col5 = st.columns(5)
    for col, name, poster in zip([col1, col2, col3, col4, col5], names, posters):
        with col:
            movie_card(name, poster)
