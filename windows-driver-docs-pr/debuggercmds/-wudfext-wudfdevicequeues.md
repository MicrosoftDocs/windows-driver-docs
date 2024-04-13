---
title: "!wudfext.wudfdevicequeues"
description: "The !wudfext.wudfdevicequeues extension displays information about all the I/O queues for a device."
keywords: ["!wudfext.wudfdevicequeues Windows Debugging"]
ms.date: 05/23/2017
topic_type:
- apiref
ms.topic: reference
api_name:
- wudfext.wudfdevicequeues
api_type:
- NA
---

# !wudfext.wudfdevicequeues

The **!wudfext.wudfdevicequeues** extension displays information about all the I/O queues for a device.

```dbgcmd
!wudfext.wudfdevicequeues pWDFDevice
```

## Parameters

<span id="_______pWDFDevice______"></span><span id="_______pwdfdevice______"></span><span id="_______PWDFDEVICE______"></span> *pWDFDevice*   
Specifies the address of the **IWDFDevice** interface for which to display information about all of its associated I/O queues. The [**!wudfext.wudfdriverinfo**](-wudfext-wudfdriverinfo.md) extension command determines the address of **IWDFDevice**.

## DLL

Wudfext.dll

## Additional Information

For more information, see [User-Mode Driver Framework Debugging](../debugger/user-mode-driver-framework-debugging.md).

## Remarks

The following is an example of the **!wudfext.wudfdevicequeues** display:

```dbgcmd
## kd> !wudfdevicequeues 0xf2f80 
--------------------------------------------------
Queue: 1 (!wudfqueue 0x000f3500)
    WdfIoQueueDispatchSequential, POWER MANAGED, WdfIoQueuePowerOn, CAN ACCEPT, CAN DISPATCH
    Number of driver owned requests: 1
      IWDFIoRequest 0x000fa7c0     CWdfIoRequest 0x000fa748
    Number of waiting requests: 199
      IWDFIoRequest 0x000fa908     CWdfIoRequest 0x000fa890
      IWDFIoRequest 0x000faa50     CWdfIoRequest 0x000fa9d8
...
      IWDFIoRequest 0x000fa678     CWdfIoRequest 0x000fa600
    Driver's callback interfaces.
      IQueueCallbackRead 0x000f343c
      IQueueCallbackDeviceIoControl 0x000f3438
      IQueueCallbackWrite 0x000f3440
```
