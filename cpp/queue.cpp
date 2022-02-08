#include "singly_linked_list.cpp"

template <typename T>
class Queue{
  public:
    Queue() = default;
    Queue(T firstElem){
      offer(firstElem);
    }

    int size(){
      return list.getSize();
    }

    bool isEmpty(){
      return size() == 0;
    }

    T peek(){
      if (isEmpty()) throw std::runtime_error("Queue Empty");
      return list.peekFirst();
    }

    T poll(){
      if (isEmpty()) throw std::runtime_error("Queue Empty");
      return list.removeFirst();
    }

    void offer(T elem){
      list.addLast(elem);
    }

    std::string toString(){
      return list.toString();
    }

  private:
    SinglyLinkedList<T> list;
};

int main(){
  Queue<int> queue;
  for (int i {}; i < 5; i++){
      queue.offer(i);
  }
  for (int i {}; i < 3; i++){
      std::cout<<queue.poll()<<std::endl;
  }
  return 0;
}
