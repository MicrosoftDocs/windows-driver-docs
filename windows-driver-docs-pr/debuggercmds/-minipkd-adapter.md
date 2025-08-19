---
title: "!minipkd.adapter"
description: "The !minipkd.adapter extension displays information about the specified adapter."
keywords: ["!minipkd.adapter Windows Debugging"]
ms.date: 05/23/2017
topic_type:
- apiref
ms.topic: reference
api_name:
- minipkd.adapter
api_type:
- NA
---

# !minipkd.adapter


The **!minipkd.adapter** extension displays information about the specified adapter.

```dbgcmd
!minipkd.adapter Address 
```

## Parameters


<span id="_______Address______"></span><span id="_______address______"></span><span id="_______ADDRESS______"></span> *Address*   
Specifies the address of an adapter.

## DLL

Minipkd.dll

 

## Additional Information

For more information, see [SCSI Miniport Debugging](../debugger/scsi-miniport-debugging.md).

## Remarks

The address of an adapter can be found in the **DevExt** field of the [**!minipkd.adapters**](-minipkd-adapters.md) display.

