import streamlit as st
import pandas as pd
import preprocessor,helper
import plotly.express as px
import matplotlib.pyplot as plt
import seaborn as sns
import plotly.figure_factory as ff

df = pd.read_csv("https://drive.google.com/file/d/1gv5JZ2PKg-mCkYX_73qg6etJTTxNhmF_/view?usp=drive_link")
region_df = pd.read_csv("https://drive.google.com/file/d/14I8B5ilWmfgxaBt0hxzpv_8WDVKftBo2/view?usp=drive_link")

df =preprocessor.preprocess(df,region_df)

st.sidebar.title("Olympics Analysis")
st.sidebar.image("data:image/png;base64,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")

user_menu = st.sidebar.radio(
    'Select an option',
    ('Medal Tally','Overall Analysis','Country-wise Analysis','Athlete-wise Analysis')
)

if user_menu == 'Medal Tally':
    st.sidebar.header("Medal Tally")
    years, country = helper.country_year_list(df)

    selected_year = st.sidebar.selectbox("Select Year",years)
    selected_country = st.sidebar.selectbox("Select Country", country)

    medal_tally = helper.fetch_medal_tally(df,selected_year,selected_country)
    if selected_year == 'Overall' and selected_country == "Overall":
        st.title("Overall Tally")
    if selected_year != 'Overall' and selected_country == "Overall":
        st.title("Medal Tally in " + str(selected_year) + " Olympics")
    if selected_year == 'Overall' and selected_country != "Overall":
        st.title(selected_country + " overall performance")
    if selected_year != 'Overall' and selected_country != "Overall":
        st.title(selected_country + " perfomance in " + str(selected_year) + " Olympics")
    st.table(medal_tally)

if user_menu == "Overall Analysis":
    editions = df['Year'].unique().shape[0] - 1
    cities = df['City'].unique().shape[0]
    sports = df['Sport'].unique().shape[0]
    events = df['Event'].unique().shape[0]
    athletes = df['Name'].unique().shape[0]
    nations = df['region'].unique().shape[0]

    st.title("Top Statistics")
    col1, col2, col3 = st.columns(3)
    with col1 :
        st.header("Editions")
        st.title(editions)
    with col2 :
        st.header("Hosts")
        st.title(cities)
    with col3 :
        st.header("Sports")
        st.title(sports)

    col1, col2, col3 = st.columns(3)
    with col1:
        st.header("Events")
        st.title(events)
    with col2:
        st.header("Nations")
        st.title(nations)
    with col3:
        st.header("Athletes")
        st.title(athletes)

    nations_over_time = helper.data_over_time(df,'region')
    fig = px.line(nations_over_time,x="Edition",y="region")
    st.title("Participating Nations over the years")
    st.plotly_chart(fig)

    events_over_time = helper.data_over_time(df,'Event')
    fig = px.line(events_over_time,x="Edition",y="Event")
    st.title("Events over the years")
    st.plotly_chart(fig)

    athletes_over_time = helper.data_over_time(df, 'Name')
    fig = px.line(athletes_over_time, x="Edition", y="Name")
    st.title("Athletes over the years")
    st.plotly_chart(fig)

    st.title("No. of Events over time(Every Sport)")
    fig, axes = plt.subplots(figsize=(20,20))
    x = df.drop_duplicates(['Year','Sport','Event'])
    ax= sns.heatmap(x.pivot_table(index='Sport',columns='Year',values='Event',aggfunc='count').fillna(0).astype('int'),annot=True)
    st.pyplot(fig)

    st.title("Most Successful Athletes")
    sport_list = df['Sport'].unique().tolist()
    sport_list.sort()
    sport_list.insert(0,'Overall')
    selected_sport = st.selectbox('Select a Sport',sport_list)
    x = helper.most_successful(df,selected_sport)
    st.table(x)

if user_menu == 'Country-wise Analysis':
    st.sidebar.title("Country-wise Analysis")
    country_list = df['region'].dropna().unique().tolist()
    country_list.sort()

    selected_country = st.sidebar.selectbox("Select a Country",country_list)

    country_df = helper.yearwise_medal_tally(df,selected_country)
    fig = px.line(country_df, x="Year", y="Medal")
    st.title(selected_country + " Medal tally over the years")
    st.plotly_chart(fig)

    st.title(selected_country + " excels in the following sports")
    pt = helper.country_event_heatmap(df,selected_country)
    fig, axes = plt.subplots(figsize=(20, 20))
    ax = sns.heatmap(pt,annot=True)
    st.pyplot(fig)

    st.title("Top 10 athletes of " + selected_country)
    top10_df = helper.most_successful_countrywise(df,selected_country)
    st.table(top10_df)

if user_menu == 'Athlete-wise Analysis':
    athlete_df = df.drop_duplicates(subset=['Name', 'region'])

    # Age Distribution Plot
    st.title("Distribution of Age")
    x1 = athlete_df['Age'].dropna()
    x2 = athlete_df[athlete_df['Medal'] == 'Gold']['Age'].dropna()
    x3 = athlete_df[athlete_df['Medal'] == 'Silver']['Age'].dropna()
    x4 = athlete_df[athlete_df['Medal'] == 'Bronze']['Age'].dropna()
    if all(len(x) > 0 for x in [x1, x2, x3, x4]):
        fig = ff.create_distplot([x1, x2, x3, x4], ['Overall Age', 'Gold Medalist', 'Silver Medalist', 'Bronze Medalist'], show_hist=False, show_rug=False)
        fig.update_layout(autosize=False, width=1000, height=600)
        st.plotly_chart(fig)
    else:
        st.warning("Insufficient data for age distribution plot.")

    # Gold Medalist Age by Sport
    st.title("Distribution of Age wrt Sports (Gold Medalist)")
    x = []
    name = []
    famous_sports = ['Basketball', 'Judo', 'Football', 'Tug-Of-War', 'Athletics',
                     'Swimming', 'Badminton', 'Sailing', 'Gymnastics',
                     'Art Competitions', 'Handball', 'Weightlifting', 'Wrestling',
                     'Water Polo', 'Hockey', 'Rowing', 'Fencing',
                     'Shooting', 'Boxing', 'Taekwondo', 'Cycling', 'Diving', 'Canoeing',
                     'Tennis', 'Golf', 'Softball', 'Archery',
                     'Volleyball', 'Synchronized Swimming', 'Table Tennis', 'Baseball',
                     'Rhythmic Gymnastics', 'Rugby Sevens',
                     'Beach Volleyball', 'Triathlon', 'Rugby', 'Polo', 'Ice Hockey']
    for sport in famous_sports:
        temp_df = athlete_df[athlete_df['Sport'] == sport]
        ages = temp_df[temp_df['Medal'] == 'Gold']['Age'].dropna()
        if len(ages) > 0:
            x.append(ages)
            name.append(sport)
    if x:
        fig = ff.create_distplot(x, name, show_hist=False, show_rug=False)
        fig.update_layout(autosize=False, width=1000, height=600)
        st.plotly_chart(fig)
    else:
        st.warning("No gold medalist data available for selected sports.")

    # Height vs. Weight Scatterplot
    st.title('Height Vs Weight')
    sport_list = df['Sport'].unique().tolist()
    sport_list.sort()
    sport_list.insert(0, 'Overall')
    selected_sport = st.selectbox('Select a Sport', sport_list)
    temp_df = helper.weight_v_height(df, selected_sport)
    temp_df = temp_df.dropna(subset=['Height', 'Weight'])
    if not temp_df.empty:
        fig, ax = plt.subplots()
        sns.scatterplot(x='Weight', y='Height', hue='Medal', style='Sex', s=60, data=temp_df, ax=ax)
        st.pyplot(fig)
    else:
        st.warning(f"No data available for {selected_sport}.")

    # Men vs. Women Participation
    st.title("Men Vs Women Participation Over the Years")
    final = helper.men_vs_women(df)
    fig = px.line(final, x="Year", y=["Male", "Female"])
    fig.update_layout(autosize=False, width=1000, height=600)
    st.plotly_chart(fig)
