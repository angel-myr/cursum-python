SELECT * FROM Amigos WHERE id_amigo in (2,8)

INSERT INTO Amigos(nombre, apellido, grupo, sexo)
VALUES('Angel', 'Marin', 'UNMSM', 'M')

UPDATE Amigos SET nombre = 'Angel', apellido = 'Marin', grupo = 'UNMSM', sexo = 'M'
WHERE id_amigo = 1

DELETE FROM Amigos WHERE id_amigo = 1