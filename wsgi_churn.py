import os
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parent))

from app_churn import app

if __name__ == '__main__':
    port = int(os.environ.get('PORT', 5000))
    debug = os.environ.get('DEBUG', 'False') == 'True'
    app.run(host='0.0.0.0', port=port, debug=debug)
