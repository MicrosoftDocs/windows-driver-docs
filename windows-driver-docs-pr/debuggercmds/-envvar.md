---
title: "!envvar (WinDbg)"
description: "The !envvar extension displays the value of the specified environment variable."
keywords: ["!envvar Windows Debugging"]
ms.date: 05/23/2017
topic_type:
- apiref
ms.topic: reference
api_name:
- envvar
api_type:
- NA
---

# !envvar


The **!envvar** extension displays the value of the specified environment variable.

```dbgcmd
!envvar Variable
```

## Parameters


<span id="_______Variable______"></span><span id="_______variable______"></span><span id="_______VARIABLE______"></span> *Variable*   
Specifies the environment variable whose value is displayed. *Variable* is not case sensitive.

## DLL

Exts.dll

 

## Additional Information

For more information about environment variables, see [Environment Variables](../debugger/environment-variables.md) and the Microsoft Windows SDK documentation.

## Remarks

The **!envvar** extension works both in user mode and in kernel mode. However, in kernel mode, when you set the idle thread as the current process, the pointer to the Process Environment Block (PEB) is **NULL**, so it fails. In kernel mode, the **!envvar** extension displays the environment variables on the target computer, as the following example shows.

```dbgcmd
0:000> !envvar _nt_symbol_path
        _nt_symbol_path = srv*C:\mysyms*https://msdl.microsoft.com/download/symbols
```

