from clases import Profesor, Estudiante
cesar = Profesor("cc", "1000001", "Cesar Augusto", "Diaz Arriaga", "cesar@profe.com", "Masculino", "32100000001", "Ingenieria de software")

cesar.hablar()

adrian = Estudiante("1", "cc", "1000002", "Adrian", "Perez", "adrian.perez@email.com", "Masculino", "321000002", 25, "1")

adrian.hablar()

adriana = Estudiante("2", "ti", "20000000001", "Adriana Marcela", "Moreno", "adriana@email.com", "Femenino", "32100000003", 17, "1")

adriana.set_nombres("Andrea")
adriana.hablar()
