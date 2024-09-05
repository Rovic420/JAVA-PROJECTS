public class Car {
    public void CarPrice() {
        int CarPrice = 500;
        CarPrice = CarPrice * 55 + 44 % 63;
        System.out.println("The Car price sales is: " + CarPrice);
    }
    
    public static void main(String[] args) {
    Car Car = new Car();
    Car.CarPrice();
  }
}