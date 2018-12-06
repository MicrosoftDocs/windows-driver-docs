---
title: Unidrv Capabilities
description: Unidrv Capabilities
ms.assetid: e715e6c7-32cf-4db1-a6d2-3577824249c1
keywords:
- Unidrv, capabilities
- Unidrv WDK print
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# Unidrv Capabilities





The Universal Printer Driver (Unidrv) provides the following capabilities:

-   Support for all non-Postscript printers, using printer-specific [Unidrv minidrivers](unidrv-minidrivers.md) that describe each printer's characteristics.

-   A [Unidrv user interface](unidrv-user-interface.md), based on the TreeView control and property sheets, that is consistent for all printers, but is also modifiable for each printer's unique options.

-   A single [Unidrv renderer](unidrv-renderer.md) that, along with the GDI graphics engine, converts Microsoft Win32 GDI calls from applications into printer commands that can be sent to the print spooler.

 

 




