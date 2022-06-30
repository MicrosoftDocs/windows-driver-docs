---
title: Installing GPUView
description: "This section lists the components that are packaged with GPUView and describes how to install GPUView."
ms.date: 06/30/2022
---

# Installing GPUView

GPUView and other files that are associated with it are included with the [Windows Performance Toolkit (WPT)](/windows-hardware/test/wpt/, installed with the [Windows Assessment and Deployment Kit (ADK)](/windows-hardware/get-started/adk-install) as an installable option of the WPT MSI (Microsoft Software Intaller).

The WPT MSI installs several files and directories. The following table lists a few GPUView-specific files.

| File | Purpose |
| ---- | ------- |
| GPUView.exe | Program for viewing ETL files with video data |
| Readme.txt | Various additional information |
| plugins     | Directory that contains various plugin DLLs that are used to interpret events |
| Log.cmd     | Script to turn on and off the appropriate information for logging |
| SymbolSearchPath.txt | A text file that sets the symbol path to resolve stackwalk and other events |
| DxEtw.dll | DLL used by GPUView for internal processing |

The MSI file is self-extracting. It installs (or uninstalls) the WPT on your operating system. The default installation directory is in the *\Microsoft Windows Performance Toolkit* directory. For example, the WPT for an x86 platform might be installed in a directory such as *\Program Files (x86)\Windows Kits\10\Windows Performance Toolkit*. You can choose the Custom Installation option for custom placement of the binaries and corresponding support files.
