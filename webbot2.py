from playwright.sync_api import sync_playwright
import time
with sync_playwright() as p:
    navegador=p.chromium.launch(headless=False)
    pagina=navegador.new_page()
    pagina.goto('http://127.0.0.1:5500/formulario.html')
    
    with open("usuario.csv","r",encoding="utf-8") as arquivos:
        for linha in arquivos:
            pagina.fill('xpath=//*[@id="nome"]',linha.split(",")[0])
            time.sleep(1)
            pagina.fill('xpath=//*[@id="email"]',linha.split(",")[1])
            time.sleep(1)
            pagina.fill('xpath=//*[@id="telefone"]',linha.split(",")[2]) 
            time.sleep(1) 
            pagina.fill('xpath=//*[@id="endereco"]',linha.split(",")[3])   
            time.sleep(0.1)
            pagina.locator('xpath=//*[@id="formulario-cadastro"]/input[5]').click()
            time.sleep(4)
            pagina.fill('xpath=//*[@id="nome"]',"")
            pagina.fill('xpath=//*[@id="email"]',"")
            pagina.fill('xpath=//*[@id="telefone"]','')
            pagina.fill('xpath=//*[@id="endereco"]',"")
            time.sleep(5)
