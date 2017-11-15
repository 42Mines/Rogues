weapons = {}
weapons["sword"] = {damages: 10, instability: 0.1}
weapons["axe"]   = {damages: 12, instability: 3}

hero = {life: 100, char: 'P', xp_reward:0, weapon: weapons["sword"]}

ennemies = {}
ennemies["snake"] = {life: 12, char: 'S', xp_reward: 10, weapon: {damages: 5, instability: 0.01}}
ennemies["ghost"] = {life: 20, char: 'G', xp_reward: 30, weapon: {damages: 7, instability: 2}}