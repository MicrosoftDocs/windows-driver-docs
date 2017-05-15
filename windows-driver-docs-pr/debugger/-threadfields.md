---
title: threadfields
description: The threadfields extension displays the names and offsets of the fields within the executive thread (ETHREAD) block.
ms.assetid: 1b36e922-9079-4dc5-911a-f635ec026084
keywords: ["threadfields Windows Debugging"]
topic_type:
- apiref
api_name:
- threadfields
api_type:
- NA
---

# !threadfields


The **!threadfields** extension displays the names and offsets of the fields within the executive thread (ETHREAD) block.

``` syntax
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

``` syntax
kd> dt nt!_ETHREAD 
```

Here is an example of **!threadfields** from a Windows 2000 system:

``` syntax
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

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20[debugger\debugger]:%20!threadfields%20%20RELEASE:%20%285/15/2017%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")




