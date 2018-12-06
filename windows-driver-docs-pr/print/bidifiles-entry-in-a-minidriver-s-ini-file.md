---
title: BidiFiles Entry in a Minidriver's INI File
description: BidiFiles Entry in a Minidriver's INI File
ms.assetid: 953a29d2-f778-410e-bc8a-a09e294f2473
keywords:
- BidiFiles section
- INF files WDK print , bidi extension file information
- bidi extension files WDK printer autoconfig
- in-box autoconfiguration support WDK printer , bidi extension files
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# BidiFiles Entry in a Minidriver's INI File


A printer minidriver communicates information about the bidi extension file to the port monitor by means of a minidriver-specific INI file. The port monitor uses this information during port initialization.

The following sample shows the `BidiFiles` section of the INI file. The `BidiSPMFile` entry would be used for a standard TCP/IP port monitor, and the `BidiWSDFile` entry would be used for a Web Services for Devices (WSD) port monitor.

```INI
# OEM Mapping & Extension GDL files 
# 
[BidiFiles]
BidiSPMFile = BidiSPM_AcmeXXX.XML
BidiWSDFile  = BidiWSD_AcmeXXX.XML
```
