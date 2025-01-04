from flask import render_template

class IndexController():
    
    def index(self):
        """Resonsavel por reenderizar uma pagina html

        Returns:
            flask.Response: Resposta requisição com template da pagina inicial
        """
        
        return render_template("index.html")