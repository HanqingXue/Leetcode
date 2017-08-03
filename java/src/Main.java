public class Main {

    public static void main(String[] args) {
        int [] data = {7, 3, 5, 8, 2, 6, 4, 1, 0};
        SelectSort(data);
        assert isSort(data);
        show(data);

    }

    public static boolean less(int a, int b) {
        return  a < b;
    }

    public static void exch(int[] numArray, int i, int j) {
        int temp = numArray[i];
        numArray[i] = numArray[j];
        numArray[j] = temp;
    }

    public static void show(int [] numArray) {
        for (int i = 0; i < numArray.length; i++)
            System.out.printf("The %d th element is %d\n", i, numArray[i]);
    }

    public static boolean  isSort(int [] numArray) {
        for (int i = 0; i < numArray.length - 1; i++) {
            if (less(numArray[i], numArray[i+1])) {
                return false;
            }
        }
        return true;
    }

    public static void BubbleSort(int[] numArray) {

    }

    public static void SelectSort(int[] numArray) {
        for (int i = 0; i < numArray.length; i++){
            int min = i;
            for (int j = i + 1; j < numArray.length; j++) {
                if (less(numArray[j], numArray[min])) min = j;
            }
            exch(numArray, i, min);
        }
    }
}
