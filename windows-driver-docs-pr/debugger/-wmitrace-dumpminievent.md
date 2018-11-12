---
title: wmitrace.dumpminievent
description: The wmitrace.dumpminievent extension displays the system event log trace fragment, which is stored in a dump file.
ms.assetid: 94debe5f-d125-44d0-99c4-90d8794525df
keywords: ["wmitrace.dumpminievent Windows Debugging"]
ms.author: domars
ms.date: 05/23/2017
topic_type:
- apiref
api_name:
- wmitrace.dumpminievent
api_type:
- NA
ms.localizationpriority: medium
---

# !wmitrace.dumpminievent


The **!wmitrace.dumpminievent** extension displays the system event log trace fragment, which is stored in a dump file.

```dbgcmd
!wmitrace.dumpminievent
```

## <span id="ddk__wmitrace_strdump_dbg"></span><span id="DDK__WMITRACE_STRDUMP_DBG"></span>


### <span id="DLL"></span><span id="dll"></span>DLL

This extension is exported by Wmitrace.dll.

This extension is available in Windows Vista Service Pack 1 (SP1) and later versions of Windows.

This extension is useful only when debugging a minidump file or a full dump file.

### <span id="Additional_Information"></span><span id="additional_information"></span><span id="ADDITIONAL_INFORMATION"></span>Additional Information

For a conceptual overview of event tracing, see the Microsoft Windows SDK. For information about tracing tools, see the Windows Driver Kit (WDK).

Remarks
-------

The *system event log trace fragment* is a copy of the contents of the last buffer of the System Event Log. The **!wmitrace.dumpminievent** extension displays its contents in event log format.

 

 





