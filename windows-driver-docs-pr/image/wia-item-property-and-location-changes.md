---
title: WIA Item Property and Location Changes
author: windows-driver-content
description: WIA Item Property and Location Changes
ms.assetid: 4e8b3d2a-a28c-41d1-9c4b-8d85f28cf904
ms.author: windowsdriverdev
ms.date: 04/20/2017
ms.topic: article
ms.prod: windows-hardware
ms.technology: windows-devices
---

# WIA Item Property and Location Changes


## <a href="" id="ddk-wia-item-property-and-location-changes-si"></a>


The simplest way to ensure application compatibility in Windows Vista and previous operating systems is to implement the WIA properties in the Windows XP and Windows Me locations *and* in the Windows Vista locations. Normally, WIA applications that are written for Windows Vista operate only with the WIA properties and locations added for Windows Vista, while applications that are written for Windows XP and Windows Me work only with the WIA properties and locations that are defined in those operating systems. Implementing the properties in both locations allows applications that are written for Windows Vista, Windows XP, and Windows Me to work with the same property set implementation.

In operating systems before Windows Vista, the following WIA properties were located on the root item of a scanner driver that supported flatbed platen scanning. In Windows Vista, they are located on the flatbed item.

-   [**WIA\_DPS\_HORIZONTAL\_BED\_SIZE**](https://msdn.microsoft.com/library/windows/hardware/ff551399) (known as [**WIA\_IPS\_MAX\_HORIZONTAL\_SIZE**](https://msdn.microsoft.com/library/windows/hardware/ff552607) in Windows Vista)

-   [**WIA\_DPS\_VERTICAL\_BED\_SIZE**](https://msdn.microsoft.com/library/windows/hardware/ff551445) (known as [**WIA\_IPS\_MAX\_VERTICAL\_SIZE**](https://msdn.microsoft.com/library/windows/hardware/ff552611) in Windows Vista)

-   [**WIA\_DPS\_OPTICAL\_XRES**](https://msdn.microsoft.com/library/windows/hardware/ff551409) (known as [**WIA\_IPS\_OPTICAL\_XRES**](https://msdn.microsoft.com/library/windows/hardware/ff552620) in Windows Vista)

-   [**WIA\_DPS\_OPTICAL\_YRES**](https://msdn.microsoft.com/library/windows/hardware/ff551410) (known as [**WIA\_IPS\_OPTICAL\_YRES**](https://msdn.microsoft.com/library/windows/hardware/ff552622) in Windows Vista)

-   [**WIA\_DPS\_PREVIEW**](https://msdn.microsoft.com/library/windows/hardware/ff551422) (known as [**WIA\_IPS\_PREVIEW**](https://msdn.microsoft.com/library/windows/hardware/ff552643) in Windows Vista)

-   [**WIA\_DPS\_SHOW\_PREVIEW\_CONTROL**](https://msdn.microsoft.com/library/windows/hardware/ff551432) (known as [**WIA\_IPS\_SHOW\_PREVIEW\_CONTROL**](https://msdn.microsoft.com/library/windows/hardware/ff552652) in Windows Vista)

**Note**   The duplication of WIA properties is needed only for scanners that support flatbed platen scanning or document feeder scanning. The paired properties have the same property identifier for compatibility. The driver can add WIA\_DPS\_*Xxx* properties for the root item and WIA\_IPS\_*Xxx* for other items.

 

 

 


--------------------
[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bimage\image%5D:%20WIA%20Item%20Property%20and%20Location%20Changes%20%20RELEASE:%20%288/17/2016%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")


