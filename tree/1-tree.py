
class TreeNode:
    def __init__(self, val):
        self.val = val
        self.children = []
        self.parent = None

    def add_child(self, child):
        child.parent = self
        self.children.append(child)

    def get_level(self):
        level = 0
        node = self
        while node.parent:
            level += 1
            node = node.parent
        return level

    def print(self):
        spaces = " " * self.get_level() * 3
        prefix = spaces + "|__" if self.parent else ""
        print(prefix + self.val)
        if not self.children:
            return
        for child in self.children:
            child.print()
        print()


def build_tree():
    root = TreeNode("watchlist")

    anime = TreeNode("anime")
    root.add_child(anime)
    anime.add_child(TreeNode("naruto"))
    anime.add_child(TreeNode("one_piece"))
    anime.add_child(TreeNode("death_node"))

    movie = TreeNode("movie")
    root.add_child(movie)
    movie.add_child(TreeNode("pulp_fiction"))
    movie.add_child(TreeNode("django_unchained"))
    movie.add_child(TreeNode("reservoir_dogs"))

    series = TreeNode("series")
    root.add_child(series)
    series.add_child(TreeNode("breaking_bad"))
    series.add_child(TreeNode("game_of_thrones"))
    series.add_child(TreeNode("dark"))

    root.print()

if __name__ == '__main__':
    build_tree()


    








