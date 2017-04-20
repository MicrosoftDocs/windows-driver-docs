---
title: Reporting Multisample Support
description: Reporting Multisample Support
ms.assetid: 05db3a79-08b3-4476-a016-d9a9bfa48504
keywords:
- DirectX 8.0 release notes WDK Windows 2000 display , multisample rendering, reporting
- multisample rendering WDK DirectX 8.0 , reporting
- rendering multisamples WDK DirectX 8.0 , reporting
ms.author: windows-driver-content
ms.date: 04/20/2017
ms.topic: article
ms.prod: windows-hardware
ms.technology: windows-devices
---

# Reporting Multisample Support


## <span id="ddk_reporting_multisample_support_gg"></span><span id="DDK_REPORTING_MULTISAMPLE_SUPPORT_GG"></span>


A driver reports the multisample capabilities of its associated hardware by specifying the number of samples per pixel for each surface format it reports. The [**DDPIXELFORMAT**](https://msdn.microsoft.com/library/windows/hardware/ff550274) structure has been extended to include a structure called **MultiSampleCaps**. This structure has members that let the driver express the number of samples per pixel for both flip (fullscreen) and blt (windowed) multisampling. Each of these members is a WORD type in which each bit of the WORD value indicates support for a given number of samples per pixel. Hence, the driver can express support for several different sample counts with a single surface format entry.

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20[display\display]:%20Reporting%20Multisample%20Support%20%20RELEASE:%20%282/10/2017%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")




