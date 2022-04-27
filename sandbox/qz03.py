class Pond:
    ducks: list[str]
    bread_slices: int
    def __init__(self, duck_list: list[str], bread: int]):
        """Create a pond objects."""
        Self.ducks = duck_list
        Self.bread_slices = bread

        def add_bred(self, slices:int) -> None:
            Self.bread_slices += slices

    def feeding_frenzy(self) -> None:
        for duck in ducks:
            if(self.bread_slices >= 2):
                self.bread_slices -= 2
            else:
                print(f"{duck} didn't get fed!")