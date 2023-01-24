public class Main {
    public static void main(String[] args) {

        Publikacja nowa = new Publikacja("Rewelacyjna Publikacja", 100.0);
        System.out.println(nowa);
        System.out.println(Publikacja.getIle());
        Publikacja stara = new Publikacja("Stara Publikacja", 20, 1970, 12, 12);
        System.out.println(stara);
        System.out.println(Publikacja.getIle());
        System.out.println(stara.equals(nowa));

        // debug
//        System.out.println("debug");
//        Czasopismo czasopismo1 = new Czasopismo("Publikacja Nieznana", 19, 1999, 12, 19, 1);
//        Czasopismo czasopismo2 = new Czasopismo("Publikacja Nieznana", 19, 1999, 12, 19, 1);
//        System.out.println(czasopismo1.equals(czasopismo2)); // nie dziala
//        System.out.println(czasopismo2.equals(czasopismo1));
//        System.out.println(czasopismo1);
//        System.out.println(czasopismo2);
//        System.out.println(Publikacja.getIle());
//        czasopismo2.setDataWydania(2015, 81, 994);
//        System.out.println(czasopismo2);
//        Czasopismo czasopismo3 = new Czasopismo("Publikacja Czasopismo 3", 19, 1642, 5, 7, 3);
//        System.out.println(czasopismo3);
//        Publikacja stara2 = new Publikacja("Stara Publikacja", 20, 1970, 12, 12);
//        System.out.println(stara.equals(stara2));
//        stara2.zwiekszCene(10);
//        System.out.println(stara2);
//        System.out.println(stara.equals(stara2));
//        System.out.println(czasopismo2.equals(czasopismo1));
    }
}
