def freelance_attributes(freelance, index, page_number):
    ranking       = index + 1
    full_name     = freelance.find('p', 'profile-card-header__full-name').string.strip()
    location      = freelance.find('p', 'profile-card-header__location').string.strip()
    freelance_url = freelance.find('a')['href'].split('?')[0] if freelance.find('a') != None else None
    rating        = freelance.find('div','profile-card-reputation__item').find(attrs={"data-rating-star":True})['data-rating-star'] \
                        if freelance.find('div','profile-card-reputation__item').find(attrs={"data-rating-star":True}) else None
    num_recos         = freelance.find('div','profile-card-reputation__recommendation-label').find('strong').text \
                                 if freelance.find('div','profile-card-reputation__recommendation-label') \
                                 else None
    num_missions  = freelance.find('div','profile-card-reputation__item') \
                             .find('span','sr-only') \
                             .previous_sibling.strip('()') if freelance.find('div','profile-card-reputation__item').find('span','sr-only') \
                             else None
    tjm           = freelance.find('p', 'profile-card-reputation__rate').find('strong').text
    badge         = freelance.find('div','profile-card__badge-level') \
                   .find('span') \
                   .text if freelance.find('div','profile-card__badge-level').find('span') else None
    title         = freelance.find('h2').text.strip().capitalize()
    dispo         = freelance.find('p','availability-indicator').text.strip() if freelance.find('p','availability-indicator') != None else None # Used to output ''
    dispo_details = freelance.find('p','availability-indicator')['class'] if freelance.find('p','availability-indicator') != None else None # Used to output ''
    if dispo_details is not None and len(dispo_details) > 1:
        del dispo_details[0]

    dict_freelance = {'ranking':ranking,
                        'full_name':full_name,
                        'location':location,
                        'freelance_url':freelance_url,
                        'rating':rating,
                        'num_missions':num_missions,
                        'num_recos':num_recos,
                        'tjm':tjm,
                        'badge':badge,
                        'title':title,
                        'dispo':dispo,
                        'dispo_details':dispo_details
                       }
    #print('Successfully parsed {}'.format(full_name))
    dict_freelance['page_number'] = page_number
    return dict_freelance, full_name


def freelance_skills(skill, full_name, skill_number):
    dict_skills = {'full_name':full_name,
                'skill':skill.text.strip(),
                'skill_ranking':skill_number,
                'skill_certified':skill.has_attr('data-content'),
                'skill_comment':skill['data-content'] if skill.has_attr('data-content') else None}
    return dict_skills
