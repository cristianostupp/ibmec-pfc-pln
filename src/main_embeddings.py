from db_vetorial import DBVetorial

db = DBVetorial()
res = db.buscar("reajuste salarial", k=3)

for match in res["documents"][0]:
    print("🎯 Resultado:", match)
