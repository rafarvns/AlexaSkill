import mysql.connector
from mysql.connector import Error

try:
    connection = mysql.connector.connect(host='mysql',
                                         database='soletrando',
                                         user='root',
                                         password='123456')
    create_database_sql = """
        CREATE TABLE IF NOT EXISTS dificuldade (
            `id` INT NOT NULL AUTO_INCREMENT,
            `nivel` VARCHAR
        );
        CREATE TABLE IF NOT EXISTS soletrando (
            `id` INT NOT NULL AUTO_INCREMENT,
            `palavra` VARCHAR(100),
            `palavra_comp` VARCHAR,
            `dificuldade` INT,
            CONSTRAINT fk_dificuldade
            FOREIGN KEY (dificuldade) 
                REFERENCES dificuldade(id)
        );

        TRUNCATE TABLE dificuldade;
        TRUNCATE TABLE soletrando;

        INSERT INTO `dificuldade` (nivel) VALUES ('Fácil');
        INSERT INTO `dificuldade` (nivel) VALUES ('Normal');
        INSERT INTO `dificuldade` (nivel) VALUES ('Difícil');

        INSERT INTO `soletrando` (palavra, palavra_comp, dificuldade) VALUES ('CASA', 'c. a. s. a.', 1);
        INSERT INTO `soletrando` (palavra, palavra_comp, dificuldade) VALUES ('ROUPA', 'r. o. u. p. a.', 1);
        INSERT INTO `soletrando` (palavra, palavra_comp, dificuldade) VALUES ('OLHOS', 'o. l. h. o. s.', 1);
        INSERT INTO `soletrando` (palavra, palavra_comp, dificuldade) VALUES ('SOPA', 's. o. p. a.', 1);
        INSERT INTO `soletrando` (palavra, palavra_comp, dificuldade) VALUES ('UVA', 'u. v. a.', 1);

        INSERT INTO `soletrando` (palavra, palavra_comp, dificuldade) VALUES ('PANELA', 'p. a. n. e. l. a.', 2);
        INSERT INTO `soletrando` (palavra, palavra_comp, dificuldade) VALUES ('TECLADO', 't. e. c. l. a. d. o.', 2);
        INSERT INTO `soletrando` (palavra, palavra_comp, dificuldade) VALUES ('MONITOR', 'm. o. n. i. t. o. r.', 2);

        INSERT INTO `soletrando` (palavra, palavra_comp, dificuldade) VALUES ('ROTEADOR', 'r. o. t. e. a. d. o. r.', 3);
        INSERT INTO `soletrando` (palavra, palavra_comp, dificuldade) VALUES ('AQUECEDOR', 'a. q. u. e. c. e. d. o. r.', 3);
     """

    if connection.is_connected():
        db_Info = connection.get_server_info()
        print("Connected to MySQL Server version ", db_Info)
        cursor = connection.cursor()
        result = cursor.execute(create_database_sql)
        print("Tabelas criadas e dados inseridos com sucesso!")
        record = cursor.fetchone()
        print("You're connected to database: ", record)

except Error as e:
    print("Error while connecting to MySQL", e)
finally:
    if (connection.is_connected()):
        cursor.close()
        connection.close()
        print("MySQL connection is closed")