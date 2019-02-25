---
title: Sample Port Monitor
description: Sample Port Monitor
ms.assetid: dac754bf-f39d-439c-974b-889436211ef3
keywords:
- port monitors WDK print , samples
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# Sample Port Monitor





Source code for LOCALMON (Localmon.dll), the port monitor that supports local LPT and COM ports, is included in the Windows Driver Kit (WDK).

Beginning with Windows 2000, all of the functions that LOCALMON exports were incorporated into Localspl.dll, the Local Print Provider. Another change in Windows 2000 and later operating system versions is that port monitors are divided into two DLLs: a port monitor server DLL, and a port monitor user interface DLL. The source code for these DLLs is located in the \\Src\\Print\\Monitors\\Localmon and \\Src\\Print\\Monitors\\Localui subdirectories.

 

 




