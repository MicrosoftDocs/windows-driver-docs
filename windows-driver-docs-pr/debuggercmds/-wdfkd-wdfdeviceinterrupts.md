---
title: "!wdfkd.wdfdeviceinterrupts"
description: "The !wdfkd.wdfdeviceinterrupts extension displays all the interrupt objects for a specified device handle."
keywords: ["!wdfkd.wdfdeviceinterrupts Windows Debugging"]
ms.date: 05/23/2017
topic_type:
- apiref
ms.topic: reference
api_name:
- wdfkd.wdfdeviceinterrupts
api_type:
- NA
---

# !wdfkd.wdfdeviceinterrupts

The **!wdfkd.wdfdeviceinterrupts** extension displays all the interrupt objects for a specified device handle.

```dbgcmd
!wdfkd.wdfdeviceinterrupts Handle
```

## Parameters

<span id="_______Handle______"></span><span id="_______handle______"></span><span id="_______HANDLE______"></span> *Handle*   
A handle to a WDFDEVICE-typed object.

## DLL

Wdfkd.dll

## Frameworks

KMDF 1, UMDF 2

## Additional Information

For more information, see [Kernel-Mode Driver Framework Debugging](../debugger/kernel-mode-driver-framework-debugging.md).
