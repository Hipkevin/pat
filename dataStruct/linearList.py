class LinearList:
    def __init__(self, max_space_size=10):
        super(LinearList, self).__init__()

        self.data = [None] * max_space_size
        self.max_space_size = max_space_size

        self._length = 0

    def __len__(self):
        return self._length

    def __str__(self):
        return str(self.data[0: self._length])

    @property
    def length(self):
        return self._length

    @length.setter
    def _set_length(self, l):
        self._length = l

    def isEmpty(self):
        """
        判断表是否为空

        TIme: O(1)
        Space: O(1)

        :return: 表空 -> True | 表非空 -> False
        """
        return self.data[0] is None

    def findByIndex(self, index: int) -> object:
        """
        线性表下标从0开始

        Time: O(1)
        Space: O(1)

        :param index: 查询索引
        :return: 相应元素，查询失败返回None
        """
        if index < 0 or index > self._length:
            return None
        else:
            return self.data[index]

    def findElementsByVal(self, val: object) -> list:
        """
        查找线性表中指定值的索引
        存在多个值则全部返回

        Time: O(n)
        Space: O(1)

        :param val: 查询值
        :return: 结果索引列表
        """

        res = list()
        for idx, d in enumerate(self.data):
            if d == val:
                res.append(idx)

        return res

    def findElementByVal(self, val: object) -> int:
        """
        查找线性表中指定值的索引

        Time: less than O(n)
        Space: O(1)

        :param val: 查询值
        :return: 结果索引，查询失败返回None
        """

        for idx, d in enumerate(self.data):
            if d == val:
                return idx
        else:
            # for循环正常执行(无break、return等中断操作)
            return None

    def insert(self, index: int, val) -> bool:
        """
        在指定位置插入元素

        表空: 插入第一个位置并返回True
        表满: 插入失败返回False
        表非空 && 越界: 插入失败返回False
        表非空 && 未越界: 插入指定位置并返回True

        Time: O(n)
        Space: O(1)

        :param index: 插入位置
        :param val: 新元素的值
        :return: 是否插入成功
        """

        if self.isEmpty():
            index = 0

        if index < 0 or index > self._length \
                or index >= self.max_space_size:

            return False

        else:
            for i in range(self._length, index-1, -1):
                self.data[i] = self.data[i-1]

            self.data[index] = val

            self._length += 1
            return True

    def delete(self, index: int) -> bool:
        """
        删除指定位置的元素

        表空: 返回True
        表非空 && 越界: 返回False
        表非空 && 未越界: 删除指定元素并返回True

        Time: O(n)
        Space: O(1)

        :param index: 删除索引
        :return: 删除成功 -> True | 删除失败 -> False
        """

        if self.isEmpty():
            return True

        if index < 0 or index > self._length:
            return False

        else:
            for i in range(index, self._length):
                self.data[i] = self.data[i + 1]

            self._length -= 1
            return True