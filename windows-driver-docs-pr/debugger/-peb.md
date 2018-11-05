---
title: peb
description: The peb extension displays a formatted view of the information in the process environment block (PEB).
ms.assetid: 01687f13-9eb7-48f0-a0d6-54fee00084ab
keywords: ["PEB (process environment block)", "process, process environment block (PEB)", "peb Windows Debugging"]
ms.author: domars
ms.date: 05/23/2017
topic_type:
- apiref
api_name:
- peb
api_type:
- NA
ms.localizationpriority: medium
---

# !peb


The **!peb** extension displays a formatted view of the information in the process environment block (PEB).

```dbgcmd
!peb [PEB-Address]
```

## <span id="ddk__peb_dbg"></span><span id="DDK__PEB_DBG"></span>Parameters


<span id="_______PEB-Address______"></span><span id="_______peb-address______"></span><span id="_______PEB-ADDRESS______"></span> *PEB-Address*   
The hexadecimal address of the process whose PEB you want to examine. (This is not the address of the PEB as derived from the kernel process block for the process.) If *PEB-Address* is omitted in user mode, the PEB for the current process is used. If it is omitted in kernel mode, the PEB corresponding to the current [process context](changing-contexts.md#process-context) is displayed.

### <span id="DLL"></span><span id="dll"></span>DLL

<table>
<colgroup>
<col width="50%" />
<col width="50%" />
</colgroup>
<tbody>
<tr class="odd">
<td align="left"><p><strong>Windows 2000</strong></p></td>
<td align="left"><p></p>
Kdextx86.dll
Ntsdexts.dll</td>
</tr>
<tr class="even">
<td align="left"><p><strong>Windows XP and later</strong></p></td>
<td align="left"><p>Exts.dll</p></td>
</tr>
</tbody>
</table>

 

### <span id="Additional_Information"></span><span id="additional_information"></span><span id="ADDITIONAL_INFORMATION"></span>Additional Information

For information about process environment blocks, see *Microsoft Windows Internals* by Mark Russinovich and David Solomon. (This book may not be available in some languages and countries.)

Remarks
-------

The PEB is the user-mode portion of Microsoft Windows process control structures.

If the **!peb** extension with no argument gives you an error in kernel mode, you should use the [**!process**](-process.md) extension to determine the PEB address for the desired process. Make sure your [process context](changing-contexts.md#process-context) is set to the desired process, and then use the PEB address as the argument for **!peb**.

The exact output displayed depends on the Windows version and on whether you are debugging in kernel mode or user mode. The following example is taken from a kernel debugger attached to a Windows Server 2003 target:

```dbgcmd
kd> !peb
PEB at 7ffdf000
    InheritedAddressSpace:    No
    ReadImageFileExecOptions: No
    BeingDebugged:            No
    ImageBaseAddress:         4ad00000
    Ldr                       77fbe900
    Ldr.Initialized:          Yes
    Ldr.InInitializationOrderModuleList: 00241ef8 . 00242360
    Ldr.InLoadOrderModuleList:           00241e90 . 00242350
    Ldr.InMemoryOrderModuleList:         00241e98 . 00242358
            Base TimeStamp                     Module
        4ad00000 3d34633c Jul 16 11:17:32 2002 D:\WINDOWS\system32\cmd.exe
        77f40000 3d346214 Jul 16 11:12:36 2002 D:\WINDOWS\system32\ntdll.dll
        77e50000 3d3484ef Jul 16 13:41:19 2002 D:\WINDOWS\system32\kernel32.dll
....
    SubSystemData:     00000000
    ProcessHeap:       00140000
    ProcessParameters: 00020000
    WindowTitle:  'D:\Documents and Settings\Administrator\Desktop\Debuggers.lnk'
    ImageFile:    'D:\WINDOWS\system32\cmd.exe'
    CommandLine:  '"D:\WINDOWS\system32\cmd.exe" '
    DllPath:      'D:\WINDOWS\system32;D:\WINDOWS\system32;....
    Environment:  00010000
        ALLUSERSPROFILE=D:\Documents and Settings\All Users
        APPDATA=D:\Documents and Settings\UserTwo\Application Data
        CLIENTNAME=Console
....
        windir=D:\WINDOWS
```

The similar [**!teb**](-teb.md) extension displays the thread environment block.

 

 





