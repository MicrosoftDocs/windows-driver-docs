---
title: "!minipkd.srb"
description: "The !minipkd.srb extension displays the specified SCSI request block (SRB) data structure."
keywords: ["minipkd.srb Windows Debugging"]
ms.date: 05/23/2017
topic_type:
- apiref
ms.topic: reference
api_name:
- minipkd.srb
api_type:
- NA
---

# !minipkd.srb


The **!minipkd.srb** extension displays the specified SCSI request block (SRB) data structure.

```dbgcmd
!minipkd.srb SRB 
```

## Parameters


<span id="_______SRB______"></span><span id="_______srb______"></span> *SRB*   
Specifies the address of an SRB.

## DLL

Minipkd.dll

 

## Additional Information

For more information, see [SCSI Miniport Debugging](../debugger/scsi-miniport-debugging.md).

## Remarks

The addresses of all currently active requests can be found in the *SRB* fields of the output from the [**!minipkd.req**](-minipkd-req.md) command.

This extension displays the status of the SRB, the driver it is addressed to, the SCSI that issued the SRB and its address, and a hexadecimal flag value. If 0x10000 is set in the flag value, this request is currently in the miniport.

