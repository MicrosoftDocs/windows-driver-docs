---
title: Sample Port Monitor
description: Sample Port Monitor
ms.assetid: dac754bf-f39d-439c-974b-889436211ef3
keywords:
- port monitors WDK print , samples
ms.date: 08/01/2019
ms.localizationpriority: medium
---

# Sample Port Monitor

> [!NOTE]
> The LOCALMON print monitor sample has been archived and is not available in the [Windows Driver Kit (WDK) 10 samples](https://github.com/microsoft/Windows-driver-samples) repo on GitHub.

Source code for LOCALMON (Localmon.dll), the port monitor that supports local LPT and COM ports, is included in the the [Windows Driver Kit (WDK) 8.0 samples](https://go.microsoft.com/fwlink/p/?LinkId=616509) archive and the [Windows Driver Kit (WDK) 8.1 samples](https://go.microsoft.com/fwlink/p/?LinkId=618052) archive.

The functions that LOCALMON exports are incorporated into Localspl.dll, the Local Print Provider. Port monitors are divided into two DLLs: a port monitor server DLL, and a port monitor user interface DLL.

The source code for these DLLs is located in the \\Print Monitors Samples\\C++\\localmon and \\Print Monitors Samples\\C++\\localui subdirectories of the WDK samples archives listed above.
