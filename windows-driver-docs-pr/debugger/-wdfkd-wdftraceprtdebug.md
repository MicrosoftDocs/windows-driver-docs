---
title: wdfkd.wdftraceprtdebug
description: The wdfkd.wdftraceprtdebug extension enables and disables the Traceprt.dll diagnostic mode, which generates verbose debugging information.
ms.assetid: e12e0ff1-fc27-4d95-b48a-73cab8f1e363
keywords: ["wdfkd.wdftraceprtdebug Windows Debugging"]
ms.author: domars
ms.date: 05/23/2017
topic_type:
- apiref
api_name:
- wdfkd.wdftraceprtdebug
api_type:
- NA
ms.localizationpriority: medium
---

# !wdfkd.wdftraceprtdebug


The **!wdfkd.wdftraceprtdebug** extension enables and disables the Traceprt.dll diagnostic mode, which generates verbose debugging information.

```dbgcmd
!wdfkd.wdftraceprtdebug {on | off}
```

## <span id="Parameters"></span><span id="parameters"></span><span id="PARAMETERS"></span>Parameters


<span id="_______on______"></span><span id="_______ON______"></span> **on**   
Enables the Traceprt.dll diagnostic mode.

<span id="_______off______"></span><span id="_______OFF______"></span> **off**   
Disables the Traceprt.dll diagnostic mode.

### <span id="DLL"></span><span id="dll"></span>DLL

Wdfkd.dll

### <span id="Frameworks"></span><span id="frameworks"></span><span id="FRAMEWORKS"></span>Frameworks

KMDF 1, UMDF 2

### <span id="Additional_Information"></span><span id="additional_information"></span><span id="ADDITIONAL_INFORMATION"></span>Additional Information

For more information, see [Kernel-Mode Driver Framework Debugging](kernel-mode-driver-framework-debugging.md).

Remarks
-------

You should use the !wdfkd.wdftraceprtdebug extension only at the direction of technical support.

 

 





