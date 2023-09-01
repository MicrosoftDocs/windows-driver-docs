---
title: isainfo (WinDbg)
description: The isainfo extension displays information about PNPISA cards or devices present in the system..
keywords: ["I/O Bus", "CARD_INFORMATION", "isainfo Windows Debugging"]
ms.date: 08/29/2023
topic_type:
- apiref
ms.topic: reference
api_name:
- isainfo
api_type:
- NA
---

# !isainfo

The **!isainfo** extension displays information about PNPISA cards or devices present in the system..

```dbgcmd
!isainfo [Card]
```

## Parameters

*Card*

Specifies a PNPISA Card. If *Card* is 0 or omitted, all the devices and cards on the PNPISA (that is, the PC I/O) Bus are displayed.

### DLL

Kdexts.dll

## Remarks

Here is an example of the output from this extension:

```dbgcmd
0: kd> !isainfo
ISA PnP FDO @ 0x867b9938, DevExt @ 0x867b99f0, Bus # 0
Flags (0x80000000)  DF_BUS

  ISA PnP PDO @ 0x867B9818, DevExt @ 0x86595388
  Flags (0x40000818)  DF_ENUMERATED, DF_ACTIVATED, 
                      DF_REQ_TRIMMED, DF_READ_DATA_PORT
```
