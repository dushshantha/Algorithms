package com.copilotiq;


public class StartHere {

    public static void main(String[] args) {

        /**
         * Answer to question 2:
         * I use the BinaryTree data structure that was created here
         */
        int[] vals = new int[]{9,8,7,6,5,4,3,2,1};
        BinaryTree bt = new BinaryTree(vals);
        bt.inOrderPrint();

        /**
         * Another example to test the accuracy of the Tree
         */
        int[] vals2 = new int[]{2,3,4,1,8,5,};
        BinaryTree bt2 = new BinaryTree(vals2);
        bt2.inOrderPrint();

        /**
         * Answer to Question 3: Creating a balanced BinaryTree using a Sorted Array.
         * For simplicity, wanted the array to be ascending order
         */
        BinaryTree btBalanced = new BinaryTree(reverseArray(vals), true);
        //btBalanced.inOrderPrint();
        btBalanced.preOrderPrint();

        /**
         * Answer to Question 4:
         * Created V2 of the BinaryTree that has bi-directional links.
         *
         */
        BinaryTreeV2 btV2 = new BinaryTreeV2(vals2);
        btV2.inOrderPrint();
        NodeV2 leftmostNode = btV2.root.leftChild;
        while (leftmostNode != null){
            System.out.print(leftmostNode.val + " ");
            leftmostNode = leftmostNode.rightNear;
        }
        System.out.println();

        NodeV2 rightmostNode = btV2.root.rightChild;
        while (rightmostNode != null){
            System.out.print(rightmostNode.val + " ");
            rightmostNode = rightmostNode.leftNear;
        }

        /**
         * Answer to question 5 is in the implementation.
         */



    }

    /**
     * @param arr - array to be reversed
     * @return - reversed array
     * This method is to reverse a given array
     */
    private static int[] reverseArray(int[] arr){
        int temp;
        int i = 0;
        int j = arr.length - 1;
        while (i < j) {
            temp = arr[j];
            arr[j] = arr[i];
            arr[i] = temp;
            i++;
            j--;
        }
        return arr;
    }
}
