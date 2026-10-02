import java.util.Random;
import java.util.Scanner;

public class rock_paper_scissor {
    public static void main(String[] args){
        Scanner scanner=new Scanner(System.in);
        Random random=new Random();

        String[] items={"rock", "paper", "scissor"};
        String guess;
        String system;
        String loop="yes";

        System.out.print("Enter your guess (rock, paper, scissor): ");
        guess=scanner.nextLine().toLowerCase();
        system=items[random.nextInt(3)];
        do{
            if(!guess.equals("rock") && !guess.equals("paper") && !guess.equals("scissor") ){
                System.out.println("invalid input!");
                continue;
            }
            System.out.println("system: "+system);
            if(guess.equals(system)){
                System.out.println("tie");
            }
            else if((guess.equals("rock") && system.equals("paper")) ||
                    (guess.equals("scissor") && system.equals("paper"))||
                    (guess.equals("rock") && system.equals("scissor"))){
                System.out.println("you win");
            }
            else{
                System.out.println("you loose!");
            }
            System.out.print("play again (yes/no): ");
            loop=scanner.nextLine().toLowerCase();
        }while(loop.equals("yes"));
        System.out.println("Thanks for playing!😊");
    }
}
