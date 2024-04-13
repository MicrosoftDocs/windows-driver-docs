---
title: Print Ticket and Capabilities - Unidrv/Pscript5
description: Print ticket and print capabilities provider interface implemented by Unidrv/Pscript5 plug-ins
keywords:
- Unidrv WDK print
ms.date: 01/30/2023
---

# Print ticket and print capabilities provider interface implemented by Unidrv/Pscript5 plug-ins

[!include[Print Support Apps](../includes/print-support-apps.md)]

The [Microsoft Universal Printer Driver](microsoft-universal-printer-driver.md) (Unidrv) and [Microsoft PostScript Printer Driver](microsoft-postscript-printer-driver.md) (Pscript5) core printer drivers on Windows Vista provide the means for plug-ins to implement print ticket support. Because Unidrv and Pscript5 both support loading multiple plug-ins for a single driver, each plug-in is able to provide its own provider implementation. The driver vendor is responsible for ensuring that each of the OEM plug-in provider implementations works correctly with the others. Not all of the plug-ins in a printer driver need to support the provider interface. However, the versions of the print ticket schema that are supported by the core driver are a subset of the versions that are supported by the core driver and all of the available plug-in providers. Because calls into the plug-in provider are driven by the application, the plug-in provider must be implemented in a thread-safe manner.
