---
title: wdfkd.wdfdevicequeues
description: The wdfkd.wdfdevicequeues extension displays information about all of the framework queue objects that belong to a specified device.
ms.assetid: bd0e7fcc-b561-48fb-901a-605e9d647b61
keywords: ["wdfkd.wdfdevicequeues Windows Debugging"]
ms.author: domars
ms.date: 05/23/2017
topic_type:
- apiref
api_name:
- wdfkd.wdfdevicequeues
api_type:
- NA
ms.localizationpriority: medium
---

# !wdfkd.wdfdevicequeues


The **!wdfkd.wdfdevicequeues** extension displays information about all of the framework queue objects that belong to a specified device.

```dbgcmd
!wdfkd.wdfdevicequeues Handle
```

## <span id="Parameters"></span><span id="parameters"></span><span id="PARAMETERS"></span>Parameters


<span id="_______Handle______"></span><span id="_______handle______"></span><span id="_______HANDLE______"></span> *Handle*   
A handle to a WDFDEVICE-typed object.

### <span id="DLL"></span><span id="dll"></span>DLL

Wdfkd.dll

### <span id="Frameworks"></span><span id="frameworks"></span><span id="FRAMEWORKS"></span>Frameworks

KMDF 1, UMDF 2

### <span id="Additional_Information"></span><span id="additional_information"></span><span id="ADDITIONAL_INFORMATION"></span>Additional Information

For more information, see [Kernel-Mode Driver Framework Debugging](kernel-mode-driver-framework-debugging.md) and [**!wdfkd.wdfqueue**](-wdfkd-wdfqueue.md).

Remarks
-------

The following example shows the display from the **!wdfkd.wdfdevicequeues** extension.

```dbgcmd
kd> !wdfdevicequeues 0x7cad31c8 

# Dumping queues of WDFDEVICE 0x7cad31c8
=====================================
## Number of queues: 3
----------------------------------
Queue: 1 (!wdfqueue 0x7d67d1e8)
    Manual, Not power-managed, PowerOn, Can accept, Can dispatch, ExecutionLevelDispatch, SynchronizationScopeNone
    Number of driver owned requests: 0
    Number of waiting requests: 0


## This is WDF internal queue for create requests.
----------------------------------
Queue: 2 (!wdfqueue 0x7ce7d1e8)
    Parallel, Power-managed, PowerOff, Can accept, Can dispatch, ExecutionLevelDispatch, SynchronizationScopeNone
    Number of driver owned requests: 0
    Number of waiting requests: 0


##     EvtIoDefault: (0xf221fad0) wdfrawbusenumtest!EvtIoQueueDefault
----------------------------------
Queue: 3 (!wdfqueue 0x7cd671e8)
    Parallel, Power-managed, PowerOff, Can accept, Can dispatch, ExecutionLevelDispatch, SynchronizationScopeNone
    Number of driver owned requests: 0
    Number of waiting requests: 0


    EvtIoDeviceControl: (0xf2226ac0) wdfrawbusenumtest!RawBus_RawPdo_EvtDeviceControl
```

 

 





