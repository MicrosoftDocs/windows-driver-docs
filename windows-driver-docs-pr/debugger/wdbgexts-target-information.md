---
title: WdbgExts Target Information
description: WdbgExts Target Information
ms.assetid: 70b26047-2f3a-4d35-861f-a9ca17d1d5f9
keywords: ["WdbgExts extensions, target"]
ms.author: domars
ms.date: 05/23/2017
ms.localizationpriority: medium
---

# WdbgExts Target Information


To determine if the target uses 32-bit or 64-bit pointers for memory addresses, use the function [**IsPtr64**](https://msdn.microsoft.com/library/windows/hardware/ff551094).

For information about the target's operating system, use the [**Ioctl**](https://msdn.microsoft.com/library/windows/hardware/ff551084) operation [**IG\_GET\_KERNEL\_VERSION**](https://msdn.microsoft.com/library/windows/hardware/ff550918). To get the total number of processors on the target and find out which one is the current processor, use the function [**GetKdContext**](https://msdn.microsoft.com/library/windows/hardware/ff546962).

The [**GetDebuggerData**](https://msdn.microsoft.com/library/windows/hardware/ff546573) function returns a KDDEBUGGER\_DATA64 or KDDEBUGGER\_DATA32 structure that contains information about the target that the [debugger engine](introduction.md#debugger-engine) has queried or determined during the current session. This information includes certain key target locations and specific status values.

The debugger caches some information obtained from the target. The function [**GetDebuggerCacheSize**](https://msdn.microsoft.com/library/windows/hardware/ff546568) will return the size of this cache.

### <span id="additional_information"></span><span id="ADDITIONAL_INFORMATION"></span>Additional Information

For a more powerful target API, see [Target Information](target-information.md) in the [Using the Debugger Engine API](using-the-debugger-engine-api.md) section of this documentation.

 

 





