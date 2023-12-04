### THIS RUNS REGEX ON PATIENT NOTES TEXT TO EXTRACT EVIDENCE OF HOUSING INSECURITY ###

housing_insecurity_regex = r"(?i)\b(?:homeless|unstable hous|evict|Houseless|hotel|motel|tent\b|RV|encampment|housing insecurity|housing needs|lack of housing|SLS|supportive living services|couch surfing|shelter|transitional housing)"

def housing_regex_match_bool(s):
    result = None
    if type(s) is str:
        result =  re.search(housing_insecurity_regex, s)
    return result is not None

def housing_regex_match(s):
    result = None
    if type(s) is str:
        result =  re.search(housing_insecurity_regex, s)
    return result.group() if result else None


def run_regex(df):

    # Replace 'full_text' with the name of the field containing the patient notes 
    df['HousingInstability_regex_bool'] = df.apply(lambda x: housing_regex_match_bool(x['full_text']), axis=1)
    df['HousingInstability_regex'] = df.apply(lambda x: housing_regex_match(x['full_text']), axis=1)

    return df    

## USAGE ##

# df_with_regex = run_regex(df)

