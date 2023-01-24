import java.time.LocalDate;

public class Publikacja {

    private static int ile;

    private String tytul;
    private double cena;
    private LocalDate dataWydania;


    Publikacja(String tytul, double cena, int rok, int miesiac, int dzien){
        this.tytul = tytul;
        this.cena = cena;
        this.dataWydania = LocalDate.of(rok, miesiac, dzien);
        ile++;
    }

    Publikacja(String tytul, double cena){
        this(tytul, cena, LocalDate.now().getYear(), LocalDate.now().getMonthValue(), LocalDate.now().getDayOfMonth());
    }

    public static int getIle() {
        return ile;
    }

    public String getTytul() {
        return tytul;
    }

    public double getCena() {
        return cena;
    }

    public LocalDate getDataWydania() {
        return dataWydania;
    }

    public void setDataWydania(int rok, int miesiac, int dzien) {
        if (miesiac < 1 || miesiac > 12) {
            miesiac = LocalDate.now().getMonthValue();
            System.out.println("Niepoprawne dane. Miesiac pobrany z daty systemowej.");
        }
        if (dzien < 1 || dzien > 31) {
            dzien = LocalDate.now().getDayOfMonth();
            System.out.println("Niepoprawne dane. Dzien pobrany z daty systemowej.");
        }
        this.dataWydania = LocalDate.of(rok, miesiac, dzien);
    }

    @Override
    public String toString() {
        if (tytul.equals("Publikacja Nieznana")) {
            return this.getClass().toString() + " [" + dataWydania.getYear() + "-" + dataWydania.getMonthValue() + "-" + dataWydania.getDayOfMonth() + "] " +
                    "[cena=" + cena +
                    ']';
        }
        return this.getClass().toString() + " [" + dataWydania.getYear() + "-" + dataWydania.getMonthValue() + "-" + dataWydania.getDayOfMonth() + "] " +
                "[tytul=" + tytul +
                ", cena=" + cena +
                ']';
    }

    @Override
    public boolean equals(Object o) {
        if (this == o) return true;
        if (o == null || getClass() != o.getClass()) return false;
        Publikacja publ = (Publikacja) o;
        return cena == publ.getCena() &&
                tytul.equals(publ.getTytul()) &&
                dataWydania.equals(publ.getDataWydania());
    }

    // Aby zwiekszyc  cene o 30% nalezy wywolac zwiekszCene(30)
    void zwiekszCene(double procent) {
        cena += cena * (procent / 100);
    }

}

