---
title: IPrintOemDriverPS COM Interface
description: IPrintOemDriverPS COM Interface
keywords:
- IPrintOemDriverPS
ms.date: 07/14/2023
---

# IPrintOemDriverPS COM Interface

[!include[Print Support Apps](../includes/print-support-apps.md)]

The `IPrintOemDriverPS` COM interface provides a rendering plug-in with access to utility operations supplied by the printer graphics DLL for Pscript5. These operations send a data stream to the print spooler and obtain driver-managed information.

The following table lists and describes all of the methods defined by the `IPrintOemDriverPS` interface.

| Method | Description |
|--|--|
| [**IPrintOemDriverPS::DrvGetDriverSetting**](/windows-hardware/drivers/ddi/prcomoem/nf-prcomoem-iprintoemdriverps-drvgetdriversetting) | Returns the current status of printer features and other internal information. |
| [**IPrintOemDriverPS::DrvWriteSpoolBuf**](/windows-hardware/drivers/ddi/prcomoem/nf-prcomoem-iprintoemdriverps-drvwritespoolbuf) | Sends printer data to the spooler. |

For more information, see [Implementing Printer Driver COM Interfaces](implementing-printer-driver-com-interfaces.md).
