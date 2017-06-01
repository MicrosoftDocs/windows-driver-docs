---
title: wdfkd.wdfqueue
description: The wdfkd.wdfqueue extension displays information about a specified framework queue object and the framework request objects that are in the queue.
ms.assetid: 100917dc-9ce9-48d6-a285-58ea78a4c2f4
keywords: ["wdfkd.wdfqueue Windows Debugging"]
ms.author: windowsdriverdev
ms.date: 05/23/2017
ms.topic: article
ms.prod: windows-hardware
ms.technology: windows-devices
topic_type:
- apiref
api_name:
- wdfkd.wdfqueue
api_type:
- NA
---

# !wdfkd.wdfqueue


The **!wdfkd.wdfqueue** extension displays information about a specified framework queue object and the framework request objects that are in the queue.

```
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

```
kd> !wdfqueue 0x7ce7d1e8 

# Dumping WDFQUEUE 0x7ce7d1e8
=========================
Parallel, Power-managed, PowerOff, Can accept, Can dispatch, ExecutionLevelDispatch, SynchronizationScopeNone
    Number of driver owned requests: 0
    Number of waiting requests: 0


    EvtIoDefault: (0xf221fad0) wdfrawbusenumtest!EvtIoQueueDefault
```

The queue in the preceding example is configured for parallel dispatching, is power-managed but is currently in the Off state, and can both accept and dispatch requests.

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20[debugger\debugger]:%20!wdfkd.wdfqueue%20%20RELEASE:%20%285/15/2017%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")




