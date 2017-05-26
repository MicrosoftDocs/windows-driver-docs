---
title: GFlags Flag Table
description: GFlags Flag Table
ms.assetid: 09029471-8b29-4232-bee1-d2802035b0fb
keywords: ["GFlags, flag table"]
ms.author: windowsdriverdev
ms.date: 05/23/2017
ms.topic: article
ms.prod: windows-hardware
ms.technology: windows-devices
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
<td align="left"><p>[Buffer DbgPrint Output](buffer-dbgprint-output.md)</p></td>
<td align="left"><p>FLG_DISABLE_DBGPRINT</p></td>
<td align="left"><p>0x08000000</p></td>
<td align="left"><p>ddp</p></td>
<td align="left"><p>R,K</p></td>
</tr>
<tr class="even">
<td align="left"><p>[Create kernel mode stack trace database](create-kernel-mode-stack-trace-database.md)</p></td>
<td align="left"><p>FLG_KERNEL_STACK_TRACE_DB</p></td>
<td align="left"><p>0x2000</p></td>
<td align="left"><p>kst</p></td>
<td align="left"><p>R</p></td>
</tr>
<tr class="odd">
<td align="left"><p>[Create user mode stack trace database](create-user-mode-stack-trace-database.md)</p></td>
<td align="left"><p>FLG_USER_STACK_TRACE_DB</p></td>
<td align="left"><p>0x1000</p></td>
<td align="left"><p>ust</p></td>
<td align="left"><p>R,K,I</p></td>
</tr>
<tr class="even">
<td align="left"><p>[Debug initial command](debug-initial-command.md)</p></td>
<td align="left"><p>FLG_DEBUG_INITIAL_COMMAND</p></td>
<td align="left"><p>0x04</p></td>
<td align="left"><p>dic</p></td>
<td align="left"><p>R</p></td>
</tr>
<tr class="odd">
<td align="left"><p>[Debug WinLogon](debug-winlogon.md)</p></td>
<td align="left"><p>FLG_DEBUG_INITIAL_COMMAND_EX</p></td>
<td align="left"><p>0x04000000</p></td>
<td align="left"><p>dwl</p></td>
<td align="left"><p>R</p></td>
</tr>
<tr class="even">
<td align="left"><p>[Disable heap coalesce on free](disable-heap-coalesce-on-free.md)</p></td>
<td align="left"><p>FLG_HEAP_DISABLE_COALESCING</p></td>
<td align="left"><p>0x00200000</p></td>
<td align="left"><p>dhc</p></td>
<td align="left"><p>R,K,I</p></td>
</tr>
<tr class="odd">
<td align="left"><p>[Disable paging of kernel stacks](disable-paging-of-kernel-stacks.md)</p></td>
<td align="left"><p>FLG_DISABLE_PAGE_KERNEL_STACKS</p></td>
<td align="left"><p>0x080000</p></td>
<td align="left"><p>dps</p></td>
<td align="left"><p>R</p></td>
</tr>
<tr class="even">
<td align="left"><p>[Disable protected DLL verification](disable-protected-dll-verification.md)</p></td>
<td align="left"><p>FLG_DISABLE_PROTDLLS</p></td>
<td align="left"><p>0x80000000</p></td>
<td align="left"><p>dpd</p></td>
<td align="left"><p>R,K,I</p></td>
</tr>
<tr class="odd">
<td align="left"><p>[Disable stack extension](disable-stack-extension.md)</p></td>
<td align="left"><p>FLG_DISABLE_STACK_EXTENSION</p></td>
<td align="left"><p>0x010000</p></td>
<td align="left"><p>dse</p></td>
<td align="left"><p>I</p></td>
</tr>
<tr class="even">
<td align="left"><p>[Early critical section event creation](early-critical-section-event-creation.md)</p></td>
<td align="left"><p>FLG_CRITSEC_EVENT_CREATION</p></td>
<td align="left"><p>0x10000000</p></td>
<td align="left"><p>cse</p></td>
<td align="left"><p>R,K,I</p></td>
</tr>
<tr class="odd">
<td align="left"><p>[Enable application verifier](enable-application-verifier.md)</p></td>
<td align="left"><p>FLG_APPLICATION_VERIFIER</p></td>
<td align="left"><p>0x0100</p></td>
<td align="left"><p>vrf</p></td>
<td align="left"><p>R,K,I</p></td>
</tr>
<tr class="even">
<td align="left"><p>[Enable bad handles detection](enable-bad-handles-detection.md)</p></td>
<td align="left"><p>FLG_ENABLE_HANDLE_EXCEPTIONS</p></td>
<td align="left"><p>0x40000000</p></td>
<td align="left"><p>bhd</p></td>
<td align="left"><p>R,K</p></td>
</tr>
<tr class="odd">
<td align="left"><p>[Enable close exception](enable-close-exception.md)</p></td>
<td align="left"><p>FLG_ENABLE_CLOSE_EXCEPTIONS</p></td>
<td align="left"><p>0x400000</p></td>
<td align="left"><p>ece</p></td>
<td align="left"><p>R,K</p></td>
</tr>
<tr class="even">
<td align="left"><p>[Enable debugging of Win32 subsystem](enable-debugging-of-win32-subsystem.md)</p></td>
<td align="left"><p>FLG_ENABLE_CSRDEBUG</p></td>
<td align="left"><p>0x020000</p></td>
<td align="left"><p>d32</p></td>
<td align="left"><p>R</p></td>
</tr>
<tr class="odd">
<td align="left"><p>[Enable exception logging](enable-exception-logging.md)</p></td>
<td align="left"><p>FLG_ENABLE_EXCEPTION_LOGGING</p></td>
<td align="left"><p>0x800000</p></td>
<td align="left"><p>eel</p></td>
<td align="left"><p>R,K</p></td>
</tr>
<tr class="even">
<td align="left"><p>[Enable heap free checking](enable-heap-free-checking.md)</p></td>
<td align="left"><p>FLG_HEAP_ENABLE_FREE_CHECK</p></td>
<td align="left"><p>0x20</p></td>
<td align="left"><p>hfc</p></td>
<td align="left"><p>R,K,I</p></td>
</tr>
<tr class="odd">
<td align="left"><p>[Enable heap parameter checking](enable-heap-parameter-checking.md)</p></td>
<td align="left"><p>FLG_HEAP_VALIDATE_PARAMETERS</p></td>
<td align="left"><p>0x40</p></td>
<td align="left"><p>hpc</p></td>
<td align="left"><p>R,K,I</p></td>
</tr>
<tr class="even">
<td align="left"><p>[Enable heap tagging](enable-heap-tagging.md)</p></td>
<td align="left"><p>FLG_HEAP_ENABLE_TAGGING</p></td>
<td align="left"><p>0x0800</p></td>
<td align="left"><p>htg</p></td>
<td align="left"><p>R,K,I</p></td>
</tr>
<tr class="odd">
<td align="left"><p>[Enable heap tagging by DLL](enable-heap-tagging-by-dll.md)</p></td>
<td align="left"><p>FLG_HEAP_ENABLE_TAG_BY_DLL</p></td>
<td align="left"><p>0x8000</p></td>
<td align="left"><p>htd</p></td>
<td align="left"><p>R,K,I</p></td>
</tr>
<tr class="even">
<td align="left"><p>[Enable heap tail checking](enable-heap-tail-checking.md)</p></td>
<td align="left"><p>FLG_HEAP_ENABLE_TAIL_CHECK</p></td>
<td align="left"><p>0x10</p></td>
<td align="left"><p>htc</p></td>
<td align="left"><p>R,K,I</p></td>
</tr>
<tr class="odd">
<td align="left"><p>[Enable heap validation on call](enable-heap-validation-on-call.md)</p></td>
<td align="left"><p>FLG_HEAP_VALIDATE_ALL</p></td>
<td align="left"><p>0x80</p></td>
<td align="left"><p>hvc</p></td>
<td align="left"><p>R,K,I</p></td>
</tr>
<tr class="even">
<td align="left"><p>[Enable loading of kernel debugger symbols](enable-loading-of-kernel-debugger-symbols.md)</p></td>
<td align="left"><p>FLG_ENABLE_KDEBUG_SYMBOL_LOAD</p></td>
<td align="left"><p>0x040000</p></td>
<td align="left"><p>ksl</p></td>
<td align="left"><p>R,K</p></td>
</tr>
<tr class="odd">
<td align="left"><p>[Enable object handle type tagging](enable-object-handle-type-tagging.md)</p></td>
<td align="left"><p>FLG_ENABLE_HANDLE_TYPE_TAGGING</p></td>
<td align="left"><p>0x01000000</p></td>
<td align="left"><p>eot</p></td>
<td align="left"><p>R,K</p></td>
</tr>
<tr class="even">
<td align="left"><p>[Enable page heap](enable-page-heap.md)</p></td>
<td align="left"><p>FLG_HEAP_PAGE_ALLOCS</p></td>
<td align="left"><p>0x02000000</p></td>
<td align="left"><p>hpa</p></td>
<td align="left"><p>R,K,I</p></td>
</tr>
<tr class="odd">
<td align="left"><p></p>
[Enable pool tagging](enable-pool-tagging.md)
(Windows 2000 and Windows XP only)</td>
<td align="left"><p>FLG_POOL_ENABLE_TAGGING</p></td>
<td align="left"><p>0x0400</p></td>
<td align="left"><p>ptg</p></td>
<td align="left"><p>R</p></td>
</tr>
<tr class="even">
<td align="left"><p>[Enable system critical breaks](enable-system-critical-breaks.md)</p></td>
<td align="left"><p>FLG_ENABLE_SYSTEM_CRIT_BREAKS</p></td>
<td align="left"><p>0x100000</p></td>
<td align="left"><p>scb</p></td>
<td align="left"><p>R, K, I</p></td>
</tr>
<tr class="odd">
<td align="left"><p>[Load image using large pages if possible](load-image-using-large-pages-if-possible.md)</p></td>
<td align="left"></td>
<td align="left"></td>
<td align="left"><p>lpg</p></td>
<td align="left"><p>I</p></td>
</tr>
<tr class="even">
<td align="left"><p>[Maintain a list of objects for each type](maintain-a-list-of-objects-for-each-type.md)</p></td>
<td align="left"><p>FLG_MAINTAIN_OBJECT_TYPELIST</p></td>
<td align="left"><p>0x4000</p></td>
<td align="left"><p>otl</p></td>
<td align="left"><p>R</p></td>
</tr>
<tr class="odd">
<td align="left"><p>[Enable silent process exit monitoring](enable-silent-process-exit-monitoring.md)</p></td>
<td align="left"><p>FLG_MONITOR_SILENT_PROCESS_EXIT</p></td>
<td align="left"><p>0x200</p></td>
<td align="left"></td>
<td align="left"><p>R</p></td>
</tr>
<tr class="even">
<td align="left"><p>[Object Reference Tracing](object-reference-tracing.md)</p>
<p>(Windows Vista and later)</p></td>
<td align="left"></td>
<td align="left"></td>
<td align="left"></td>
<td align="left"><p>R, K</p></td>
</tr>
<tr class="odd">
<td align="left"><p>[Show loader snaps](show-loader-snaps.md)</p></td>
<td align="left"><p>FLG_SHOW_LDR_SNAPS</p></td>
<td align="left"><p>0x02</p></td>
<td align="left"><p>sls</p></td>
<td align="left"><p>R,K,I</p></td>
</tr>
<tr class="even">
<td align="left"><p>[Special Pool](special-pool.md)</p></td>
<td align="left"></td>
<td align="left"></td>
<td align="left"><p>spp</p></td>
<td align="left"><p>R</p>
<p>R,K (Windows Vista and later)</p></td>
</tr>
<tr class="odd">
<td align="left"><p>[Stop on exception](stop-on-exception.md)</p></td>
<td align="left"><p>FLG_STOP_ON_EXCEPTION</p></td>
<td align="left"><p>0x01</p></td>
<td align="left"><p>soe</p></td>
<td align="left"><p>R,K,I</p></td>
</tr>
<tr class="even">
<td align="left"><p>[Stop on hung GUI](stop-on-hung-gui.md)</p></td>
<td align="left"><p>FLG_STOP_ON_HUNG_GUI</p></td>
<td align="left"><p>0x08</p></td>
<td align="left"><p>shg</p></td>
<td align="left"><p>K</p></td>
</tr>
<tr class="odd">
<td align="left"><p>[Stop on unhandled user-mode exception](stop-on-unhandled-user-mode-exception.md)</p></td>
<td align="left"><p>FLG_STOP_ON_UNHANDLED_EXCEPTION</p></td>
<td align="left"><p>0x20000000</p></td>
<td align="left"><p>sue</p></td>
<td align="left"><p>R,K,I</p></td>
</tr>
</tbody>
</table>

 

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20[debugger\debugger]:%20GFlags%20Flag%20Table%20%20RELEASE:%20%285/15/2017%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")




