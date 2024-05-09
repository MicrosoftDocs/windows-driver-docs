---
title: "!wudfext.wudfusbtarget"
description: "The !wudfext.wudfusbtarget extension displays information about a USB I/O target."
keywords: ["!wudfext.wudfusbtarget Windows Debugging"]
ms.date: 05/23/2017
topic_type:
- apiref
ms.topic: reference
api_name:
- wudfext.wudfusbtarget
api_type:
- NA
---

# !wudfext.wudfusbtarget

The **!wudfext.wudfusbtarget** extension displays information about a USB I/O target.

```dbgcmd
!wudfext.wudfusbtarget pWDFUSBTarget TypeName
```

## Parameters

<span id="_______pWDFUSBTarget______"></span><span id="_______pwdfusbtarget______"></span><span id="_______PWDFUSBTARGET______"></span> *pWDFUSBTarget*   
Specifies the address of the **IWDFUsbTargetDevice** interface to display information about. The [**!wudfext.wudfobject**](-wudfext-wudfobject.md) extension command determines the address of **IWDFUsbTargetDevice**.

<span id="_______TypeName______"></span><span id="_______typename______"></span><span id="_______TYPENAME______"></span> *TypeName*   
Optional. Specifies the type of the interface (for example, **IWDFDevice**). If a value for *TypeName* is supplied, the extension uses the value as the type of the interface. If an asterisk (\*) is supplied as *TypeName*, or if *TypeName* is omitted, the extension attempts to automatically determine the type of the supplied interface.

## DLL

Wudfext.dll

## Additional Information

For more information, see [User-Mode Driver Framework Debugging](../debugger/user-mode-driver-framework-debugging.md).
