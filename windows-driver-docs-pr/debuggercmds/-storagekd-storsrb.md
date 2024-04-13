---
title: "!storagekd.storsrb"
description: "The !storagekd.storsrb extension displays information about the specified Storage (or SCSI) Request Block (SRB)."
keywords: ["!storagekd.storsrb Windows Debugging"]
ms.date: 05/23/2017
topic_type:
- apiref
ms.topic: reference
api_name:
- storagekd.storsrb
api_type:
- NA
---

# !storagekd.storsrb

The **!storagekd.storsrb** extension displays information about the specified Storage (or SCSI) Request Block (SRB).

```dbgcmd
!storagekd.storsrb Address 
```

## Parameters

<span id="_______Address"></span><span id="_______address"></span><span id="_______ADDRESS"></span> *Address*  
Specifies the address of the SRB.

## DLL

Storagekd.dll

## Remarks

Here is an example of the **!storagekd.storsrb** display:

**0: kd&gt; !storagekd.storsrb ffffe00111fe25b0**

```dbgcmd
    SRB is a STORAGE request block (SRB_EX)
    SRB EX 0xffffe00111fe25b0 Function 28  Version  1, Signature 53524258, SrbStatus: 0x02[Aborted], SrbFunction 0x00 [EXECUTE SCSI]
    Address Type is BTL8

       SRB_EX Data Type [SrbExDataTypeScsiCdb16] 
    [EXECUTE SCSI] SRB_EX: 0xffffe00111fe2648  OriginalRequest: 0xffffe001125a9010  DataBuffer/Length: 0xffffe00112944000 / 0x00000200
    PTL: (0, 1, 1)  CDB: 28 00 00 00 00 00 00 00 01 00 00 00 00 00 00 00  OpCode: SCSI/READ (10)   
```
