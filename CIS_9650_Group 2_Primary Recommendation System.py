import pandas as pd ## to read csv file
import numpy as np

df = pd.read_csv("speed-dating2_V3.csv") ## reads the csv file which is saved into a variable
matched = df[df["match"] == 1] ## separate those who matched with a date

print("====================================================================")

def groups(row):
    if row['field'] == 'law' or row['field'] == 'mba' or row['field'] == 'economics' or row['field'] == 'business' or row['field'] == 'law and english literature [j.d./ph.d.]' or row['field'] == 'business school' or row['field'] == 'business; media' or row['field'] == 'money' or row['field'] == 'finance' or row['field'] == 'finance&economics' or row['field'] == 'mathematical finance' or row['field'] == 'business & international affairs' or row['field'] == 'operations research' or row['field'] == 'operations research [seas]' or row['field'] == 'marketing' or row['field'] == 'business [mba]' or row['field'] == 'business- mba' or row['field'] == 'economics; english' or row['field'] == 'economics; sociology' or row['field'] == 'international affairs - economic development' or row['field'] == 'business; marketing' or row['field'] == 'business/ finance/ real estate' or row['field'] == 'international affairs/finance' or row['field'] == 'international affairs' or row['field'] == 'international finance and business'  or row['field'] == 'international business' or row['field'] == 'international finance; economic policy' or row['field'] == 'international development' or row['field'] == 'business/law' or row['field'] == 'business and international affairs [mba/mia dual degree]' or row['field'] == 'master of international affairs' or row['field'] == 'mba / master of international affairs [sipa]' or row['field'] == 'finance/economics' or row['field'] == 'intellectual property law' or row['field'] == 'business consulting' or row['field'] == 'fundraising management' or row['field'] == 'law/business' or row['field'] == 'consulting' or row['field'] == 'math of finance' or row['field'] == 'mba - private equity / real estate' or row['field'] == 'general management/finance' or row['field'] == 'mba finance':
        return 'Business'
    elif row['field'] == 'social work' or row['field'] == 'german literature' or row['field'] == 'master of social work' or row['field'] == 'psychology and english' or row['field'] == 'english' or row['field'] == 'anthropology/education' or row['field'] == 'speech pathology' or row['field'] == 'speech language pathology' or row['field'] == 'ed.d. in higher education policy at tc' or row['field'] == 'higher ed. - m.a.' or row['field'] == 'school psychology' or row['field'] == 'counseling psychology' or row['field'] == 'creative writing [nonfiction]' or row['field'] == 'elementary education - preservice' or row['field'] == 'education leadership - public school administration' or row['field'] == 'history' or row['field'] == 'human rights: middle east' or row['field'] == 'sipa-international affairs' or row['field'] == 'african-american studies/history' or row['field'] == 'public health' or row['field'] == 'masters in public administration' or row['field'] == 'masters of social work&education' or row['field'] == 'political science' or row['field'] == 'organized psychology' or row['field'] == 'undergrad - gs' or row['field'] == 'journalism' or row['field'] == 'elementary/childhood education [ma]' or row['field'] == 'masters of social work' or row['field'] == 'communications' or row['field'] == 'international educational development' or row['field'] == 'education administration' or row['field'] == 'religion' or row['field'] == 'sociology' or row['field'] == 'polish' or row['field'] == 'philosophy' or row['field'] == 'theory'  or row['field'] == 'comparative literature' or row['field'] == 'history of religion' or row['field'] == 'modern chinese literature' or row['field'] == 'american studies [masters]' or row['field'] == 'english and comp lit' or row['field'] == 'clinical psychology' or row['field'] == 'psychology' or row['field'] == 'religion; gsas' or row['field'] == 'public administration' or row['field'] == 'master in public administration' or row['field'] == 'history [gsas - phd]' or row['field'] == 'american studies'  or row['field'] == 'japanese literature' or row['field'] == 'philosophy [ph.d.]' or row['field'] == 'ma science education' or row['field'] == 'french' or row['field'] == 'social studies education' or row['field'] == 'education policy' or row['field'] == 'education- literacy specialist' or row['field'] == 'bilingual education' or row['field'] == 'education' or row['field'] == 'math education' or row['field'] == 'tesol' or row['field'] == 'elementary education' or row['field'] == 'cognitive studies in education' or row['field'] == 'museum anthropology' or row['field'] == 'curriculum and teaching/giftedness' or row['field'] == 'english education' or row['field'] == 'urban planning' or row['field'] == 'international security policy - sipa' or row['field'] == 'communications in education' or row['field'] == 'creative writing' or row['field'] == 'creative writing - nonfiction' or row['field'] == 'writing: literary nonfiction' or row['field'] == 'nonfiction writing' or row['field'] == 'education leadership - public school administration' or row['field'] == 'mfa writing' or row['field'] == 'sipa - energy' or row['field'] == 'public policy' or row['field'] == 'human rights' or row['field'] == 'teaching of english' or row['field'] == 'gsas' or row['field'] == 'mfa creative writing' or row['field'] == 'mfa acting program' or row['field'] == 'organizational psychology' or row['field'] == 'international relations' or row['field'] == 'anthropology':
        return 'Social Science/Humanities'
    elif row['field'] == 'applied maths/econs' or row['field'] == 'statistics' or row['field'] == 'mathematics' or row['field'] == 'architecture' or row['field'] == 'physics' or row['field'] == 'stats' or row['field'] == 'qmss' or row['field'] == 'ma in quantitative methods' or row['field'] == 'architecture' or row['field'] == 'math':
        return 'Science(Physics, Architecture, Math)'   
    elif row['field'] == 'biology' or row['field'] == 'gs postbacc premed' or row['field'] == 'epidemiology' or row['field'] == 'medicine' or row['field'] == 'biotechnology' or row['field'] == 'tc [health ed]' or row['field'] == 'chemistry' or row['field'] == 'microbiology' or row['field'] == 'climate-earth and environ. science' or row['field'] == 'marine geophysics' or row['field'] == 'nutrition/genetics' or row['field'] == 'nutrition' or row['field'] == 'applied physiology & nutrition' or row['field'] == 'biochemistry' or row['field'] == 'cell biology' or row['field'] == 'health policy' or row['field'] == 'sociomedical sciences- school of public health' or row['field'] == 'medical informatics' or row['field'] == 'international affairs and public health' or row['field'] == 'climate' or row['field'] == 'ma biotechnology' or row['field'] == 'ecology' or row['field'] == 'computational biochemistry' or row['field'] == 'neurobiology' or row['field'] == 'biomedicine' or row['field'] == 'conservation biology' or row['field'] == 'biotechnology' or row['field'] == 'genetics' or row['field'] == 'molecular biology' or row['field'] == 'genetics & development' or row['field'] == 'medicine and biochemistry' or row['field'] == 'neuroscience and education' or row['field'] == 'neurosciences/stem cells' or row['field'] == 'biochemistry & molecular biophysics' or row['field'] == 'biomedical informatics' or row['field'] == 'climate dynamics' or row['field'] == 'climate change':
        return 'Biology/Chemistry/Ecology/Medical'
    elif row['field'] == 'arts administration' or row['field'] == 'art history' or row['field'] == 'art education' or row['field'] == 'music education' or row['field'] == 'mfa -film' or row['field'] == 'theatre management & producing' or row['field'] == 'film' or row['field'] == 'theater' or row['field'] == 'classics' or row['field'] == 'art history/medicine' or row['field'] == 'art administration':
        return 'Art'
    elif row['field'] == 'electrical engineering' or row['field'] == 'computer science' or row['field'] == 'industrial engineering' or row['field'] == 'mechanical engineering' or row['field'] == 'engineering' or row['field'] == 'electrical engg.' or row['field'] == 'environmental engineering' or row['field'] == 'instructional media and technology' or row['field'] == 'instructional tech & media' or row['field'] == 'financial engineering' or row['field'] == 'biomedical engineering' or row['field'] == 'industrial engineering/operations research' or row['field'] == 'masters of industrial engineering':
        return 'Engineering/Technology'
    else: 
        return 'NaN'
    
matched["Career"] = matched.apply(groups, axis = 1)
## Added a new column "Career" where each row was based on the "field" column.
## This was done to make categorizing jobs easier, as the filed column had over 100 groups.

new_matched = matched.reset_index(drop = True) ## resets index to add ID to each row. Old index is based on original dataframe
new_matched['ID'] = new_matched.index + 1 ## ID is set to the index. We add plus one since index begins at 0

cols = new_matched.columns.tolist() # sets column names to new variable in order to reorder the ID column as the first column
cols = cols[-1:] + cols[:-1] ## ID column becomes first column within the variable

new_matched = new_matched[cols] ## Variable is added to the dataframe to get ID as the first column

# cols = new_matched.columns.tolist() used this to see the names of the columns in order to rename them

matched2 = new_matched[["ID", "gender", "age", "Career","race","importance_same_race",
                        "importance_same_religion","attractive_important","sincere_important",
                        "intelligence_important","funny_important","ambition_important",
                        "shared_interests_important", "sports","exercise","museums","art",
                        "hiking","gaming","clubbing","reading","theater","movies","concerts",
                        "yoga"]]
matched2.rename(columns = {"gender":"Gender", "age":"Age", "race":"Race", "importance_same_race":"Race_Important",
                           "importance_same_religion":"Religion_Important","attractive_important":"Attractive_Important", 
                           "sincere_important":"Sincere_Important", "intelligence_important":"Intelligence_Important",
                           "funny_important":"Funny_Important","ambition_important":"Ambition_Important","shared_interets_important":"Shared_Interets_Important",
                           "sports":"Sports","exercise":"Exercise","museums":"Museums","art":"Art","hiking":"Hiking","gaming":"Gaming",
                           "clubbing":"Night Club","reading":"Reading","theater":"Theater","movies":"Movies","concerts":"Concerts",
                           "yoga":"Yoga"}, inplace = True)

## new dataframe is saved with inplace = True and can now be use for the while loop 
## While loop will use user input to determine the selection.

## Our Reccomendation System

while True:
    
    print("\nWelcome to our blind-dating service!")
    print("Let's find you your perfect match(es).")
    name = input("First, what is your name? ")
    
    typ = int(input("How old do you want your date to be? "))
    if typ < 21 or typ > 42:
        print("\nSorry, no one under 21 or over 42 is in our blind-dating service.")
        continue
    
    print("Great! Now let's go over some perferences.")
    gen = str(input("Interested in female or male? "))
    act = str(input("Do you want to have an active lifestyle? (y/n) "))
    ind = str(input("Would you rather spend your time indoors at home? (y/n) "))
    indOut = str(input("Would you rather be indoors somewhere else? (y/n) "))
    car = str(input("Do you want your partner to have the same career? (y/n) "))
    
    if act == "y" and ind == "n" and indOut == "n" and car == "n":
        print("Which activity is your favorite?")
        actH = str(input("Sports, Exercise, Hiking, Yoga: "))
        actH_rating = int(input("How would you rate it? (1-10) "))
        perf = matched2[
        (matched2['Age'] == typ) & 
        (matched2['Gender'] == gen) & 
        (matched2[actH] == actH_rating)
        ]
    elif act == "n" and ind == "y" and indOut == "n" and car == "n":  
        print("Which home activity is your favorite?")
        actH = str(input("Movies, Art, Gaming, Reading: "))
        actH_rating = int(input("How would you rate it? (1-10) "))
        perf = matched2[
        (matched2['Age'] == typ) & 
        (matched2['Gender'] == gen) & 
        (matched2[actH] == actH_rating)
        ]
    elif act == "n" and ind == "n" and indOut == "y" and car == "n":
        print("Choose your favorite place to be:")
        actH = str(input("Theater, Museums, Concerts, Night Club: "))
        actH_rating = int(input("How would you rate it? (1-10) "))
        perf = matched2[
        (matched2['Age'] == typ) & 
        (matched2['Gender'] == gen) & 
        (matched2[actH] == actH_rating)
        ]
    elif act == "n" and ind == "n" and indOut == "n" and car == "y":
        print("\nPlease pick one of the following options: ")
        gps = str(input("Art, Biology/Chemistry/Ecology/Medicial, Business, Engineering/Technology, Science(Physics, Architecture, Math), Social Science/Humanities: "))
        perf = matched2[
        (matched2['Age'] == typ) & 
        (matched2['Gender'] == gen) & 
        (matched2["Career"] == gps)
        ]
    elif act == "y" and ind == "y" and indOut == "y" and car == "y":
        print("Which activity is your favorite?")
        actH = str(input("Sports, Exercise, Hiking, Yoga: "))
        actH_rating = int(input("How would you rate it? (1-10) "))
        print("Which home activity is your favorite?")
        actH2 = str(input("Movies, Art, Gaming, Reading: "))
        actH_rating2 = int(input("How would you rate it? (1-10) "))
        print("Choose your favorite place to be:")
        actH3 = str(input("Theater, Museums, Concerts, Night Club: "))
        actH_rating3 = int(input("How would you rate it? (1-10) "))
        print("\nPlease pick one of the following options: ")
        gps = str(input("Art, Biology/Chemistry/Ecology/Medicial, Business, Engineering/Technology, Science(Physics, Architecture, Math), Social Science/Humanities: "))
        perf = matched2[
        (matched2['Age'] == typ) & 
        (matched2['Gender'] == gen) & 
        (matched2[actH] == actH_rating) &
        (matched2[actH2] == actH_rating2) &
        (matched2[actH3] == actH_rating3) &
        (matched2["Career"] == gps)
        ]
    elif act == "y" and ind == "y" and indOut == "n" and car == "n":
        print("Which activity is your favorite?")
        actH = str(input("Sports, Exercise, Hiking, Yoga: "))
        actH_rating = int(input("How would you rate it? (1-10) "))
        print("Which home activity is your favorite?")
        actH2 = str(input("Movies, Art, Gaming, Reading: "))
        actH_rating2 = int(input("How would you rate it? (1-10) "))
        perf = matched2[
        (matched2['Age'] == typ) & 
        (matched2['Gender'] == gen) & 
        (matched2[actH] == actH_rating) &
        (matched2[actH2] == actH_rating2)
        ]
    elif act == "y" and ind == "y" and indOut == "y" and car == "n":
        print("Which activity is your favorite?")
        actH = str(input("Sports, Exercise, Hiking, Yoga: "))
        actH_rating = int(input("How would you rate it? (1-10) "))
        print("Which home activity is your favorite?")
        actH2 = str(input("Movies, Art, Gaming, Reading: "))
        actH_rating2 = int(input("How would you rate it? (1-10) "))
        print("Choose your favorite place to be:")
        actH3 = str(input("Theater, Museums, Concerts, Night Club: "))
        actH_rating3 = int(input("How would you rate it? (1-10) "))
        perf = matched2[
        (matched2['Age'] == typ) & 
        (matched2['Gender'] == gen) & 
        (matched2[actH] == actH_rating) &
        (matched2[actH2] == actH_rating2) &
        (matched2[actH3] == actH_rating3)
        ]
    elif act == "n" and ind == "y" and indOut == "y" and car == "n":  
        print("Which home activity is your favorite?")
        actH = str(input("Movies, Art, Gaming, Reading: "))
        actH_rating = int(input("How would you rate it? (1-10) "))
        print("Choose your favorite place to be:")
        actH2 = str(input("Theater, Museums, Concerts, Night Club: "))
        actH_rating2 = int(input("How would you rate it? (1-10) "))
        perf = matched2[
        (matched2['Age'] == typ) & 
        (matched2['Gender'] == gen) & 
        (matched2[actH] == actH_rating) &
        (matched2[actH2] == actH_rating2)
        ]
    elif act == "n" and ind == "y" and indOut == "y" and car == "y":  
        print("Which home activity is your favorite?")
        actH = str(input("Movies, Art, Gaming, Reading: "))
        actH_rating = int(input("How would you rate it? (1-10) "))
        print("Choose your favorite place to be:")
        actH2 = str(input("Theater, Museums, Concerts, Night Club: "))
        actH_rating2 = int(input("How would you rate it? (1-10) "))
        print("\nPlease pick one of the following options: ")
        gps = str(input("Art, Biology/Chemistry/Ecology/Medicial, Business, Engineering/Technology, Science(Physics, Architecture, Math), Social Science/Humanities: "))
        perf = matched2[
        (matched2['Age'] == typ) & 
        (matched2['Gender'] == gen) & 
        (matched2[actH] == actH_rating) &
        (matched2[actH2] == actH_rating2) &
        (matched2["Career"] == gps)
        ]
    elif act == "n" and ind == "n" and indOut == "y" and car == "y":
        print("Choose your favorite place to be:")
        actH = str(input("Theater, Museums, Concerts, Night Club: "))
        actH_rating = int(input("How would you rate it? (1-10) "))
        print("\nPlease pick one of the following options: ")
        gps = str(input("Art, Biology/Chemistry/Ecology/Medicial, Business, Engineering/Technology, Science(Physics, Architecture, Math), Social Science/Humanities: "))
        perf = matched2[
        (matched2['Age'] == typ) & 
        (matched2['Gender'] == gen) & 
        (matched2[actH] == actH_rating) &
        (matched2["Career"] == gps)
        ]
    elif act == "y" and ind == "n" and indOut == "y" and car == "n":
        print("Which activity is your favorite?")
        actH = str(input("Sports, Exercise, Hiking, Yoga: "))
        actH_rating = int(input("How would you rate it? (1-10) "))
        print("Choose your favorite place to be:")
        actH2 = str(input("Theater, Museums, Concerts, Night Club: "))
        actH_rating2 = int(input("How would you rate it? (1-10) "))
        perf = matched2[
        (matched2['Age'] == typ) & 
        (matched2['Gender'] == gen) & 
        (matched2[actH] == actH_rating) &
        (matched2[actH2] == actH_rating2)
        ]
    elif act == "y" and ind == "n" and indOut == "n" and car == "y":
        print("Which activity is your favorite?")
        actH = str(input("Sports, Exercise, Hiking, Yoga: "))
        actH_rating = int(input("How would you rate it? (1-10) "))
        print("\nPlease pick one of the following options: ")
        gps = str(input("Art, Biology/Chemistry/Ecology/Medicial, Business, Engineering/Technology, Science(Physics, Architecture, Math), Social Science/Humanities: "))
        perf = matched2[
        (matched2['Age'] == typ) & 
        (matched2['Gender'] == gen) & 
        (matched2[actH] == actH_rating) &
        (matched2["Career"] == gps)
        ]
    elif act == "n" and ind == "y" and indOut == "n" and car == "y":
        print("Which home activity is your favorite?")
        actH = str(input("Movies, Art, Gaming, Reading: "))
        actH_rating = int(input("How would you rate it? (1-10) "))
        print("\nPlease pick one of the following options: ")
        gps = str(input("Art, Biology/Chemistry/Ecology/Medicial, Business, Engineering/Technology, Science(Physics, Architecture, Math), Social Science/Humanities: "))
        perf = matched2[
        (matched2['Age'] == typ) & 
        (matched2['Gender'] == gen) & 
        (matched2[actH] == actH_rating) &
        (matched2["Career"] == gps)
        ]
    elif act == "y" and ind == "n" and indOut == "y" and car == "y":  
        print("Which activity is your favorite?")
        actH = str(input("Sports, Exercise, Hiking, Yoga: "))
        actH_rating = int(input("How would you rate it? (1-10) "))
        print("Choose your favorite place to be:")
        actH2 = str(input("Theater, Museums, Concerts, Night Club: "))
        actH_rating2 = int(input("How would you rate it? (1-10) "))
        print("\nPlease pick one of the following options: ")
        gps = str(input("Art, Biology/Chemistry/Ecology/Medicial, Business, Engineering/Technology, Science(Physics, Architecture, Math), Social Science/Humanities: "))
        perf = matched2[
        (matched2['Age'] == typ) & 
        (matched2['Gender'] == gen) & 
        (matched2[actH] == actH_rating) &
        (matched2[actH2] == actH_rating2) &
        (matched2["Career"] == gps)
        ]
        
    print(f"\nThank you {name} for using our service.")
    print(len(perf),"potential matches found!")
    print("You can view all matches below:")
    print(perf[["ID", "Race","Sports","Reading","Concerts"]])
    
    anotherEntry = input("Another entry? (y/n) ")
    if anotherEntry == "n":
        break
print("Have a great time with your blind date(s)!")










