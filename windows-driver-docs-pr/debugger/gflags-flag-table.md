---
title: GFlags Flag Table
description: GFlags Flag Table
ms.assetid: 09029471-8b29-4232-bee1-d2802035b0fb
keywords: ["GFlags, flag table"]
ms.author: domars
ms.date: 05/23/2017
ms.localizationpriority: medium
---

# GFlags Flag Table


## <span id="ddk_gflags_flag_table_dtools"></span><span id="DDK_GFLAGS_FLAG_TABLE_DTOOLS"></span>


The following table lists the flags that GFlags changes, the hexadecimal value and abbreviation for each flag, and the destination (R for registry, K for kernel, I for image file) in which the flag is valid.

For a detailed description of each flag, see the [Global Flag Reference](global-flag-reference.md).

For information about using GFlags, see [GFlags Overview](gflags-overview.md) and [GFlags Details](gflags-details.md).

**Important**   Pool tagging is permanently enabled in Windows Server 2003 and later versions of Windows. On these systems, the **Enable pool tagging** check box on the **Global Flags** dialog box is dimmed, and commands to enable or disable pool tagging fail.

 

**Note**  The symbolic name of each flag is provided for reference only. Because symbolic names change, they are not a reliable identifier of a global flag.

 

<table>
<colgroup>
<col width="20%" />
<col width="20%" />
<col width="20%" />
<col width="20%" />
<col width="20%" />
</colgroup>
<thead>
<tr class="header">
<th align="left">Description</th>
<th align="left">Symbolic Name</th>
<th align="left">Hexadecimal Value</th>
<th align="left">Abbreviation</th>
<th align="left">Destination</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td align="left"><p><a href="buffer-dbgprint-output.md" data-raw-source="[Buffer DbgPrint Output](buffer-dbgprint-output.md)">Buffer DbgPrint Output</a></p></td>
<td align="left"><p>FLG_DISABLE_DBGPRINT</p></td>
<td align="left"><p>0x08000000</p></td>
<td align="left"><p>ddp</p></td>
<td align="left"><p>R,K</p></td>
</tr>
<tr class="even">
<td align="left"><p><a href="create-kernel-mode-stack-trace-database.md" data-raw-source="[Create kernel mode stack trace database](create-kernel-mode-stack-trace-database.md)">Create kernel mode stack trace database</a></p></td>
<td align="left"><p>FLG_KERNEL_STACK_TRACE_DB</p></td>
<td align="left"><p>0x2000</p></td>
<td align="left"><p>kst</p></td>
<td align="left"><p>R</p></td>
</tr>
<tr class="odd">
<td align="left"><p><a href="create-user-mode-stack-trace-database.md" data-raw-source="[Create user mode stack trace database](create-user-mode-stack-trace-database.md)">Create user mode stack trace database</a></p></td>
<td align="left"><p>FLG_USER_STACK_TRACE_DB</p></td>
<td align="left"><p>0x1000</p></td>
<td align="left"><p>ust</p></td>
<td align="left"><p>R,K,I</p></td>
</tr>
<tr class="even">
<td align="left"><p><a href="debug-initial-command.md" data-raw-source="[Debug initial command](debug-initial-command.md)">Debug initial command</a></p></td>
<td align="left"><p>FLG_DEBUG_INITIAL_COMMAND</p></td>
<td align="left"><p>0x04</p></td>
<td align="left"><p>dic</p></td>
<td align="left"><p>R</p></td>
</tr>
<tr class="odd">
<td align="left"><p><a href="debug-winlogon.md" data-raw-source="[Debug WinLogon](debug-winlogon.md)">Debug WinLogon</a></p></td>
<td align="left"><p>FLG_DEBUG_INITIAL_COMMAND_EX</p></td>
<td align="left"><p>0x04000000</p></td>
<td align="left"><p>dwl</p></td>
<td align="left"><p>R</p></td>
</tr>
<tr class="even">
<td align="left"><p><a href="disable-heap-coalesce-on-free.md" data-raw-source="[Disable heap coalesce on free](disable-heap-coalesce-on-free.md)">Disable heap coalesce on free</a></p></td>
<td align="left"><p>FLG_HEAP_DISABLE_COALESCING</p></td>
<td align="left"><p>0x00200000</p></td>
<td align="left"><p>dhc</p></td>
<td align="left"><p>R,K,I</p></td>
</tr>
<tr class="odd">
<td align="left"><p><a href="disable-paging-of-kernel-stacks.md" data-raw-source="[Disable paging of kernel stacks](disable-paging-of-kernel-stacks.md)">Disable paging of kernel stacks</a></p></td>
<td align="left"><p>FLG_DISABLE_PAGE_KERNEL_STACKS</p></td>
<td align="left"><p>0x080000</p></td>
<td align="left"><p>dps</p></td>
<td align="left"><p>R</p></td>
</tr>
<tr class="even">
<td align="left"><p><a href="disable-protected-dll-verification.md" data-raw-source="[Disable protected DLL verification](disable-protected-dll-verification.md)">Disable protected DLL verification</a></p></td>
<td align="left"><p>FLG_DISABLE_PROTDLLS</p></td>
<td align="left"><p>0x80000000</p></td>
<td align="left"><p>dpd</p></td>
<td align="left"><p>R,K,I</p></td>
</tr>
<tr class="odd">
<td align="left"><p><a href="disable-stack-extension.md" data-raw-source="[Disable stack extension](disable-stack-extension.md)">Disable stack extension</a></p></td>
<td align="left"><p>FLG_DISABLE_STACK_EXTENSION</p></td>
<td align="left"><p>0x010000</p></td>
<td align="left"><p>dse</p></td>
<td align="left"><p>I</p></td>
</tr>
<tr class="even">
<td align="left"><p><a href="early-critical-section-event-creation.md" data-raw-source="[Early critical section event creation](early-critical-section-event-creation.md)">Early critical section event creation</a></p></td>
<td align="left"><p>FLG_CRITSEC_EVENT_CREATION</p></td>
<td align="left"><p>0x10000000</p></td>
<td align="left"><p>cse</p></td>
<td align="left"><p>R,K,I</p></td>
</tr>
<tr class="odd">
<td align="left"><p><a href="enable-application-verifier.md" data-raw-source="[Enable application verifier](enable-application-verifier.md)">Enable application verifier</a></p></td>
<td align="left"><p>FLG_APPLICATION_VERIFIER</p></td>
<td align="left"><p>0x0100</p></td>
<td align="left"><p>vrf</p></td>
<td align="left"><p>R,K,I</p></td>
</tr>
<tr class="even">
<td align="left"><p><a href="enable-bad-handles-detection.md" data-raw-source="[Enable bad handles detection](enable-bad-handles-detection.md)">Enable bad handles detection</a></p></td>
<td align="left"><p>FLG_ENABLE_HANDLE_EXCEPTIONS</p></td>
<td align="left"><p>0x40000000</p></td>
<td align="left"><p>bhd</p></td>
<td align="left"><p>R,K</p></td>
</tr>
<tr class="odd">
<td align="left"><p><a href="enable-close-exception.md" data-raw-source="[Enable close exception](enable-close-exception.md)">Enable close exception</a></p></td>
<td align="left"><p>FLG_ENABLE_CLOSE_EXCEPTIONS</p></td>
<td align="left"><p>0x400000</p></td>
<td align="left"><p>ece</p></td>
<td align="left"><p>R,K</p></td>
</tr>
<tr class="even">
<td align="left"><p><a href="enable-debugging-of-win32-subsystem.md" data-raw-source="[Enable debugging of Win32 subsystem](enable-debugging-of-win32-subsystem.md)">Enable debugging of Win32 subsystem</a></p></td>
<td align="left"><p>FLG_ENABLE_CSRDEBUG</p></td>
<td align="left"><p>0x020000</p></td>
<td align="left"><p>d32</p></td>
<td align="left"><p>R</p></td>
</tr>
<tr class="odd">
<td align="left"><p><a href="enable-exception-logging.md" data-raw-source="[Enable exception logging](enable-exception-logging.md)">Enable exception logging</a></p></td>
<td align="left"><p>FLG_ENABLE_EXCEPTION_LOGGING</p></td>
<td align="left"><p>0x800000</p></td>
<td align="left"><p>eel</p></td>
<td align="left"><p>R,K</p></td>
</tr>
<tr class="even">
<td align="left"><p><a href="enable-heap-free-checking.md" data-raw-source="[Enable heap free checking](enable-heap-free-checking.md)">Enable heap free checking</a></p></td>
<td align="left"><p>FLG_HEAP_ENABLE_FREE_CHECK</p></td>
<td align="left"><p>0x20</p></td>
<td align="left"><p>hfc</p></td>
<td align="left"><p>R,K,I</p></td>
</tr>
<tr class="odd">
<td align="left"><p><a href="enable-heap-parameter-checking.md" data-raw-source="[Enable heap parameter checking](enable-heap-parameter-checking.md)">Enable heap parameter checking</a></p></td>
<td align="left"><p>FLG_HEAP_VALIDATE_PARAMETERS</p></td>
<td align="left"><p>0x40</p></td>
<td align="left"><p>hpc</p></td>
<td align="left"><p>R,K,I</p></td>
</tr>
<tr class="even">
<td align="left"><p><a href="enable-heap-tagging.md" data-raw-source="[Enable heap tagging](enable-heap-tagging.md)">Enable heap tagging</a></p></td>
<td align="left"><p>FLG_HEAP_ENABLE_TAGGING</p></td>
<td align="left"><p>0x0800</p></td>
<td align="left"><p>htg</p></td>
<td align="left"><p>R,K,I</p></td>
</tr>
<tr class="odd">
<td align="left"><p><a href="enable-heap-tagging-by-dll.md" data-raw-source="[Enable heap tagging by DLL](enable-heap-tagging-by-dll.md)">Enable heap tagging by DLL</a></p></td>
<td align="left"><p>FLG_HEAP_ENABLE_TAG_BY_DLL</p></td>
<td align="left"><p>0x8000</p></td>
<td align="left"><p>htd</p></td>
<td align="left"><p>R,K,I</p></td>
</tr>
<tr class="even">
<td align="left"><p><a href="enable-heap-tail-checking.md" data-raw-source="[Enable heap tail checking](enable-heap-tail-checking.md)">Enable heap tail checking</a></p></td>
<td align="left"><p>FLG_HEAP_ENABLE_TAIL_CHECK</p></td>
<td align="left"><p>0x10</p></td>
<td align="left"><p>htc</p></td>
<td align="left"><p>R,K,I</p></td>
</tr>
<tr class="odd">
<td align="left"><p><a href="enable-heap-validation-on-call.md" data-raw-source="[Enable heap validation on call](enable-heap-validation-on-call.md)">Enable heap validation on call</a></p></td>
<td align="left"><p>FLG_HEAP_VALIDATE_ALL</p></td>
<td align="left"><p>0x80</p></td>
<td align="left"><p>hvc</p></td>
<td align="left"><p>R,K,I</p></td>
</tr>
<tr class="even">
<td align="left"><p><a href="enable-loading-of-kernel-debugger-symbols.md" data-raw-source="[Enable loading of kernel debugger symbols](enable-loading-of-kernel-debugger-symbols.md)">Enable loading of kernel debugger symbols</a></p></td>
<td align="left"><p>FLG_ENABLE_KDEBUG_SYMBOL_LOAD</p></td>
<td align="left"><p>0x040000</p></td>
<td align="left"><p>ksl</p></td>
<td align="left"><p>R,K</p></td>
</tr>
<tr class="odd">
<td align="left"><p><a href="enable-object-handle-type-tagging.md" data-raw-source="[Enable object handle type tagging](enable-object-handle-type-tagging.md)">Enable object handle type tagging</a></p></td>
<td align="left"><p>FLG_ENABLE_HANDLE_TYPE_TAGGING</p></td>
<td align="left"><p>0x01000000</p></td>
<td align="left"><p>eot</p></td>
<td align="left"><p>R,K</p></td>
</tr>
<tr class="even">
<td align="left"><p><a href="enable-page-heap.md" data-raw-source="[Enable page heap](enable-page-heap.md)">Enable page heap</a></p></td>
<td align="left"><p>FLG_HEAP_PAGE_ALLOCS</p></td>
<td align="left"><p>0x02000000</p></td>
<td align="left"><p>hpa</p></td>
<td align="left"><p>R,K,I</p></td>
</tr>
<tr class="odd">
<td align="left"><p></p>
<a href="enable-pool-tagging.md" data-raw-source="[Enable pool tagging](enable-pool-tagging.md)">Enable pool tagging</a>
(Windows 2000 and Windows XP only)</td>
<td align="left"><p>FLG_POOL_ENABLE_TAGGING</p></td>
<td align="left"><p>0x0400</p></td>
<td align="left"><p>ptg</p></td>
<td align="left"><p>R</p></td>
</tr>
<tr class="even">
<td align="left"><p><a href="enable-system-critical-breaks.md" data-raw-source="[Enable system critical breaks](enable-system-critical-breaks.md)">Enable system critical breaks</a></p></td>
<td align="left"><p>FLG_ENABLE_SYSTEM_CRIT_BREAKS</p></td>
<td align="left"><p>0x100000</p></td>
<td align="left"><p>scb</p></td>
<td align="left"><p>R, K, I</p></td>
</tr>
<tr class="odd">
<td align="left"><p><a href="load-image-using-large-pages-if-possible.md" data-raw-source="[Load image using large pages if possible](load-image-using-large-pages-if-possible.md)">Load image using large pages if possible</a></p></td>
<td align="left"></td>
<td align="left"></td>
<td align="left"><p>lpg</p></td>
<td align="left"><p>I</p></td>
</tr>
<tr class="even">
<td align="left"><p><a href="maintain-a-list-of-objects-for-each-type.md" data-raw-source="[Maintain a list of objects for each type](maintain-a-list-of-objects-for-each-type.md)">Maintain a list of objects for each type</a></p></td>
<td align="left"><p>FLG_MAINTAIN_OBJECT_TYPELIST</p></td>
<td align="left"><p>0x4000</p></td>
<td align="left"><p>otl</p></td>
<td align="left"><p>R</p></td>
</tr>
<tr class="odd">
<td align="left"><p><a href="enable-silent-process-exit-monitoring.md" data-raw-source="[Enable silent process exit monitoring](enable-silent-process-exit-monitoring.md)">Enable silent process exit monitoring</a></p></td>
<td align="left"><p>FLG_MONITOR_SILENT_PROCESS_EXIT</p></td>
<td align="left"><p>0x200</p></td>
<td align="left"></td>
<td align="left"><p>R</p></td>
</tr>
<tr class="even">
<td align="left"><p><a href="object-reference-tracing.md" data-raw-source="[Object Reference Tracing](object-reference-tracing.md)">Object Reference Tracing</a></p>
<p>(Windows Vista and later)</p></td>
<td align="left"></td>
<td align="left"></td>
<td align="left"></td>
<td align="left"><p>R, K</p></td>
</tr>
<tr class="odd">
<td align="left"><p><a href="show-loader-snaps.md" data-raw-source="[Show loader snaps](show-loader-snaps.md)">Show loader snaps</a></p></td>
<td align="left"><p>FLG_SHOW_LDR_SNAPS</p></td>
<td align="left"><p>0x02</p></td>
<td align="left"><p>sls</p></td>
<td align="left"><p>R,K,I</p></td>
</tr>
<tr class="even">
<td align="left"><p><a href="special-pool.md" data-raw-source="[Special Pool](special-pool.md)">Special Pool</a></p></td>
<td align="left"></td>
<td align="left"></td>
<td align="left"><p>spp</p></td>
<td align="left"><p>R</p>
<p>R,K (Windows Vista and later)</p></td>
</tr>
<tr class="odd">
<td align="left"><p><a href="stop-on-exception.md" data-raw-source="[Stop on exception](stop-on-exception.md)">Stop on exception</a></p></td>
<td align="left"><p>FLG_STOP_ON_EXCEPTION</p></td>
<td align="left"><p>0x01</p></td>
<td align="left"><p>soe</p></td>
<td align="left"><p>R,K,I</p></td>
</tr>
<tr class="even">
<td align="left"><p><a href="stop-on-hung-gui.md" data-raw-source="[Stop on hung GUI](stop-on-hung-gui.md)">Stop on hung GUI</a></p></td>
<td align="left"><p>FLG_STOP_ON_HUNG_GUI</p></td>
<td align="left"><p>0x08</p></td>
<td align="left"><p>shg</p></td>
<td align="left"><p>K</p></td>
</tr>
<tr class="odd">
<td align="left"><p><a href="stop-on-unhandled-user-mode-exception.md" data-raw-source="[Stop on unhandled user-mode exception](stop-on-unhandled-user-mode-exception.md)">Stop on unhandled user-mode exception</a></p></td>
<td align="left"><p>FLG_STOP_ON_UNHANDLED_EXCEPTION</p></td>
<td align="left"><p>0x20000000</p></td>
<td align="left"><p>sue</p></td>
<td align="left"><p>R,K,I</p></td>
</tr>
</tbody>
</table>

 

 

 





