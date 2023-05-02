# NIESKOŃCZONE

capacity = 6
minimum_threshold = int(capacity / 2)


class Head:
    def __init__(self, tab=None, fill=0, next=None):
        if tab is None:
            self.tab = [None for i in range(capacity)]
        else:
            self.tab = tab
        self.fill = fill
        self.next = next

    def __str__(self):
        string = str(self.tab)
        nxt = self.next
        while nxt is not None:
            string += str(nxt.tab)
            nxt = nxt.next
        return string

    def insert(self, data, idx):
        if self.fill < capacity:
            if idx + 1 <= self.fill:
                val = data
                for i in range(idx, capacity):
                    temp = self.tab[i]
                    self.tab[i] = val
                    val = temp
                self.fill += 1
            else:
                self.tab[self.fill] = data
                self.fill += 1
        elif self.fill == capacity:
            nxt = self.next
            temp_tab = self.tab
            temp_tab.insert(idx, data)
            self.tab = [temp_tab[i] if i <= minimum_threshold - 1 else None for i in range(capacity)]
            self.fill = minimum_threshold
            self.next = Head(temp_tab[minimum_threshold:] + [None] * (capacity - minimum_threshold - 1),
                             capacity - minimum_threshold + 1, nxt)

    def delete(self, idx):
        if self.fill > minimum_threshold:
            if idx + 1 == self.fill:
                self.tab[idx] = None
                self.fill -= 1
            elif idx + 1 <= self.fill:
                del self.tab[idx]
                self.tab += [None]
                self.fill -= 1
        elif self.fill <= minimum_threshold:
            if self.next is None:
                del self.tab[idx]
                self.tab += [None]
                self.fill -= 1
            elif self.next.fill == minimum_threshold:
                del self.tab[idx]
                self.tab += [None]
                self.fill -= 1
                for i in range(minimum_threshold):
                    self.tab[self.fill+i] = self.next.tab[i]
                self.fill = self.fill + minimum_threshold
                self.next = self.next.next
            else:
                del self.tab[idx]
                self.tab.insert(self.fill - 1, self.next.tab[0])
                self.next.delete(0)
        if self.next is not None and self.next.tab[0] is None:
            self.next = None


class Mylist:
    def __init__(self):
        self.mylist = Head()

    def __str__(self):
        return str(self.mylist)

    def get_head_and_idx(self, idx):
        this = self.mylist
        nxt = self.mylist.next
        if nxt is not None and idx > self.mylist.fill - 1:
            idx_sum = nxt.fill + this.fill
            idx_prev_sum = this.fill
            while nxt.next is not None and idx_sum <= idx:
                idx_prev_sum += this.next.fill
                idx_sum += nxt.next.fill
                this = this.next
                nxt = nxt.next
            i = idx - idx_prev_sum
            return nxt, i
        else:
            return this, idx

    def get(self, idx):
        head, i = self.get_head_and_idx(idx)
        return head.tab[i]

    def insert(self, data, idx):
        head, i = self.get_head_and_idx(idx)
        head.insert(data, i)

    def delete(self, idx):
        head, i = self.get_head_and_idx(idx)
        head.delete(i)


def main():
    X = Mylist()
    print('Utworzenie pustej tablicy:')
    print(X)
    print('\nUżycie insert w pętli:')
    for i in range(1, 10):
        X.insert(i, i - 1)
        print(X)
    print('\nUżycie get:')
    print(X.get(4))
    print('\nDwukrotne użycie insert:')
    X.insert(10, 1)
    X.insert(11, 8)
    print(X)
    print('\nDwukrotne użycie delete:')
    X.delete(1)
    X.delete(2)
    print(X)


if __name__ == '__main__':
    main()
