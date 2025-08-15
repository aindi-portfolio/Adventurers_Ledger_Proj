# Django + PostgreSQL

This directory holds all the necessary files to run the data base.

Ensure you install all the dependencies from the requirements.txt file.

list of features:
1. Seed items - armor, weapons, equipment, monsters (D&D api)
2. stater items
3. encounter - fighting
    button for escape - character is able to escape the encounter - view function
    button for attack - both lose health - decreasing the monster health 
        rounds: calculate for each round on the front end
            check if someone lost after each round, update front-end, then back-end


starter_item:
 character
 user creates a new character: in views do a db querry of * items that have the specified names