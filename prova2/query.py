class Query:
    def __init__(self, database):
        self.database = database

    # Questão 1
    def get_by_birth_and_cpf(self, name):
        query = "MATCH (t:Teacher{name:$name}) RETURN t.ano_nasc, t.cpf"
        parameters = {"name": name}
        return self.database.execute_query(query, parameters)

    def get_professors_by_fisrt_letter(self, letter):
        query = "MATCH (t:Teacher) WHERE t.name STARTS WITH $letter RETURN t.name, t.cpf"
        parameters = {"letter": letter}
        return self.database.execute_query(query, parameters)

    def get_teachers_by_city(self, city):
        query = "MATCH (t:Teacher)-[:WORKS]->(s:School)-[:LOCATES]->(c:City{name:$city}) RETURN t.name"
        parameters = {"city": city}
        return self.database.execute_query(query, parameters)

    def get_schools_by_number(self, min, max):
        query = "MATCH (s:School) WHERE $min <= s.number <= $max RETURN s.name, s.address, s.number"
        parameters = {"min": min, "max": max}
        return self.database.execute_query(query, parameters)

    # Questão 2
    def get_youngest_and_oldest_teacher(self):
        query = "MATCH (t:Teacher) RETURN max(t.ano_nasc), min(t.ano_nasc)"
        return self.database.execute_query(query)
    
    def get_average_population(self):
        query = "MATCH (c:City) RETURN avg(c.population)"
        return self.database.execute_query(query)
    
    def get_city_by_cep(self, cep):
        query = "MATCH (c:City{cep:$cep}) RETURN replace(c.name, 'a', 'A')"
        parameters = {"cep": cep}
        return self.database.execute_query(query, parameters)
    
    def get_third_letter(self):
        query = "MATCH (t:Teacher) RETURN substring(t.name, 2, 1)"
        data = self.database.execute_query(query)
        answer = ""
        for d in data:
            answer += d[0] + ", "
        return answer[:-2]
