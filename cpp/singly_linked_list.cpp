#include <iostream>
#include <cmath>

template <typename T>
class SinglyLinkedList;

template <typename T>
class Node{
  public:
    Node(T datan, Node<T> *nextn = nullptr): data{datan}, next{nextn}{}
    std::string toString(){
      return std::to_string(data);
    }
  private:
    T data;
    Node<T> *next;

    friend class SinglyLinkedList<T>;
};

template <typename T>
class SinglyLinkedList{
  public:
    void clear(){
      Node<T>* trav {head};
      while (trav != nullptr){
        Node<T> *next {trav->next};
        delete trav;
        trav = nullptr;
        trav = next;
      }
      head = tail = trav = nullptr;
      size = 0;
    }
    bool isEmpty(){
      return size == 0;
    }

    int getSize(){
      return size;
    }

    void add(T elem){
      addLast(elem);
    }

    void addFirst(T elem){
      if (isEmpty()){
        head = tail = {new Node<T>{elem, nullptr}};
      } else {
        Node<T>* new_node = {new Node<T>{elem, head}};
        head = new_node;
      }
      size++;
    }

    void addLast(T elem){
      if (isEmpty()){
        head = tail = {new Node<T>{elem, nullptr}};
      } else {
        Node<T>* new_node = {new Node<T>{elem, nullptr}};
        tail->next = new_node;
        tail = new_node;
      }
      size++;
    }

    T peekFirst(){
      if (isEmpty()) throw std::runtime_error("Empty list");
      return head -> data;
    }

    T peekLast(){
      if (isEmpty()) throw std::runtime_error("Empty list");
      return tail -> data;
    }

    T removeFirst(){
      if (isEmpty()) throw std::runtime_error("Empty list");

      T data = head -> data;
      Node<T> *tmp = head;
      head = head -> next;
      delete tmp;
      tmp = nullptr;
      --size;

      if (isEmpty()) tail = nullptr;

      return data;
    }

    T removeLast(){
      if (isEmpty()) throw std::runtime_error("Empty list");

      T data {tail -> data};
      Node<T>* trav {head};
      for (trav=head;trav->next != tail; trav = trav -> next){}

      Node<T>* removed_node {trav -> next};
      tail = trav;

      removed_node->data = NAN;
      removed_node -> next = nullptr;
      delete removed_node;
      removed_node = nullptr;
      --size;

      if (isEmpty()) head = nullptr;
      else tail -> next = nullptr;

      return data;
    }

    T remove(Node<T>* node){
      if (node->next == nullptr) return removeLast();

      Node<T>* removed_node {node -> next};
      node -> next = node -> next -> next;

      T data {removed_node->data};

      removed_node->data = NAN;
      removed_node -> next = nullptr;
      delete removed_node;
      removed_node = nullptr;
      --size;

      return data;
    }

    T removeAt(int index){
      if (index < 0 or index >= size) throw std::invalid_argument("");

      if (index == 0){
        return removeFirst();
      }

      if (index == size - 1){
        return removeLast();
      }
      Node<T>* trav;
      int i;

      for(i = 0, trav = head; i != index-1; i++)
        trav = trav -> next;

      return remove(trav);
    }

    int indexOf(T obj){
      int index {};
      Node<T>* trav {head};

      if (std::isnan(obj)){
        for(trav = head; trav != nullptr; trav = trav->next, index++)
          if (std::isnan(trav -> data))
            return index;
      } else
        for(trav = head; trav != nullptr; trav = trav->next, index++)
          if (trav -> data == obj)
            return index;
      return -1;
    }

    bool contains(T obj){
      return indexOf(obj) != 1;
    }

    std::string toString() {
      std::string sb {'['};
      Node<T> *trav = head;
      while (trav != nullptr){
        if (trav == tail){
          sb += std::to_string(trav->data) + "]";
        } else {
          sb += std::to_string(trav->data) + ", ";
        }
        trav = trav->next;
      }
      return sb;
    }
  private:
    int size {};
    Node<T> *head = nullptr;
    Node<T> *tail = nullptr;
};


/*
int main(){
  SinglyLinkedList<int> list;
  for(int i {}; i<5; i++)
    list.add(i);
  std::cout<<list.toString()<<std::endl;
  std::cout<<list.removeAt(4)<<std::endl;
  list.contains(3);
  std::cout<<list.toString()<<std::endl;

  return 0;
}
*/
