---
title: Introduction to Rendering Plug-Ins
description: Introduction to Rendering Plug-Ins
ms.assetid: 7e6756ca-822a-4386-bcbd-363a10b1b2a3
keywords:
- rendering plug-ins WDK print , about rendering plug-ins
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# Introduction to Rendering Plug-Ins





When you add support for a new printer device to either the [Microsoft Universal printer driver](microsoft-universal-printer-driver.md) (Unidrv) or the [Microsoft PostScript printer driver](microsoft-postscript-printer-driver.md) (Pscript), you can implement COM interface methods to modify the data that the driver sends to the print spooler.

You accomplish this customization by providing a user-mode DLL. This DLL is referred to as a *rendering plug-in*.

It supports following two types of customization:

-   Provide customized versions of some graphics DDI rendering functions.

-   Implement Unidrv-specific or Pscript-specific COM interface methods that modify the rendered image or scan line data stream, or insert Postscript code at specific injection points, before the data stream is sent to the spooler.

**Note**   Rendering plug-ins should never spawn a window directly. For Windows Vista and later, you can provide asynchronous event notification messages to a client computer by using the Asynchronous User Notification XML schema, asyncui.xsd. For more information, see [Asynchronous User Notification Schema](https://msdn.microsoft.com/library/windows/hardware/ff545066)..

 

 

 




