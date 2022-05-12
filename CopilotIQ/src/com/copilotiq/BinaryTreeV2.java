package com.copilotiq;

/**
 * This version of the BinaryTree class handles the bi-directional on the same level.
 */
public class BinaryTreeV2{

    NodeV2 root;

    public BinaryTreeV2(int[] values){
        construct(values);
    }

    /**
     * Answer to Question 5:
     * @param val - value to be inserted
     * @param root - root node
     * @param leftNearest - leftNearest Node of the new Node
     * @param rightNearest - rightNearest Node of the new Node
     * @return the root
     *
     * This insert method will incrementally build the Binary tree with bi-directional links to the nearest nodes
     * in the same level. The key here is:
     *  if new node is a left child, nearest right is the right child of the parent
     *  and nearest left is the right child of the left nearest of the parent. And Vise versa for the right child.
     *
     */
    public NodeV2 insert(int val, NodeV2 root, NodeV2 leftNearest, NodeV2 rightNearest){
        if(root == null){
            return new NodeV2(val, leftNearest, rightNearest);
        } else {
            if(val < root.val){
                root.leftChild = insert(val, root.leftChild,
                        root.leftNear != null? root.leftNear.rightChild : null,
                        root.rightChild);
            } else if(root.val < val) {
                root.rightChild = insert(val, root.rightChild,
                        root.leftChild,
                        root.rightNear != null ? root.rightNear.leftChild: null);
            }
        }
        return root;
    }

    private void construct(int[] values){
        for ( int i: values){
            this.root = insert(i, this.root, null, null);
        }
    }

    public void inOrderPrint(){
        inOrderHelper(this.root);
        System.out.println();
    }

    private void inOrderHelper(NodeV2 root){
        if(root != null){
            inOrderHelper(root.leftChild);
            System.out.print( root.val + " ");
            inOrderHelper(root.rightChild);
        }
    }
}
