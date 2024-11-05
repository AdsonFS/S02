from database import Database
from query import Query
from teacher_crud import TeacherCRUD

# neo4j on docker
db = Database("bolt://localhost:7687", "neo4j", "S202senha")
# db.drop_all()

qr = Query(db)


# Questao 1
print("Questao 1")
print("a. " + str(qr.get_by_birth_and_cpf("Renzo")))
print("b. " + str(qr.get_professors_by_fisrt_letter('M')))
print("c. " + str(qr.get_teachers_by_city('Serra da Saudade')))
print("d. " + str(qr.get_schools_by_number(150, 550)))

print("\n\n")
# Questao 2
print("Questao 2")
print("a. " + str(qr.get_youngest_and_oldest_teacher()))
print("b. " + str(qr.get_average_population()))
print("c. " + str(qr.get_city_by_cep("37540-000")))
print("d. " + str(qr.get_third_letter()))



# Questao 3
print("Questao 3")

teacherCrud = TeacherCRUD(db)
teacherCrud.create("Chris Lima", 1956, "189.052.396-66")
print("c. " + str(teacherCrud.read("Chris Lima")))

teacherCrud.update("Chris Lima", "162.052.777-77")


