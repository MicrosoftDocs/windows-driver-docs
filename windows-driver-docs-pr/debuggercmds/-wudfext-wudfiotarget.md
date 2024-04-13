---
title: "!wudfext.wudfiotarget"
description: "The !wudfext.wudfiotarget extension displays information about an I/O target including the target's state and list of sent requests."
keywords: ["!wudfext.wudfiotarget Windows Debugging"]
ms.date: 05/23/2017
topic_type:
- apiref
ms.topic: reference
api_name:
- wudfext.wudfiotarget
api_type:
- NA
---

# !wudfext.wudfiotarget

The **!wudfext.wudfiotarget** extension displays information about an I/O target including the target's state and list of sent requests.

```dbgcmd
!wudfext.wudfiotarget pWDFTarget TypeName
```

## Parameters

<span id="_______pWDFTarget______"></span><span id="_______pwdftarget______"></span><span id="_______PWDFTARGET______"></span> *pWDFTarget*   
Specifies the address of the **IWDFIoTarget** interface to display information about. The [**!wudfext.wudfobject**](-wudfext-wudfobject.md) extension command determines the address of **IWDFIoTarget**.

<span id="_______TypeName______"></span><span id="_______typename______"></span><span id="_______TYPENAME______"></span> *TypeName*   
Optional. Specifies the type of the interface (for example, **IWDFDevice**). If a value for *TypeName* is supplied, the extension uses the value as the type of the interface. If an asterisk (\*) is supplied as *TypeName*, or if *TypeName* is omitted, the extension attempts to automatically determine the type of the supplied interface.

## DLL

Wudfext.dll

## Additional Information

For more information, see [User-Mode Driver Framework Debugging](../debugger/user-mode-driver-framework-debugging.md).
