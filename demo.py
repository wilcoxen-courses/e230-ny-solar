"""
demo.py
Spring 2022 PJW

Demonstrate some basic features of Pandas.
"""

import pandas as pd

#
#  Make sure all rows are printed
#

pd.set_option('display.max_rows', None)

#
#  Read the file into a DataFrame
#

raw_states = pd.read_csv('state-data.csv')

#
#  Show its type
#

print( '\nraw_states is a DataFrame object:', type(raw_states) )

#%%

#
#  What does the DataFrame look like?
#

print( '\nContents of raw_states:' )
print(raw_states)

#%%

#
#  Columns and index?
#

print( '\nColumns:', list(raw_states.columns) )
print( '\nIndex (rows):', list(raw_states.index) )

#%%

#
#  Construct a new DataFrame that uses the names as the
#  index.
#

states = raw_states.set_index('name')

print( '\nStates after index set:')
print(states)

#%%

#
#  Get a column and do some things with it. Works just like a dictionary
#  where the column name is the key and the column is the value.
#

pop = states['pop']

print( '\nPopulation:' )
print( pop )
print( '\nPop is a Series object:', type(pop) )
print( '\nIndex:', list(pop.index) )

#%%

#
#  Get a subset of pops and print them in millions
#

some_states = ['California','Texas','New York']

print( '\nData for selected states:')
print( pop[some_states]/1e6 )

#
#  Get a single population; note that it's a scalar, not
#  a Series.
#

print( "\nFlorida's population:", pop['Florida']/1e6 )

#%%

#
#  Get a row. Use .loc[] to indicate that we want to pick out a
#  row using the index.
#

pa_row = states.loc['Pennsylvania']
print( '\nPA row, returned as a series and printed vertically:')
print(pa_row)

#%%

#
#  Normalize the columns in states by the PA row. Multiply by
#  100 to convert things to percentages of PA. The two approaches
#  below are equivalent.
#

normed = 100*states/pa_row
normed2 = 100*states.div(pa_row,axis='columns')

print( '\nNormed by PA, method 1:')
print(normed)

print( '\nNormed by PA, method 2')
print(normed2)

#%%
#
#  Pick out normalized median personal income and sort it from low
#  to high. Then round it to 2 places using the .round() method.
#

low_to_high = normed['med_pers_inc'].sort_values()
low_to_high = low_to_high.round(2)

#
#  Print the normalized incomes rounded to 2 places.
#

print( '\nMedian personal income relative to PA:')
print( low_to_high )

#%%

#
#  Print the bottom 10 using .iloc[], which picks out rows using
#  integers starting at 0.
#

print( '\nStates with the lowest median personal income, relative to PA:')
print( low_to_high.iloc[ 0:10 ] )

#
#  print the top 5, which are at the end
#

print( '\nStates with the highest median personal income, relative to PA:')
print( low_to_high.iloc[ -5: ] )

#
#  alternative: use list indexing:
#

print( '\nUsing list indexing:' )
print( low_to_high[ -5: ] )
