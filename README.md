# Project teenspirit

Installer les packages pythons :
pip install -r requirements.txt

### Pour récuper toutes les infos liées à un tweet et son user:
python main.py search <json_output_file>

-> pour l'instant, on ne récupère que 100 tweets par recherche.
TODO: Pour récupérer plus de tweets, récursion comme pour le getUserTimeline

## Pour récupérer les tweets d'une liste d'users
Dans get_users.py remplir la liste des users
python get_users.py <json_output_file>

