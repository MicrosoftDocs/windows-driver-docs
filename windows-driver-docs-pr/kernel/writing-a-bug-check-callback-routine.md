---
title: Writing a Bug Check Callback Routine
description: Writing a Bug Check Callback Routine
ms.assetid: 62aefe67-e197-4c45-b994-19bd7369dbc1
keywords: ["bug check callback routines WDK kernel", "callback routines WDK bug checks", "registering callback routines", "KeRegisterBugCheckCallback", "BugCheckCallback"]
ms.date: 05/02/2019
ms.localizationpriority: medium
---

# Writing a Bug Check Reason Callback Routine

Drivers can register callback routines that the system executes when it issues a bug check. Drivers can use a bug check callback routine to reset their device to a known state.

In Windows the system calls the [*KBUGCHECK_REASON_CALLBACK_ROUTINE*](https://docs.microsoft.com/windows-hardware/drivers/ddi/content/wdm/nc-wdm-kbugcheck_reason_callback_routine) callback function after the crash dump file is written.

The KBUGCHECK_REASON_CALLBACK_ROUTINE can be used to write secondary data to the crash dump file.
 
A driver can implement a KBUGCHECK_REASON_CALLBACK_ROUTINE to add pages of driver-specific data to the crash dump file. Drivers use the [**KeRegisterBugCheckReasonCallback**](https://docs.microsoft.com/windows-hardware/drivers/ddi/content/wdm/nf-wdm-keregisterbugcheckcallback) and [**KeDeregisterBugCheckReasonCallback**](https://docs.microsoft.com/windows-hardware/drivers/ddi/content/wdm/nf-wdm-kederegisterbugcheckcallback) routines to register these three types of *BugCheckXxxCallback* callback routines.

The [*KBUGCHECK_CALLBACK_REASON enumeration*](https://docs.microsoft.com/windows-hardware/drivers/ddi/content/wdm/ne-wdm-_kbugcheck_callback_reason) specifies the types of call back routines.

The following types of callbacks are commonly used.

**KbCallbackAddPages** - The callback is executed to provide one or more pages of data that the system adds to the primary section of the crash dump file. The [*KBUGCHECK_ADD_PAGES structure*](https://docs.microsoft.com/windows-hardware/drivers/ddi/content/wdm/ns-wdm-_kbugcheck_add_pages) describes one or more pages of driver-supplied data to be written by a KbCallbackAddPages callback routine to the crash dump file. For more information about this type of callback, see "Implementing KbCallbackAddPages Callback Routine" in this topic.

**KbCallbackDumpIo** - The callback is executed each time a section of the dump file is written. The [KBUGCHECK_DUMP_IO structure](https://docs.microsoft.com/windows-hardware/drivers/ddi/content/wdm/ns-wdm-_kbugcheck_dump_io) is used to describe an I/O operation on the crash dump file. For more information about this type of callback, see "Implementing KbCallbackDumpIo Callback Routine" in this topic.

**KbCallbackSecondaryDumpData** - The callback is executed each time a section of the dump file is written. 
The [KBUGCHECK_SECONDARY_DUMP_DATA structure](https://docs.microsoft.com/windows-hardware/drivers/ddi/content/wdm/ns-wdm-_kbugcheck_secondary_dump_data) structure describes a section of driver-supplied data to be written to the crash dump file. For more information about this type of callback, see "Implementing KbCallbackSecondaryDumpData Callback Routine" in this topic.

For general information about bug check data, see [Reading Bug Check Callback Data](https://docs.microsoft.com/windows-hardware/drivers/debugger/reading-bug-check-callback-data).


## Bug Check Callback Routine Restrictions

A bug check callback routine executes at IRQL = HIGH\_LEVEL, which imposes strong restrictions on what it can do.

A bug check callback routine cannot:

- Allocate memory

- Access pageable memory

- Use any synchronization mechanisms

- Call any routine that must execute at IRQL = DISPATCH\_LEVEL or below

Bug check callback routines are guaranteed to run without interruption, so no synchronization is required. (If the bug check routine does use any synchronization mechanisms, the system will deadlock.)

A driver's bug check callback routine can safely use the <strong>READ\_PORT\_*XXX</strong><em>, **READ\_REGISTER\_</em>XXX<strong><em>, *</em>WRITE\_PORT\_*XXX</strong><em>, and **WRITE\_REGISTER\_</em>XXX*** routines to communicate with the driver's device. (For information about these routines, see [Hardware Abstraction Layer Routines](https://msdn.microsoft.com/library/windows/hardware/ff546644).)

## Using BugCheckCallback

Prior to Windows XP Service Pack 1 (SP1) and Windows Server 2003, drivers could also use BugCheckCallback to store data in the crash dump file: the system called each BugCheckCallback routine before writing the crash dump file, so any data written to the buffer that was passed to BugCheckCallback was stored in the crash dump file.

For more information, see [*KBUGCHECK_CALLBACK_ROUTINE callback function*](https://docs.microsoft.com/windows-hardware/drivers/ddi/content/wdm/nc-wdm-kbugcheck_callback_routine).


## Implementing KbCallbackAddPages Callback Routine

A kernel-mode driver can implement a <i>KbCallbackAddPages</i> callback routine to add one or more pages of data to a crash dump file when a bug check occurs. To register this routine with the operating system, the driver calls the <a href="https://msdn.microsoft.com/library/windows/hardware/ff553110">KeRegisterBugCheckReasonCallback</a> routine. Before the driver unloads, it must call the <a href="https://msdn.microsoft.com/library/windows/hardware/ff552003">KeDeregisterBugCheckReasonCallback</a> routine to remove the registration.

Starting with Windows 8, a registered <i>KbCallbackAddPages</i> routine is called during a <a href="https://msdn.microsoft.com/library/windows/hardware/ff551867">kernel memory dump</a> or a <a href="https://msdn.microsoft.com/library/windows/hardware/ff539190">complete memory dump</a>. In earlier versions of Windows, a registered <i>KbCallbackAddPages</i> routine is called during a kernel memory dump, but not during a complete memory dump. By default, a kernel memory dump includes only the physical pages that are being used by the Windows kernel at the time that the bug check occurs, whereas a complete memory dump includes all of the physical memory that is used by Windows. A complete memory dump does not, by default, include physical memory that is used by the platform firmware.

Your <i>KbCallbackAddPages</i> routine can supply driver-specific data to add to the dump file. For example, for a kernel memory dump, this additional data can include physical pages that are not mapped to the system address range in virtual memory but that contain information that can help you to debug your driver. The <i>KbCallbackAddPages</i> routine might add to the dump file any driver-owned physical pages that are unmapped or that are mapped to user-mode addresses in virtual memory.

When a bug check occurs, the operating system calls all the registered <i>KbCallbackAddPages</i> routines to poll drivers for data to add to the crash dump file. Each call adds one or more pages of contiguous data to the crash dump file. A <i>KbCallbackAddPages</i> routine can supply either a virtual address or a physical address for the starting page. If more than one page is supplied during a call, the pages are contiguous in either virtual or physical memory, depending on whether the starting address is virtual or physical. To supply noncontiguous pages, the <i>KbCallbackAddPages</i> routine can set a flag in the <b>KBUGCHECK_ADD_PAGES</b> structure to indicate that it has additional data and has to be called again. For more information, see <a href="https://msdn.microsoft.com/library/windows/hardware/ff551839">KBUGCHECK_ADD_PAGES</a>.

Unlike a KbCallbackSecondaryDumpData routine, which appends data to the secondary crash dump region, a <i>KbCallbackAddPages</i> routine adds pages of data to the primary crash dump region. During debugging, primary crash dump data is easier to access than secondary crash dump data.

Before the operating system calls a <i>KbCallbackAddPages</i> routine, it fills in the <b>BugCheckCode</b> member of the <b>KBUGCHECK_ADD_PAGES</b> structure that <i>ReasonSpecificData</i> points to. During the call, the <i>KbCallbackAddPages</i> routine must set the values of the <b>Flags</b>, <b>Address</b>, and <b>Count</b> members of this structure. If the <i>KbCallbackAddPages</i> routine is called more than one time, the operating system preserves the value that the callback routine wrote to the <b>Context</b> member in the previous call. Before the first call, the operating system initializes <b>Context</b> to <b>NULL</b>.

A <i>KbCallbackAddPages</i> routine is very restricted in the actions it can take. For more information, see "Bug Check Callback Routine Restrictions" in this topic.

## Implementing a KbCallbackDumpIo callback routine

The driver's <i>KbCallbackDumpIo</i> callback routine is called each time data is written to the crash dump file. The system passes, in the <i>ReasonSpecificData</i> parameter, a description of the data being written. The <b>Buffer</b> member points to the current data, and the <b>BufferLength</b> member specifies its length. The <b>Type</b> member indicates the type of data currently being written, such as dump file header information, memory state, or data provided by a driver. For a description of the possible types of information, see <a href="https://msdn.microsoft.com/library/windows/hardware/ff551871">KBUGCHECK_DUMP_IO_TYPE</a>.

The system can write the crash dump file either sequentially, or out of order. If the system is writing the crash dump file sequentially, then the <b>Offset</b> member of <i>ReasonSpecificData</i> is -1; otherwise, <b>Offset</b> is set to the current offset, in bytes, in the crash dump file.

When the system writes the file sequentially, it calls each <i>KbCallbackDumpIo</i> routine one or more times when writing the header information (<b>Type</b> = <b>KbDumpIoHeader</b>), one or more times when writing the main body of the crash dump file (<b>Type</b> = <b>KbDumpIoBody</b>), and one or more times when writing the secondary dump data (<b>Type</b> = <b>KbDumpIoSecondaryDumpData</b>). Once the system has completed writing the crash dump file, it calls the callback with <b>Buffer</b> = <b>NULL</b>, <b>BufferLength</b> = 0, and <b>Type</b> = <b>KbDumpIoComplete</b>.

The main purpose of a <i>KbCallbackDumpIo</i> routine is to allow system crash dump data to be written to devices other than the disk. For example, a device that monitors system state can use the callback to report that the system has issued a bug check, and to provide a crash dump for analysis.

Use <a href="https://msdn.microsoft.com/library/windows/hardware/ff553110">KeRegisterBugCheckReasonCallback</a> to register a <i>KbCallbackDumpIo</i> routine. A driver can subsequently remove the callback by using the <a href="https://msdn.microsoft.com/library/windows/hardware/ff552003">KeDeregisterBugCheckReasonCallback</a> routine. If the driver can be unloaded, it must remove any registered callbacks in its <a href="https://msdn.microsoft.com/library/windows/hardware/ff564886">Unload</a> routine.

A <i>KbCallbackDumpIo</i> routine is strongly restricted in the actions it can take. For more information, see "Bug Check Callback Routine Restrictions" in this topic.

## Implementing KbCallbackSecondaryDumpData

The system uses <i>KbCallbackSecondaryDumpData</i> routines to poll drivers for crash dump data.

The system sets the <b>InBuffer</b>, <b>InBufferLength</b>, <b>OutBuffer</b>, and <b>MaximumAllowed</b> members of the <a href="https://msdn.microsoft.com/library/windows/hardware/ff551879">KBUGCHECK_SECONDARY_DUMP_DATA</a> structure that <i>ReasonSpecificData</i> points to. The <b>MaximumAllowed</b> member specifies the maximum amount of dump data the routine can provide.

The value of the <b>OutBuffer</b> member determines whether the system is requesting the size of the driver's dump data, or the data itself, as follows:

<ul>
<li>
If the <b>OutBuffer</b> member of KBUGCHECK_SECONDARY_DUMP_DATA is <b>NULL</b>, the system is only requesting size information. The <i>KbCallbackSecondaryDumpData</i> routine fills in the <b>OutBuffer</b> and <b>OutBufferLength</b> members. 
</li>

<li>
If the <b>OutBuffer</b> member of KBUGCHECK_SECONDARY_DUMP_DATA equals the <b>InBuffer</b> member, the system is requesting the driver's secondary dump data. The <i>KbCallbackSecondaryDumpData</i> routine fills in the <b>OutBuffer</b> and <b>OutBufferLength</b> members, and writes the data to the buffer specified by <b>OutBuffer</b>.
</li>
</ul>

The <b>InBuffer</b> member of KBUGCHECK_SECONDARY_DUMP_DATA points  to a small buffer for the routine's use. The <b>InBufferLength</b> member specifies the size of the buffer. If the amount of data to be written is less than <b>InBufferLength</b>, the callback routine can use this buffer to supply the crash dump data to the system. The callback routine then sets <b>OutBuffer</b> to <b>InBuffer</b> and <b>OutBufferLength</b> to the actual amount of data written to the buffer.

A driver that must write an amount of data that is larger than <b>InBufferLength</b> can use its own buffer to provide the data. This buffer must have been allocated before the callback routine is executed, and must reside in resident memory (such as nonpaged pool). The callback routine then sets <b>OutBuffer</b> to point to the driver's buffer, and <b>OutBufferLength</b> to the amount of data in the buffer to be written to the crash dump file.

In Windows XP and Windows Server 2003, if <b>OutBuffer</b> is set to point to a driver-allocated buffer, the buffer must begin on a page-aligned boundary in memory. Otherwise, no data is written to the secondary data area of the crash dump file. In Windows Vista and later versions of Windows, there is no such alignment requirement.

Each block of data to be written to the crash dump file is tagged with the value of the <b>Guid</b> member of <a href="https://msdn.microsoft.com/library/windows/hardware/ff551879">KBUGCHECK_SECONDARY_DUMP_DATA</a>. The GUID used must be unique to the driver. To display the secondary dump data corresponding to this GUID, you can use the <b>.enumtag</b> command or the <b>IDebugDataSpaces3::ReadTagged</b> method in a debugger extension. For information about debuggers and debugger extensions, see <a href="https://msdn.microsoft.com/938ef180-84de-442f-9b6c-1138c2fc8d5a">Windows Debugging</a>.

A driver can write multiple blocks with the same GUID to the crash dump file, but this is very poor practice, because only the first block will be accessible to the debugger. Drivers that register multiple <i>KbCallbackSecondaryDumpData</i> routines should allocate a unique GUID for each callback.

Use <a href="https://msdn.microsoft.com/library/windows/hardware/ff553110">KeRegisterBugCheckReasonCallback</a> to register a <i>KbCallbackSecondaryDumpData</i> routine. A driver can subsequently remove the callback routine by using the <a href="https://msdn.microsoft.com/library/windows/hardware/ff552003">KeDeregisterBugCheckReasonCallback</a> routine. If the driver can be unloaded, then it must remove any registered callback routines in its <a href="https://msdn.microsoft.com/library/windows/hardware/ff564886">Unload</a> routine.

A <i>KbCallbackSecondaryDumpData</i> routine is very restricted in the actions it can take. For more information, see "Bug Check Callback Routine Restrictions" in this topic.


#### Callback Routine Examples

To define the callback routine, you must first provide a function declaration that identifies the type of callback routine you're defining. Windows provides a set of callback function types for drivers. Declaring a function using the callback function types helps <a href="https://msdn.microsoft.com/2F3549EF-B50F-455A-BDC7-1F67782B8DCA">Code Analysis for Drivers</a>, <a href="https://msdn.microsoft.com/74feeb16-387c-4796-987a-aff3fb79b556">Static Driver Verifier</a> (SDV), and other verification tools find errors, and it's a requirement for writing drivers for the Windows operating system.

For example, to define a <i>KbCallbackAddPages</i> callback routine that is named <code>MyKbCallbackAddPages</code>, use the KBUGCHECK_REASON_CALLBACK_ROUTINE type as shown in this code example:

<div class="code"><span codelanguage=""><table>
<tr>
<th></th>
</tr>
<tr>
<td>
<pre>KBUGCHECK_REASON_CALLBACK_ROUTINE MyBugCheckAddPagesCallback;</pre>
</td>
</tr>
</table></span></div>
Then, implement your callback routine as follows:

<div class="code"><span codelanguage=""><table>
<tr>
<th></th>
</tr>
<tr>
<td>
<pre>_Use_decl_annotations_
VOID
  MyBugCheckAddPagesCallback(
    KBUGCHECK_CALLBACK_REASON  Reason,
    struct _KBUGCHECK_REASON_CALLBACK_RECORD  *Record,
    PVOID  ReasonSpecificData,
    ULONG  ReasonSpecificDataLength 
    )
  {
      // Function body
  }</pre>
</td>
</tr>
</table></span></div>
The KBUGCHECK_REASON_CALLBACK_ROUTINE function type is defined in the Wdm.h header file. To more accurately identify errors when you run the code analysis tools, be sure to add the _Use_decl_annotations_ annotation to your function definition. The _Use_decl_annotations_ annotation ensures that the annotations that are applied to the KBUGCHECK_REASON_CALLBACK_ROUTINE function type in the header file are used. For more information about the requirements for function declarations, see <a href="https://msdn.microsoft.com/3260b53e-82be-4dbc-8ac5-d0e52de77f9d">Declaring Functions by Using Function Role Types for WDM Drivers</a>. For information about _Use_decl_annotations_, see <a href="https://go.microsoft.com/fwlink/p/?linkid=286697">Annotating Function Behavior</a>.

<div class="code"></div>


