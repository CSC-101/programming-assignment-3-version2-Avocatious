from data import CountyDemographics
import county_demographics



## Task 1:
def population_total(counties: list[CountyDemographics]) -> int:
    """ This function returns the total 2014 population from a provided list """
    total_population = 0
    for county in counties:
        total_population += county.population['2014 Population']
    return total_population
    #When I return the full data set the population will be 318857056

## Task 2:
def filter_by_state(county_demographics: list[CountyDemographics], state: str) -> list[CountyDemographics]:
    return [county for county in county_demographics if county.state == state]

## Task 3:
def population_by_education(counties: list[CountyDemographics], key: str) -> float:
    """ this function returns the total population given by education percentage"""
    total = 0.0
    for county in counties:
        if key in county.education:
            total += (county.education[key] / 100) * county.population['2014 Population']
    return total

def population_by_ethnicity(counties: list[CountyDemographics], key: str) -> float:
    """function calculates the total population by ethnicity"""
    total = 0.0
    for county in counties:
        if key in county.ethnicities:
            total += (county.ethnicities[key] / 100) * county.population['2014 Population']
    return total

def population_below_poverty_level(counties: list[CountyDemographics]) -> float:
    """function calculates the population below poverty level"""
    total = 0.0
    for county in counties:
        if 'Persons Below Poverty Level' in county.income:
            total += (county.income['Persons Below Poverty Level'] / 100) * county.population['2014 Population']
    return total

## Task 4:
def percent_by_education(counties: list[CountyDemographics], key: str) -> float:
    """Calculate the percentage of population by education level"""
    sub_pop = population_by_education(counties, key)
    total_pop = population_total(counties)
    if total_pop == 0:
        return 0.0
    return (sub_pop / total_pop) * 100

def percent_by_ethnicity(counties: list[CountyDemographics], key: str) -> float:
    """Calculate the percentage of population by ethnicity"""
    sub_pop = population_by_ethnicity(counties, key)
    total_pop = population_total(counties)
    if total_pop == 0:
        return 0.0
    return (sub_pop / total_pop) * 100

def population_by_income(counties: list[CountyDemographics]) -> float:
    """Calculate the total population below the poverty level across the counties"""
    total = 0.0
    for county in counties:
        # Make sure the 'Persons Below Poverty Level' key exists in the county data
        if 'Persons Below Poverty Level' in county.income:
            # Calculate the subppopulation of people below the poverty level
            total += (county.income['Persons Below Poverty Level'] / 100) * county.population['2014 Population']
    return total

def percent_by_education(counties: list[CountyDemographics]) -> float:
    """Calculate the percentage of population below the poverty level"""
    sub_pop = population_by_income(counties)
    total_pop = population_total(counties)
    if total_pop == 0:
        return 0.0
    return (sub_pop / total_pop) * 100

## Task 5:
def education_greater_than(counties: list[CountyDemographics], key: str, threshold: float) -> list[CountyDemographics]:
    """Return counties with education percentage greater than threshold"""

    return [county for county in counties if key in county.education and county.education[key] > threshold]
def education_less_than(counties: list[CountyDemographics], key: str, threshold: float) -> list[CountyDemographics]:
    """Return counties with education percentage less than threshold"""
    return [county for county in counties if key in county.education and county.education[key] < threshold]

def ethnicity_greater_than(counties: list[CountyDemographics], key: str, threshold: float) -> list[CountyDemographics]:
    """Return counties with ethnicity percentage greater than threshold"""
    return [county for county in counties if key in county.ethnicities and county.ethnicities[key] > threshold]


def ethnicity_less_than(counties: list[CountyDemographics], key: str, threshold: float) -> list[CountyDemographics]:
    """Return counties with ethnicity percentage less than threshold"""
    return [county for county in counties if key in county.ethnicities and county.ethnicities[key] < threshold]

def below_poverty_level_greater_than(counties: list[CountyDemographics], threshold: float) -> list[CountyDemographics]:
    """Return counties with persons below poverty level percentage greater than threshold"""
    return [county for county in counties if "Persons Below Poverty Level" in county.population and county.population["Persons Below Poverty Level"] > threshold]

def below_poverty_level_less_than(counties: list[CountyDemographics], threshold: float) -> list[CountyDemographics]:
    """Return counties with persons below poverty level percentage less than threshold"""
    return [county for county in counties if "Persons Below Poverty Level" in county.population and county.population["Persons Below Poverty Level"] < threshold]
