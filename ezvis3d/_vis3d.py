
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

        #default config
        # self.width = '600px'
        # self.height = '600px'


    def plot(self, df_data, center=False, save=False):
        "df_data format is a dataframe with columns x, y, z (required), and style, filter (optional)"
        data = df_data.to_json(orient='records')
        options = self.to_dict()
        return plot(data, options, center=center, save=save)

    def html(self, df_data, center=False, save=False):
        "df_data format is a dataframe with columns x, y, z (required), and style, filter (optional)"
        data = df_data.to_json(orient='records')
        options = self.to_dict()
        return html(data, options, center=center, save=save)

    # def html(self, json_data, save=False):
    #     "json_data is a json list of records, each with fields x, y, z (required), and style, filter (optional)"
    #     options = self.to_dict()
    #     return html(json_data, options, save=save)
