---
title: Customized Data Stream Filtering
author: windows-driver-content
description: Customized Data Stream Filtering
ms.assetid: 768d4b95-4d8d-4460-9a8c-c80785f7f799
keywords: ["Unidrv, data stream filtering", "data stream filtering WDK Unidrv", "customized data stream filtering WDK Unidrv", "filtering WDK Unidrv", "Unidrv WDK print"]
---

# Customized Data Stream Filtering


## <a href="" id="ddk-customized-data-stream-filtering-gg"></a>


Unidrv allows customized code to perform final post-processing of image data before it is spooled. Such processing might consist of removing adjacent dots, or any other data filtering operation that Unidrv does not provide.

To perform final postprocessing of image data, provide a rendering plug-in that implements the [**IPrintOemUni::FilterGraphics**](https://msdn.microsoft.com/library/windows/hardware/ff554252) method.

The [**IPrintOemUni::FilterGraphics**](https://msdn.microsoft.com/library/windows/hardware/ff554252) method receives scan line data as input. The method must process the data and then send it to the print spooler by calling [**IPrintOemDriverUni::DrvWriteSpoolBuf**](https://msdn.microsoft.com/library/windows/hardware/ff553138). If the **IPrintOemUni::FilterGraphics** method is implemented, Unidrv does not spool printer data. Instead, it sends every data block to the **IPrintOemUni::FilterGraphics** method.

 

 


--------------------
[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bprint\print%5D:%20Customized%20Data%20Stream%20Filtering%20%20RELEASE:%20%289/1/2016%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")


