---
title: "!wdfkd.wdfobject"
description: "The !wdfkd.wdfobject extension displays information about a specified framework object."
keywords: ["!wdfkd.wdfobject Windows Debugging"]
ms.date: 05/23/2017
topic_type:
- apiref
ms.topic: reference
api_name:
- wdfkd.wdfobject
api_type:
- NA
---

# !wdfkd.wdfobject

The **!wdfkd.wdfobject** extension displays information about a specified framework object.

```dbgcmd
!wdfkd.wdfobject FrameworkObject
```

## Parameters


<span id="_______FrameworkObject______"></span><span id="_______frameworkobject______"></span><span id="_______FRAMEWORKOBJECT______"></span> *FrameworkObject*   
A pointer to a framework object.

## DLL

Wdfkd.dll

### Frameworks

KMDF 1, UMDF 2

## Additional Information

For more information, see [Kernel-Mode Driver Framework Debugging](../debugger/kernel-mode-driver-framework-debugging.md).

## Remarks

If the Kernel-Mode Driver Framework (KMDF) verifier is enabled for a driver and the public handle type was marked for tracking, the display from the **!wdfkd.wdfobject** extension includes the tag tracker (that is, the tracking object), as in the following example.

```dbgcmd
kd> !wdfobject 0x83584e38 

The type for object 0x83584e38 is FxDevice
State: FxObjectStateCreated (0x1)

!wdfhandle 0x7ca7b1c0

dt FxDevice 0x83584e38

    context:  dt 0x83584ff8 ROOT_CONTEXT (size is 0x1 bytes)
     <no associated attribute callbacks>

Object debug extension 83584e20
   !wdftagtracker 0x83722d80
   Verifier lock 0x831cefa8

   State history:
    [0] FxObjectStateCreated (0x1)
```

