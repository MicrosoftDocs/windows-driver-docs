---
title: WIA Driver Versioning
author: windows-driver-content
description: WIA Driver Versioning
MS-HAID:
- 'WIA\_arch\_59e55bce-0b0a-45c2-86e4-3e8a527140ad.xml'
- 'image.wia\_driver\_versioning'
MSHAttr:
- 'PreferredSiteName:MSDN'
- 'PreferredLib:/library/windows/hardware'
ms.assetid: 9ebd79ac-d742-4524-9573-5873f7a8ec37
---

# WIA Driver Versioning


A driver reports the version of WIA (or STI for legacy drivers) that it supports in the version field that is returned from [**IStiUSD::GetCapabilities**](https://msdn.microsoft.com/library/windows/hardware/ff543817). Drivers typically set this field to STI\_VERSION, which is defined in *Sti.h*.

In the Windows Driver Kit (WDK) for Windows Vista, the value of STI\_VERSION is greater than the value of STI\_VERSION in previous operating systems. If a driver has the Windows Vista value for its driver version, it must support Windows Vista [IStream data transfers](istream-data-transfers.md).

A Windows Vista driver that adheres to the new Windows Vista WIA model must return STI\_VERSION\_3 in the version field that is returned from **IStiUSD::GetCapabilities**.

 

 


--------------------
[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bimage\image%5D:%20WIA%20Driver%20Versioning%20%20RELEASE:%20%288/17/2016%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")


