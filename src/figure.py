class Figure:
    def get_area(self):
        raise NotImplementedError

    def get_perimeter(self):
        raise NotImplementedError

    def add_area(self, figure):
        if not isinstance(figure, Figure):
            raise ValueError
        return self.get_area() + figure.get_area()
