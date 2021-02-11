---
title: WdbgExts Target Information
description: WdbgExts Target Information
keywords: ["WdbgExts extensions, target"]
ms.date: 05/23/2017
ms.localizationpriority: medium
---

# WdbgExts Target Information


To determine if the target uses 32-bit or 64-bit pointers for memory addresses, use the function [**IsPtr64**](/windows-hardware/drivers/ddi/wdbgexts/nf-wdbgexts-isptr64).

For information about the target's operating system, use the [**Ioctl**](/windows-hardware/drivers/ddi/wdbgexts/nc-wdbgexts-pwindbg_ioctl_routine) operation [**IG\_GET\_KERNEL\_VERSION**](/windows-hardware/drivers/ddi/wdbgexts/ns-wdbgexts-_dbgkd_get_version64). To get the total number of processors on the target and find out which one is the current processor, use the function [**GetKdContext**](/windows-hardware/drivers/ddi/wdbgexts/nf-wdbgexts-getkdcontext).

The [**GetDebuggerData**](/windows-hardware/drivers/ddi/wdbgexts/nf-wdbgexts-getdebuggerdata) function returns a KDDEBUGGER\_DATA64 or KDDEBUGGER\_DATA32 structure that contains information about the target that the [debugger engine](introduction.md#debugger-engine) has queried or determined during the current session. This information includes certain key target locations and specific status values.

The debugger caches some information obtained from the target. The function [**GetDebuggerCacheSize**](/windows-hardware/drivers/ddi/wdbgexts/nf-wdbgexts-getdebuggercachesize) will return the size of this cache.

### <span id="additional_information"></span><span id="ADDITIONAL_INFORMATION"></span>Additional Information

For a more powerful target API, see [Target Information](target-information.md) in the [Using the Debugger Engine API](using-the-debugger-engine-api.md) section of this documentation.

 

