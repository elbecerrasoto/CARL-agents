# CARL-Agents #

Repo description

## Proposed _Repo_ organization ##

**`./`**
+ `agent.py` Agent API (Base Class)
+ `agents/` Instances of CARL agents, shared API
  + `commons/` Shared agent-submodules 
  + `sampleAgent/` Some agent
+ `algorithms/` RL algorithms, non-shared API (for the moment)
  + `commons/` Shared algorithms-submodules 
  + `sampleAlgorithm/` Some algorithm
+ `__init__.py`
+ `README.md`
+ `runs/` Experiments
  + `commons/` Shared run-submodules 
  + `sampleRun/` Some experiment
