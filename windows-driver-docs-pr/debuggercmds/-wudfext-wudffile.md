---
title: "!wudfext.wudffile"
description: "The !wudfext.wudffile extension displays information about a framework file."
keywords: ["!wudfext.wudffile Windows Debugging"]
ms.date: 05/23/2017
topic_type:
- apiref
ms.topic: reference
api_name:
- wudfext.wudffile
api_type:
- NA
---

# !wudfext.wudffile

The **!wudfext.wudffile** extension displays information about a framework file.

```dbgcmd
!wudfext.wudffile pWDFFile [TypeName] 
```

## Parameters

<span id="_______pWDFFile______"></span><span id="_______pwdffile______"></span><span id="_______PWDFFILE______"></span> *pWDFFile*   
Specifies the address of the **IWDFFile** interface to display information about.

<span id="_______TypeName______"></span><span id="_______typename______"></span><span id="_______TYPENAME______"></span> *TypeName*   
Optional. Specifies the type of the interface (for example, **IWDFDevice**). If a value for *TypeName* is supplied, the extension uses the value as the type of the interface. If an asterisk (\*) is supplied as *TypeName*, or if *TypeName* is omitted, the extension attempts to automatically determine the type of the supplied interface.

## DLL

Wudfext.dll

## Additional Information

For more information, see [User-Mode Driver Framework Debugging](../debugger/user-mode-driver-framework-debugging.md).
