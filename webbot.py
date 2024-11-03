from playwright.sync_api import sync_playwright
with sync_playwright() as p:
        navegador=p.chromium.launch()
        pagina=navegador.new_page()
        pagina.goto("https://www.mercadolivre.com.br/ofertas/supermercado#nav-header")
        elementos=pagina.query_selector_all('div')
        with open("precos.txt", "w", encoding="utf-8") as arquivo:
                for elemento in elementos:
                        texto = elemento.text_content()
                        if "R$" in texto:
                               
                                arquivo.write(texto + "\n")
