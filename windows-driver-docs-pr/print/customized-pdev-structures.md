---
title: Customized PDEV Structures
author: windows-driver-content
description: Customized PDEV Structures
ms.assetid: e5c51b9a-5f73-4411-88d8-931981a8450c
keywords:
- rendering plug-ins WDK print , PDEV structures
- PDEV WDK print
ms.author: windowsdriverdev
ms.date: 04/20/2017
ms.topic: article
ms.prod: windows-hardware
ms.technology: windows-devices
---

# Customized PDEV Structures


## <a href="" id="ddk-customized-pdev-structures-gg"></a>


The rendering plug-ins implement three methods to support private PDEV structures. Unidrv rendering plug-ins must implement the following methods:

[**IPrintOemUni::EnablePDEV**](https://msdn.microsoft.com/library/windows/hardware/ff554249)

[**IPrintOemUni::DisablePDEV**](https://msdn.microsoft.com/library/windows/hardware/ff554238)

[**IPrintOemUni::ResetPDEV**](https://msdn.microsoft.com/library/windows/hardware/ff554270)

Pscript5 rendering plug-ins must implement the following methods:

[**IPrintOemPS::EnablePDEV**](https://msdn.microsoft.com/library/windows/hardware/ff553215)

[**IPrintOemPS::DisablePDEV**](https://msdn.microsoft.com/library/windows/hardware/ff553209)

[**IPrintOemPS::ResetPDEV**](https://msdn.microsoft.com/library/windows/hardware/ff553233)

PDEV structure is a generic term. It refers to a private, locally defined structure for use by the module that defines it. Typically, it is used for storing physical device characteristics. Each printer driver, and each rendering plug-in, defines its own PDEV structure. There is no globally defined structure of type "PDEV".

 

 


--------------------
[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bprint\print%5D:%20Customized%20PDEV%20Structures%20%20RELEASE:%20%289/1/2016%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")


