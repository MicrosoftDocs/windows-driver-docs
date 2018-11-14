---
title: Bug Check 0xA IRQL_NOT_LESS_OR_EQUAL
description: The IRQL_NOT_LESS_OR_EQUAL bug check has a value of 0x0000000A.
ms.assetid: a32b80f5-9822-41af-8668-836a70b05c0f
keywords: ["Bug Check 0xA IRQL_NOT_LESS_OR_EQUAL", "IRQL_NOT_LESS_OR_EQUAL"]
ms.author: domars
ms.date: 05/23/2017
topic_type:
- apiref
api_name:
- IRQL_NOT_LESS_OR_EQUAL
api_type:
- NA
ms.localizationpriority: medium
---

# Bug Check 0xA: IRQL\_NOT\_LESS\_OR\_EQUAL


The IRQL\_NOT\_LESS\_OR\_EQUAL bug check has a value of 0x0000000A. This indicates that Microsoft Windows or a kernel-mode driver accessed paged memory at an invalid address while at a raised interrupt request level (IRQL). This is typically either a bad pointer or a pageability problem.

**Important** This topic is for programmers. If you are a customer who has received a blue screen error code while using your computer, see [Troubleshoot blue screen errors](https://windows.microsoft.com/windows-10/troubleshoot-blue-screen-errors).

## IRQL\_NOT\_LESS\_OR\_EQUAL Parameters


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
<td align="left"><p>The virtual memory address that could not be accessed.</p>
<p>Use <strong><a href="-pool.md" data-raw-source="[!pool](-pool.md)">!pool</a></strong> on this address to see whether it&#39;s Paged pool. These commands, may also be useful in gathering information about the failure: <strong><a href="-pte.md" data-raw-source="[!pte](-pte.md)">!pte</a></strong>, <strong><a href="-address.md" data-raw-source="[!address](-address.md)">!address</a></strong>, and <strong><a href="ln--list-nearest-symbols-.md" data-raw-source="[ln (List Nearest Symbols)](ln--list-nearest-symbols-.md)">ln (List Nearest Symbols)</a></strong>.</p></td>
</tr>
<tr class="even">
<td align="left"><p>2</p></td>
<td align="left"><p>IRQL at time of the fault.</p>
<p>VALUES:</p>
<p>2 : The IRQL was DISPATCH_LEVEL at the time of the fault. END_VALUES</p></td>
</tr>
<tr class="odd">
<td align="left"><p>3</p></td>
<td align="left"><p>Bitfield describing the operation that caused the fault.</p>
<p><strong>Bit 0:</strong></p>
<p>VALUES:</p>
<p>0: Read operation</p>
<p>1: Write operation</p>
<p><strong>Bit 3:</strong> (Only available on chipsets that support this level of reporting.)</p>
<p>VALUES:</p>
<p>0: Not an execute operation</p>
<p>1: Execute operation</p>
<strong>Bit 0 and Bit 3 combined values:</strong>
<p>0x0 : Fault trying to READ from the address in parameter 1.</p>
<p>0x1 : Fault trying to WRITE to the address in parameter 1.</p>
<p>0x8 : Fault trying to EXECUTE code from the address in parameter 1.</p>
<p>This value is usually caused by:</p>
<ul>
<li>Calling a function that cannot be called at DISPATCH_LEVEL while at DISPATCH_LEVEL</li>
<li>Forgetting to release a spinlock</li>
<li>Marking code as pageable when it must be non-pageable (e.g., because the code acquires a spinlock, or is called in a DPC)</li>
</ul></td>
</tr>
<tr class="even">
<td align="left"><p>4</p></td>
<td align="left"><p>The instruction pointer at the time of the fault.</p>
<p>Use the <strong><a href="ln--list-nearest-symbols-.md" data-raw-source="[ln (List Nearest Symbols)](ln--list-nearest-symbols-.md)">ln (List Nearest Symbols)</a></strong> command on this address to see the name of the function.</p></td>
</tr>
</tbody>
</table>

 

Cause
-----

Bug check 0xA is usually caused by kernel mode device drivers using improper addresses.

This bug check indicates that an attempt was made to access an invalid address while at a raised interrupt request level (IRQL). This is either a bad memory pointer or a pageability problem with the device driver code.

1. If parameter 1 is less than 0x1000, then this is likely a NULL pointer dereference.
2. If !pool reports that parameter 1 is Paged pool, then the IRQL is too high to access this data. Run at a lower IRQL or allocate the data in NonPagedPool.
3. If parameter 3 indicates that this was an attempt to execute pageable code, then the IRQL is too high to call this function. Run at a lower IRQL or do not mark the code as pageable.
4. Otherwise, this may be a bad pointer, possibly caused by use-after-free or bit-flipping. Investigate the validity of parameter 1 with [**!pte**](-pte.md), [**!address**](-address.md), and [**ln (List Nearest Symbols)**](ln--list-nearest-symbols-.md).

Resolution
----------

If a kernel debugger is available, obtain a stack trace: the [**!analyze**](https://docs.microsoft.com/windows-hardware/drivers/debugger/-analyze) debug extension displays information about the bug check and can be very helpful in determining the root cause, then enter one of the [**k (Display Stack Backtrace)**](https://docs.microsoft.com/windows-hardware/drivers/debugger/k--kb--kc--kd--kp--kp--kv--display-stack-backtrace-) commands to view the call stack.

**Gather Information**

Examine the name of the driver if that was listed on the blue screen.

Check the System Log in Event Viewer for additional error messages that might help pinpoint the device or driver that is causing the error. For more information, see [Open Event Viewer](https://windows.microsoft.com/windows/what-information-event-logs-event-viewer#1TC=windows-7). Look for critical errors in the system log that occurred in the same time window as the blue screen.

**Driver Verifier**

Driver Verifier is a tool that runs in real time to examine the behavior of drivers. For example, Driver Verifier checks the use of memory resources, such as memory pools. If it sees errors in the execution of driver code, it proactively creates an exception to allow that part of the driver code to be further scrutinized. The driver verifier manager is built into Windows and is available on all Windows PCs. To start the driver verifier manager, type *Verifer* at a command prompt. You can configure which drivers you would like to verify. The code that verifies drivers adds overhead as it runs, so try and verify the smallest number of drivers as possible. For more information, see [Driver Verifier](https://msdn.microsoft.com/library/windows/hardware/ff545448).

Here is a debugging example:

```dbgcmd
kd> .bugcheck       [Lists bug check data.]
Bugcheck code 0000000a
Arguments 00000000 0000001c 00000000 00000000

kd> kb [Lists the stack trace.]
ChildEBP RetAddr  Args to Child
8013ed5c 801263ba 00000000 00000000 e12ab000 NT!_DbgBreakPoint
8013eecc 801389ee 0000000a 00000000 0000001c NT!_KeBugCheckEx+0x194
8013eecc 00000000 0000000a 00000000 0000001c NT!_KiTrap0E+0x256
8013ed5c 801263ba 00000000 00000000 e12ab000
8013ef64 00000246 fe551aa1 ff690268 00000002 NT!_KeBugCheckEx+0x194

kd> kv [Lists the trap frames.]
ChildEBP RetAddr  Args to Child
8013ed5c 801263ba 00000000 00000000 e12ab000 NT!_DbgBreakPoint (FPO: [0,0,0])
8013eecc 801389ee 0000000a 00000000 0000001c NT!_KeBugCheckEx+0x194
8013eecc 00000000 0000000a 00000000 0000001c NT!_KiTrap0E+0x256 (FPO: [0,0] TrapFrame @ 8013eee8)
8013ed5c 801263ba 00000000 00000000 e12ab000
8013ef64 00000246 fe551aa1 ff690268 00000002 NT!_KeBugCheckEx+0x194

kd> .trap 8013eee8 [Gets the registers for the trap frame at the time of the fault.]
eax=dec80201 ebx=ffdff420 ecx=8013c71c edx=000003f8 esi=00000000 edi=87038e10
eip=00000000 esp=8013ef5c ebp=8013ef64 iopl=0         nv up ei pl nz na pe nc
cs=0008  ss=0010  ds=0023  es=0023  fs=0030  gs=0000             efl=00010202
ErrCode = 00000000
00000000 ???????????????    [The current instruction pointer is NULL.]

kd> kb       [Gives the stack trace before the fault.]
ChildEBP RetAddr  Args to Child
8013ef68 fe551aa1 ff690268 00000002 fe5620d2 NT!_DbgBreakPoint
8013ef74 fe5620d2 fe5620da ff690268 80404690
NDIS!_EthFilterIndicateReceiveComplete+0x31
8013ef64 00000246 fe551aa1 ff690268 00000002 elnkii!_ElnkiiRcvInterruptDpc+0x1d0
```

Remarks
-------

The error that generates this bug check usually occurs after the installation of a faulty device driver, system service, or BIOS.

If you encounter bug check 0xA while upgrading to a later version of Windows, this error might be caused by a device driver, a system service, a virus scanner, or a backup tool that is incompatible with the new version.

**Resolving a faulty hardware problem:** If hardware has been added to the system recently, remove it to see if the error recurs. If existing hardware has failed, remove or replace the faulty component. You should run hardware diagnostics supplied by the system manufacturer. For details on these procedures, see the owner's manual for your computer.

**Resolving a faulty system service problem:** Disable the service and confirm that this resolves the error. If so, contact the manufacturer of the system service about a possible update. If the error occurs during system startup, investigate the Windows repair options. For more information, see [Recovery options in Windows 10](https://windows.microsoft.com/windows-10/windows-10-recovery-options).

**Resolving an antivirus software problem:** Disable the program and confirm that this resolves the error. If it does, contact the manufacturer of the program about a possible update.

For general blue screen troubleshooting information, see [**Blue Screen Data**](blue-screen-data.md).

 

 




