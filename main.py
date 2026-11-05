from fastapi import FastAPI

app = FastAPI(title="API do Sistema Alimentício")

matriculas = [
    { "id": 1, "MatriculaAluno": "20211gestao.tmn0001", "Nome": "Beatriz Lima", "Idade": 21, "Turma": "Gestão" },
    { "id": 2, "MatriculaAluno": "20241ed.tmn0002", "Nome": "Carlos Eduardo", "Idade": 17, "Turma": "Edificação" },
    { "id": 3, "MatriculaAluno": "20241ed.tmn0003", "Nome": "Mariana Souza", "Idade": 17, "Turma": "Edificação" },
    { "id": 4, "MatriculaAluno": "20221inf.tmn0066", "Nome": "Lucas Gabriel", "Idade": 19, "Turma": "Informática" }
]

@app.get("/")
def inicio():
    return { "mensagem": "API da Escola e Alimentação funcionando!" }

@app.get("/matriculas")
def listar_matriculas():
    return { "matriculas": matriculas }

@app.get("/Nome")
def listar_nomes():
    return { "Nome": sorted(set(matricula["Nome"] for matricula in matriculas)) }

@app.get("/Idade")
def listar_idade():
    return { "Idade": sorted(set(matricula["Idade"] for matricula in matriculas)) }

@app.get("/matriculas/{id}")
def buscar_matricula(id: int):
    for matricula in matriculas:
        if matricula["id"] == id:
            return matricula
    return { "erro": "Matrícula não encontrada" }

@app.get("/matriculas/Nome/{Nome}")
def buscar_por_nome(Nome: str):
    resultados = []
    for m in matriculas:
        if Nome.lower() in m["Nome"].lower():
            resultados.append(m)
            
    if resultados:
        return { "resultados": resultados }
    return { "erro": "Nome não encontrado" }

@app.get("/matriculas/Turma/{Turma}")
def buscar_por_Turma(Turma: str):
    resultados = []
    for m in matriculas:
        if m["Turma"].lower() == Turma.lower():
            resultados.append(m)
            
    if resultados:
        return { "resultados": resultados }
    return { "erro": "Turma não encontrada" }

@app.get("/matriculas/Idade/{Idade}")
def buscar_por_Idade(Idade: int):
    resultados = []
    for m in matriculas:
        if m["Idade"] == Idade:
            resultados.append(m)
            
    if resultados:
        return { "resultados": resultados }
    return { "erro": "Idade não encontrada" }

#rotas post
@app.post("/matriculas")
def adicionar_aluno(MatriculaAluno: str, Nome: str, Idade: int, Turma: str):
    novo_id = matriculas[-1]["id"] + 1 if matriculas else 1
    
    novo_aluno = {
        "id": novo_id,
        "MatriculaAluno": MatriculaAluno,
        "Nome": Nome,
        "Idade": Idade,
        "Turma": Turma
    }
    matriculas.append(novo_aluno)
    return {
        "mensagem": "Novo(a) aluno(a) adicionado confira:",
        "aluno_adicionado": novo_aluno
    }
