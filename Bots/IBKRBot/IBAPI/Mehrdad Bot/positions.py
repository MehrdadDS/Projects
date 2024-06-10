# positions.py
import time
import pandas as pd

class Positions:
    def __init__(self, app):
        self.app = app
        self.positions = []

    def update_positions(self):
        self.app.reqPositions()
        while len(self.app.positions) == 0:
            time.sleep(1)
        self.positions = self.app.positions
        self.app.positions = []
        return self.positions

    def get_positions_df(self):
        positions_data = self.update_positions()
        positions_df = pd.DataFrame(positions_data)
        return positions_df
