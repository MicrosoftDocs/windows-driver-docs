---
title: Bug Check 0x1E KMODE_EXCEPTION_NOT_HANDLED
description: The KMODE_EXCEPTION_NOT_HANDLED bug check has a value of 0x0000001E. This indicates that a kernel-mode program generated an exception which the error handler did not catch.
ms.assetid: 4a30b770-b2c4-4fdd-b431-95f2b40ef5f7
keywords: ["Bug Check 0x1E KMODE_EXCEPTION_NOT_HANDLED", "KMODE_EXCEPTION_NOT_HANDLED"]
ms.author: domars
ms.date: 08/23/2018
topic_type:
- apiref
api_name:
- KMODE_EXCEPTION_NOT_HANDLED
api_type:
- NA
ms.localizationpriority: medium
---

# Bug Check 0x1E: KMODE\_EXCEPTION\_NOT\_HANDLED


The KMODE\_EXCEPTION\_NOT\_HANDLED bug check has a value of 0x0000001E. This indicates that a kernel-mode program generated an exception which the error handler did not catch.

**Important** This topic is for programmers. If you are a customer who has received a blue screen error code while using your computer, see [Troubleshoot blue screen errors](https://windows.microsoft.com/windows-10/troubleshoot-blue-screen-errors).

## KMODE\_EXCEPTION\_NOT\_HANDLED Parameters


<table>
<colgroup>
<col width="50%" />
<col width="50%" />
</colgroup>
<thead>
<tr class="header">
<th align="left">Parameter</th>
<th align="left">Description</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td align="left"><p>1</p></td>
<td align="left"><p>The exception code that was not handled</p></td>
</tr>
<tr class="even">
<td align="left"><p>2</p></td>
<td align="left"><p>The address at which the exception occurred</p></td>
</tr>
<tr class="odd">
<td align="left"><p>3</p></td>
<td align="left"><p>Parameter 0 of the exception</p></td>
</tr>
<tr class="even">
<td align="left"><p>4</p></td>
<td align="left"><p>Parameter 1 of the exception</p></td>
</tr>
</tbody>
</table>

 

Cause
-----

This is a common bug check. To interpret it, you must identify which exception was generated.

Common exception codes include:

-   0x80000002: STATUS\_DATATYPE\_MISALIGNMENT

    An unaligned data reference was encountered.

-   0x80000003: STATUS\_BREAKPOINT

    A breakpoint or ASSERT was encountered when no kernel debugger was attached to the system.

-   0xC0000005: STATUS\_ACCESS\_VIOLATION

    A memory access violation occurred. (Parameter 4 of the bug check is the address that the driver attempted to access.)

For a complete list of exception codes, see [NTSTATUS Values](https://msdn.microsoft.com/library/cc704588.aspx). The exception codes are also listed in the ntstatus.h file located in the inc directory of the [Windows Driver Kit](https://docs.microsoft.com/windows-hardware/drivers/).


Resolution
----------

**If you are not equipped to debug this problem**, you can use some basic troubleshooting techniques described in [**Blue Screen Data**](blue-screen-data.md). If a driver is identified in the bug check message, disable the driver or check with the manufacturer for driver updates.

**If you plan to debug this problem**, you may find it difficult to obtain a stack trace. Parameter 2 (the exception address) should pinpoint the driver or function that caused this problem.

If exception code 0x80000003 occurs, this indicates that a hard-coded breakpoint or assertion was hit, but the system was started with the **/NODEBUG** switch. This problem should rarely occur. If it occurs repeatedly, make sure a kernel debugger is connected and the system is started with the **/DEBUG** switch.

If exception code 0x80000002 occurs, the trap frame will supply additional information.

If the specific cause of the exception is unknown, the following should be considered:

**Hardware incompatibility**

Confirm that any new hardware that is installed is compatible with the installed version of Windows. For example, you can get information about required hardware at [Windows 10 Specifications](https://www.microsoft.com/windows/windows-10-specifications).

**Faulty device driver or system service**

In addition, a faulty device driver or system service might be responsible for this error. Hardware issues, such as BIOS incompatibilities, memory conflicts, and IRQ conflicts can also generate this error.

If a driver is listed by name within the bug check message, disable or remove that driver. Disable or remove any drivers or services that were recently added. If the error occurs during the startup sequence and the system partition is formatted with NTFS file system, you might be able to use Safe Mode to disable the driver in Device Manager.

Check the System Log in Event Viewer for additional error messages that might help pinpoint the device or driver that is causing bug check 0x1E. You should also run hardware diagnostics, especially the memory scanner, supplied by the system manufacturer. For details on these procedures, see the owner's manual for your computer.

The error that generates this message can occur after the first restart during Windows Setup, or after Setup is finished. A possible cause of the error is a system BIOS incompatibility. BIOS problems can be resolved by upgrading the system BIOS version.

**To get a stack trace if the normal stack tracing procedures fail**

1.  Use the [**kb (Display Stack Backtrace)**](k--kb--kc--kd--kp--kp--kv--display-stack-backtrace-.md) command to display parameters in the stack trace. Look for the call to **NT!PspUnhandledExceptionInSystemThread**. (If this function is not listed, see the note below.)

2.  The first parameter to **NT!PspUnhandledExceptionInSystemThread** is a pointer to a structure, which contains pointers to an **except** statement:

    ```cpp
    typedef struct _EXCEPTION_POINTERS {
        PEXCEPTION_RECORD ExceptionRecord;
        PCONTEXT ContextRecord;
        } EXCEPTION_POINTERS, *PEXCEPTION_POINTERS;

    ULONG PspUnhandledExceptionInSystemThread(
        IN PEXCEPTION_POINTERS ExceptionPointers
        )
    ```

    Use the [**dd (Display Memory)**](d--da--db--dc--dd--dd--df--dp--dq--du--dw--dw--dyb--dyd--display-memor.md) command on that address to display the necessary data.

3.  The first retrieved value is an exception record and the second is a context record. Use the [**.exr (Display Exception Record)**](-exr--display-exception-record-.md) command and the [**.cxr (Display Context Record)**](-cxr--display-context-record-.md) command with these two values as their arguments, respectively.

4.  After the **.cxr** command executes, use the **kb** command to display a stack trace that is based on the context record information. This stack trace indicates the calling stack where the unhandled exception occurred.

**Note**  This procedure assumes that you can locate **NT!PspUnhandledExceptionInSystemThread**. However, in some cases (such as an access violation crash) you will not be able to do this. In that case, look for **ntoskrnl!KiDispatchException**. The third parameter passed to this function is a trap frame address. Use the [**.trap (Display Trap Frame)**](-trap--display-trap-frame-.md) command with this address to set the Register Context to the proper value. You can then perform stack traces and issue other commands.

 

Here is an example of bug check 0x1E on an x86 processor:

```dbgcmd
kd> .bugcheck                 get the bug check data
Bugcheck code 0000001e
Arguments c0000005 8013cd0a 00000000 0362cffff

kd> kb                        start with a stack trace 
FramePtr  RetAddr   Param1   Param2   Param3   Function Name 
8013ed5c  801263ba  00000000 00000000 fe40cb00 NT!_DbgBreakPoint 
8013eecc  8013313c  0000001e c0000005 8013cd0a NT!_KeBugCheckEx+0x194
fe40cad0  8013318e  fe40caf8 801359ff fe40cb00 NT!PspUnhandledExceptionInSystemThread+0x18
fe40cad8  801359ff  fe40cb00 00000000 fe40cb00 NT!PspSystemThreadStartup+0x4a
fe40cf7c  8013cb8e  fe43a44c ff6ce388 00000000 NT!_except_handler3+0x47
00000000  00000000  00000000 00000000 00000000 NT!KiThreadStartup+0xe

kd> dd fe40caf8 L2            dump EXCEPTION_POINTERS structure
0xFE40CAF8  fe40cd88 fe40cbc4                   ..@...@.

kd> .exr fe40cd88             first DWORD is the exception record
Exception Record @ FE40CD88:
   ExceptionCode: c0000005
  ExceptionFlags: 00000000
  Chained Record: 00000000
ExceptionAddress: 8013cd0a
NumberParameters: 00000002
   Parameter[0]: 00000000
   Parameter[1]: 0362cfff

kd> .cxr fe40cbc4             second DWORD is the context record
CtxFlags: 00010017
eax=00087000 ebx=00000000 ecx=03ff0000 edx=ff63d000 esi=0362cfff edi=036b3fff
eip=8013cd0a esp=fe40ce50 ebp=fe40cef8 iopl=0         nv dn ei pl nz ac po cy
vip=0    vif=0
cs=0008  ss=0010  ds=0023  es=0023  fs=0030  gs=0000             efl=00010617
0x8013cd0a  f3a4             rep movsb

kd> kb                        kb gives stack for context record
ChildEBP RetAddr  Args to Child
fe40ce54 80402e09 ff6c4000 ff63d000 03ff0000 NT!_RtlMoveMemory@12+0x3e
fe40ce68 80403c18 ffbc0c28 ff6ce008 ff6c4000 HAL!_HalpCopyBufferMap@20+0x49
fe40ce9c fe43b1e4 ff6cef90 ffbc0c28 ff6ce009 HAL!_IoFlushAdapterBuffers@24+0x148
fe40ceb8 fe4385b4 ff6ce388 6cd00800 ffbc0c28 QIC117!_kdi_FlushDMABuffers@20+0x28
fe40cef8 fe439894 ff6cd008 ffb6c820 fe40cf4c QIC117!_cqd_CmdReadWrite@8+0x26e
fe40cf18 fe437d92 ff6cd008 ffb6c820 ff6e4e50 QIC117!_cqd_DispatchFRB@8+0x210
fe40cf30 fe43a4f5 ff6cd008 ffb6c820 00000000 QIC117!_cqd_ProcessFRB@8+0x134
fe40cf4c 80133184 ff6ce388 00000000 00000000 QIC117!_kdi_ThreadRun@4+0xa9
fe40cf7c 8013cb8e fe43a44c ff6ce388 00000000 NT!_PspSystemThreadStartup@8+0x40
```

 

 




