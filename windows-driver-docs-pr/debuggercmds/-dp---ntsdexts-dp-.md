---
title: "!dp ( ntsdexts.dp)"
description: "The !dp extension in Ntsdexts.dll displays a CSR process."
keywords: ["!dp ( ntsdexts.dp) Windows Debugging"]
ms.date: 05/23/2017
topic_type:
- apiref
ms.topic: reference
api_name:
- dp ( ntsdexts.dp)
api_type:
- NA
---

# !dp (!ntsdexts.dp)


The **!dp** extension in Ntsdexts.dll displays a CSR process.

This extension command should not be confused with the [**dp (Display Memory)**](d--da--db--dc--dd--dd--df--dp--dq--du--dw--dw--dyb--dyd--display-memor.md) command, or with the [**!kdext\*.dp**](-db---dc---dd---dp---dq---du---dw.md) extension command.

```dbgcmd
!dp [v] [ PID | CSR-Process ]
```

## <span id="ddk__ntsdexts_dp_dbg"></span><span id="DDK__NTSDEXTS_DP_DBG"></span>Parameters


<span id="_______v______"></span><span id="_______V______"></span> **v**   
Verbose mode. Causes the display to include structure and thread list.

<span id="_______PID______"></span><span id="_______pid______"></span> *PID*   
Specifies the process ID of the CSR process.

<span id="_______CSR-Process______"></span><span id="_______csr-process______"></span><span id="_______CSR-PROCESS______"></span> *CSR-Process*   
Specifies the hexadecimal address of the CSR process.

## DLL


Ntsdexts.dll



 

## Remarks

This extension displays the process address, process ID, sequence number, flags, and reference count. If verbose mode is selected, additional details are displayed, and thread information is shown for each process.

If no process is specified, all processes are displayed.

## See also


[**!dt**](-dt.md)


