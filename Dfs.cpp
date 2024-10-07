#include<iostream>
using namespace std;

class node{
    public:
    int data;
    node*left;
    node*right;
    node(int d){
        this->data = d;
        this->right = NULL;
        this->left = NULL;
    }
};

node*buildtree(node*root){
    cout<<"enter the data:";
    int data;
    cin>>data;
    root = new node(data);
    
    if(data == -1){
        return NULL;
    }

    cout<<"Enter the data for inserting in left:"<<data<<endl;
    root->left = buildtree(root->left);
    cout<<"Enter the data for inserting in right:"<<data<<endl;
    root->right = buildtree(root->right);
    return root;

}

node* preorder(node*root){
    if(root == NULL){
        return root;
    }
    else{
        cout<<root->data<<" ";
        preorder(root->left);
        preorder(root->right);
    }
}

node*inorder(node*root){
    if(root == NULL){
        return root;
    }
    else{
        inorder(root->left);
        cout<<root->data<<" ";
        inorder(root->right);
    }
}

node*postorder(node*root){
    if(root == NULL){
        return root;
    }
    else{
        postorder(root->left);
        postorder(root->right);
        cout<<root->data<<" ";
    }
}

int main(){
    node*root = NULL;
    root = buildtree(root);
    preorder(root);
    inorder(root);
    postorder(root);

    return 0;
}