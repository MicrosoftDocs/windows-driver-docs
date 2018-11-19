---
title: Customized Data Stream Filtering
description: Customized Data Stream Filtering
ms.assetid: 768d4b95-4d8d-4460-9a8c-c80785f7f799
keywords:
- Unidrv, data stream filtering
- data stream filtering WDK Unidrv
- customized data stream filtering WDK Unidrv
- filtering WDK Unidrv
- Unidrv WDK print
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# Customized Data Stream Filtering





Unidrv allows customized code to perform final post-processing of image data before it is spooled. Such processing might consist of removing adjacent dots, or any other data filtering operation that Unidrv does not provide.

To perform final postprocessing of image data, provide a rendering plug-in that implements the [**IPrintOemUni::FilterGraphics**](https://msdn.microsoft.com/library/windows/hardware/ff554252) method.

The [**IPrintOemUni::FilterGraphics**](https://msdn.microsoft.com/library/windows/hardware/ff554252) method receives scan line data as input. The method must process the data and then send it to the print spooler by calling [**IPrintOemDriverUni::DrvWriteSpoolBuf**](https://msdn.microsoft.com/library/windows/hardware/ff553138). If the **IPrintOemUni::FilterGraphics** method is implemented, Unidrv does not spool printer data. Instead, it sends every data block to the **IPrintOemUni::FilterGraphics** method.

 

 




