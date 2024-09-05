public class Main {
  
  public void Seasons() {
    System.out.println("Ive finished the season 1 of Anime that i am watching");
    }
    
   public void Episodes(int AnimeEpisodes) {
     System.out.println("The total episodes of Anime that ive already watched is " + AnimeEpisodes);
     }
     
   public static void main(String[] args) {
     
     Main AnimeList = new Main();
     
     AnimeList.Seasons();
     AnimeList.Episodes(12);
     
}
}