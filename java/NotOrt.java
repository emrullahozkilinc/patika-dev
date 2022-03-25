import java.util.Scanner;

public class NotOrt {
    public static void main(String[] args){
        Scanner not=new Scanner(System.in);
        int fizik,kimya,turkce,tarih,toplam;
        double ortalama;
        System.out.println("Fizik notunuzu giriniz: ");
        fizik=not.nextInt();
        System.out.println("Kimya notunuzu giriniz: ");
        kimya=not.nextInt();
        System.out.println("Tarih notunuzu giriniz: ");
        tarih=not.nextInt();
        System.out.println("Türkçe notunuzu giriniz: ");
        turkce=not.nextInt();

        toplam=fizik+kimya+tarih+turkce;
        ortalama=toplam/4;

        System.out.println((ortalama>60)?"Sınıfı geçtiniz":"Sınıfta kaldınız");
    }
}
