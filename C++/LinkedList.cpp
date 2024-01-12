#include<iostream>

using namespace std;

class Node{
    public:
        Node* next;
        int val;
        Node(int val=0, Node* next = nullptr){
            this->next = next;
            this->val = val;
        }
};

class LinkedList{
    public:
        Node* head;
        Node* tail;
        int size;
        LinkedList(){
            this->head = NULL;
            this->tail = NULL;
            this->size = 0;
        }

        ~LinkedList(){
            Node* cur = this->head;
            while(cur){
                Node* next = cur->next;
                delete cur;
                cur = next;
            }
        }
        
        void append(int val);
        void print();
};

void LinkedList::append(int val){
    Node* node = new Node(val);
    if (this->head == NULL){
        this->head = node;
        this->tail = node;
    }
    else{
        this->tail->next = node;
        this->tail = node;
    }
    this->size++;
}

void LinkedList::print(){
    Node* cur = this->head;
    while(cur){
        cout<<cur->val<<"->";
        cur = cur->next;    
    }
    cout << "NULL" << endl;
}

int main(){
    LinkedList list;
    srand(time(NULL));
    for (int i = 0; i < 10; i++)
    {
        list.append(rand() % 100 + 1);
    }
    list.print();
    return 0;
}
