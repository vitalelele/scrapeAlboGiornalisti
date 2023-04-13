import pandas as pd


def writeFile(tableGiornalisti):
    file = open("alboGiornalisti.txt", "w")
    file.write(tableGiornalisti)
    file.close()


def main():
    # Pagina web con elenco albo giornalisti
    url = "https://www.odgtaa.it/albo/elenco_completo"
    all_tables = pd.read_html(url)
    writeFile(all_tables[0].to_string())

if __name__ == "__main__":
    main()
