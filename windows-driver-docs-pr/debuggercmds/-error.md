---
title: "!error (WinDbg)"
description: "The !error extension decodes and displays information about an error value."
keywords: ["error codes", "Win32 error codes", "WinSock error codes", "!error Windows Debugging"]
ms.date: 05/23/2017
topic_type:
- apiref
ms.topic: reference
api_name:
- error
api_type:
- NA
---

# !error


The **!error** extension decodes and displays information about an error value.

```dbgcmd
!error Value [Flags]
```

## <span id="ddk__error_dbg"></span><span id="DDK__ERROR_DBG"></span>Parameters


<span id="_______Value______"></span><span id="_______value______"></span><span id="_______VALUE______"></span> *Value*   
Specifies one of the following error codes:

-   Win32

-   Winsock

-   NTSTATUS

-   NetAPI

<span id="_______Flags______"></span><span id="_______flags______"></span><span id="_______FLAGS______"></span> *Flags*   
If *Flags* is set to 1, the error code is read as an NTSTATUS code.

## DLL


Ext.dll



 

## Remarks

The following example shows you how to use **!error**.

```dbgcmd
0:000> !error 2
Error code: (Win32) 0x2 (2) - The system cannot find the file specified.
0:000> !error 2 1
Error code: (NTSTATUS) 0x2 - STATUS_WAIT_2
```

