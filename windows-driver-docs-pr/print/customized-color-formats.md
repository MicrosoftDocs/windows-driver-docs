---
title: Customized Color Formats
author: windows-driver-content
description: Customized Color Formats
ms.assetid: 309d33e8-6338-4c32-8e03-d6cbf3371e16
keywords:
- Unidrv, color formats
- color formats WDK Unidrv
- customized color formats WDK Unidrv
- Unidrv WDK print
ms.author: windows-driver-content
ms.date: 04/20/2017
ms.topic: article
ms.prod: windows-hardware
ms.technology: windows-devices
---

# Customized Color Formats


## <a href="" id="ddk-customized-color-formats-gg"></a>


Unidrv supports several color formats, which are listed in [Handling Color Formats](handling-color-formats.md). For these formats, Unidrv converts GDI bitmaps into the correct format before sending it to the printer. If your printer accepts formats not supported by Unidrv, you must provide a rendering plug-in that implements the [**IPrintOemUni::ImageProcessing**](https://msdn.microsoft.com/library/windows/hardware/ff554261) method.

If you implement [**IPrintOemUni::ImageProcessing**](https://msdn.microsoft.com/library/windows/hardware/ff554261), and if the user selects a color format (ColorMode option) that Unidrv cannot handle, then each time a buffer of GDI bitmap data is ready for printing, Unidrv calls the method and passes the bitmap's address as an input argument. The method must convert the bitmap to the specified format, perform [customized halftoning](customized-halftoning.md) operations if necessary, and call the [**IPrintOemDriverUni::DrvWriteSpoolBuf**](https://msdn.microsoft.com/library/windows/hardware/ff553138) method to send the modified bitmap to the print spooler. It must also call the [**IPrintOemDriverUni::DrvXMoveTo**](https://msdn.microsoft.com/library/windows/hardware/ff553141) and [**IPrintOemDriverUni::DrvYMoveTo**](https://msdn.microsoft.com/library/windows/hardware/ff553144) methods to update the cursor position. For more information about these operations, see the description of **IPrintOemUni::ImageProcessing**.

If a rendering plug-in implements [**IPrintOemUni::ImageProcessing**](https://msdn.microsoft.com/library/windows/hardware/ff554261), it can also implement [**IPrintOemUni::MemoryUsage**](https://msdn.microsoft.com/library/windows/hardware/ff554264).

 

 


--------------------
[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bprint\print%5D:%20Customized%20Color%20Formats%20%20RELEASE:%20%289/1/2016%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")


