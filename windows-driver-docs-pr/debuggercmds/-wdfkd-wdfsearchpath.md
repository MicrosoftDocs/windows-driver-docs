---
title: "!wdfkd.wdfsearchpath"
description: "The !wdfkd.wdfsearchpath extension sets the search path to formatting files for Kernel-Mode Driver Framework (KMDF) error log records."
keywords: ["!wdfkd.wdfsearchpath Windows Debugging"]
ms.date: 05/23/2017
topic_type:
- apiref
ms.topic: reference
api_name:
- wdfkd.wdfsearchpath
api_location:
- Wdfkd.dll
api_type:
- DllExport
---

# !wdfkd.wdfsearchpath

The **!wdfkd.wdfsearchpath** extension sets the search path to formatting files for Kernel-Mode Driver Framework (KMDF) error log records.

```dbgcmd
!wdfkd.wdfsearchpath Path
```

## Parameters

<span id="_______Path______"></span><span id="_______path______"></span><span id="_______PATH______"></span> *Path*   
The path of a directory that contains KMDF formatting files.

## DLL

Wdfkd.dll

## Frameworks

KMDF 1, UMDF 2

## Additional Information

For more information, see [Kernel-Mode Driver Framework Debugging](../debugger/kernel-mode-driver-framework-debugging.md).

## Remarks

The KMDF formatting files are included in the Windows Driver Kit (WDK). The path to the formatting files depends on the installation directory of your WDK and on the version of the WDK that you have installed. The KMDF formatting files have extension tmf (trace message formatting). To determine the search path, browse or search your WDK installation for file names of the form Wdf*VersionNumber*.tmf. The following example shows how to use the **!wdfkd.wdfsearchpath** extension.

```dbgcmd
kd> !wdfsearchpath C:\WinDDK\7600\tools\tracing\amd64
```

The TRACE\_FORMAT\_SEARCH\_PATH environment variable also controls the search path, but the **!wdfkd.wdfsearchpath** extension takes precedence over the search path that TRACE\_FORMAT\_SEARCH\_PATH specifies.
