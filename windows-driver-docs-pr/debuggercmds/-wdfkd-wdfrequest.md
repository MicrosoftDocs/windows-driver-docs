---
title: "!wdfkd.wdfrequest"
description: "The !wdfkd.wdfrequest extension displays information about a specified framework request object and the WDM I/O request packet (IRP) that is associated with the request object."
keywords: ["!wdfkd.wdfrequest Windows Debugging"]
ms.date: 05/23/2017
topic_type:
- apiref
ms.topic: reference
api_name:
- wdfkd.wdfrequest
api_type:
- NA
---

# !wdfkd.wdfrequest

The **!wdfkd.wdfrequest** extension displays information about a specified framework request object and the WDM I/O request packet (IRP) that is associated with the request object.

```dbgcmd
!wdfkd.wdfrequest Handle
```

## Parameters

<span id="_______Handle______"></span><span id="_______handle______"></span><span id="_______HANDLE______"></span> *Handle*   
A handle to a framework request object.

## DLL

Wdfkd.dll

### Frameworks

KMDF 1, UMDF 2

## Additional Information

For more information, see [Kernel-Mode Driver Framework Debugging](../debugger/kernel-mode-driver-framework-debugging.md).
