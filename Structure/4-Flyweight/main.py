import random
from enum import Enum
from collections import defaultdict

TreeType = Enum('TreeType', 'apple_tree cherry_tree peach_tree')


class Tree:
    pool = dict()

    def __new__(cls, tree_type):
        obj = cls.pool.get(tree_type, None)
        if not obj:
            obj = object.__new__(cls)
            cls.pool[tree_type] = obj
            obj.tree_type = tree_type
        return obj

    def render(self, age, x, y):
        print(
            f'render a tree of type {self.tree_type} and age {age} at({x}, {y})')
        TreeMap.update_map(tree_type=self.tree_type, coordinate=(x, y))


class TreeMap:
    # record the map coordination
    treemap = defaultdict(list)

    @classmethod
    def update_map(cls, tree_type, coordinate):
        cls.treemap[tree_type].append(coordinate)

    @classmethod
    def overview(cls):
        for tree_type, coordinate in cls.treemap.items():
            print(tree_type, coordinate)


def main():
    rnd = random.Random()
    age_min, age_max = 1, 30
    min_point, max_point = 0, 100
    tree_counter = 0
    for _ in range(10):
        t1 = Tree(TreeType.apple_tree)
        t1.render(rnd.randint(age_min, age_max), rnd.randint(
            min_point, max_point), rnd.randint(min_point, max_point))
        tree_counter += 1

    for _ in range(3):
        t1 = Tree(TreeType.cherry_tree)
        t1.render(rnd.randint(age_min, age_max), rnd.randint(
            min_point, max_point), rnd.randint(min_point, max_point))
        tree_counter += 1

    for _ in range(5):
        t1 = Tree(TreeType.peach_tree)
        t1.render(rnd.randint(age_min, age_max), rnd.randint(
            min_point, max_point), rnd.randint(min_point, max_point))
        tree_counter += 1

    print(f'trees rendered: {tree_counter}')
    print(f'trees actually created: {len(Tree.pool)}')
    print(TreeMap.overview())

    t4 = Tree(TreeType.cherry_tree)
    t5 = Tree(TreeType.cherry_tree)
    t6 = Tree(TreeType.apple_tree)

    print(f'{id(t4)}=={id(t5)}? {id(t4)==id(t5)}')
    print(f'{id(t5)}=={id(t6)}? {id(t5)==id(t6)}')


if __name__ == "__main__":
    main()
