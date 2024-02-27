name = input("Enter name : ")
age = input("Enter age : ")
job = input("Enter job : ")

html = """
<!DOCTYPE html>
<html>
<head>
<style>
#customers {
  font-family: Arial, Helvetica, sans-serif;
  border-collapse: collapse;
  width: 100%;
}

#customers td, #customers th {
  border: 1px solid #ddd;
  padding: 8px;
}

#customers tr:nth-child(even){background-color: #f2f2f2;}

#customers tr:hover {background-color: #ddd;}

#customers th {
  padding-top: 12px;
  padding-bottom: 12px;
  text-align: left;
  background-color: #04AA6D;
  color: white;
}
</style>
</head>
<body>

<h1>Students Table</h1>

<table id="customers">
  <tr>
    <th>Name</th>
    <th>Age</th>
    <th>Job</th>
  </tr>
"""

html += f"""
<tr>
    <td>{name}</td>
    <td>{age}</td>
    <td>{job}</td>
  </tr>
"""

html += """
</table>
</body>
</html>
"""

open("table.html", "w").write(html)
