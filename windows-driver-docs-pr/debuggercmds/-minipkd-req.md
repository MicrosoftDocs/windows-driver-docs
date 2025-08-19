---
title: "!minipkd.req"
description: "The !minipkd.req extension displays information about all of the currently active requests on the specified adapter or device."
keywords: ["minipkd.req Windows Debugging"]
ms.date: 05/23/2017
topic_type:
- apiref
ms.topic: reference
api_name:
- minipkd.req
api_type:
- NA
---

# !minipkd.req


The **!minipkd.req** extension displays information about all of the currently active requests on the specified adapter or device.

```dbgcmd
!minipkd.req Adapter 
!minipkd.req Device 
```

## Parameters


<span id="_______Adapter______"></span><span id="_______adapter______"></span><span id="_______ADAPTER______"></span> *Adapter*   
Specifies the address of the adapter.

<span id="_______Device______"></span><span id="_______device______"></span><span id="_______DEVICE______"></span> *Device*   
Specifies the physical device object (PDO) for the Logical Unit Extension (LUN) device.

## DLL

Minipkd.dll

 

## Additional Information

For more information, see [SCSI Miniport Debugging](../debugger/scsi-miniport-debugging.md).

## Remarks

The PDO for a LUN can be found in the **DevObj** field of the [**!minipkd.adapters**](-minipkd-adapters.md) display.

