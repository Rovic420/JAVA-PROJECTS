import java.util.Random;

public class Main {
  
  private String[] GameList = {
    "WILDRIFT", "CODM", "PUBG", "COC", "BLUE ARCHIVE" 
    };
    
    public String getRandomGames() {
      Random random = new Random();
      int index = random.nextInt(GameList.length);
      return GameList[index];
      }
      
      public static void main(String[] args) {
        Main GamesList = new Main();
        String Game = GamesList.getRandomGames();
        System.out.println("I suggest you this game : " + Game);
        }
  }