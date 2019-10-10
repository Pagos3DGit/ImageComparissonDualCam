#============================
import os
on_rtd = os.environ.get('READTHEDOCS', None) == 'True'

if not on_rtd:  # only import and set the theme if we're building docs locally
    import sphinx_rtd_theme
    html_theme = 'sphinx_rtd_theme'
    html_theme_path = [sphinx_rtd_theme.get_html_theme_path()]

#==============================pifacedigitalo.core==========================================================================================
listener.register(0, pifacedigitalio.IODIR_ON, print_flag)
listener.activate()
    def __init__(self, chip=None):
    def __init__(self, chip=None, daemon=False):
        if chip is None:
            chip = PiFaceDigital()
        super(InputEventListener, self).__init__(
            pifacecommon.mcp23s17.GPIOB, chip)
        
        super(InputEventListener, self).__init__(pifacecommon.mcp23s17.GPIOB,
                                                 chip)
        self.detector.daemon = daemon
        self.dispatcher.daemon = daemon


def init(init_board=True,
#================================pifacedigitalo.version.py========================================================================

__version__ = '3.0.5'
__version__ = '3.1.0'
