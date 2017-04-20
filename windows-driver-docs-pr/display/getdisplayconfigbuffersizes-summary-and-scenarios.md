---
title: GetDisplayConfigBufferSizes Summary and Scenarios
description: GetDisplayConfigBufferSizes Summary and Scenarios
ms.assetid: b0d14ba7-fe61-49e9-81c5-097e6e07a51a
keywords:
- connecting displays WDK Windows 7 display , CCD APIs, GetDisplayConfigBufferSizes
- connecting displays WDK Windows Server 2008 R2 display , CCD APIs, GetDisplayConfigBufferSizes
- configuring displays WDK Windows 7 display , CCD APIs, GetDisplayConfigBufferSizes
- configuring displays WDK Windows Server 2008 R2 display , CCD APIs, GetDisplayConfigBufferSizes
- CCD concepts WDK Windows 7 display , GetDisplayConfigBufferSizes
- CCD concepts WDK Windows Server 2008 R2 display , GetDisplayConfigBufferSizes
- GetDisplayConfigBufferSizes WDK Windows 7 display
- GetDisplayConfigBufferSizes WDK Windows Server 2008 R2 display
ms.author: windows-driver-content
ms.date: 04/20/2017
ms.topic: article
ms.prod: windows-hardware
ms.technology: windows-devices
---

# GetDisplayConfigBufferSizes Summary and Scenarios


This section applies only to Windows 7 and later, and Windows Server 2008 R2 and later versions of Windows operating system.

The following sections summarize how a caller uses [**GetDisplayConfigBufferSizes**](https://msdn.microsoft.com/library/windows/hardware/ff566772) CCD function and provide scenarios for using **GetDisplayConfigBufferSizes**.

### <span id="getdisplayconfigbuffersizes_summary"></span><span id="GETDISPLAYCONFIGBUFFERSIZES_SUMMARY"></span>GetDisplayConfigBufferSizes Summary

The caller can use [**GetDisplayConfigBufferSizes**](https://msdn.microsoft.com/library/windows/hardware/ff566772) to obtain information that the caller requires for the [**QueryDisplayConfig**](https://msdn.microsoft.com/library/windows/hardware/ff569215) CCD function.

### <span id="getdisplayconfigbuffersizes_scenarios"></span><span id="GETDISPLAYCONFIGBUFFERSIZES_SCENARIOS"></span>GetDisplayConfigBufferSizes Scenarios

[**GetDisplayConfigBufferSizes**](https://msdn.microsoft.com/library/windows/hardware/ff566772) is always called before calling [**QueryDisplayConfig**](https://msdn.microsoft.com/library/windows/hardware/ff569215).

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20[display\display]:%20GetDisplayConfigBufferSizes%20Summary%20and%20Scenarios%20%20RELEASE:%20%282/10/2017%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")




