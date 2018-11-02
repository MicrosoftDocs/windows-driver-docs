---
title: wdfkd.wdfqueue
description: The wdfkd.wdfqueue extension displays information about a specified framework queue object and the framework request objects that are in the queue.
ms.assetid: 100917dc-9ce9-48d6-a285-58ea78a4c2f4
keywords: ["wdfkd.wdfqueue Windows Debugging"]
ms.author: domars
ms.date: 05/23/2017
topic_type:
- apiref
api_name:
- wdfkd.wdfqueue
api_type:
- NA
ms.localizationpriority: medium
---

# !wdfkd.wdfqueue


The **!wdfkd.wdfqueue** extension displays information about a specified framework queue object and the framework request objects that are in the queue.

```dbgcmd
!wdfkd.wdfqueue Handle
```

## <span id="Parameters"></span><span id="parameters"></span><span id="PARAMETERS"></span>Parameters


<span id="_______Handle______"></span><span id="_______handle______"></span><span id="_______HANDLE______"></span> *Handle*   
A handle to a framework queue object.

### <span id="DLL"></span><span id="dll"></span>DLL

Wdfkd.dll

### <span id="Frameworks"></span><span id="frameworks"></span><span id="FRAMEWORKS"></span>Frameworks

KMDF 1, UMDF 2

### <span id="Additional_Information"></span><span id="additional_information"></span><span id="ADDITIONAL_INFORMATION"></span>Additional Information

For more information, see [Kernel-Mode Driver Framework Debugging](kernel-mode-driver-framework-debugging.md).

Remarks
-------

The following example shows the display from a **!wdfkd.wdfqueue** extension.

```dbgcmd
kd> !wdfqueue 0x7ce7d1e8 

# Dumping WDFQUEUE 0x7ce7d1e8
=========================
Parallel, Power-managed, PowerOff, Can accept, Can dispatch, ExecutionLevelDispatch, SynchronizationScopeNone
    Number of driver owned requests: 0
    Number of waiting requests: 0


    EvtIoDefault: (0xf221fad0) wdfrawbusenumtest!EvtIoQueueDefault
```

The queue in the preceding example is configured for parallel dispatching, is power-managed but is currently in the Off state, and can both accept and dispatch requests.

 

 





