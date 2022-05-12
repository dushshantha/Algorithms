package com.copilotiq;

public class BinaryTree {

    Node root;

    public BinaryTree(){
        this.root = null;
    }

    public BinaryTree(int[] values){
        construct(values);
    }

    public BinaryTree(int[] values, boolean balanced){
        if (balanced){
            constructBalanced(values);
        } else {
            construct(values);
        }
    }

    public Node insert(int val, Node root){
        if(root == null){
            return new Node(val);
        } else {
            if(val < root.val){
                root.leftChild = insert(val, root.leftChild);
            } else if(root.val < val) {
                root.rightChild = insert(val, root.rightChild);
            }
        }
        return root;
    }

    private void construct(int[] values){
        for ( int i: values){
            this.root = insert(i, this.root);
        }
    }

    /**
     *
     * @param sortedValues - sorted array of values. Should be in ascending order for simplicity
     *
     *
     * This will construct a balanced binary tree.
     */
    private void constructBalanced(int[] sortedValues){

        this.root = insertBalanced(sortedValues, 0, sortedValues.length - 1, this.root);

    }

    /**
     *
     * @param sortedValues
     * @param l - leftmost index of the array
     * @param r - rightmost index of the array
     * @return Node
     */
    private Node insertBalanced(int[] sortedValues, int l, int r, Node root){
        if(l > r){
            return null;
        }
        int mid = (l + r)/2;
        //System.out.print(mid + " - " + sortedValues[mid] + "\n");
        root = insert(sortedValues[mid], root);
        root.leftChild = insertBalanced(sortedValues, l, mid - 1, root.leftChild);
        root.rightChild = insertBalanced(sortedValues, mid + 1, r, root.rightChild);

        return root;
    }

    public void inOrderPrint(){
        inOrderHelper(this.root);
        System.out.println();
    }

    private void inOrderHelper(Node root){
        if(root != null){
            inOrderHelper(root.leftChild);
            System.out.print( root.val + " ");
            inOrderHelper(root.rightChild);
        }
    }

    public void preOrderPrint(){
        preOrderHelper(this.root);
        System.out.println();
    }

    private void preOrderHelper(Node root){
        if(root != null){
            System.out.print( root.val + " ");
            preOrderHelper(root.leftChild);
            preOrderHelper(root.rightChild);
        }
    }


}
