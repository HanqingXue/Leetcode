public class Main {

    public static void main(String[] args) {
        System.out.println("Hello World!");
        System.out.print(less(10, 9));
    }

    public static boolean less(int a, int b) {
        return  a < b;
    }

    public static void show(int [] numArray) {
        for (int i = 0; i < numArray.length; i++)
            System.out.printf("The %d th element is %d", i, numArray[i]);
    }

    public static boolean  isSort(int [] numArray) {
        for (int i = 0; i < numArray.length - 1; i++) {
            if (less(numArray[i], numArray[i+1])) {
                return false;
            }
        }
    }

    public static void BubbleSort(int[] numArray) {

    }

    public static void SelectSort(int[] numArray) {

    }
}
