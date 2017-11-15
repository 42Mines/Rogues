weapons_conf = {}
weapons_conf["sword"] = {"damages": 10, "instability": 0.1}
weapons_conf["axe"]   = {"damages": 12, "instability": 3}

hero_conf = {"life": 100, "char": 'P', "xp_reward":0, "weapon": weapons_conf["sword"], "type": "Hero"}

ennemies_conf = {}
ennemies_conf["snake"] = {"life": 12, "char": 'S', "xp_reward": 10, "weapon": {"damages": 5, "instability": 0.01}, "type": "Snake"}
ennemies_conf["ghost"] = {"life": 20, "char": 'G', "xp_reward": 30, "weapon": {"damages": 7, "instability": 2}, "type": "Ghost"}
