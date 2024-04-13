---
title: "!wdfkd.wdftagtracker"
description: "The !wdfkd.wdftagtracker extension displays all available tag information (including tag value, line, file, and time) for a specified tag tracker."
keywords: ["!wdfkd.wdftagtracker Windows Debugging"]
ms.date: 05/23/2017
topic_type:
- apiref
ms.topic: reference
api_name:
- wdfkd.wdftagtracker
api_type:
- NA
---

# !wdfkd.wdftagtracker

The **!wdfkd.wdftagtracker** extension displays all available tag information (including tag value, line, file, and time) for a specified tag tracker.

```dbgcmd
!wdfkd.wdftagtracker TagObjectPointer [Flags]
```

## Parameters

<span id="_______TagObjectPointer______"></span><span id="_______tagobjectpointer______"></span><span id="_______TAGOBJECTPOINTER______"></span> *TagObjectPointer*   
A pointer to a tag tracker.

<span id="_______Flags______"></span><span id="_______flags______"></span><span id="_______FLAGS______"></span> *Flags*   
Optional. The kind of information to display. *Flags* can be any combination of the following bits. The default value is 0x0.

<span id="Bit_0__0x1_"></span><span id="bit_0__0x1_"></span><span id="BIT_0__0X1_"></span>Bit 0 (0x1)  
Displays the history of acquire operations and release operations on the object.

<span id="Bit_1__0x2_"></span><span id="bit_1__0x2_"></span><span id="BIT_1__0X2_"></span>Bit 1 (0x2)  
Displays the line number of the object in hexadecimal instead of decimal.

## DLL

Wdfkd.dll

### Frameworks

KMDF 1, UMDF 2

## Additional Information

For more information, see [Kernel-Mode Driver Framework Debugging](../debugger/kernel-mode-driver-framework-debugging.md).

## Remarks

To retrieve a pointer to a tag tracker, use the [**!wdfkd.wdfobject**](-wdfkd-wdfobject.md) extension on an internal framework object pointer.

To use tag tracking, you must enable both the Kernel-Mode Driver Framework (KMDF) verifier and handle tracking in the registry. Both of these settings are stored in the driver's **Parameters\\Wdf** subkey of the **HKEY\_LOCAL\_MACHINE\\System\\CurrentControlSet\\Services** key.

To enable the KMDF verifier, set a nonzero value for **VerifierOn**.

To enable handle tracking, set the value of **TrackHandles** to the name of one or more object types, or specify an asterisk (\*) to track all object types. For example, the following example specifies the tracking of references to all WDFDEVICE and WDFQUEUE objects.

```text
TrackHandles: MULTI_SZ: WDFDEVICE WDFQUEUE
```

When you enable handle tracking for an object type, the framework tracks the references that are taken on any object of that type. This setting is useful in finding driver memory leaks that unreleased references cause. **TrackHandles** works only if the KMDF verifier is enabled.
