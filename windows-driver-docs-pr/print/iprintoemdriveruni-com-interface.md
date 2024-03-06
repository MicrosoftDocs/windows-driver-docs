---
title: IPrintOemDriverUni COM Interface
description: IPrintOemDriverUni COM Interface
keywords:
- IPrintOemDriverUni
ms.date: 07/17/2023
---

# IPrintOemDriverUni COM Interface

[!include[Print Support Apps](../includes/print-support-apps.md)]

The `IPrintOemDriverUni COM` interface provides a rendering plug-in with access to utility operations supplied by the printer graphics DLL for Unidrv. These operations send a data stream to the print spooler, and obtain driver-managed information.

The following table lists and describes all of the methods defined by the **IPrintOemDriverUni** interface.

| Method | Description |
|--|--|
| [**IPrintOemDriverUni::DrvGetDriverSetting**](/windows-hardware/drivers/ddi/prcomoem/nf-prcomoem-iprintoemdriveruni-drvgetdriversetting) | Returns the current status of printer features and other internal information. |
| [**IPrintOemDriverUni::DrvGetGPDData**](/windows-hardware/drivers/ddi/prcomoem/nf-prcomoem-iprintoemdriveruni-drvgetgpddata) | Enables rendering plug-ins to obtain data defined in a printer's [*generic printer description (GPD)*](/windows-hardware/drivers/#wdkgloss-generic-printer-description--gpd-) file. |
| [**IPrintOemDriverUni::DrvGetStandardVariable**](/windows-hardware/drivers/ddi/prcomoem/nf-prcomoem-iprintoemdriveruni-drvgetstandardvariable) | Enables rendering plug-ins to obtain the current value of Unidrv's [standard variables](standard-variables.md). |
| [**IPrintOemDriverUni::DrvUniTextOut**](/windows-hardware/drivers/ddi/prcomoem/nf-prcomoem-iprintoemdriveruni-drvunitextout) | Enables a rendering plug-in using a device-managed drawing surface to easily output text strings. |
| [**IPrintOemDriverUni::DrvWriteAbortBuf**](/windows-hardware/drivers/ddi/prcomoem/nf-prcomoem-iprintoemdriveruni-drvwriteabortbuf) | Enables a rendering plug-in to reset a printer after a user has terminated a print job. |
| [**IPrintOemDriverUni::DrvWriteSpoolBuf**](/windows-hardware/drivers/ddi/prcomoem/nf-prcomoem-iprintoemdriveruni-drvwritespoolbuf) | Sends printer data to the spooler. |
| [**IPrintOemDriverUni::DrvXMoveTo**](/windows-hardware/drivers/ddi/prcomoem/nf-prcomoem-iprintoemdriveruni-drvxmoveto) | Notifies Unidrv of cursor x-position changes. |
| [**IPrintOemDriverUni::DrvYMoveTo**](/windows-hardware/drivers/ddi/prcomoem/nf-prcomoem-iprintoemdriveruni-drvymoveto) | Notifies Unidrv of cursor y-position changes. |

For more information, see [Implementing Printer Driver COM Interfaces](implementing-printer-driver-com-interfaces.md).
