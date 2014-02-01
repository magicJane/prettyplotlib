__author__ = 'jgosmann'

from prettyplotlib.utils import remove_chartjunk, maybe_get_ax
from prettyplotlib.colors import set2


def eventplot(*args, **kwargs):
    ax, args, kwargs = maybe_get_ax(*args, **kwargs)
    show_ticks = kwargs.pop('show_ticks', False)

    # FIXME 1d positions
    if len(args) > 0:
        positions = args[0]
    else:
        positions = kwargs['positions']
    kwargs.setdefault('colors', [c + (1.0,) for c in set2[:len(positions)]])

    event_collections = ax.eventplot(*args, **kwargs)
    remove_chartjunk(ax, ['top', 'right'], show_ticks=show_ticks)
    return event_collections
