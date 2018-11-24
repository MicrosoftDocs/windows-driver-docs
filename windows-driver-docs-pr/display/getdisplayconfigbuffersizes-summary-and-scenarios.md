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
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# GetDisplayConfigBufferSizes Summary and Scenarios


This section applies only to Windows 7 and later, and Windows Server 2008 R2 and later versions of Windows operating system.

The following sections summarize how a caller uses [**GetDisplayConfigBufferSizes**](https://msdn.microsoft.com/library/windows/hardware/ff566772) CCD function and provide scenarios for using **GetDisplayConfigBufferSizes**.

### <span id="getdisplayconfigbuffersizes_summary"></span><span id="GETDISPLAYCONFIGBUFFERSIZES_SUMMARY"></span>GetDisplayConfigBufferSizes Summary

The caller can use [**GetDisplayConfigBufferSizes**](https://msdn.microsoft.com/library/windows/hardware/ff566772) to obtain information that the caller requires for the [**QueryDisplayConfig**](https://msdn.microsoft.com/library/windows/hardware/ff569215) CCD function.

### <span id="getdisplayconfigbuffersizes_scenarios"></span><span id="GETDISPLAYCONFIGBUFFERSIZES_SCENARIOS"></span>GetDisplayConfigBufferSizes Scenarios

[**GetDisplayConfigBufferSizes**](https://msdn.microsoft.com/library/windows/hardware/ff566772) is always called before calling [**QueryDisplayConfig**](https://msdn.microsoft.com/library/windows/hardware/ff569215).

 

 





