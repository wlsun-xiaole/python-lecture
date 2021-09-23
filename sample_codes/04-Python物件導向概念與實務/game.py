import rpg_simple as rpg

Player1 = rpg.Knight("Winnie")
Player2 = rpg.Wizard("Maruko")

# Start
print('==== Start ====')
Player1.showStatus()
Player2.showStatus()
print('===============')

# Round 1
## Player 1 攻擊
atk_point = Player1.attack()
## Player 2 防守
def_res = Player2.defense(atk_point)
## 更新 Player 2 血量
Player2.updateHP(def_res)

print('=== Round 1 ===')
Player1.showStatus()
Player2.showStatus()
print('===============')

# Round 2
## Player 2 攻擊
atk_point = Player2.attack()
## Player 1 防守
def_res = Player1.defense(atk_point)
## 更新 Player 1 血量
Player1.updateHP(def_res)

print('=== Round 2 ===')
Player1.showStatus()
Player2.showStatus()
print('===============')
