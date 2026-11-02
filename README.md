# edurobots

Educational PORIS models based on
[pyPORIS_user](https://github.com/cosmoBots/pyPORIS_user), with the
[pyPORIS](https://github.com/cosmoBots/pyPORIS) toolchain as a submodule.

## Setup

Run the following commands from the repository root:

```bash
git submodule update --init --recursive
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
```

Python 3 is required for generation. Java is needed to open the default Swing
configuration panel. The optional web viewer uses Node.js and npm; see the
toolchain README for its setup.

## Models and generated products

GraphML source models live under `models/`. The toolchain generates Python
classes from GraphML, then exports XML from the Python model. ODS generation
is optional.

```text
models/       GraphML sources and cluster.yaml descriptors
output/py/    generated Python classes and physical companions
output/xml/   generated configuration panel XML
output/ods/   optional generated spreadsheets
```

Generated products are ignored by Git. Legacy XML, ODS, `.out` files and
generated Python classes alongside the source models have been removed;
regenerate them with the current toolchain when needed.

Physical companions may contain handwritten behavior. Keep that code outside
the ignored output tree if it needs to be versioned, and preserve local edits
before deleting generated directories.

## Generate and explore a model

Use the path relative to `models/`, without the `.graphml` extension:

```bash
pyPORIS/porispanel.sh example/example
```

Useful options:

```bash
pyPORIS/porispanel.sh --no-panel example/example  # generate without opening a panel
pyPORIS/porispanel.sh --ods example/example       # also generate a spreadsheet
pyPORIS/porispanel.sh --web example/example       # open the optional web viewer
```

The default viewer is the Java Swing panel. `--web` selects the browser viewer.
Neither viewer is required when using `--no-panel`.

For a model split across several GraphML diagrams, use the directory wrapper:

```bash
pyPORIS/porispanel_dir.sh osiris
pyPORIS/porispanel_dir.sh missionrobot
```

Each directory model needs a `cluster.yaml` descriptor. OSIRIS uses:

```yaml
cluster: osi
root: osiris
```

`cluster` names the generated model; `root` identifies the root GraphML file
without its extension. OSIRIS generates `output/py/osiris/osi/osiPORIS.py`
and `output/xml/osiris/osi.xml`. To create a descriptor for a new directory
model, use `pyPORIS/porispanel_dir.sh --cluster <name> <directory>`.

The missionrobot cluster is named `mr`, with `missionrobot` as its root diagram.
It generates `output/py/missionrobot/mr/mrPORIS.py` and
`output/xml/missionrobot/mr.xml`, keeping the composed model's products separate
from those of the individual `missionrobot/missionrobot` diagram. Use a cluster
name different from the diagram names to avoid XML and ODS filename collisions.

Numeric range labels accept both `minimum < default < maximum` and
`minimum ≤ default ≤ maximum`. Both forms describe inclusive bounds. The
educational models use `<` for easier typing; this is a separator in the
diagram notation, not a strict inequality.

## Private models

Keep private models under `models/secret/`, for example
`models/secret/tanknet.graphml`, and invoke them as `secret/tanknet`.
Directories named `secret` are ignored at any depth, including the generated
Python, XML and ODS product paths. Do not force-add private files to Git.

## Updating the toolchain

The repository pins a specific pyPORIS commit. To update it to `main`:

```bash
git -C pyPORIS fetch origin
git -C pyPORIS switch main
git -C pyPORIS merge --ff-only origin/main
git add pyPORIS
git commit -m "chore(deps): update pyPORIS"
```

Review local submodule changes before updating. Generated products can be
regenerated from the source models after the update. See `pyPORIS/README.md`
for additional commands and cosmoSys synchronization setup.
