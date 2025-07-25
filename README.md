# grn-thesis

This repo contains code for the pipeline to simulate gene regulatory networks and cell trajectories by using simulators SERGIO and Slingshot to calculate gene expression data and pseudotimes for synethetic cell systems. 

The full pipeline is pipeline.ipynb. You will need to fix the filepaths/move data around. You should be able to find the repository for Slingshot here https://github.com/mossjacob/pyslingshot. You will also need at least the gene.py and sergio.py files from SERGIO https://github.com/PayamDiba/SERGIO. 

# Data Directory

This directory includes some small test GRNs that I used. More importantly, there are some scripts in the pre/postprocessing folders that could be useful. In `preprocessing` I have some scripts for converting tab deliminated files and also for creating csvs from txt files which I had to do for a lot of SERGIO data. In `postprocessing` there is a script to create 'ground truth' files which are simply files that map target genes to their affector genes. This is a type of file in SERGIO so it may be helpful to have scripts for creating them in the pipeline. 

# GRN inital files 

The advantage of this pipeline is that you can create the GRN you want to simulate. You can use the notebook in src/grn_creation to easily create the required files and also get visualizations of the networks.

### cell differentiation file 

This should be a num_cells x num_cells matrix, with each value indicating the probability of the row cell type transitioning to the column cell type.

Requirements: at least one start cell type and one terminal cell type. 

### gene interaction file

This file describes how each gene is regulated by another. The file structure should be as follows:

Every row is an interaction.

The columns are: target gene, number of regulators, regulator 1, regulation intensity, regulator 2, regulation intensity of regulator 2,..., 2.0

The final column is an indicator of regulation type. I still don't fully understand what this means in SERGIO so I don't usually change it. 

### master regulator file 

Master regulators are genes in the gene regulatory network and unregulated by other genes. The structure of this file is: 

master regulator gene id, regulation coefficient on cell type 1, regulation coefficient on cell type 2,..., regulation coefficient on cell type n

# Visualizing

If you have GRN files and want to visualize how the network looks, feel free to run the scripts in src/visualize. `network_visualizer` just visualizes the GRN with colored edges that represent up/downregulation. `recreate_from_file` provides the same simple visuals that you get when running the pipeline in src/grn_creation in case a visual gets lost. 

# Simulating the network 

Utilize src/pipeline.ipynb to finish running the simulation

--------------

## Experiment directories

These contain the experiments I ran for writing my thesis document. Feel free to reference them for examples on how I used the pipeline
