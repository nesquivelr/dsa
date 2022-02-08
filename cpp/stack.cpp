#include "singly_linked_list.cpp"

template <typename T>
class Stack{
  public:
    Stack() = default;
    Stack(T firstElem){
      push(firstElem);
    }
    int size(){
      return list.getSize();
    }
    bool isEmpty(){
      return size() == 0;
    }
    void push(T elem){
      list.addLast(elem);
    }

    T pop(){
      if (isEmpty())
        throw std::out_of_range("");
      return list.removeLast();
    }

    T peek(){
      if (isEmpty())
        throw std::out_of_range("");
      return list.peekLast();
    }
  private:
    SinglyLinkedList<T> list;
};

int main(){
  Stack<int> stack;
  for (int i {}; i < 5; i++){
      stack.push(i);
      std::cout<<stack.peek()<<std::endl;
  }
  for (int i {}; i < 3; i++){
      std::cout<<stack.pop()<<std::endl;
  }
  return 0;
}
