---
title: Customizing Other Printer Interface Operations
description: Customizing Other Printer Interface Operations
ms.assetid: ae59d2e7-9049-432d-b519-9e7c88af8d48
keywords:
- user interface plug-ins WDK print , customization methods
- UI plug-ins WDK print , customization methods
- IPrintOemUI
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# Customizing Other Printer Interface Operations





A UI plug-in can optionally implement any of the following IPrintOemUI methods:

[**IPrintOemUI::DeviceCapabilities**](https://msdn.microsoft.com/library/windows/hardware/ff554162)

[**IPrintOemUI::DevQueryPrintEx**](https://msdn.microsoft.com/library/windows/hardware/ff554172)

[**IPrintOemUI::PrinterEvent**](https://msdn.microsoft.com/library/windows/hardware/ff554182)

[**IPrintOemUI::UpgradePrinter**](https://msdn.microsoft.com/library/windows/hardware/ff554189)

The methods are equivalent to similarly named functions exported by the user-mode [printer interface DLL](printer-interface-dll.md) that is used by Unidrv and Pscript5. These customization methods do not replace the equivalent functions in the driver's printer interface DLL. In each case, the printer interface DLL function is called first, and then the driver calls the plug-in's customization method.

 

 




