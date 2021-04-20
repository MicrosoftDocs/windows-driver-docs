---
title: Customized Color Formats
description: Customized Color Formats
keywords:
- Unidrv, color formats
- color formats WDK Unidrv
- customized color formats WDK Unidrv
- Unidrv WDK print
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# Customized Color Formats





Unidrv supports several color formats, which are listed in [Handling Color Formats](handling-color-formats.md). For these formats, Unidrv converts GDI bitmaps into the correct format before sending it to the printer. If your printer accepts formats not supported by Unidrv, you must provide a rendering plug-in that implements the [**IPrintOemUni::ImageProcessing**](/windows-hardware/drivers/ddi/prcomoem/nf-prcomoem-iprintoemuni-imageprocessing) method.

If you implement [**IPrintOemUni::ImageProcessing**](/windows-hardware/drivers/ddi/prcomoem/nf-prcomoem-iprintoemuni-imageprocessing), and if the user selects a color format (ColorMode option) that Unidrv cannot handle, then each time a buffer of GDI bitmap data is ready for printing, Unidrv calls the method and passes the bitmap's address as an input argument. The method must convert the bitmap to the specified format, perform [customized halftoning](customized-halftoning.md) operations if necessary, and call the [**IPrintOemDriverUni::DrvWriteSpoolBuf**](/windows-hardware/drivers/ddi/prcomoem/nf-prcomoem-iprintoemdriveruni-drvwritespoolbuf) method to send the modified bitmap to the print spooler. It must also call the [**IPrintOemDriverUni::DrvXMoveTo**](/windows-hardware/drivers/ddi/prcomoem/nf-prcomoem-iprintoemdriveruni-drvxmoveto) and [**IPrintOemDriverUni::DrvYMoveTo**](/windows-hardware/drivers/ddi/prcomoem/nf-prcomoem-iprintoemdriveruni-drvymoveto) methods to update the cursor position. For more information about these operations, see the description of **IPrintOemUni::ImageProcessing**.

If a rendering plug-in implements [**IPrintOemUni::ImageProcessing**](/windows-hardware/drivers/ddi/prcomoem/nf-prcomoem-iprintoemuni-imageprocessing), it can also implement [**IPrintOemUni::MemoryUsage**](/windows-hardware/drivers/ddi/prcomoem/nf-prcomoem-iprintoemuni-memoryusage).

 

