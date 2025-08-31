Word2Vec – Prognoza vremena

Ovaj projekt koristi Word2Vec model iz biblioteke gensim za treniranje vektorskih reprezentacija riječi na temelju teksta iz datoteke podaci.txt.
Cilj je pokazati kako se riječi iz domena vremenske prognoze grupiraju po sličnosti i kako se mogu vršiti analogije među njima.

------------------------------------------------------------
Preduvjeti
------------------------------------------------------------
- Operacijski sustav: Linux, macOS ili Windows
- Python: verzija 3.8 ili novija
- Potrebne biblioteke:
  - gensim
  - numpy

Instalacija paketa:
    pip install gensim numpy

------------------------------------------------------------
Struktura projekta
------------------------------------------------------------
- word2vec_prognoza.py – glavna Python skripta koja trenira model i ispisuje primjere.
- podaci.txt – tekstualna datoteka s rečenicama (baza podataka).

------------------------------------------------------------
Pokretanje programa
------------------------------------------------------------
1. Provjerite da se datoteke word2vec_prognoza.py i podaci.txt nalaze u istom direktoriju.
2. Pokrenite skriptu u terminalu/command promptu:

    python word2vec_prognoza.py

------------------------------------------------------------
Rezultati
------------------------------------------------------------
Skripta će:
- trenirati Word2Vec model nad podacima,
- ispisati slične riječi za zadane pojmove (npr. vjetar, temperaturi),
- prikazati vektorsku reprezentaciju neke riječi (sunčano),
- pronaći riječ koja ne pripada skupu (npr. proljeće, pretežno, sunčano),
- izračunati sličnost riječi (suhi i zrak, jasno i zrak),
- ispitati jednostavne analogije među riječima,
- provjeriti postoji li neka riječ u vokabularu (magla, dinosaur).
