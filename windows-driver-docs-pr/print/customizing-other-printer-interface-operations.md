---
title: Customizing Other Printer Interface Operations
description: Customizing Other Printer Interface Operations
keywords:
- user interface plug-ins WDK print , customization methods
- UI plug-ins WDK print , customization methods
- IPrintOemUI
ms.date: 04/20/2017
---

# Customizing Other Printer Interface Operations





A UI plug-in can optionally implement any of the following IPrintOemUI methods:

[**IPrintOemUI::DeviceCapabilities**](/windows-hardware/drivers/ddi/prcomoem/nf-prcomoem-iprintoemui-devicecapabilities)

[**IPrintOemUI::DevQueryPrintEx**](/windows-hardware/drivers/ddi/prcomoem/nf-prcomoem-iprintoemui-devqueryprintex)

[**IPrintOemUI::PrinterEvent**](/windows-hardware/drivers/ddi/prcomoem/nf-prcomoem-iprintoemui-printerevent)

[**IPrintOemUI::UpgradePrinter**](/windows-hardware/drivers/ddi/prcomoem/nf-prcomoem-iprintoemui-upgradeprinter)

The methods are equivalent to similarly named functions exported by the user-mode [printer interface DLL](printer-interface-dll.md) that is used by Unidrv and Pscript5. These customization methods do not replace the equivalent functions in the driver's printer interface DLL. In each case, the printer interface DLL function is called first, and then the driver calls the plug-in's customization method.

 

