import pandas as pd
import plotly.graph_objs as go

# Use this file to read in your data and prepare the plotly visualizations. The path to the data files are in
# `data/file_name.csv`



def return_figures():
    """Creates four plotly visualizations

    Args:
        None

    Returns:
        list (dict): list containing the four plotly visualizations

    """

    # Percentage of survived person 
    # as a bar chart
    titanic = pd.read_csv('data/titanic.csv')
    survived = titanic['Survived'].value_counts(normalize=True)
    graph_one = []    
    graph_one.append(
      go.Bar(
      x = survived.index.tolist(),
      y = survived.values
      
      )
    )

    layout_one = dict(title = 'Percentage of survided passenger',
                xaxis = dict(title = 'Survived'),
                yaxis = dict(title = 'Percentage'),
                )

# second chart plots    Distribution of Age among the Survived people 
    graph_two = []

    graph_two.append(
      go.Box(
      x = titanic['Survived'].values,
      y = titanic['Age'].values,
      )
    )

    layout_two = dict(title = 'Distribution of Age among the Survived people',
                xaxis = dict(title = 'Survived',),
                yaxis = dict(title = 'Age'),
                )


# third chart plots relation between the survived people and their far
    graph_three = []
    graph_three.append(
      go.Bar(
      x = titanic['Survived'].values,
      y = titanic['Fare'].values,
      )
    )

    layout_three = dict(title = 'Relation between the survived <br> people and their far',
                xaxis = dict(title = 'Survived'),
                yaxis = dict(title = 'Fare')
                       )
    
# fourth chart shows rural population vs arable land
    graph_four = []
    sex = titanic['Sex'].value_counts(normalize=True)   
    graph_four.append(
      go.Bar(
      x = sex.index.tolist(),
      y = sex.values
      
      )
    )
    layout_four = dict(title = 'Percentage of sex representation',
                   xaxis = dict(title = 'Sex'),
                   yaxis = dict(title = 'Percentage')
              )
    
    # append all charts to the figures list
    figures = []
    figures.append(dict(data=graph_one, layout=layout_one))
    figures.append(dict(data=graph_two, layout=layout_two))
    figures.append(dict(data=graph_three, layout=layout_three))
    figures.append(dict(data=graph_four, layout=layout_four))

    return figures