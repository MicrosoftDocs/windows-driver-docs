---
title: "!wdfkd.wdfopenhandles"
description: "The !wdfkd.wdfopenhandles extension displays information about all the handles that are open on the specified WDF device."
keywords: ["!wdfkd.wdfopenhandles Windows Debugging"]
ms.date: 05/23/2017
topic_type:
- apiref
ms.topic: reference
api_name:
- wdfkd.wdfopenhandles
api_type:
- NA
---

# !wdfkd.wdfopenhandles

The **!wdfkd.wdfopenhandles** extension displays information about all the handles that are open on the specified WDF device.

```dbgcmd
!wdfkd.wdfopenhandles Handle [Flags]
```

## Parameters

<span id="_______Handle______"></span><span id="_______handle______"></span><span id="_______HANDLE______"></span> *Handle*   
A handle to a framework device object (WDFDEVICE).

<span id="_______Flags______"></span><span id="_______flags______"></span><span id="_______FLAGS______"></span> *Flags*   
Optional. Specifies the kind of information to display. *Flags* can be any combination of the following bits. The default value is 0x0.

<span id="Bit_0__0x1_"></span><span id="bit_0__0x1_"></span><span id="BIT_0__0X1_"></span>Bit 0 (0x1)  
Displays file object context information.

## DLL

Wdfkd.dll

### Frameworks

KMDF 1, UMDF 2

## Additional Information

For more information, see [Kernel-Mode Driver Framework Debugging](../debugger/kernel-mode-driver-framework-debugging.md).

