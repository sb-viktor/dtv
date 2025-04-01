# directory tree viewer

A simple Python script to display the directory tree structure in the terminal

## Features
- Displays folder and file structure in a tree format.
- Option to show only folders or include files.
- Handles errors gracefully (e.g., inaccessible directories).

## Usage
when running the script, set the folder and `-f` if you want to see along with the files

```bash
C:\My Projects\dtv> py dtv.py "W:\My Projects\dtv"

Directory tree for 'C:\My Projects\dtv':
├── .git
│   ├── hooks
│   ├── info
│   ├── logs
│   │   └── refs
│   │       ├── heads
│   │       └── remotes
│   │           └── origin
│   ├── objects
│   │   ├── 06
│   │   ├── ef
│   │   ├── info
│   │   └── pack
│   └── refs
│       ├── heads
│       ├── remotes
│       │   └── origin
│       └── tags
└── .idea
    ├── dictionaries
    └── inspectionProfiles

```
