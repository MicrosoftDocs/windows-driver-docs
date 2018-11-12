---
title: teb
description: The teb extension displays a formatted view of the information in the thread environment block (TEB).
ms.assetid: 4137b54b-f784-412d-bffd-e8a71a54155e
keywords: ["teb Windows Debugging"]
ms.author: domars
ms.date: 05/23/2017
topic_type:
- apiref
api_name:
- teb
api_type:
- NA
ms.localizationpriority: medium
---

# !teb


The **!teb** extension displays a formatted view of the information in the thread environment block (TEB).

```dbgcmd
!teb [TEB-Address] 
```

## <span id="ddk__teb_dbg"></span><span id="DDK__TEB_DBG"></span>Parameters


<span id="_______TEB-Address______"></span><span id="_______teb-address______"></span><span id="_______TEB-ADDRESS______"></span> *TEB-Address*   
The hexadecimal address of the thread whose TEB you want to examine. (This is not the address of the TEB as derived from the kernel thread block for the thread.) If *TEB-Address* is omitted in user mode, the TEB for the current thread is used. If it is omitted in kernel mode, the TEB corresponding to the current [register context](changing-contexts.md#register-context) is displayed.

### <span id="DLL"></span><span id="dll"></span>DLL

Exts.dll

### <span id="Additional_Information"></span><span id="additional_information"></span><span id="ADDITIONAL_INFORMATION"></span>Additional Information

For information about thread environment blocks, see *Microsoft Windows Internals* by Mark Russinovich and David Solomon.

Remarks
-------

The TEB is the user-mode portion of Microsoft Windows thread control structures.

If the **!teb** extension with no argument gives you an error in kernel mode, you should use the [**!process**](-process.md) extension to determine the TEB address for the desired thread. Make sure your [register context](changing-contexts.md#register-context) is set to the desired thread, and then use the TEB address as the argument for **!teb**.

Here is an example of this command's output in user mode:

```dbgcmd
0:001> ~
   0  id: 324.458   Suspend: 1 Teb 7ffde000 Unfrozen
.  1  id: 324.48c   Suspend: 1 Teb 7ffdd000 Unfrozen

0:001> !teb 
TEB at 7FFDD000
    ExceptionList:    76ffdc
    Stack Base:       770000
    Stack Limit:      76f000
    SubSystemTib:     0
 FiberData:        1e00
    ArbitraryUser:    0
    Self:             7ffdd000
    EnvironmentPtr:   0
 ClientId:         324.48c
    Real ClientId:    324.48c
    RpcHandle:        0
    Tls Storage:      0
    PEB Address:      7ffdf000
    LastErrorValue:   0
    LastStatusValue:  0
    Count Owned Locks:0
    HardErrorsMode:   0
```

The similar [**!peb**](-peb.md) extension displays the process environment block.

 

 





