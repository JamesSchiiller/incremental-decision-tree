virtualenv -p python3.6 venv
source venv/bin/activate
pip install numpy
pip install pandas
pip install sklearn
python train.py
python update.py
python perform.py
python print_tree.py

references: 
https://github.com/doubleplusplus/incremental_decision_tree-CART-Random_Forest_python