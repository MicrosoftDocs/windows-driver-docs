---
title: WdbgExts Target Information
description: WdbgExts Target Information
ms.assetid: 70b26047-2f3a-4d35-861f-a9ca17d1d5f9
keywords: ["WdbgExts extensions, target"]
ms.author: windowsdriverdev
ms.date: 05/23/2017
ms.topic: article
ms.prod: windows-hardware
ms.technology: windows-devices
---

# WdbgExts Target Information


To determine if the target uses 32-bit or 64-bit pointers for memory addresses, use the function [**IsPtr64**](https://msdn.microsoft.com/library/windows/hardware/ff551094).

For information about the target's operating system, use the [**Ioctl**](https://msdn.microsoft.com/library/windows/hardware/ff551084) operation [**IG\_GET\_KERNEL\_VERSION**](https://msdn.microsoft.com/library/windows/hardware/ff550918). To get the total number of processors on the target and find out which one is the current processor, use the function [**GetKdContext**](https://msdn.microsoft.com/library/windows/hardware/ff546962).

The [**GetDebuggerData**](https://msdn.microsoft.com/library/windows/hardware/ff546573) function returns a KDDEBUGGER\_DATA64 or KDDEBUGGER\_DATA32 structure that contains information about the target that the [debugger engine](introduction.md#debugger-engine) has queried or determined during the current session. This information includes certain key target locations and specific status values.

The debugger caches some information obtained from the target. The function [**GetDebuggerCacheSize**](https://msdn.microsoft.com/library/windows/hardware/ff546568) will return the size of this cache.

### <span id="additional_information"></span><span id="ADDITIONAL_INFORMATION"></span>Additional Information

For a more powerful target API, see [Target Information](target-information.md) in the [Using the Debugger Engine API](using-the-debugger-engine-api.md) section of this documentation.

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20[debugger\debugger]:%20WdbgExts%20Target%20Information%20%20RELEASE:%20%285/15/2017%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")




