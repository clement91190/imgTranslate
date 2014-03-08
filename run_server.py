import os
from imgTranslate import app
import imgTranslate.urls

if __name__ == '__main__':
    #port = int(os.environ.get('PORT', 5000))
    port = 5001
    debug = (port == 5000)
    app.run(host='0.0.0.0', port=port, debug=debug)
