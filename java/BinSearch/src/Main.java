import java.lang.*;
import java.util.*;

public class Main {
    /*
      Generate a intger number in between 0 to 6
     */
    public static void main(String[] args) {
        int [] testData = new int[10];

        for (int i=0; i < 10; i++) {
            testData[i] = randomInt(0, 10);
        }
        Arrays.sort(testData);

        for (int i=0; i < 10; i++) {
            System.out.println(testData[i]);
        }

        int key = (int)(Math.random() * 6);
        System.out.printf("The key is %d ", key);

        int value = rank(key, testData);
        System.out.println(value);

        if (rank(key, testData) == -1) {
            System.out.println("Not found");
        } else {
            System.out.println("ok");
        }
    }

    /*
    * @param key: the number to find in an existing array.
    * @param intArray: A sorted array.
    * @return : the first index of key or -1(not found)
    * */
    public static int rank(int key, int [] intArray) {
        int low = 0;
        int high = intArray.length -1 ;

        while (low <= high) {
            int mid = low + (high - low) / 2;
            if (key < intArray[mid]) high = mid - 1;
            else if(key > intArray[mid]) low = mid + 1;
            else return mid;
        }

        return -1;
    }

    public static int randomInt(int minimum, int maximum) {
        return  minimum + (int)(Math.random() * maximum);
    }
}
