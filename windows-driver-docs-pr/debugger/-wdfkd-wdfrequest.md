---
title: wdfkd.wdfrequest
description: The wdfkd.wdfrequest extension displays information about a specified framework request object and the WDM I/O request packet (IRP) that is associated with the request object.
ms.assetid: 8b99ec30-ac2b-421d-8b20-bfbd09d41dfb
keywords: ["wdfkd.wdfrequest Windows Debugging"]
ms.author: domars
ms.date: 05/23/2017
topic_type:
- apiref
api_name:
- wdfkd.wdfrequest
api_type:
- NA
ms.localizationpriority: medium
---

# !wdfkd.wdfrequest


The **!wdfkd.wdfrequest** extension displays information about a specified framework request object and the WDM I/O request packet (IRP) that is associated with the request object.

```dbgcmd
!wdfkd.wdfrequest Handle
```

## <span id="Parameters"></span><span id="parameters"></span><span id="PARAMETERS"></span>Parameters


<span id="_______Handle______"></span><span id="_______handle______"></span><span id="_______HANDLE______"></span> *Handle*   
A handle to a framework request object.

### <span id="DLL"></span><span id="dll"></span>DLL

Wdfkd.dll

### <span id="Frameworks"></span><span id="frameworks"></span><span id="FRAMEWORKS"></span>Frameworks

KMDF 1, UMDF 2

### <span id="Additional_Information"></span><span id="additional_information"></span><span id="ADDITIONAL_INFORMATION"></span>Additional Information

For more information, see [Kernel-Mode Driver Framework Debugging](kernel-mode-driver-framework-debugging.md).

 

 





