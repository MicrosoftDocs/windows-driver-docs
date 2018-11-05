---
title: wmitrace.dumpmini
description: The wmitrace.dumpmini extension displays the system trace fragment, which is stored in a dump file.
ms.assetid: c6b4c09f-3a73-4467-849b-8570477bc9af
keywords: ["wmitrace.dumpmini Windows Debugging"]
ms.author: domars
ms.date: 05/23/2017
topic_type:
- apiref
api_name:
- wmitrace.dumpmini
api_type:
- NA
ms.localizationpriority: medium
---

# !wmitrace.dumpmini


The **!wmitrace.dumpmini** extension displays the system trace fragment, which is stored in a dump file.

```dbgcmd
!wmitrace.dumpmini
```

## <span id="ddk__wmitrace_strdump_dbg"></span><span id="DDK__WMITRACE_STRDUMP_DBG"></span>


### <span id="DLL"></span><span id="dll"></span>DLL

This extension is exported by Wmitrace.dll.

This extension is available in Windows Vista and later versions of Windows.

This extension is useful only when debugging a minidump file or a full dump file.

### <span id="Additional_Information"></span><span id="additional_information"></span><span id="ADDITIONAL_INFORMATION"></span>Additional Information

For a conceptual overview of event tracing, see the Microsoft Windows SDK. For information about tracing tools, see the Windows Driver Kit (WDK).

Remarks
-------

The *system trace fragment* is a copy of the contents of the last buffer of the System Context Log. Under normal conditions, this is the trace session whose logger ID is 2.

 

 





