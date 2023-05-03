import inquirer

def menu():
    form = [
        inquirer.List('lang',
        message='what language?',
        choices=['en', 'pt-br']),

        inquirer.List('season',
        message='what season?',
        choices=['current', 'i will choose']
        )
    ]

    response = inquirer.prompt(form)

    if response['lang'] == 'en':
        lang = 'en'
        
    elif response['lang'] == 'pt-br':
        lang = 'pt-br'

    if response['season'] == 'current':
        season = 'current'

        return lang, season

    elif response['season'] == 'i will choose':
        formSeason = [
            inquirer.List('season',
            message='what season? (month)',
            choices=['Winter(1,2,3)', 'Spring(4,5,6)', 'Summer(7,8,9)', 'Fall(10,11,12)']
            ),inquirer.Text('year', message="What year? ex: 2018"),
        ]

        r = inquirer.prompt(formSeason)
        
        

        if r['season'] == 'Winter(1,2,3)':
            season = 'winter'
            
        elif r['season'] == 'Spring(4,5,6)':
            season = 'spring'
            
        elif r['season'] == 'Summer(7,8,9)':
            season = 'summer'

        elif r['season'] == 'Fall(10,11,12)':
            season = 'fall'

        else:
            season = 'winter'
        
        year = r['year']
        year = year.strip()
        
        season = year + ' ' + season

        return lang, season
    
if __name__ == '__main__':
    menu()