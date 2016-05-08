# Schelling Segregation Model
=========================================

## Summary

The Schelling segregation model is a classic agent-based model, demonstrating how even a mild preference for similar neighbors can lead to a much higher degree of segregation than we would intuitively expect. The model consists of agents on a square grid, where each grid cell can contain at most one agent. Agents come in two colors: red and blue. They are happy if a certain number of their eight possible neighbors are of the same color, and unhappy otherwise. Unhappy agents will pick a random empty cell to move to each step, until they are happy. The model keeps running until there are no unhappy agents.

By default, the number of similar neighbors the agents need to be happy is set to 3. That means the agents would be perfectly happy with a majority of their neighbors being of a different color (e.g. a Blue agent would be happy with five Red neighbors and three Blue ones). Despite this, the model consistently leads to a high degree of segregation, with most agents ending up with no neighbors of a different color.

## How to Run

To run the model interactively, run ``run.py`` in this directory. e.g.

```
    $ python run.py
``` 

Then open your browser to [http://127.0.0.1:8888/](http://127.0.0.1:8888/) and press Reset, then Run.

To view and run some example model analyses, launch the IPython Notebook and open ``analysis.ipynb``. 

## Files

* ``run.py``: Launches a model visualization server.
* ``model/world.py``: Contains the overall model class.
* ``model/agents.py``: Contains the class that defines the model agents.
* ``model/server.py``: Defines classes for visualizing the model, both as text and using the Mesa modular server.
* ``analysis.ipybn``: Notebook demonstrating how to run experiments and parameter sweeps on the model.
* ``requirements.txt``: Defines additional external requirements for running the model; in this case, it's just matplotlib, for the interactive analysis in the IPython Notebook.

## Further Reading

Schelling's original paper describing the model:

[Schelling, Thomas C. Dynamic Models of Segregation. Journal of Mathematical Sociology. 1971, Vol. 1, pp 143-186.](https://www.stat.berkeley.edu/~aldous/157/Papers/Schelling_Seg_Models.pdf)

An interactive, browser-based explanation and implementation:

[Parable of the Polygons](http://ncase.me/polygons/), by Vi Hart and Nicky Case.