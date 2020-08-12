def refactoring_data(df):
    ##### Global ranking #####
    NUM_FREELANCES_PER_PAGE = 24
    df['global_ranking']    = df['ranking'] + (df['page_number'] - 1) * NUM_FREELANCES_PER_PAGE
    lambda_func             = lambda x : 'Not available - Info not provided' if (x == '' or x is None) \
                                    else ('Available Full Time' if x[1] == 'FULL_TIME' \
                                             else 'Available Partial' if x[1] == 'PARTIAL' \
                                             else 'Not Available')
    df['dispo_final']       = df['dispo_details'].map(lambda_func)
    df['global_ranking']    = df['global_ranking'].astype(int)
    df['ranking']           = df['ranking'].astype(int)
    df['page_number']       = df['page_number'].astype(int)
    df['rating']            = df['rating'].astype(float)
    df['tjm']               = df['tjm'].str.strip('€').str.replace(u'\xa0', u'') # replace(u'\xa0', ' ') is for thousands : 1 250 is interpreted as 1\xa0250
    df['tjm']               = df['tjm'].astype(int)
    df['num_missions']      = df['num_missions'].fillna(0).astype(int) 
