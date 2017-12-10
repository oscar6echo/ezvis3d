
from ._wrapper import Wrapper
from ._plot import plot, html


class Vis3d(Wrapper):
    """
    Main vis3d Object

    Examples: http://visjs.org/graph3d_examples.html
    Docs: http://visjs.org/docs/graph3d/
    """

    def __init__(self):
        Wrapper.__init__(self)

        # default config
        # self.width = '600px'
        # self.height = '600px'

    def plot(self, df_data, center=False, save=False,
             save_name=None, save_path='saved', dated=True, notebook=True):
        "df_data format is a dataframe with columns x, y, z (required), and style, filter (optional)"
        data = df_data.to_json(orient='records')
        options = self.to_dict()
        return plot(data, options, center=center, save=save,
                    save_name=save_name, save_path=save_path, dated=dated, notebook=notebook)

    def html(self, df_data, center=False, save=False,
             save_name=None, save_path='saved', dated=True, notebook=True):
        "df_data format is a dataframe with columns x, y, z (required), and style, filter (optional)"
        data = df_data.to_json(orient='records')
        options = self.to_dict()
        return html(data, options, center=center, save=save,
                    save_name=save_name, save_path=save_path, dated=dated, notebook=notebook)
