---
title: Sample IDE Controller Minidrivers
author: windows-driver-content
description: Sample IDE Controller Minidrivers
ms.assetid: 3c8779ae-30d7-4ab8-b6d8-a711f917564c
keywords: ["IDE controller minidrivers WDK storage , samples", "storage IDE controller minidrivers WDK , samples"]
---

# Sample IDE Controller Minidrivers


## <span id="ddk_sample_ide_controller_minidrivers_kg"></span><span id="DDK_SAMPLE_IDE_CONTROLLER_MINIDRIVERS_KG"></span>


This section identifies the sample IDE controller minidriver included with the Microsoft Windows Driver Kit (WDK).

The WDK includes the source code for the *pciide.sys* generic controller minidriver. See the sample code in the \\src\\storage directory of the WDK.

This sample is 64-bit compliant. It builds with Microsoft Visual C 6.0 and does not implement Plug and Play or Power Management.

The *pciide.sys* sample is binary compatible between Windows 95/98/Me and NT-based versions of the operating system, provided no Windows 95/98/Me VxD calls nor any NT-based system calls are embedded in the minidriver.

 

 


--------------------
[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20[storage\storage]:%20Sample%20IDE%20Controller%20Minidrivers%20%20RELEASE:%20%285/9/2016%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")


