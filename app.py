import dash
import pandas as pd
import dash_core_components as dcc
import dash_html_components as html
import numpy as np

external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css']

app = dash.Dash(__name__, external_stylesheets=external_stylesheets)
server = app.server

north_america_user_rating = pd.read_csv('short1.csv')

north_america_user_rating = north_america_user_rating.drop_duplicates(['userID', 'Title'])
north_america_user_rating_pivot2 = north_america_user_rating.pivot(index='userID', columns='Title', values='Rating').fillna(0)

X = north_america_user_rating_pivot2.values.T

from sklearn.decomposition import TruncatedSVD

SVD = TruncatedSVD(n_components=12, random_state=17)
matrix = SVD.fit_transform(X)


import warnings
warnings.filterwarnings("ignore", category=RuntimeWarning)
corr = np.corrcoef(matrix)

north_america_book_title = north_america_user_rating_pivot2.columns
north_america_book_list = list(north_america_book_title)
book_index = north_america_book_list.index("Wild Animus")
book_index2 = north_america_book_list.index("A Time to Kill")
book_index3 = north_america_book_list.index("The Da Vinci Code")
book_index4 = north_america_book_list.index("The Secret Life of Bees")
book_index5 = north_america_book_list.index("The Red Tent (Bestselling Backlist)")
book_index6 = north_america_book_list.index("Divine Secrets of the Ya-Ya Sisterhood: A Novel")
book_index7 = north_america_book_list.index("A Painted House")
book_index8 = north_america_book_list.index("Life of Pi")
book_index9 = north_america_book_list.index("The Nanny Diaries: A Novel")
book_index10 = north_america_book_list.index("Bridget Jones's Diary")
book_index11 = north_america_book_list.index("Snow Falling on Cedars")
book_index12 = north_america_book_list.index("Girl with a Pearl Earring")
book_index13 = north_america_book_list.index("Where the Heart Is (Oprah's Book Club (Paperback))")
book_index14 = north_america_book_list.index("Harry Potter and the Sorcerer's Stone (Harry Potter (Paperback))")
book_index15 = north_america_book_list.index("The Pilot's Wife : A Novel")
book_index16 = north_america_book_list.index("The Pelican Brief")
book_index17 = north_america_book_list.index("The Summons")
book_index18 = north_america_book_list.index("House of Sand and Fog")
book_index19 = north_america_book_list.index("The Testament")
book_index20 = north_america_book_list.index("The Girls' Guide to Hunting and Fishing")


corr_book_index = corr[book_index]
corr_book_index2 = corr[book_index2]
corr_book_index3 = corr[book_index3]
corr_book_index4 = corr[book_index4]
corr_book_index5 = corr[book_index5]
corr_book_index6 = corr[book_index6]
corr_book_index7 = corr[book_index7]
corr_book_index8 = corr[book_index8]
corr_book_index9 = corr[book_index9]
corr_book_index10 = corr[book_index10]
corr_book_index11 = corr[book_index11]
corr_book_index12 = corr[book_index12]
corr_book_index13 = corr[book_index13]
corr_book_index14 = corr[book_index14]
corr_book_index15 = corr[book_index15]
corr_book_index16 = corr[book_index16]
corr_book_index17 = corr[book_index17]
corr_book_index18 = corr[book_index18]
corr_book_index19 = corr[book_index19]
corr_book_index20 = corr[book_index20]


all_options = {
        "Wild Animus": list(north_america_book_title[(corr_book_index < 1.0) & (corr_book_index > 0.9)]),
        "A Time to Kill": list(north_america_book_title[(corr_book_index2 < 1.0) & (corr_book_index2 > 0.9)]),
        "The Da Vinci Code": list(north_america_book_title[(corr_book_index3 < 1.0) & (corr_book_index3 > 0.9)]),
        "The Secret Life of Bees": list(north_america_book_title[(corr_book_index4 < 1.0) & (corr_book_index4 > 0.9)]),
        "The Red Tent (Bestselling Backlist)": list(north_america_book_title[(corr_book_index5 < 1.0) & (corr_book_index5 > 0.9)]),
        "Divine Secrets of the Ya-Ya Sisterhood: A Novel": list(north_america_book_title[(corr_book_index6 < 1.0) & (corr_book_index6 > 0.9)]),
        "A Painted House": list(north_america_book_title[(corr_book_index7 < 1.0) & (corr_book_index7 > 0.9)]),
        "Life of Pi": list(north_america_book_title[(corr_book_index8 < 1.0) & (corr_book_index8 > 0.9)]),
        "The Nanny Diaries: A Novel": list(north_america_book_title[(corr_book_index9 < 1.0) & (corr_book_index9 > 0.9)]),
        "Bridget Jones's Diary": list(north_america_book_title[(corr_book_index10 < 1.0) & (corr_book_index10 > 0.9)]),
        "Snow Falling on Cedars": list(north_america_book_title[(corr_book_index11 < 1.0) & (corr_book_index11 > 0.9)]),
        "Girl with a Pearl Earring": list(north_america_book_title[(corr_book_index12 < 1.0) & (corr_book_index12 > 0.9)]),
        "Where the Heart Is (Oprah's Book Club (Paperback))": list(north_america_book_title[(corr_book_index13 < 1.0) & (corr_book_index13 > 0.9)]),
        "Harry Potter and the Sorcerer's Stone (Harry Potter (Paperback))": list(north_america_book_title[(corr_book_index14 < 1.0) & (corr_book_index14 > 0.9)]),
        "The Pilot's Wife : A Novel": list(north_america_book_title[(corr_book_index15 < 1.0) & (corr_book_index15 > 0.9)]),
        "The Pelican Brief": list(north_america_book_title[(corr_book_index16 < 1.0) & (corr_book_index16 > 0.9)]),
        "The Summons": list(north_america_book_title[(corr_book_index17 < 1.0) & (corr_book_index17 > 0.9)]),
        "House of Sand and Fog": list(north_america_book_title[(corr_book_index18 < 1.0) & (corr_book_index18 > 0.9)]),
        "The Testament": list(north_america_book_title[(corr_book_index19 < 1.0) & (corr_book_index19 > 0.9)]),
        "The Girls' Guide to Hunting and Fishing": list(north_america_book_title[(corr_book_index20 < 1.0) & (corr_book_index20 > 0.9)])

}
app.layout = html.Div([
    html.H1("Book Recommendations", style={"text-align":"center"}),

    html.Div(
        [
            dcc.Dropdown(
                id='top-books-dropdown',
                options=[{'label': k, 'value': k} for k in all_options.keys()],
                placeholder='Select Book From List'
            ),

    html.Hr(),

    dcc.Dropdown(id='suggest-books-dropdown'),

    html.Hr(),

    html.Div(id='display-selected-values')
]),
])


@app.callback(
    dash.dependencies.Output('suggest-books-dropdown', 'options'),
    [dash.dependencies.Input('top-books-dropdown', 'value')])
def set_rec_book_options(selected_book):
    return [{'label': i, 'value': i} for i in all_options[selected_book]]


@app.callback(
    dash.dependencies.Output('suggest-books-dropdown', 'value'),
    [dash.dependencies.Input('suggest-books-dropdown', 'options')])
def set_rec_book_value(available_options):
    return available_options[0]['value']


@app.callback(
    dash.dependencies.Output('display-selected-values', 'children'),
    [dash.dependencies.Input('top-books-dropdown', 'value'),
     dash.dependencies.Input('suggest-books-dropdown', 'value')])
def set_display_children(selected_book, recommended_book):
    return u'{} is recommended because you like {}'.format(
        recommended_book, selected_book,
    )


if __name__ == '__main__':
    app.run_server(debug=True)
