---
title: "!blockeddrv"
description: "The !blockeddrv extension displays the list of blocked drivers on the target computer."
keywords: ["blocked drivers", "!blockeddrv Windows Debugging"]
ms.date: 05/23/2017
topic_type:
- apiref
ms.topic: reference
api_name:
- blockeddrv
api_type:
- NA
---

# !blockeddrv


The **!blockeddrv** extension displays the list of blocked drivers on the target computer.

```dbgcmd
    !blockeddrv
```

## <span id="ddk__blockeddrv_dbg"></span><span id="DDK__BLOCKEDDRV_DBG"></span>


## DLL

Kdexts.dll

 

## Remarks

Here is an example:

```dbgcmd
kd> !blockeddrv
Driver:      Status    GUID
afd.sys      0:        {00000008-0206-0001-0000-000030C964E1}
agp440.sys   0:        {0000005C-175A-E12D-5000-010020885580}
atapi.sys    0:        {0000005C-B04A-E12E-5600-000020885580}
audstub.sys  0:        {0000005C-B04A-E12E-5600-000020885580}
Beep.SYS     0:        {0000005C-B04A-E12E-5600-000020885580}
Cdfs.SYS     0:        {00000008-0206-0001-0000-000008F036E1}
.....
```

