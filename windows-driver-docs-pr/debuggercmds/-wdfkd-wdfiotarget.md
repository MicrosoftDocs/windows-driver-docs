---
title: "!wdfkd.wdfiotarget"
description: "The !wdfkd.wdfiotarget extension displays information about a specified I/O target object."
keywords: ["!wdfkd.wdfiotarget Windows Debugging"]
ms.date: 05/23/2017
topic_type:
- apiref
ms.topic: reference
api_name:
- wdfkd.wdfiotarget
api_type:
- NA
---

# !wdfkd.wdfiotarget

The **!wdfkd.wdfiotarget** extension displays information about a specified I/O target object.

```dbgcmd
!wdfkd.wdfiotarget Handle [Flags]
```

## Parameters

<span id="_______Handle______"></span><span id="_______handle______"></span><span id="_______HANDLE______"></span> *Handle*   
A handle to an I/O target object.

<span id="_______Flags______"></span><span id="_______flags______"></span><span id="_______FLAGS______"></span> *Flags*   
Optional. Flags that specify the kind of information to display. *Flags* can be any combination of the following bits. The default value is 0x0.

<span id="Bit_0__0x1_"></span><span id="bit_0__0x1_"></span><span id="BIT_0__0X1_"></span>Bit 0 (0x1)  
The display will include details for each of the I/O target's pending request objects.

## DLL

Wdfkd.dll

### Frameworks

KMDF 1, UMDF 2

## Additional Information

For more information, see [Kernel-Mode Driver Framework Debugging](../debugger/kernel-mode-driver-framework-debugging.md).

## Remarks

The following example shows a display from the **!wdfkd.wdfiotarget** extension.

```dbgcmd
kd> !wdfiotarget 0x7c9630b8 

# WDFIOTARGET 8369cf40
=========================
WDFDEVICE: 0x7ca7b1c0
Target Device:  !devobj 0x81ede5d8
Target PDO: !devobj 0x822b8a90

Type: Instack target
State:  WdfIoTargetStarted

Requests waiting: 0

Requests sent: 0

Requests sent with ignore-target-state: 0
```

The output in the preceding example includes the address of the I/O target's parent framework device object, along with the addresses of the WDM DEVICE\_OBJECT structures that represent the target driver's device object and the target device's physical device object (PDO).
