---
title: "!minipkd.lun"
description: "The !minipkd.lun extension displays detailed information about the specified Logical Unit Extension (LUN)."
keywords: ["minipkd.lun Windows Debugging"]
ms.date: 05/23/2017
topic_type:
- apiref
ms.topic: reference
api_name:
- minipkd.lun
api_type:
- NA
---

# !minipkd.lun


The **!minipkd.lun** extension displays detailed information about the specified Logical Unit Extension (LUN).

```dbgcmd
!minipkd.lun LUN 
!minipkd.lun Device 
```

## Parameters


<span id="_______LUN______"></span><span id="_______lun______"></span> *LUN*   
Specifies the address of the LUN.

<span id="_______Device______"></span><span id="_______device______"></span><span id="_______DEVICE______"></span> *Device*   
Specifies the physical device object (PDO) for the LUN.

## DLL

Minipkd.dll

 

## Additional Information

For more information, see [SCSI Miniport Debugging](../debugger/scsi-miniport-debugging.md).

## Remarks

A LUN is typically referred to as a *device*. Thus, this extension displays information about a device on an adapter.

The LUN can be specified either by its address (which can be found in the **LUN** field of the [**!minipkd.adapters**](-minipkd-adapters.md) display), or by its physical device object (which can be found in the **DevObj** field of the **!minipkd.adapters** display).

