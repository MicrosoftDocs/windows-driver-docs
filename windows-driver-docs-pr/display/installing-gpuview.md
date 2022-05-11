---
title: Installing GPUView
description: "This section lists the components that are packaged with GPUView and describes how to install GPUView."
ms.date: 05/10/2022
---

# Installing GPUView

This section lists the components that are packaged with GPUView and describes how to install GPUView.

GPUView is shipped with the Windows Performance Toolkit (WPT) as an installable option of the WPT MSI. You should install the appropriate WPT MSI for the appropriate platform (for example, Wpt_x86.msi for an x86 platform or Wpt_amd64.msi for an amd64 platform). 

The MSI file installs the following files.

| Files Purpose                                                                                           | Purpose                                                                      |
|---------------------------------------------------------------------------------------------------------|------------------------------------------------------------------------------|
| EULA.rtf                                                                                                | Legal agreement                                                              |
| GPUView.chm                                                                                             | GPUView help file                                                            |
| Readme.txt                                                                                              | Any additional information that does not fit in the format of the help file  |
| GPUView.exe                                                                                             | Program for viewing ETL files with video data                                |
| AEplugin.dll, DWMPlugin.dll, FWPlugin.dll, MFPlugin.dll, NTPlugin.dll, DxPlugin.dll, and DxgkPlugin.dll | Plug-ins that are used to interpret events                                   |
| DxEtw.dll and Perf_gpuv.dll                                                                             | DLLs used by GPUView for internal processing and accessing xperf information |
| CoreTPlugin.dll                                                                                         | Plug-in that is used for the Statistical Options dialog box                  |
| Log.cmd, Circularlog.cmd                                                                                | Script to turn on and off the appropriate information for logging            |

The MSI file is self-extracting. It installs (or uninstalls) GPUView on your operating system. The default installation directory is in the \Microsoft Windows Performance Toolkit directory. You can choose the Custom Installation option for custom placement of the binaries and corresponding support files.

