---
title: Introduction to Rendering Plug-Ins
author: windows-driver-content
description: Introduction to Rendering Plug-Ins
ms.assetid: 7e6756ca-822a-4386-bcbd-363a10b1b2a3
keywords: ["rendering plug-ins WDK print , about rendering plug-ins"]
---

# Introduction to Rendering Plug-Ins


## <a href="" id="ddk-introduction-to-rendering-plug-ins-gg"></a>


When you add support for a new printer device to either the [Microsoft Universal printer driver](microsoft-universal-printer-driver.md) (Unidrv) or the [Microsoft PostScript printer driver](microsoft-postscript-printer-driver.md) (Pscript), you can implement COM interface methods to modify the data that the driver sends to the print spooler.

You accomplish this customization by providing a user-mode DLL. This DLL is referred to as a *rendering plug-in*.

It supports following two types of customization:

-   Provide customized versions of some graphics DDI rendering functions.

-   Implement Unidrv-specific or Pscript-specific COM interface methods that modify the rendered image or scan line data stream, or insert Postscript code at specific injection points, before the data stream is sent to the spooler.

**Note**   Rendering plug-ins should never spawn a window directly. For Windows Vista and later, you can provide asynchronous event notification messages to a client computer by using the Asynchronous User Notification XML schema, asyncui.xsd. For more information, see [Asynchronous User Notification Schema](https://msdn.microsoft.com/library/windows/hardware/ff545066)..

 

 

 


--------------------
[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bprint\print%5D:%20Introduction%20to%20Rendering%20Plug-Ins%20%20RELEASE:%20%289/1/2016%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")


