---
title: process
description: The process extension displays information about the specified process, or about all processes, including the EPROCESS block.
ms.assetid: 57f55632-8320-47cc-8a20-5a2cf3b42b3a
keywords: ["process Windows Debugging"]
ms.author: domars
ms.date: 08/02/2018
topic_type:
- apiref
api_name:
- process
api_type:
- NA
ms.localizationpriority: medium
---

# !process


The !process extension displays information about the specified process, or about all processes, including the EPROCESS block.

This extension can be used only during kernel-mode debugging.

Syntax

```dbgcmd
!process [/s Session] [/m Module] [Process [Flags]]
!process [/s Session] [/m Module] 0 Flags ImageName
```

## <span id="Parameters"></span><span id="parameters"></span><span id="PARAMETERS"></span>Parameters


<span id="_s_Session"></span><span id="_s_session"></span><span id="_S_SESSION"></span>**/s** **** *Session*  
Specifies the session that owns the desired process.

<span id="_m_Module"></span><span id="_m_module"></span><span id="_M_MODULE"></span>**/m** **** *Module*  
Specifies the module that owns the desired process.

<span id="_Process"></span><span id="_process"></span><span id="_PROCESS"></span> *Process*  
Specifies the hexadecimal address or the process ID of the process on the target computer.

The value of *Process* determines whether the !process extension displays a process address or a process ID . If *Process* is omitted in any version of Windows, the debugger displays data only about the current system process. If *Process* is 0 and *ImageName* is omitted, the debugger displays information about all active processes. If -1 is specifed for *Process* information about the current process is displayed.

<span id="Flags"></span><span id="flags"></span><span id="FLAGS"></span>*Flags*  
Specifies the level of detail to display. *Flags* can be any combination of the following bits. If *Flags* is 0, only a minimal amount of information is displayed. The default varies according to the version of Windows and the value of *Process*. The default is 0x3 if *Process* is omitted or if *Process* is either 0 or -1; otherwise, the default is 0xF.

<span id="Bit_0__0x1_"></span><span id="bit_0__0x1_"></span><span id="BIT_0__0X1_"></span>Bit 0 (0x1)  
Displays time and priority statistics.

<span id="Bit_1__0x2_"></span><span id="bit_1__0x2_"></span><span id="BIT_1__0X2_"></span>Bit 1 (0x2)  
Displays a list of threads and events associated with the process, and their wait states.

<span id="Bit_2__0x4_"></span><span id="bit_2__0x4_"></span><span id="BIT_2__0X4_"></span>Bit 2 (0x4)  
Displays a list of threads associated with the process. If this is included without Bit 1 (0x2), each thread is displayed on a single line. If this is included along with Bit 1, each thread is displayed with a stack trace.

<span id="Bit_3__0x8_"></span><span id="bit_3__0x8_"></span><span id="BIT_3__0X8_"></span>Bit 3 (0x8)  
 Displays the return address and the stack pointer for each function The display of function arguments is suppressed.

<span id="Bit_4__0x10_"></span><span id="bit_4__0x10_"></span><span id="BIT_4__0X10_"></span>Bit 4 (0x10)  
 Sets the process context equal to the specified process for the duration of this command. This results in a more accurate display of thread stacks. Because this flag is equivalent to using [**.process /p /r**](-process--set-process-context-.md) for the specified process, any existing user-mode module list will be discarded. If *Process* is zero, the debugger displays all processes, and the process context is changed for each one. If you are only displaying a single process and its user-mode state has already been refreshed (for example, with **.process /p /r**), it is not necessary to use this flag. This flag is only effective when used with Bit 0 (0x1).

<span id="ImageName"></span><span id="imagename"></span><span id="IMAGENAME"></span>*ImageName*  
Specifies the name of the process to be displayed. The debugger displays all processes whose executable image names match *ImageName*. The image name must match that in the EPROCESS block. In general, this is the executable name that was invoked to start the process, including the file extension (usually .exe), and truncated after the fifteenth character. There is no way to specify an image name that contains a space. When *ImageName* is specified, *Process* must be zero.

## <span id="DLL"></span><span id="dll"></span>DLL


Kdexts.dll

## <span id="Additional_Information"></span><span id="additional_information"></span><span id="ADDITIONAL_INFORMATION"></span>Additional Information


For information about processes in kernel mode, see [Changing Contexts](changing-contexts.md). For more information about analyzing processes and threads, see *Microsoft Windows Internals*, by Mark Russinovich and David Solomon.

Remarks
-------

The following is an example of a **!process 0 0** display:

```dbgcmd
kd> !process 0 0
**** NT ACTIVE PROCESS DUMP ****
PROCESS 80a02a60  Cid: 0002    Peb: 00000000  ParentCid: 0000
    DirBase: 00006e05  ObjectTable: 80a03788  TableSize: 150.
    Image: System
PROCESS 80986f40  Cid: 0012    Peb: 7ffde000  ParentCid: 0002
    DirBase: 000bd605  ObjectTable: 8098fce8  TableSize:  38.
    Image: smss.exe
PROCESS 80958020  Cid: 001a    Peb: 7ffde000  ParentCid: 0012
    DirBase: 0008b205  ObjectTable: 809782a8  TableSize: 150.
    Image: csrss.exe
PROCESS 80955040  Cid: 0020    Peb: 7ffde000  ParentCid: 0012
    DirBase: 00112005  ObjectTable: 80955ce8  TableSize:  54.
    Image: winlogon.exe
PROCESS 8094fce0  Cid: 0026    Peb: 7ffde000  ParentCid: 0020
    DirBase: 00055005  ObjectTable: 80950cc8  TableSize: 222.
    Image: services.exe
PROCESS 8094c020  Cid: 0029    Peb: 7ffde000  ParentCid: 0020
    DirBase: 000c4605  ObjectTable: 80990fe8  TableSize: 110.
    Image: lsass.exe
PROCESS 809258e0  Cid: 0044    Peb: 7ffde000  ParentCid: 0026
    DirBase: 001e5405  ObjectTable: 80925c68  TableSize:  70.
    Image: SPOOLSS.EXE
```

The following table describes some of the elements of the **!process 0 0** output.

<table>
<colgroup>
<col width="50%" />
<col width="50%" />
</colgroup>
<thead>
<tr class="header">
<th align="left">Element</th>
<th align="left">Meaning</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td align="left"><p>Process address</p></td>
<td align="left"><p>The eight-character hexadecimal number after the word PROCESS is the address of the EPROCESS block. In the final entry in the preceding example, the process address is 0x809258E0.</p></td>
</tr>
<tr class="even">
<td align="left"><p>Process ID (PID)</p></td>
<td align="left"><p>The hexadecimal number after the word Cid. In the final entry in the preceding example, the PID is 0x44, or decimal 68.</p></td>
</tr>
<tr class="odd">
<td align="left"><p>Process Environment Block (PEB)</p></td>
<td align="left"><p>The hexadecimal number after the word Peb is the address of the process environment block. In the final entry in the preceding example, the PEB is located at address 0x7FFDE000.</p></td>
</tr>
<tr class="even">
<td align="left"><p>Parent process PID</p></td>
<td align="left"><p>The hexadecimal number after the word ParentCid is the PID of the parent process. In the final entry in the preceding example, the parent process PID is 0x26, or decimal 38.</p></td>
</tr>
<tr class="odd">
<td align="left"><p>Image</p></td>
<td align="left"><p>The name of the module that owns the process. In the final entry in the preceding example, the owner is spoolss.exe. In the first entry, the owner is the operating system itself.</p></td>
</tr>
<tr class="even">
<td align="left"><p>Process object address</p></td>
<td align="left"><p>The hexadecimal number after the word ObjectTable. In the final entry in the preceding example, the address of the process object is 0x80925c68.</p></td>
</tr>
</tbody>
</table>

 

To display full details on one process, set *Flags* to 7. The process itself can be specified by setting *Process* equal to the process address, setting *Process* equal to the process ID, or setting *ImageName* equal to the executable image name. Here is an example:

```dbgcmd
kd> !process fb667a00 7
PROCESS fb667a00 Cid: 0002  Peb: 00000000 ParentCid: 0000
  DirBase: 00030000 ObjectTable: e1000f88 TableSize: 112.
  Image: System
  VadRoot fb666388 Clone 0 Private 4. Modified 9850. Locked 0.
  FB667BBC MutantState Signalled OwningThread 0
  Token               e10008f0
  ElapsedTime            15:06:36.0338
  UserTime             0:00:00.0000
  KernelTime            0:00:54.0818
  QuotaPoolUsage[PagedPool]     1480
Working Set Sizes (now,min,max) (3, 50, 345)
  PeakWorkingSetSize        118
  VirtualSize            1 Mb
  PeakVirtualSize          1 Mb
  PageFaultCount          992
  MemoryPriority          BACKGROUND
  BasePriority           8
  CommitCharge           8

    THREAD fb667780 Cid 2.1 Teb: 00000000 Win32Thread: 80144900 WAIT: (WrFreePage) KernelMode Non-Alertable
    80144fc0 SynchronizationEvent
    Not impersonating
    Owning Process fb667a00
    WaitTime (seconds)   32278
    Context Switch Count  787
    UserTime         0:00:00.0000
    KernelTime        0:00:21.0821
    Start Address Phase1Initialization (0x801aab44)
    Initial Sp fb26f000 Current Sp fb26ed00
    Priority 0 BasePriority 0 PriorityDecrement 0 DecrementCount 0

    ChildEBP RetAddr Args to Child
    fb26ed18 80118efc c0502000 804044b0 00000000 KiSwapThread+0xb5
    fb26ed3c 801289d9 80144fc0 00000008 00000000 KeWaitForSingleObject+0x1c2
```

Note that the address of the process object can be used as input to other extensions, such as [**!handle**](-handle.md), to obtain further information.

The following table describes some of the elements in the previous example.

<table>
<colgroup>
<col width="50%" />
<col width="50%" />
</colgroup>
<thead>
<tr class="header">
<th align="left">Element</th>
<th align="left">Meaning</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td align="left">WAIT</td>
<td align="left">The parenthetical comment after this heading gives the reason for the wait. The command <strong><a href="dt--display-type-.md" data-raw-source="[dt nt!_KWAIT_REASON](dt--display-type-.md)">dt nt!_KWAIT_REASON</a></strong> will display a list of all wait reasons.</td>
</tr>
<tr class="even">
<td align="left"><p>ElapsedTime</p></td>
<td align="left"><p>Lists the amount of time that has elapsed since the process was created. This is displayed in units of Hours:Minutes:Seconds.Milliseconds.</p></td>
</tr>
<tr class="odd">
<td align="left"><p>UserTime</p></td>
<td align="left"><p>Lists the amount of time the process has been running in user mode. If the value for UserTime is exceptionally high, it might identify a process that is depleting system resources. Units are the same as those of ElapsedTime.</p></td>
</tr>
<tr class="even">
<td align="left"><p>KernelTime</p></td>
<td align="left"><p>Lists the amount of time the process has been running in kernel mode. If the value for KernelTime is exceptionally high, it might identify a process that is depleting system resources. Units are the same as those of ElapsedTime.</p></td>
</tr>
<tr class="odd">
<td align="left"><p>Working Set sizes</p></td>
<td align="left"><p>Lists the current, minimum and maximum working set size for the process, in pages. An exceptionally large working set size can be a sign of a process that is leaking memory or depleting system resources.</p></td>
</tr>
<tr class="even">
<td align="left"><p>QuotaPoolUsage entries</p></td>
<td align="left"><p>Lists the paged and nonpaged pool used by the process. On a system with a memory leak, looking for excessive nonpaged pool usage on all the processes can tell you which process has the memory leak.</p></td>
</tr>
<tr class="odd">
<td align="left"><p>Clone</p></td>
<td align="left"><p>Indicates whether or not the process was created by the POSIX or Interix subsystems.</p></td>
</tr>
<tr class="even">
<td align="left"><p>Private</p></td>
<td align="left"><p>Indicates the number of private (non-sharable) pages currently being used by the process. This includes both paged in and paged out memory.</p></td>
</tr>
</tbody>
</table>

 

In addition to the process list information, the thread information contains a list of the resources on which the thread has locks. This information is listed in the third line of output after the thread header. In this example, the thread has a lock on one resource, a SynchronizationEvent with an address of 80144fc0. By comparing this address to the list of locks shown by the [**!kdext\*.locks**](-locks---kdext--locks-.md) extension, you can determine which threads have exclusive locks on resources.

The [**!stacks**](-stacks.md) extension gives a brief summary of the state of every thread. This can be used instead of the !process extension to get a quick overview of the system, especially when debugging multithread issues, such as resource conflicts or deadlocks.

 

 





