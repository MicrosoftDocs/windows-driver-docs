---
title: "!wudfext.wudfusbpipe"
description: "The !wudfext.wudfusbpipe extension displays information about a USB pipe object."
keywords: ["!wudfext.wudfusbpipe Windows Debugging"]
ms.date: 05/23/2017
topic_type:
- apiref
ms.topic: reference
api_name:
- wudfext.wudfusbpipe
api_type:
- NA
---

# !wudfext.wudfusbpipe

The **!wudfext.wudfusbpipe** extension displays information about a USB pipe object.

```dbgcmd
!wudfext.wudfusbpipe pWDFUSBPipe TypeName
```

## Parameters

<span id="_______pWDFUSBPipe______"></span><span id="_______pwdfusbpipe______"></span><span id="_______PWDFUSBPIPE______"></span> *pWDFUSBPipe*   
Specifies the address of the **IWDFUsbTargetPipe** interface to display information about. The [**!wudfext.wudfobject**](-wudfext-wudfobject.md) extension command determines the address of **IWDFUsbTargetPipe**.

<span id="_______TypeName______"></span><span id="_______typename______"></span><span id="_______TYPENAME______"></span> *TypeName*   
Optional. Specifies the type of the interface (for example, **IWDFDevice**). If a value for *TypeName* is supplied, the extension uses the value as the type of the interface. If an asterisk (\*) is supplied as *TypeName*, or if *TypeName* is omitted, the extension attempts to automatically determine the type of the supplied interface.

## DLL

Wudfext.dll

## Additional Information

For more information, see [User-Mode Driver Framework Debugging](../debugger/user-mode-driver-framework-debugging.md).
