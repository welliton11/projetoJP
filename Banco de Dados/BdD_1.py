import sqlite3

conexao = sqlite3.connect('dataBase.db')
cursor = conexao.cursor()

cursor.execute('SELECT * FROM clientes')
# cursor.execute('DELETE FROM clientes WHERE nome = "Matheus" AND id != 1160')
conexao.commit()

for l in cursor.fetchall():
    print(l)

cursor.close()
conexao.close()

# (736, 'Bernardo', 96.0) henry , gabriel, gael, vitoria, manuela, lara, beatriz, isabela, rafael, valentina, aline, theo, danilo, nathalia, matheus

# (1031, 'Danilo', 83.0)
# (1152, 'Nathalia', 84.0)
# (1160, 'Matheus', 99.0)
# (1161, 'Beatriz', 87.0)
# (1174, 'Nathalia', 89.0)
# (1176, 'Bernardo', 60.0)
# (1179, 'Lara', 81.0)
# (1183, 'Gael', 100.0)
# (1190, 'Vitória', 73.0)
# (1197, 'Lara', 74.0)
# (1205, 'Aline', 78.0)
# (1222, 'Vitória', 83.0)
# (1246, 'Isabela', 96.0)
# (1265, 'Isabela', 60.0)
# (1290, 'Rafael', 77.0)
# (1291, 'Bernardo', 63.0)
# (1301, 'Henry', 98.0)
# (1314, 'Aline', 99.0)
# (1323, 'Manuela', 76.0)
# (1365, 'Gabriel', 77.0)
# (1375, 'Henry', 92.0)
# (1394, 'Bernardo', 97.0)
# (1430, 'Rafael', 76.0)
# (1431, 'Gael', 77.0)
# (1442, 'Valentina', 68.0)
# (1443, 'Beatriz', 63.0)
# (1446, 'Nathalia', 76.0)
# (1481, 'Isabela', 63.0)
# (1486, 'Lara', 98.0)
# (1490, 'Manuela', 87.0)
# (1492, 'Rafael', 90.0)
# (1532, 'Lara', 71.0)
# (1539, 'Gabriel', 70.0)
# (1557, 'Beatriz', 73.0)
# (1562, 'Isabela', 98.0)
# (1570, 'Nathalia', 84.0)
# (1587, 'Rafael', 99.0)
# (1595, 'Nathalia', 94.0)
# (1617, 'Danilo', 66.0)
# (1623, 'Gabriel', 93.0)
# (1625, 'Rafael', 90.0)
# (1644, 'Bernardo', 67.0)
# (1671, 'Henry', 86.0)
# (1674, 'Valentina', 64.0)
# (1682, 'Nathalia', 78.0)
# (1683, 'Gael', 86.0)
# (1701, 'Nathalia', 77.0)
# (1704, 'Valentina', 84.0)
# (1707, 'Theo', 68.0)
# (1713, 'Matheus', 89.0)
# (1721, 'Bernardo', 72.0)
# (1722, 'Valentina', 92.0)
# (1729, 'Matheus', 98.0)
# (1758, 'Bernardo', 64.0)
# (1768, 'Henry', 64.0)
# (1770, 'Gabriel', 96.0)
# (1775, 'Danilo', 61.0)
# (1819, 'Theo', 87.0)
# (1839, 'Lara', 84.0)
# (1852, 'Manuela', 83.0)
# (1862, 'Nathalia', 85.0)
# (1880, 'Vitória', 93.0)
# (1886, 'Beatriz', 84.0)
# (1944, 'Isabela', 67.0)
# (1945, 'Valentina', 95.0)
# (1967, 'Danilo', 61.0)
# (1974, 'Henry', 85.0)
# (1994, 'Lara', 61.0)
# (1998, 'Rafael', 98.0)
# (2023, 'Beatriz', 76.0)
# (2036, 'Aline', 98.0)
# (2040, 'Theo', 71.0)
# (2044, 'Valentina', 61.0)
# (2059, 'Henry', 72.0)
# (2073, 'Henry', 99.0)
# (2074, 'Theo', 93.0)
# (2087, 'Rafael', 71.0)
# (2102, 'Bernardo', 69.0)
# (2103, 'Valentina', 71.0)
# (2106, 'Vitória', 100.0)