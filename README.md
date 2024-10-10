# Definizione del problema:
## Il problema presentato riguarda la costruzione di ponti in una laguna che contiene k piccole isolette di varie dimensioni e forme. Le dimensioni e la forma delle isolette non sono rilevanti.  È nota la distanza minima in linea d’acqua tra ogni isoletta e le sue più vicine. L'obiettivo è costruire ponti tra le isolette in modo tale da garantire due condizioni:
    1.	Assicurare la completa connessione via ponte tra tutte le isolette.
    2.	Minimizzare i costi complessivi di costruzione.
## I costi sono divisi in due categorie: costi fissi che dipendono da ogni singola isola, relativi alle infrastrutture necessarie, e costi variabili di 100k€ ogni 10 metri lineari di ponte. Inoltre, alcuni ponti potrebbero essere già esistenti tra alcune isolette, il che implica che non vi siano costi aggiuntivi per quei collegamenti.
## Il problema richiede, quindi, la determinazione del modo più efficiente in termini di costi per connettere tutte le isolette della laguna rispettando queste condizioni. L’obiettivo è quello di confrontare gli approcci risolutivi implementati in Minizinc e in Clingo.
![12-ponti](https://github.com/user-attachments/assets/6157b2a9-3fd4-43ec-8893-e104e831c409)
