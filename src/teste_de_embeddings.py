from db_vetorial import DBVetorial

db = DBVetorial()

print("📦 Total de documentos no banco:", len(db.collection.get()["documents"]))

consultas = ["salário", "reajuste", "adiantamento", "pagamento de salário"]
for consulta in consultas:
    print(f"\n🔎 Consulta: {consulta}")
    res = db.buscar(consulta, k=2)
    if res["documents"] and res["documents"][0]:
        for match in res["documents"][0]:
            print("🎯", match)
    else:
        print("⚠️ Nenhum resultado.")
