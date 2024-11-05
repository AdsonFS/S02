class TeacherCRUD:
    def __init__(self, database):
        self.database = database

    def create(self, name, ano_nasc, cpf):
        query = "CREATE(:Teacher{name:$name,ano_nasc:$ano_nasc,cpf:$cpf})"
        parameters = {"name": name, "ano_nasc": ano_nasc, "cpf": cpf}
        return self.database.execute_query(query, parameters)
    
    def read(self, name):
        query = "MATCH(t:Teacher{name:$name}) RETURN t"
        parameters = {"name": name}
        return self.database.execute_query(query, parameters)
    
    def delete(self, name):
        query = "MATCH(t:Teacher{name:$name}) DELETE t"
        parameters = {"name": name}
        return self.database.execute_query(query, parameters)
    
    def update(self, name, newCpf):
        query = "MATCH(t:Teacher{name:$name}) SET t.cpf = $newCpf"
        parameters = {"name": name, "newCpf": newCpf}
        return self.database.execute_query(query, parameters)

