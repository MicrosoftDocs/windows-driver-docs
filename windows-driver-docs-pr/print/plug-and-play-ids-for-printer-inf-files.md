---
title: Plug and Play IDs for Printer INF Files
description: Plug and Play IDs for Printer INF Files
keywords:
- INF files WDK print , Plug and Play IDs
- PnP ID WDK print
- Plug and Play IDs WDK print
- identifiers WDK printer
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# Plug and Play IDs for Printer INF Files

You must specify [Plug and Play](plug-and-play-for-printers.md) (PnP) identifiers (IDs) in the [printer INF file install section](printer-inf-file-install-sections.md).

You must use the IDs in the following table, depending on the protocol that the printer uses.

|Protocol|PnP ID in the printer INF file.|
|----|----|
|IEEE 1394|The ID is always specific, with "1394" in the ID string.|
|Parallel|The ID contains "LPTENUM" in the ID string.|
|USB|The ID contains "USBPRINT" in the ID string.|
|Dot4|The ID contains "DOT4PRT" in the ID string. This ID applies to Dot4USB and parallel.|
|Bluetooth|The ID contains "BTHPRINT" in the ID string.|
|WSD|The ID contains "WSDPRINT" in the ID string.|
