import streamlit as st
import pandas as pd
import altair as alt
from PIL import Image

#Title

image = Image.open('DNA_Logo.jfif')

st.image(image, use_column_width = True)

st.write("""
# DNA Nucleotide Count Web App
         
This app counts Nucleotide composition of query DNA         
         
""")

#Input Text Box

#Header
st.header('Enter DNA sequence')

sequence_input = "GAACACGTGGAGGCAAACAGGAAGGTGAAGAAGAACTTATCCTATCAGGACGGAAGGTCCTGTGCTCGGG\nATCTTCCAGACGTCGCGACTCTAAATTGCCCCCTCTGAGGTCAAGGAACACAAGATGGTTTTGGAAATGC\nTGAACCCGATACATTATAACATCACCAGCATCGTGCCTGAAGCCATGCCTGCTGCCACCATGCCAGTCCT"

#Input Box Modifications

sequence = st.text_area("Sequence Input", sequence_input, height = 300) #Modifications for the text input
sequence = sequence.splitlines() #Split the sequence to create a list of each line
#sequence = sequence[1:] #This slices to skip sequence name (which is the first line) when reading sequence code
sequence = ''.join(sequence) #Concats lists to Strings To form one line of sequence 

st.write("""
         
***         
""")

### Prints the Inputed DNA Sequence
st.header('SEQUENCE INPUT')
sequence

#DNA Nucleotide Count
st.header('RESULT OUTPUT - DNA NUCLEOTIDE COUNT')


# Print Dictionary
st.subheader('Nucleotide Count Summary')
def DNA_nucleotide_count(seq):
    d = dict([
              ('A', seq.count('A')),
              ('T',seq.count('T')),
              ('G',seq.count('G')),
              ('C',seq.count('C'))
              ])
    return d

X = DNA_nucleotide_count(sequence)

X_label = list(X)
X_values = list(X.values())

X

# PRINT DETAILS
st.subheader('Detailed Result Breakdown')
st.write('There are ' + str(X['A']) + ' adenine (A)')
st.write('There are ' + str(X['T']) + ' thymine (T)')
st.write('There are ' + str(X['G']) + ' guanine (G)')
st.write('There are ' + str(X['C']) + ' cytosine (C)')


#Print DataFrame
st.subheader('Tabular Result Breakdown')
df = pd.DataFrame.from_dict(X, orient='index')
df = df.rename({0: 'count'}, axis = 'columns')
df.reset_index(inplace = True)
df.reset_index(inplace = True)
df = df.rename(columns = {'index': 'nucleotide'})
st.write(df)

#Visualization
st.subheader('Result Visualization')
p = alt.Chart(df).mark_bar().encode(
    x = 'nucleotide',
    y = 'count'
)

p = p.properties(
    width=alt.Step(80) #Bar Width to make it thicker
)

st.write(p)  