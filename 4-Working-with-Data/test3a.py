import pandas as pd

songs = {'Album':['Thriller','Back in Black', 'The Dark Side of the Moon','The Bodyguard','Bat out of Hell'],'Released':[1982,1980,1793,1992,1977],'Length':['00:42:19','00:42:19','00:42:19','00:42:19','00:42:19']}

df = pd.DataFrame(songs)

x = df['Length']