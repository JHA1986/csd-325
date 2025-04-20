# Jonah Aney CSD325 Module 7.2 Assignment: Test Cases

# The function that accepts the parameters, city, country, population, language.
# Population and language being optional. -JHA
def get_location(city, country, population=None, language=None):
# Formated string with city and country parameters. - JHA
    base = f"{city.title()}, {country.title()}"
# Add population and language parameters if available - JHA
    if population:
        base += f" - population {population}"
    if language:
        base += f" - {language}"
    return base
# Display strings using the values given for the parameters. - JHA
print(get_location("Omaha","United States"))
print(get_location("Sidney", "Australia", "5,000,000"))
print(get_location("Calgary", "Canada", "1,400,000", "English"))
