package com.copilotiq;

/**
 * NodeV2 extends the Node class and additional members leftNear and rightNear of Type NodeV2 was added to track the
 * links to the nearest left and right nodes
 */
public class NodeV2 {
    int val;
    NodeV2 leftChild;
    NodeV2 rightChild;
    NodeV2 leftNear, rightNear;

    public NodeV2(int val){
        this.val = val;
        this.leftChild = null;
        this.rightChild = null;
        this.leftNear = null;
        this.rightNear = null;
    }

    public NodeV2(int val, NodeV2 leftNear, NodeV2 rightNear){
        this.val = val;
        this.leftChild = null;
        this.rightChild = null;
        this.leftNear = leftNear;
        if(leftNear != null)
            leftNear.rightNear = this;
        this.rightNear = rightNear;
        if(rightNear != null)
            rightNear.leftNear = this;

    }
}
