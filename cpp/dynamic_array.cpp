#include <iostream>

class DynamicArray {
  public:
    struct Iterator {
      using iterator_category = std::forward_iterator_tag;
      using difference_type = std::ptrdiff_t;
      using value_type = int;
      using pointer = int * ;
      using reference = int & ;

      Iterator(pointer ptr): m_ptr(ptr) {}

      reference operator * () const {
        return *m_ptr;
      }
      pointer operator -> () {
        return m_ptr;
      }
      Iterator & operator++() {
        m_ptr++;
        return *this;
      }
      Iterator operator++(int) {
        Iterator tmp = * this;
        ++( * this);
        return tmp;
      }
      friend bool operator == (const Iterator & a,
        const Iterator & b) {
        return a.m_ptr == b.m_ptr;
      };
      friend bool operator != (const Iterator & a,
        const Iterator & b) {
        return a.m_ptr != b.m_ptr;
      };

      private:
        pointer m_ptr;
    };

  DynamicArray(): DynamicArray(16) {};
  DynamicArray(int capacity);
  int size() {
    return len;
  }
  bool isEmpty() {
    return size() == 0;
  }
  int get(int index) {
    return arr[index];
  }
  void set(int index, int elem) {
    arr[index] = elem;
  }
  void clear() {
    for (int i {}; i < capacity; i++)
      arr[i] = 0;
    len = 0;
  }
  void add(int elem) {
    if (len + 1 >= capacity) {
      if (capacity == 0) capacity = 1;
      else capacity *= 2;
      int * new_arr = new int[capacity] {};
      for (int i {}; i < len; i++)
        new_arr[i] = arr[i];
    }
    arr[len++] = elem;
  }
  int removeAt(int rm_index) {
    if (rm_index >= len && rm_index < 0) throw std::out_of_range("Index out of range");
    int data = arr[rm_index];
    int * new_arr = new int[len - 1] {};
    for (int i {}, j {}; i < len; i++, j++)
      if (i == rm_index) j--;
      else new_arr[j] = arr[i];
    arr = new_arr;
    capacity = --len;
    return data;
  }

  bool remove(int obj) {
    for (int i {}; i < len; i++) {
      if (arr[i] == obj) {
        removeAt(i);
        return true;
      }
    }
    return false;
  }

  int indexOf(int obj) {
    for (int i {}; i < len; i++) {
      if (arr[i] == obj)
        return i;
    }
    return -1;
  }

  bool contains(int obj) {
    return indexOf(obj) != -1;
  }

  Iterator begin() {
    return &arr[0];
  };
  Iterator end() {
    return &arr[len];
  };

  std::string toString() {
    if (len == 0) return "[]";
    else {
      std::string sb {"["};
      for (int i {}; i < len - 1; i++)
        sb.append(std::to_string(arr[i]) + ", ");
      return sb.append(std::to_string(arr[len - 1]) + "]");
    }
  }

  private:
    int * arr;
    int len {0};
    int capacity {0};
};

DynamicArray::DynamicArray(int pcapacity) {
  if (pcapacity < 0) throw std::invalid_argument("Illegal Capacity: " + std::to_string(capacity));
  capacity = pcapacity;
  arr = new int[capacity] {};
}

int main() {
  DynamicArray my_array {};
  for (int i {}; i < 40; i++) {
    my_array.add(i);
  }
  std::cout << my_array.toString() << std::endl;
  for (auto it: my_array) {
    std::cout << it << ", ";
  }
  std::cout << std::endl;
  return 0;
}
