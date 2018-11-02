---
title: handle
description: The handle extension displays information about a handle or handles that one or all processes in the target system own.
ms.assetid: ae3b7e7e-cdc1-4b83-88d7-63fe207044e3
keywords: ["handle", "handle, handle extension", "handle Windows Debugging"]
ms.author: domars
ms.date: 05/23/2017
topic_type:
- apiref
api_name:
- handle
api_type:
- NA
ms.localizationpriority: medium
---

# !handle


The **!handle** extension displays information about a handle or handles that one or all processes in the target system own.

User-Mode

```dbgcmd
!handle [Handle [UMFlags [TypeName]]] 
!handle -?
```

Kernel-Mode

```dbgcmd
    !handle [Handle [KMFlags [Process [TypeName]]]] 
```

## <span id="ddk__handle_dbg"></span><span id="DDK__HANDLE_DBG"></span>Parameters


<span id="_______Handle______"></span><span id="_______handle______"></span><span id="_______HANDLE______"></span> *Handle*   
Specifies the index of the handle to display. If *Handle* is -1 or if you omit this parameter, the debugger displays data for all handles that are associated with the current process. If *Handle* is 0, the debugger displays data for all handles.

<span id="_______UMFlags______"></span><span id="_______umflags______"></span><span id="_______UMFLAGS______"></span> *UMFlags*   
(User mode only) Specifies what the display should contain. This parameter can be a sum of any of the following bit values. (The default value is 0x1.)

<span id="Bit_0__0x1_"></span><span id="bit_0__0x1_"></span><span id="BIT_0__0X1_"></span>Bit 0 (0x1)  
Displays handle type information.

<span id="Bit_1__0x2_"></span><span id="bit_1__0x2_"></span><span id="BIT_1__0X2_"></span>Bit 1 (0x2)  
Displays basic handle information.

<span id="Bit_2__0x4_"></span><span id="bit_2__0x4_"></span><span id="BIT_2__0X4_"></span>Bit 2 (0x4)  
Displays handle name information.

<span id="Bit_3__0x8_"></span><span id="bit_3__0x8_"></span><span id="BIT_3__0X8_"></span>Bit 3 (0x8)  
Displays object-specific handle information, when available.

<span id="_______KMFlags______"></span><span id="_______kmflags______"></span><span id="_______KMFLAGS______"></span> *KMFlags*   
(Kernel mode only) Specifies what the display should contain. This parameter can be a sum of any of the following bit values. (The default value is 0x3.)

<span id="Bit_0__0x1_"></span><span id="bit_0__0x1_"></span><span id="BIT_0__0X1_"></span>Bit 0 (0x1)  
Displays basic handle information.

<span id="Bit_1__0x2_"></span><span id="bit_1__0x2_"></span><span id="BIT_1__0X2_"></span>Bit 1 (0x2)  
Displays information about objects.

<span id="Bit_2__0x4_"></span><span id="bit_2__0x4_"></span><span id="BIT_2__0X4_"></span>Bit 2 (0x4)  
Displays free handle entries. If you do not set this bit and you omit *Handle* or set it to zero, the list of handles that are displayed does not include free handles. If *Handle* specifies a single free handle, it is displayed even if you do not set this bit.

<span id="Bit_4__0x10_"></span><span id="bit_4__0x10_"></span><span id="BIT_4__0X10_"></span>Bit 4 (0x10)  
(Windows XP and later) Displays the handle from the kernel handle table instead of the current process.

<span id="Bit_5__0x20_"></span><span id="bit_5__0x20_"></span><span id="BIT_5__0X20_"></span>Bit 5 (0x20)  
(Windows XP and later) Interprets the handle as a thread ID or process ID and displays information about the corresponding kernel object.

<span id="_______Process______"></span><span id="_______process______"></span><span id="_______PROCESS______"></span> *Process*   
(Kernel mode only) Specifies a process. You can use the process ID or the hexadecimal address of the process object. This parameter must refer to a currently running process on the target system. If this parameter is -1 or if you omit it, the current process is used. If this parameter is 0, handle information from all processes is displayed.

<span id="_______TypeName______"></span><span id="_______typename______"></span><span id="_______TYPENAME______"></span> *TypeName*   
Specifies the type of handle that you want to examine. Only handles that match this type are displayed. *TypeName* is case sensitive. Valid types include Event, Section, File, Port, Directory, SymbolicLink, Mutant, WindowStation, Semaphore, Key, Token, Process, Thread, Desktop, IoCompletion, Timer, Job, and WaitablePort.

<span id="_______-_______"></span> **-?**   
(User mode only) Displays some Help text for this extension in the [Debugger Command window](debugger-command-window.md).

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
Uext.dll
Ntsdexts.dll</td>
</tr>
<tr class="even">
<td align="left"><p><strong>Windows XP and later</strong></p></td>
<td align="left"><p></p>
Kdexts.dll
Uext.dll
Ntsdexts.dll</td>
</tr>
</tbody>
</table>

 

### <span id="Additional_Information"></span><span id="additional_information"></span><span id="ADDITIONAL_INFORMATION"></span>Additional Information

For more information about handles, see the [**!htrace**](-htrace.md) extension, the Microsoft Windows SDK documentation and *Microsoft Windows Internals* by Mark Russinovich and David Solomon. (These resources may not be available in some languages and countries.)

Remarks
-------

You can use the **!handle** extension during user-mode and kernel-mode live debugging. You can also use this extension on kernel-mode dump files. However, you cannot use this extension on user-mode dump files, unless you specifically created them with handle information. (You can create such dump files by using the [**.dump /mh (Create Dump File)**](-dump--create-dump-file-.md) command.)

During live user-mode debugging, you can use the [**.closehandle (Close Handle)**](-closehandle--close-handle-.md) command to close one or more handles.

The following examples are user-mode examples of the **!handle** extension. The following command displays a list of all handles.

```dbgcmd
0:000> !handle
Handle 4
  Type          Section
Handle 8
  Type          Event
Handle c
  Type          Event
Handle 10
  Type          Event
Handle 14
  Type          Directory
Handle 5c
  Type          File
6 Handles
Type            Count
Event           3
Section         1
File            1
Directory       1
```

The following command displays detailed information about handle 0x8.

```dbgcmd
0:000> !handle 8 f
Handle 8
  Type          Event
  Attributes    0
  GrantedAccess 0x100003:
         Synch
         QueryState,ModifyState
  HandleCount   2
  PointerCount  3
  Name          <none>
  Object Specific Information
    Event Type Auto Reset
    Event is Waiting
```

The following examples are kernel-mode examples of **!handle**. The following command lists all handles, including free handles.

```dbgcmd
kd> !handle 0 4
processor number 0
PROCESS 80559800  SessionId: 0  Cid: 0000    Peb: 00000000  ParentCid: 0000
    DirBase: 00039000  ObjectTable: e1000d60  TableSize: 380.
    Image: Idle

New version of handle table at e1002000 with 380 Entries in use

0000: free handle, Entry address e1002000, Next Entry fffffffe
0004: Object: 80ed5238  GrantedAccess: 001f0fff
0008: Object: 80ed46b8  GrantedAccess: 00000000
000c: Object: e1281d00  GrantedAccess: 000f003f
0010: Object: e1013658  GrantedAccess: 00000000
......
0168: Object: ffb6c748  GrantedAccess: 00000003 (Protected)
016c: Object: ff811f90  GrantedAccess: 0012008b
0170: free handle, Entry address e10022e0, Next Entry 00000458
0174: Object: 80dfd5c8  GrantedAccess: 001f01ff
......
```

The following command show detailed information about handle 0x14 in the kernel handle table.

```dbgcmd
kd> !handle 14 13
processor number 0
PROCESS 80559800  SessionId: 0  Cid: 0000    Peb: 00000000  ParentCid: 0000
    DirBase: 00039000  ObjectTable: e1000d60  TableSize: 380.
    Image: Idle

Kernel New version of handle table at e1002000 with 380 Entries in use
0014: Object: e12751d0  GrantedAccess: 0002001f
Object: e12751d0  Type: (80ec8db8) Key
    ObjectHeader: e12751b8
        HandleCount: 1  PointerCount: 1
        Directory Object: 00000000  Name: \REGISTRY\MACHINE\SYSTEM\CONTROLSET001\CONTROL\SESSION MANAGER\EXECUTIVE
```

The following command shows information about all handles to Section objects in all processes.

```dbgcmd
!handle 0 3 0 Section
...
PROCESS fffffa8004f48940
    SessionId: none  Cid: 0138    Peb: 7f6639bf000  ParentCid: 0004
    DirBase: 10cb74000  ObjectTable: fffff8a00066f700  HandleCount:  39.
    Image: smss.exe

Handle table at fffff8a00066f700 with 39 entries in use

0040: Object: fffff8a000633f00  GrantedAccess: 00000006 (Inherit) Entry: fffff8a000670100
Object: fffff8a000633f00  Type: (fffffa80035fef20) Section
    ObjectHeader: fffff8a000633ed0 (new version)
        HandleCount: 1  PointerCount: 262144
...
```

 

 





