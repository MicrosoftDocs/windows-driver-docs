---
title: .thread (Set Register Context)
description: The .thread command specifies which thread will be used for the register context.
ms.assetid: 577276b7-a6c4-427e-ada1-10dbb62ebd5c
keywords: ["Set Register Context (.thread) command", "context, Set Register Context (.thread) command", "registers, Set Register Context (.thread) command", "call stack, Set Register Context (.thread) command", ".thread (Set Register Context) Windows Debugging"]
ms.author: domars
ms.date: 05/23/2017
topic_type:
- apiref
api_name:
- .thread (Set Register Context)
api_type:
- NA
ms.localizationpriority: medium
---

# .thread (Set Register Context)


The **.thread** command specifies which thread will be used for the register context.

```dbgcmd
.thread [/p [/r] ] [/P] [/w] [Thread]
```

## <span id="ddk_meta_set_register_context_dbg"></span><span id="DDK_META_SET_REGISTER_CONTEXT_DBG"></span>Parameters


<span id="________p______"></span><span id="________P______"></span> **/p**   
(Live debugging only) If this option is included and *Thread* is nonzero, all transition page table entries (PTEs) for the process owning this thread will be automatically translated into physical addresses before access. This may cause slowdowns, because the debugger will have to look up the physical addresses for all the memory used by this process, and a significant amount of data may need to be transferred across the debug cable. (This behavior is the same as that of [**.cache forcedecodeuser**](-cache--set-cache-size-.md).)

If the **/p** option is included and *Thread* is zero or omitted, this translation will be disabled. (This behavior is the same as that of [**.cache noforcedecodeuser**](-cache--set-cache-size-.md).)

<span id="________r______"></span><span id="________R______"></span> **/r**   
(Live debugging only) If the **/r** option is included along with the **/p** option, user-mode symbols for the process owning this thread will be reloaded after the process and register contexts have been set. (This behavior is the same as that of [**.reload /user**](-reload--reload-module-.md).)

<span id="________P______"></span><span id="________p______"></span> **/P**   
(Live debugging only) If this option is included and *Thread* is nonzero, all transition page table entries (PTEs) will be automatically translated into physical addresses before access. Unlike the **/p** option, this translates the PTEs for all user-mode and kernel-mode processes, not only the process owning this thread. This may cause slowdowns, because the debugger will have to look up the physical addresses for all memory in use, and a huge amount of data may need to be transferred across the debug cable. (This behavior is the same as that of [**.cache forcedecodeptes**](-cache--set-cache-size-.md).)

<span id="________w______"></span><span id="________W______"></span> **/w**   
(64-bit kernel debugging only) Changes the active context for the thread to the WOW64 32-bit context. The thread specified must be running in a process that has a WOW64 state.

<span id="_______Thread______"></span><span id="_______thread______"></span><span id="_______THREAD______"></span> *Thread*   
The address of the thread. If this is omitted or zero, the thread context is reset to the current thread.

### <span id="Environment"></span><span id="environment"></span><span id="ENVIRONMENT"></span>Environment

<table>
<colgroup>
<col width="50%" />
<col width="50%" />
</colgroup>
<tbody>
<tr class="odd">
<td align="left"><p><strong>Modes</strong></p></td>
<td align="left"><p>kernel mode only</p></td>
</tr>
<tr class="even">
<td align="left"><p><strong>Targets</strong></p></td>
<td align="left"><p>live, crash dump</p></td>
</tr>
<tr class="odd">
<td align="left"><p><strong>Platforms</strong></p></td>
<td align="left"><p>all</p></td>
</tr>
</tbody>
</table>

 

### <span id="Additional_Information"></span><span id="additional_information"></span><span id="ADDITIONAL_INFORMATION"></span>Additional Information

For more information about the register context and other context settings, see [Changing Contexts](changing-contexts.md).

Remarks
-------

Generally, when you are doing kernel debugging, the only visible registers are the ones associated with the current thread.

The **.thread** command instructs the kernel debugger to use the specified thread as the register context. After this command is executed, the debugger will have access to the most important registers and the stack trace for this thread. This register context persists until you allow the target to execute or use another register context command (**.thread**, [**.cxr**](-cxr--display-context-record-.md), or [**.trap**](-trap--display-trap-frame-.md)). See [Register Context](changing-contexts.md#register-context) for full details.

The **/w** option can only be used in 64-bit kernel debugging sessions on a thread running in a process that has a WOW64 state. The context retrieved will be the last context remembered by WOW64; this is usually the last user-mode code executed by *Thread*. This option can only be used if the target is in native machine mode. For example, if the target is running on a 64-bit machine that is emulating an x86-based processor using WOW64, this option cannot be used. Using the **/w** option will cause the machine mode to switch automatically to an x86-based processor.

This command does not actually change the current thread. In other words, extensions such as [**!thread**](-thread.md) and [**!teb**](-teb.md) will still default to the current thread if no arguments are used with them.

Here is an example. Use the [**!process**](-process.md) extension to find the address of the desired thread. (In this case, **!process 0 0** is used to list all processes, then **!process** is used a second time to list all the threads for the desired process.)

```dbgcmd
kd> !process 0 0
**** NT ACTIVE PROCESS DUMP ****
PROCESS fe5039e0  SessionId: 0  Cid: 0008    Peb: 00000000  ParentCid: 0000
    DirBase: 00030000  ObjectTable: fe529a88  TableSize: 145.
    Image: System

.....

PROCESS ffaa5280  SessionId: 0  Cid: 0120    Peb: 7ffdf000  ParentCid: 01e0
    DirBase: 03b70000  ObjectTable: ffaa4e48  TableSize:  23.
    Image: winmine.exe

kd> !process ffaa5280
PROCESS ffaa5280  SessionId: 0  Cid: 0120    Peb: 7ffdf000  ParentCid: 01e0
    DirBase: 03b70000  ObjectTable: ffaa4e48  TableSize:  23.
    Image: winmine.exe
    VadRoot ffaf6e48 Clone 0 Private 50. Modified 0. Locked 0.
    DeviceMap fe502e88
    Token                             e1b55d70

.....

        THREAD ffaa43a0  Cid 120.3a4  Teb: 7ffde000  Win32Thread: e1b4fea8 WAIT: (WrUserRequest) UserMode Non-Alertable
            ffadc6a0  SynchronizationEvent
        Not impersonating
        Owning Process ffaa5280
        WaitTime (seconds)      24323
        Context Switch Count    494                   LargeStack

.....
```

Now use the **.thread** command with the address of the desired thread. This sets the register context and enables you to examine the important registers and the call stack for this thread.

```dbgcmd
kd> .thread ffaa43a0
Using context of thread ffaa43a0

kd> r
Last set context:
eax=00000000 ebx=00000000 ecx=00000000 edx=00000000 esi=00000000 edi=00000000
eip=80403a0d esp=fd581c2c ebp=fd581c60 iopl=0         nv up di pl nz na pe nc
cs=0000  ss=0000  ds=0000  es=0000  fs=0000  gs=0000             efl=00000000
0000:3a0d ??              ???

kd> k
  *** Stack trace for last set context - .thread resets it
ChildEBP RetAddr  
fd581c38 8042d61c ntoskrnl!KiSwapThread+0xc5
00001c60 00000000 ntoskrnl!KeWaitForSingleObject+0x1a1
```

 

 





