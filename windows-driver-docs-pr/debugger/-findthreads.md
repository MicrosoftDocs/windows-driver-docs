---
title: findthreads
description: The findthreads extension displays summary information about one or more threads on the target system based on supplied search criteria.
ms.assetid: ED14E503-0AF2-4444-81B0-7E00A6E424E5
keywords: ["findthreads Windows Debugging"]
ms.author: domars
ms.date: 05/23/2017
topic_type:
- apiref
api_name:
- findthreads
api_type:
- NA
ms.localizationpriority: medium
---

# !findthreads


The !findthreads extension displays summary information about one or more threads on the target system based on supplied search criteria. Thread information will be displayed when the associated stack(s) reference the supplied object. This command can be used only during kernel-mode debugging.

Syntax

```dbgcmd
!findthreads [-v][-t  <Thread Address>|-i <IRP Address>|-d <Device Address>|( -a <Pointer Address> -e <End Address> | -l <Range Length>)] 
```

## <span id="ddk__thread_dbg"></span><span id="DDK__THREAD_DBG"></span>Parameters


<span id="_______-v______"></span><span id="_______-V______"></span> **-v**   
Displays verbose information on all criteria matches.

<span id="_______-t_Thread_Address______"></span><span id="_______-t_thread_address______"></span><span id="_______-T_THREAD_ADDRESS______"></span> **-t** **** *Thread Address*   
The search criteria will be all modules, wait objects, and IRPs for the thread, as well as device objects and modules generated from the attached IRPs. This option will generally provide the broadest search criteria.

<span id="_______-i_IRP_Address____________"></span><span id="_______-i_irp_address____________"></span><span id="_______-I_IRP_ADDRESS____________"></span> **-i** **** *IRP Address*   
The search criteria will be all modules and devices for the indicated IRP, as well as any reference to the IRP itself.

<span id="_______-d_Device_Address____________"></span><span id="_______-d_device_address____________"></span><span id="_______-D_DEVICE_ADDRESS____________"></span> **-d** **** *Device Address*   
The search criteria will be based from the device object. This will include the module associated with the device object (through the driver object), the device extension, any IRP attached to the device, and similar information for any attached to the device object.

<span id="_______-a_Pointer_Address____________"></span><span id="_______-a_pointer_address____________"></span><span id="_______-A_POINTER_ADDRESS____________"></span> **-a** **** *Pointer Address*   
Add a base address to the criteria. If -e or -l is correctly specified, this value will be the base of a memory range. Otherwise it is interpreted as a pointer.

<span id="_______-e_End_Address____________"></span><span id="_______-e_end_address____________"></span><span id="_______-E_END_ADDRESS____________"></span> **-e** **** *End Address*   
Specifies the end address of the memory range specified with -a.

<span id="_______-l_Range_Length______"></span><span id="_______-l_range_length______"></span><span id="_______-L_RANGE_LENGTH______"></span> **-l** **** *Range Length*   
Specifies the length of the memory range specified with -a.

### <span id="DLL"></span><span id="dll"></span>DLL

<table>
<colgroup>
<col width="50%" />
<col width="50%" />
</colgroup>
<tbody>
<tr class="odd">
<td align="left"><p><strong>Windows 10 and later</strong></p></td>
<td align="left"><p>Kdexts.dll</p></td>
</tr>
</tbody>
</table>

 

### <span id="Additional_Information"></span><span id="additional_information"></span><span id="ADDITIONAL_INFORMATION"></span>Additional Information

For information about threads in kernel mode, see [Changing Contexts](changing-contexts.md). For more information about analyzing processes and threads, see *Microsoft Windows Internals*, by Mark Russinovich and David Solomon. (This book may not be available in some languages and countries.)

Remarks
-------

Here is example output using the -v and -t options:

```dbgcmd
kd> !findthreads -v -t ffffd001ee29cdc0

Added criterion for THREAD 0xffffd001ee29cdc0
  Added criterion for THREAD STACK 0xffffd001ee2bac20
  ERROR: Object 0xffffffffffffffe0 is not an IRP
ERROR: unable to completely walk thread IRP list.
  Added criterion for MODULE kdnic(0xfffff80013120000)

Found 63 threads matching the search criteria

Found 6 criteria matches for THREAD 0xffffe0016a383740, PROCESS 0xffffe0016a220200
  Kernel stack location 0xffffd001f026a0c0 references THREAD 0xffffd001ee29cdc0
  Kernel stack location 0xffffd001f026a418 references THREAD 0xffffd001ee29cdc0
  Kernel stack location 0xffffd001f026a460 references THREAD 0xffffd001ee29cdc0
  Kernel stack location 0xffffd001f026a4d0 references THREAD 0xffffd001ee29cdc0
  Kernel stack location 0xffffd001f026a4f0 references THREAD 0xffffd001ee29cdc0
  Kernel stack location 0xffffd001f026a670 references THREAD 0xffffd001ee29cdc0


    ffffd001f026a0e0 nt!KiSwapContext+76
    ffffd001f026a190 nt!KiSwapThread+1c8
    ffffd001f026a220 nt!KiCommitThreadWait+148
    ffffd001f026a2e0 nt!KeWaitForMultipleObjects+21e
    ffffd001f026a800 nt!ObWaitForMultipleObjects+2b7
    ffffd001f026aa80 nt!NtWaitForMultipleObjects+f6
    000000c8d220fa98 nt!KiSystemServiceCopyEnd+13
    000000c8d220fa98 ntdll!ZwWaitForMultipleObjects+a
... 
```

 

 





