import java.util.Scanner;
import java.util.concurrent.TimeUnit;

public class test {
    private int pont = 0;
    boolean SpawnBreak = false;
    public static void main(String[] args){
        test clas = new test();
        Scanner input = new Scanner(System.in);
        
        //atribuiço  de pontos
        /*System.out.println("\rDeseja matar o rato? [s/n]");
        String res = input.nextLine();

        if (res.equalsIgnoreCase("s")) {
            clas.setPont(10);
            System.out.print("\r" + clas.getPont());
        } */

       while (true){
        clas.maps();
       }
    }
    public int getPont(){
        return pont;
    }
    public void setPont(int value) {
        pont = value;
    }
    public void SpawnBrainhot(){
        if (SpawnBreak == true){
            System.out.println("BrainHot Spawnado");
            SpawnBreak = false;
        } else {
            SpawnBreak = true;
        }
    }
    public void maps(){
        try {
            TimeUnit.SECONDS.sleep(2);
        } catch (InterruptedException e) {
            Thread.currentThread().interrupt();
            System.err.println("A thread foi interrompida: " + e.getMessage());
        }
        SpawnBrainhot();
        
    }
}

