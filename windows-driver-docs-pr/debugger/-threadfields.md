---
title: threadfields
description: The threadfields extension displays the names and offsets of the fields within the executive thread (ETHREAD) block.
ms.assetid: 1b36e922-9079-4dc5-911a-f635ec026084
keywords: ["threadfields Windows Debugging"]
ms.author: domars
ms.date: 05/23/2017
topic_type:
- apiref
api_name:
- threadfields
api_type:
- NA
ms.localizationpriority: medium
---

# !threadfields


The **!threadfields** extension displays the names and offsets of the fields within the executive thread (ETHREAD) block.

```dbgcmd
!threadfields
```

## <span id="ddk__threadfields_dbg"></span><span id="DDK__THREADFIELDS_DBG"></span>


### <span id="DLL"></span><span id="dll"></span>DLL

<table>
<colgroup>
<col width="50%" />
<col width="50%" />
</colgroup>
<tbody>
<tr class="odd">
<td align="left"><p><strong>Windows 2000</strong></p></td>
<td align="left"><p>Kdextx86.dll</p></td>
</tr>
<tr class="even">
<td align="left"><p><strong>Windows XP and later</strong></p></td>
<td align="left"><p>Unavailable (see the Remarks section)</p></td>
</tr>
</tbody>
</table>

 

### <span id="Additional_Information"></span><span id="additional_information"></span><span id="ADDITIONAL_INFORMATION"></span>Additional Information

For information about the ETHREAD block, see *Microsoft Windows Internals*, by Mark Russinovich and David Solomon. (This book may not be available in some languages and countries.)

Remarks
-------

This extension command is not available in Windows XP or later versions of Windows. Instead, use the [**dt (Display Type)**](dt--display-type-.md) command to show the ETHREAD structure directly:

```dbgcmd
kd> dt nt!_ETHREAD 
```

Here is an example of **!threadfields** from a Windows 2000 system:

```dbgcmd
kd> !threadfields
 ETHREAD structure offsets:

    Tcb:                           0x0
    CreateTime:                    0x1b0
    ExitTime:                      0x1b8
    ExitStatus:                    0x1c0
    PostBlockList:                 0x1c4
    TerminationPortList:           0x1cc
    ActiveTimerListLock:           0x1d4
    ActiveTimerListHead:           0x1d8
    Cid:                           0x1e0
    LpcReplySemaphore:             0x1e8
    LpcReplyMessage:               0x1fc
    LpcReplyMessageId:             0x200
    ImpersonationInfo:             0x208
    IrpList:                       0x20c
    TopLevelIrp:                   0x214
    ReadClusterSize:               0x21c
    ForwardClusterOnly:            0x220
    DisablePageFaultClustering:    0x221
    DeadThread:                    0x222
    HasTerminated:                 0x224
    GrantedAccess:                 0x228
    ThreadsProcess:                0x22c
    StartAddress:                  0x230
    Win32StartAddress:             0x234
    LpcExitThreadCalled:           0x238
    HardErrorsAreDisabled:         0x239
```

 

 





