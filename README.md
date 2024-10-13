# vsctunnel
Developing a Google Colab project using VSCode's Remote Tunnels.

## Installation
```
pip install git+https://github.com/iansyahr/vsctunnel
```

## Usage

```python
import vsctunnel as vct

#Auth Account (Github or Microsoft)
vct.auth_account("Github")

#Run VS Code CLI Remote Server with machine name "janedoe"
vct.run("janedoe")

#Kill VS Code CLI
vct.kill()
```
