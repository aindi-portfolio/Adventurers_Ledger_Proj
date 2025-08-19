def applyExperienceGain(character, xpGained):
    xpCap = getXpCapForLevel(character.level); # e.g. 100 * level
    newXp = character.experience + xpGained
    newLevel = character.level
  
    while (newXp >= xpCap):
      newXp -= xpCap
      newLevel += 1
      xpCap = getXpCapForLevel(newLevel) # Recalculates the new xpCap based off the new level gained. This is important if the xpGained amount is high enough to level more than once.
    
    character.level = newLevel
    character.experience = newXp

    return character
  
  
def getXpCapForLevel(level):
   return 100 * level; # Adjust; In the Future create a scaling formula
  