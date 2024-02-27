header = input("Enter header : ")
paragraph = input("Enter paragraph : ")

html = f"""
<h1>{header}</h1>
<p>{paragraph}</p>
"""

open("home.html","w").write(html)
print("Done")
