# Basic centerout RNN

Basic RNN for performing center-out task based on experimental monkey data. Use as starting code for simulations to study motor control.

## Getting Started
1. Clone the repository
   ```
   git clone https://github.com/NeuralAnalysis/PyalData.git
   cd PyalData
   ```
2. Create and activate the conda environment
   ```
   conda env create -f env.yml
   conda activate base_rnn
   ```
3. Install the package and dependencies with 
   ```
   pip install -e .
   ```
   from the root of the repository. 
  
## Reproducing figures
Each figure in the paper has an associated Jupyter notebook under ```paper/```. Running the cells reproduces all of the subfigures, and the first cell runs the simulations associated with the figure.
