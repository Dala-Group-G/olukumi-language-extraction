import re
import pandas as pd
def olukumi_data(file):
    # Load file
    with open(file,'r',encoding='utf-8') as f:
        text = f.read()

    # Define the pattern
    pattern = r"""
        ^([^\[\n]+?)\s*     # Local word (anything before [ )
        \[([^\]]+)\]\s+     # IPA in brackets
        ([a-z,\s]+\.?)\s*      # POS like n. v. adj.
        (.*?)               # Meaning: anything, including newlines
        (?=^[^\[\n]+?\s*\[|\Z) # Until next word [IPA] or end
    """

    # Extract matches
    matches = re.findall(pattern, text, re.MULTILINE | re.DOTALL | re.VERBOSE)

    # Put into a Dataframe
    df = pd.DataFrame(matches,columns=['Local Word','Pronunciation','POS','English Meaning'])

    # clean up 
    df['Local Word'] = df['Local Word'].str.strip().str.rstrip(':')
    df['English Meaning'] = df['English Meaning'].str.replace('\n','',regex=False).str.replace('\s+',' ',regex=True).str.strip().str.rstrip('.')

    df = df[['Local Word','English Meaning']]
    df.head(20)
    df.to_csv('olukumi_local_english.csv',index=False)