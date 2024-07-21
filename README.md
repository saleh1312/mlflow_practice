hoy hoy

to convert notebook to python script :

pip install jupytext

1- jupyter nbconvert --to python --output stage1_preprocess notebooks/1_preprocess.ipynb

2- it produce file python in notebooks , take it to src you packege

3- remove any jupyter lines by vs code ( regex ) -> # In.+