---
title: WIA Driver Error Handling and Recovery
author: windows-driver-content
description: WIA Driver Error Handling and Recovery
ms.assetid: 6b7772d9-cc54-492a-b849-27cfe8f043f5
ms.author: windowsdriverdev
ms.date: 04/20/2017
ms.topic: article
ms.prod: windows-hardware
ms.technology: windows-devices
---

# WIA Driver Error Handling and Recovery


## <a href="" id="ddk-wia-driver-errors-si"></a>


There are many points in the WIA image acquisition process where errors or delays can occur. In Microsoft Windows Millennium Edition and Windows XP, it is possible to get additional information about the error. In Windows Vista and later operating systems, it is possible to use a mechanism that allows applications and users to gracefully handle and possibly recover from these errors or delays. The Windows Vista mechanism relies on the [IStream data transfers](istream-data-transfers.md), which Windows Me and Windows XP do not support.

This section includes:

[WIA Driver Error Reporting for Windows Me and Windows XP](wia-driver-error-reporting-for-windows-me-and-windows-xp.md)

[WIA Driver Error Recovery for Windows Vista](wia-driver-error-recovery-for-windows-vista.md)

 

 


--------------------
[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bimage\image%5D:%20WIA%20Driver%20Error%20Handling%20and%20Recovery%20%20RELEASE:%20%288/17/2016%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")


