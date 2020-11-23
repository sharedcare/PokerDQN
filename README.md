# PokerDQN
## Requirements
```
python>3.5
pytorch-1.7.0
tensorflow-1.15
rlcard
```
## Installation
Make sure your Python version is **>3.5**. Install the requirements with conda.
```
git clone https://github.com/sharedcare/PokerDQN.git
conda env create -f environment.yml
```
## Todo
- [x] Poker Environment (no limit Hold'em)
- [ ] Build our own DQN agent
- [ ] Run training and test the model
- [ ] Compare our algorithm with others
- [ ] Make a demo game AI

## Tutorial
To begin with, you can play with [toy_example.py](../blob/master/toy_example.py) and [toy_example_human.py.](../blob/master/toy_example_human.py). you can also refer to [RLCard](https://github.com/datamllab/rlcard) for details.

The environment is based on [rlcard.envs.nolimitholdem](https://rlcard.org/rlcard.envs.html#module-rlcard.envs.nolimitholdem)

## References
```
@article{zha2019rlcard,
  title={RLCard: A Toolkit for Reinforcement Learning in Card Games},
  author={Zha, Daochen and Lai, Kwei-Herng and Cao, Yuanpu and Huang, Songyi and Wei, Ruzhe and Guo, Junyu and Hu, Xia},
  journal={arXiv preprint arXiv:1910.04376},
  year={2019}
}
```