---
title: IPrintOemUI2 COM Interface
description: IPrintOemUI2 COM Interface
keywords:
- IPrintOemUI2
ms.date: 07/17/2023
---

# IPrintOemUI2 COM Interface

[!include[Print Support Apps](../includes/print-support-apps.md)]

The `IPrintOemUI2` COM interface extends the [IPrintOemUI COM interface](iprintoemui-com-interface.md). In addition to all the methods in the **IPrintOemUI** interface, the `IPrintOemUI2` interface provides the following methods.

**Note**  If you are using the Windows Vista version of the Unidrv and Pscript DLLs, you can implement the following methods in Unidrv or Pscript5 plug-ins that run on Windows XP and later versions of Windows operating systems. Previous versions of the DLLs support the **IPrintOEM2::HideStandardUI** method in Pscript5 plug-ins only.

| Method | Description |
|--|--|
| [**IPrintOemUI2::DocumentEvent**](/windows-hardware/drivers/ddi/prcomoem/nf-prcomoem-iprintoemui2-documentevent) | Enables a UI plug-in to replace the core driver UI module's default implementation of the [**DrvDocumentEvent**](/windows-hardware/drivers/ddi/winddiui/nf-winddiui-drvdocumentevent) DDI. |
| [**IPrintOemUI2::HideStandardUI**](/windows-hardware/drivers/ddi/prcomoem/nf-prcomoem-iprintoemui2-hidestandardui) | Enables a UI plug-in to specify whether the standard property sheets should be displayed or hidden. |
| [**IPrintOemUI2::QueryJobAttributes**](/windows-hardware/drivers/ddi/prcomoem/nf-prcomoem-iprintoemui2-queryjobattributes) | Enables a UI plug-in to post-process the core driver's results after a call to the [**DrvQueryJobAttributes**](/windows-hardware/drivers/ddi/winddiui/nf-winddiui-drvqueryjobattributes) DDI. |

For more information, see [Implementing Printer Driver COM Interfaces](implementing-printer-driver-com-interfaces.md).
