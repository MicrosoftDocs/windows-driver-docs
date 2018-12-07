---
title: Downloading Driver-Specific Files
description: Downloading Driver-Specific Files
ms.assetid: 7ac5057a-32fb-4c3a-a5c3-3fc1217dbdc6
keywords:
- Point and Print WDK , driver-specific files
- driver-specific files WDK printer
- downloading driver-specific printer files
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# Downloading Driver-Specific Files





A client system creates a connection to a print server by calling **AddPrinterConnection**. This call results in a call to **GetPrinterDriver** on the server, which reads the [printer's INF file](printer-inf-files.md) in order to fill in a DRIVER\_INFO\_3 structure, followed by a call to **AddPrinterDriver**, with the DRIVER\_INFO\_3 structure as input. The **AddPrinterDriver** function causes all files listed in the DRIVER\_INFO\_3 structure to be sent to the client.

These functions and the DRIVER\_INFO\_3 structure are described in the Microsoft Windows SDK documentation.

 

 




