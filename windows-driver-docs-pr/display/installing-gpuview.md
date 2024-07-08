---
title: Installing GPUView
description: Lists the components that are packaged with GPUView and describes how to install GPUView.
ms.date: 07/08/2024
---

# Installing GPUView

GPUView and its associated files are a part of the [Windows Performance Toolkit (WPT)](/windows-hardware/test/wpt/), which is a feature that ships with the [Windows Assessment and Deployment Kit (ADK)](/windows-hardware/get-started/adk-install). To get GPUView, make sure that "Windows Performance Toolkit" is selected when you install the ADK.  

The WPT MSI (Microsoft Software Installer) is self-extracting. It installs several files and directories on your operating system. The default installation directory is *Windows Performance Toolkit*, with GPUView and its files installed under the *gpuview* subdirectory. For example, on an x86 machine where the Windows 11 OS is installed at the root directory on C: drive, GPUView is installed in ```C:\Program Files (x86)\Windows Kits\10\Windows Performance Toolkit\gpuview```. You can choose the Custom Installation option for custom placement of the binaries and corresponding support files.

The following table lists a few GPUView-specific files.

| File | Purpose |
| ---- | ------- |
| GPUView.exe          | Program for viewing event trace log (ETL) files with video data |
| Readme.txt           | Various additional information |
| plugins              | Directory that contains various plugin DLLs that are used to interpret events |
| Log.cmd              | Script to turn on and off the appropriate information for logging |
| SymbolSearchPath.txt | A text file that sets the symbol path to resolve stack walk and other events |
| DxEtw.dll            | DLL used by GPUView for internal processing |
