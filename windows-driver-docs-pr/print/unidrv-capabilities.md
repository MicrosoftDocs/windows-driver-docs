---
title: Unidrv Capabilities
description: Unidrv Capabilities
keywords:
- Unidrv, capabilities
- Unidrv WDK print
ms.date: 01/30/2023
---

# Unidrv Capabilities

[!include[Print Support Apps](../includes/print-support-apps.md)]

The Universal Printer Driver (Unidrv) provides the following capabilities:

- Support for all non-Postscript printers, using printer-specific [Unidrv minidrivers](unidrv-minidrivers.md) that describe each printer's characteristics.

- A [Unidrv user interface](unidrv-user-interface.md), based on the TreeView control and property sheets, that is consistent for all printers, but is also modifiable for each printer's unique options.

- A single [Unidrv renderer](unidrv-renderer.md) that, along with the GDI graphics engine, converts Microsoft Win32 GDI calls from applications into printer commands that can be sent to the print spooler.
