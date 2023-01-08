import pickle
import datetime

def add_record(data, id = None, inizialize = False):

    if inizialize:
        database = {}
    else:
        database = pickle.load( open( "db.pkl", "rb" ) )

    if id == None:
        id = max(list(database.keys())) + 1

    database[id] = data

    with open('db.pkl', 'wb') as handle:
        pickle.dump(database, handle, protocol=pickle.HIGHEST_PROTOCOL)


if __name__ == "__main__":

    id = 2
    database = pickle.load( open( "db.pkl", "rb" ) )

    correlated_id = [1,1,1]

    data = {
        "item_id": id,
        "date": datetime.datetime.now().date(),
        
        "maintitle": f"Ginnastica posturale: a cosa serve?",
        "subtitle": f"Quali i benefici e come farla",
        "paragraph2": f"La ginnastica posturale è un insieme di esercizi finalizzati a ristabilire l’equilibrio muscolare. Nello specifico è una serie di movimenti, basati sul miglioramento della postura e sulla capacità di controllo del corpo, capaci di agire su zone del corpo rigide che presentano dolori. ",
        "image1": f"../static/images/image_{id}.jpg",
        "title2": f"Benefici della ginnastica posturale",
        "paragraph3": f"""Con la ginnastica posturale è possibile agire su:
                            •	elasticità muscolare e mobilità articolare\n
                            •	forza e resistenza\n
                            •	abilità motorie,\n
                            •	rieducazione respiratoria\n
                            •	capacità di concentrazione, auto-rilassamento\n
                            •	postura, movimento ed equilibrio.\n""",
        "paragraph4": f"",
        "image2": f"../static/images/image_{id}.jpg",
        "paragraph5": f"La ginnastica posturale aiuta a mantenere vitali i muscoli e l’organismo e rallenta il processo di indebolimento dovuto al passare del tempo. Oltre alla correzione della postura, gli esercizi apportano notevoli benefici estetici e contribuiscono considerevolmente al benessere psico-fisico.Migliorano l’elasticità e la tonicità dei muscoli, la forza e la resistenza generale, l’abilità motoria, la respirazione, la gestione dello stress, il metabolismo generale, la circolazione e la pressione sanguigna, le funzioni dell’apparato digerente.",
        "paragraph6": f"Infine, la ginnastica posturale rinforza il sistema immunitario e le funzioni rigeneranti, ripristinando il corretto ciclo sonno-veglia e aumentando il rilascio di endorfine. Con la ginnastica posturale è quindi possibile curare e prevenire i più comuni disagi muscolo-scheletrici (lombalgie, sciatalgie, mal di schiena, cervicale, scoliosi, artrosi, osteoporosi), circolatori (varici, stasi venose,  ipertensione, ipotensione), organici (alterazione del neurovegetativo, insonnia, indebolimento del sistema immunitario, problematiche gastroenteriche).",

        "paragrafolaterale": f"La ginnastica posturale deve essere svolta attraverso la personalizzazione degli esercizi, la gradualità nella scelta del programma, e con movimenti lenti e precisi, in modo da avere piena sicurezza e controllo. Se non si ripettano queste indicazioni possiamo avere delle controindicazioni. Alcuni esercizi, apparentemente utili, possono essere controindicati in soggetti con specifiche problematiche.",

        "tag1": f"personal trainer",
        "tag2": f"allenamento",
        "tag3": f"posturale",
        "tag4": f"",
        "tag5": f"",


        "linkedpost1href": f"/post/{correlated_id[0]}",
        "linkedpost1title": f"{database[correlated_id[0]]['maintitle']}",
        "linkedpost1image": f"background-image: url({database[correlated_id[0]]['image1']});",
        "linkedpost1date": f' {database[correlated_id[0]]["date"].strftime("%d - %b - %Y")}',

        "linkedpost2href": f"/post/{correlated_id[1]}",
        "linkedpost2title": f"{database[correlated_id[1]]['maintitle']}",
        "linkedpost2image": f"background-image: url({database[correlated_id[1]]['image1']});",
        "linkedpost2date": f' {database[correlated_id[1]]["date"].strftime("%d - %b - %Y")}',

        "linkedpost3href": f"/post/{correlated_id[2]}",
        "linkedpost3title": f"{database[correlated_id[2]]['maintitle']}",
        "linkedpost3image": f"background-image: url({database[correlated_id[2]]['image1']});",
        "linkedpost3date": f' {database[correlated_id[2]]["date"].strftime("%d - %b - %Y")}',
    }

    add_record(data, id, inizialize=False)

