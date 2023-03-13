
import matplotlib.pyplot as plt
import base64
from io import BytesIO
from django import template


register = template.Library()

@register.filter(name='PLOT')
def PLOT(list):
    """
    <img src=\'data:image/png;base64,{}\'>'.format(encoded)
    :param list:
    :return:
    """
    fig = plt.figure()


    #plot sth
    # ok
    plt.plot(list)
    plt.grid(color='grey', linestyle='-', linewidth=1)
    # ok

    tmpfile = BytesIO()

    fig.savefig(tmpfile, format='png')
    encoded = base64.b64encode(tmpfile.getvalue()).decode('utf-8')
    plt.close(fig)
    return encoded
