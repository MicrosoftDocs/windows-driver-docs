---
title: wdfkd.wdfspinlock
description: The wdfkd.wdfspinlock extension displays information about a framework spin-lock object. This information includes the spin lock's acquisition history and the length of time that the lock was held.
ms.assetid: 73e74703-ed9b-460b-a798-41bb56942aa3
keywords: ["wdfkd.wdfspinlock Windows Debugging"]
ms.author: domars
ms.date: 05/23/2017
topic_type:
- apiref
api_name:
- wdfkd.wdfspinlock
api_type:
- NA
ms.localizationpriority: medium
---

# !wdfkd.wdfspinlock


The **!wdfkd.wdfspinlock** extension displays information about a framework spin-lock object. This information includes the spin lock's acquisition history and the length of time that the lock was held.

```dbgcmd
!wdfkd.wdfspinlock Handle
```

## <span id="Parameters"></span><span id="parameters"></span><span id="PARAMETERS"></span>Parameters


<span id="_______Handle______"></span><span id="_______handle______"></span><span id="_______HANDLE______"></span> *Handle*   
A handle to a WDFSPINLOCK-typed object.

### <span id="DLL"></span><span id="dll"></span>DLL

Wdfkd.dll

### <span id="Frameworks"></span><span id="frameworks"></span><span id="FRAMEWORKS"></span>Frameworks

KMDF 1, UMDF 2

### <span id="Additional_Information"></span><span id="additional_information"></span><span id="ADDITIONAL_INFORMATION"></span>Additional Information

For more information, see [Kernel-Mode Driver Framework Debugging](kernel-mode-driver-framework-debugging.md).

 

 





