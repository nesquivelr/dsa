#include <iostream>
#include <cmath>

template <typename T>
class DoublyLinkedList;

template <typename T>
class Node{
  public:
    Node(T datan, Node<T> *prevn = nullptr, Node<T> *nextn = nullptr)
      : data{datan}, prev{prevn}, next{nextn}{}
    std::string toString(){
      return std::to_string(data);
    }
  private:
    T data;
    Node<T> *prev, *next;

    friend class DoublyLinkedList<T>;
};

template <typename T>
class DoublyLinkedList{
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
        head = tail = {new Node<T>{elem, nullptr, nullptr}};
      } else {
        head->prev = {new Node<T>{elem, nullptr, head}};
        head = head->prev;
      }
      size++;
    }

    void addLast(T elem){
      if (isEmpty()){
        head = tail = {new Node<T>{elem, nullptr, nullptr}};
      } else {
        tail->next = {new Node<T>{elem, tail, nullptr}};
        tail = tail->next;
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
      else head -> prev = nullptr;

      return data;
    }

    T removeLast(){
      if (isEmpty()) throw std::runtime_error("Empty list");

      T data {tail -> data};
      Node<T> *tmp {tail};
      tail = tail -> prev;
      delete tmp;
      tmp = nullptr;
      --size;

      if (isEmpty()) head = nullptr;
      else tail -> next = nullptr;

      return data;
    }

    T remove(Node<T>* node){
      if (node->prev == nullptr) return removeFirst();
      if (node->next == nullptr) return removeLast();

      node->next->prev = node->prev;
      node->prev->next = node->next;

      T data {node->data};

      node->data = NAN;
      node->next = nullptr;
      node = nullptr;
      delete node;
      --size;

      return data;
    }

    T removeAt(int index){
      if (index < 0 or index >= size) throw std::invalid_argument("");

      Node<T>* trav;

      int i;
      if (index <size/2){
        for(i = 0, trav = head; i != index; i++)
          trav = trav -> next;
      } else {
        for(i = size-1, trav = tail; i!= index; i--)
          trav = trav -> prev;
      }

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


int main(){
  DoublyLinkedList<int> list;
  for(int i {}; i<5; i++)
    list.add(i);
  std::cout<<list.toString()<<std::endl;
  std::cout<<list.removeAt(4)<<std::endl;
  list.contains(3);
  std::cout<<list.toString()<<std::endl;

  return 0;
}
