---
title: wdfkd.wdfspinlock
description: The wdfkd.wdfspinlock extension displays information about a framework spin-lock object. This information includes the spin lock's acquisition history and the length of time that the lock was held.
keywords: ["wdfkd.wdfspinlock Windows Debugging"]
ms.date: 05/23/2017
topic_type:
- apiref
ms.topic: reference
api_name:
- wdfkd.wdfspinlock
api_type:
- NA
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

### Additional Information

For more information, see [Kernel-Mode Driver Framework Debugging](kernel-mode-driver-framework-debugging.md).

 

 





