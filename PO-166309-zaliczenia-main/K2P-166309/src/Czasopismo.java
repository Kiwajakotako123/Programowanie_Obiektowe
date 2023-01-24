public class Czasopismo extends Publikacja {

    private int numer;

    Czasopismo(String tytul, double cena, int rok, int miesiac, int dzien, int numer){
        super(tytul, cena, rok, miesiac, dzien);
        this.numer = numer;
    }

    public int getNumer() {
        return numer;
    }

    public void setNumer(int numer) {
        this.numer = numer;
    }

    @Override
    public String toString() {
        return super.toString() + " numer=" + numer;
    }

    @Override
    public boolean equals(Object o) {
        if (this == o) return true;
        if (o == null || getClass() != o.getClass()) return false;
        if (!super.equals(o)) return false;
        Czasopismo czasop = (Czasopismo) o;
        return numer == czasop.getNumer();
    }
}