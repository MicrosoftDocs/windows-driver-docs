---
title: GFlags Commands
description: To use GFlags, type the following commands at the command line. You can use the GFlags commands and the Global Flags Dialog Box interchangeably.
ms.assetid: 832b7269-623a-4f32-8bda-1059087bab09
keywords: ["GFlags Commands Windows Debugging"]
ms.author: domars
ms.date: 06/12/2018
topic_type:
- apiref
api_name:
- GFlags Commands
api_type:
- NA
ms.localizationpriority: medium
---

# GFlags Command Overview

For general information on how to install and locate gflags.exe, see [GFlags](gflags.md).

You can use the GFlags commands and the [Global Flags Dialog Box](global-flags-dialog-box.md) interchangeably.

## GFlags Command Usage 

To use GFlags, type the following commands at the command line.


To open the GFlags dialog box:

```console
gflags
```

To set or clear global flags in the registry:

```console
gflags /r [{+ | -}Flag [{+ | -}Flag...]]
```

To set or clear global flags for the current session:

```console
gflags /k [{+ | -}Flag [{+ | -}Flag...]]
```

To set or clear global flags for an image file:

```console
gflags /i ImageFile [{+ | -}Flag [{+ | -}Flag...]]
gflags /i ImageFile /tracedb SizeInMB
```

To set or clear the Special Pool feature (Windows Vista and later)

```console
gflags {/r | /k} {+ | -}spp {PoolTag | 0xSize}
```

To enable or disable the Object Reference Tracing feature (Windows Vista and later)

```console
gflags {/ro | /ko} [/p] [/i ImageFile | /t PoolTag;[PoolTag...]]
```

```console
gflags {/ro | /ko} /d
```

To enable and configure page heap verification:

```console
gflags /p /enable ImageFile  [ /full [/backwards] | /random Probability | /size SizeStart SizeEnd | /address AddressStart AddressEnd | /dlls DLL [DLL...] ] 
[/debug ["DebuggerCommand"] | /kdebug] [/unaligned] [/notraces] [/fault Rate [TimeOut]] [/leaks] [/protect] [/no_sync] [/no_lock_checks] 
```

To disable page heap verification:

```console
gflags /p [/disable ImageFile] [/?]
```

To display help:

```console
glags /?
```

## <span id="ddk_gflags_commands_dtools"></span><span id="DDK_GFLAGS_COMMANDS_DTOOLS"></span>Parameters


<span id="_______Flag______"></span><span id="_______flag______"></span><span id="_______FLAG______"></span> *Flag*   
Specifies a three-letter abbreviation (*FlagAbbr*) or hexadecimal value (*FlagHex*) that represents a debugging feature. The abbreviations and hexadecimal values are listed in the [GFlags Flag Table](gflags-flag-table.md).

Use one of the following flag formats:

<table>
<colgroup>
<col width="50%" />
<col width="50%" />
</colgroup>
<thead>
<tr class="header">
<th align="left">Format</th>
<th align="left">Description</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td align="left"><p>{<strong>+</strong> | <strong>-</strong>}<em>FlagAbbr</em></p></td>
<td align="left"><p>Sets (+) or clears (-) the flag represented by the flag abbreviation. Without a plus (+) or minus (-) symbol, the command has no effect.</p></td>
</tr>
<tr class="even">
<td align="left"><p>[<strong>+</strong> | <strong>-</strong>]<em>FlagHex</em></p></td>
<td align="left"><p>Adds (+) or subtracts (-) the hexadecimal value of a flag. A flag is set when its value is included in the sum. Add (+) is the default. Enter a hexadecimal value (without 0x) that represents a single flag or enter the sum of hexadecimal values for multiple flags.</p></td>
</tr>
</tbody>
</table>

 

<span id="_______ImageFile______"></span><span id="_______imagefile______"></span><span id="_______IMAGEFILE______"></span> *ImageFile*   
Specifies the name of an executable file, including the file name extension (for example, notepad.exe or mydll.dll).

<span id="________r______"></span><span id="________R______"></span> **/r**   
Registry. Displays or changes system-wide debugging flags stored in the registry. These settings take effect when you restart Windows and remain effective until you change them.

With no additional parameters, **gflags /r** displays the system-wide flags set in the registry.

<span id="________k______"></span><span id="________K______"></span> **/k**   
Kernel flag settings. Displays or changes system-wide debugging flags for this session. These settings are effective immediately, but are lost when Windows shuts down. The settings affect processes started after this command completes.

With no additional parameters, **gflags /k** displays system-wide flags set for the current session.

<span id="________i______"></span><span id="________I______"></span> **/i**   
Image file settings. Displays or changes debugging flags for a particular process. These settings are stored in the registry. They are effective for all new instances of this process and they remain effective until you change them.

With no additional parameters, **gflags /i** *ImageFile* displays the flags set for the specified process.

<span id="________tracedb_______SizeInMB______"></span><span id="________tracedb_______sizeinmb______"></span><span id="________TRACEDB_______SIZEINMB______"></span> **/tracedb** *SizeInMB*   
Sets the maximum size of the user-mode stack trace database for the process. To use this parameter, the [Create user mode stack trace database](create-user-mode-stack-trace-database.md) (ust) flag must be set for the process.

*SizeInMB* is a whole number representing the number of megabytes in decimal units. The default value is the minimum size, 8 MB; there is no maximum size. To revert to the default size, set *SizeInMB* to 0.

<span id="_______spp______"></span><span id="_______SPP______"></span> **spp**   
(Windows Vista and later.) Sets or clears the [Special Pool](special-pool.md) feature. For an example, see [Example 14: Configuring Special Pool](example-14---configuring-special-pool.md).

<span id="_______PoolTag______"></span><span id="_______pooltag______"></span><span id="_______POOLTAG______"></span> *PoolTag*   
(Windows Vista and later.) Specifies a pool tag for the [Special Pool](special-pool.md) feature. Use only with the **spp** flag.

Enter a four-character pattern for *PoolTag*, such as Tag1. It can include the **?** (substitute for any single character) and **\\*** (substitute for multiple characters) wildcard characters. For example, Fat\* or Av?4. Pool tags are always case-sensitive.

<span id="0xSize______"></span><span id="0xsize______"></span><span id="0XSIZE______"></span>**0x***Size*   
(Windows Vista and later.) Specifies a size range for the Special Pool feature. Use only with the **spp** flag. For guidance on selecting a size value, see "Selecting an Allocation Size" in [Special Pool](special-pool.md).

<span id="________ro______"></span><span id="________RO______"></span> **/ro**   
Enables, disables, and displays [Object Reference Tracing](object-reference-tracing.md) settings in the registry. To make a change to this setting effective, you must restart Windows.

Without additional parameters, **/ro** displays the Object Reference Tracing settings in the registry.

To enable Object Reference Tracing, you must include at least one pool tag (**/t** *PoolTag*) or one image file (**/i** ImageFile) in the command. For details, see [Example 15: Using Object Reference Tracing](example-15--using-object-reference-tracing.md).

The following table lists the subparameters that are valid with **/ro**.

<table>
<colgroup>
<col width="50%" />
<col width="50%" />
</colgroup>
<tbody>
<tr class="odd">
<td align="left"><p><strong>/t</strong> <em>PoolTags</em></p></td>
<td align="left"><p>Limits the trace to objects with the specified pool tags. Use a semicolon (<strong>;</strong>) to separate tag names. Enter up to 16 pool tags.</p>
<p>Enter a four-character pattern for <em>PoolTags</em>, such as Tag1.</p>
<p>If you specify more than one pool tag, Windows traces objects with any of the specified pool tags .</p>
<p>If you do not specify any pool tags, Windows traces all objects that are created by the image.</p></td>
</tr>
<tr class="even">
<td align="left"><p><strong>/i</strong> <em>ImageFile</em></p></td>
<td align="left"><p>Limits the trace to objects that are created by processes with the specified image file. You can specify only one image file with the <strong>/i</strong> parameter.</p>
<p>Enter an image file name, such as notepad.exe, with up to 64 characters. &quot;System&quot; and &quot;Idle&quot; are not valid image names.</p>
<p>If you do not specify an image file, Windows traces all objects with the specified pool tags. If you specify both an image file (<strong>/i</strong>) and one or more pool tags (<strong>/t</strong>), Windows traces objects with any of the specified pool tags that are created by the specified image.</p></td>
</tr>
<tr class="odd">
<td align="left"><p><strong>/d</strong></p></td>
<td align="left"><p>Clears the Object Reference Tracing feature settings. When used with <strong>/ro</strong>, it clears the settings in the registry.</p></td>
</tr>
<tr class="even">
<td align="left"><p><strong>/p</strong></p></td>
<td align="left"><p>Permanent. The trace data is retained until Object Reference Tracing is disabled, or the computer is shut down or restarted. By default, the trace data for an object is discarded when the object is destroyed.</p></td>
</tr>
</tbody>
</table>

 

<span id="________ko______"></span><span id="________KO______"></span> **/ko**   
Enables, disables, and displays kernel flag (run time) [Object Reference Tracing](object-reference-tracing.md) settings. Changes to this setting are effective immediately, but are lost when the system is shut down or restarted. For details, see [Example 15: Using Object Reference Tracing](example-15--using-object-reference-tracing.md).

Without additional parameters, **/ko** displays the kernel flag (run time) Object Reference Tracing settings.

To enable Object Reference Tracing, you must include at least one pool tag (**/t** *PoolTag*) or one image file (**/i** *ImageFile*) in the command.

The following table lists the subparameters that are valid with **/ko**.

<table>
<colgroup>
<col width="50%" />
<col width="50%" />
</colgroup>
<tbody>
<tr class="odd">
<td align="left"><p><strong>/t</strong> <em>PoolTags</em></p></td>
<td align="left"><p>Limits the trace to objects with the specified pool tags. Use a semicolon (<strong>;</strong>) to separate tag names. Enter up to 16 pool tags.</p>
<p>Enter a four-character pattern for <em>PoolTags</em>, such as Tag1.</p>
<p>If you specify more than one pool tag, Windows traces objects with any of the specified pool tags.</p>
<p>If you do not specify any pool tags, Windows traces all objects that are created by the image.</p></td>
</tr>
<tr class="even">
<td align="left"><p><strong>/i</strong> <em>ImageFile</em></p></td>
<td align="left"><p>Limits the trace to objects that are created by processes with the specified image file. You can specify only one image file with the <strong>/i</strong> parameter.</p>
<p>If you do not specify an image file, Windows traces all objects with the specified pool tags.</p>
<p>If you specify both an image file (<strong>/i</strong>) and one or more pool tags (<strong>/t</strong>), Windows traces objects with any of the specified pool tags that are created by the specified image.</p></td>
</tr>
<tr class="odd">
<td align="left"><p><strong>/d</strong></p></td>
<td align="left"><p>Clears the Object Reference Tracing feature settings. When used with <strong>/ro</strong>, it clears the settings in the registry.</p></td>
</tr>
<tr class="even">
<td align="left"><p><strong>/p</strong></p></td>
<td align="left"><p>Permanent. The trace data is retained until Object Reference Tracing is disabled, or the computer is shut down or restarted. By default, the trace data for an object is discarded when the object is destroyed.</p></td>
</tr>
</tbody>
</table>

 

<span id="________p______"></span><span id="________P______"></span> **/p**   
Sets page heap verification options for a process.

With no additional parameters, **gflags /p** displays a list of image files for which page heap verification is enabled.

Page heap verification monitors dynamic heap memory operations, including allocate operations and free operations, and causes a debugger break when it detects a heap error.

<span id="________disable_______ImageFile______"></span><span id="________disable_______imagefile______"></span><span id="________DISABLE_______IMAGEFILE______"></span> **/disable** *ImageFile*   
Turns off page heap verification (standard or full) for the specified image file.

This command is equivalent to turning off the [Enable page heap](enable-page-heap.md) (hpa) flag for a process (**gflags /i** *ImageFile* **-hpa**). You can use the commands interchangeably.

<span id="________enable_______ImageFile______"></span><span id="________enable_______imagefile______"></span><span id="________ENABLE_______IMAGEFILE______"></span> **/enable** *ImageFile*   
Turns on page heap verification for the specified image file.

By default, the **/enable** parameter turns on *standard* page heap verification for the image file. To enable *full* page heap verification for the image file, add the **/full** parameter to the command or use the **/i** parameter with the **+hpa** flag.

<span id="________full______"></span><span id="________FULL______"></span> **/full**   
Turns on full page heap verification for the process. Full page heap verification places a zone of reserved virtual memory at the end of each allocation.

Using this parameter is equivalent to turning on the [Enable page heap](enable-page-heap.md) (hpa) flag for a process (**gflags /i** *ImageFile* **+hpa**). You can use the commands interchangeably.

<span id="________backwards______"></span><span id="________BACKWARDS______"></span> **/backwards**   
Places the zone of reserved virtual memory at the beginning of an allocation, rather than at the end. As a result, the debugger traps overruns at the beginning of the buffer, instead of those at the end of the buffer. Valid only with the **/full** parameter.

<span id="________random_______Probability______"></span><span id="________random_______probability______"></span><span id="________RANDOM_______PROBABILITY______"></span> **/random** *Probability*   
Chooses full or standard page heap verification for each allocation, based on the specified probability.

*Probability* is a decimal integer from 0 through 100 representing the probability of full page heap verification. A probability of 100 is the same as using the **/full** parameter. A probability of 0 is the same as using standard page heap verification.

<span id="________size________SizeStart_SizeEnd______"></span><span id="________size________sizestart_sizeend______"></span><span id="________SIZE________SIZESTART_SIZEEND______"></span> **/size** *SizeStart SizeEnd*   
Enables full page heap verification for allocations within the specified size range and enables standard page heap verification for all other allocations by the process.

*SizeStart* and *SizeEnd* are decimal integers. The default is standard page heap verification for all allocations.

<span id="________address________AddressStart_AddressEnd______"></span><span id="________address________addressstart_addressend______"></span><span id="________ADDRESS________ADDRESSSTART_ADDRESSEND______"></span> **/address** *AddressStart AddressEnd*   
Enables full page heap verification for memory allocated while a return address in the specified address range is on the run-time call stack. It enables standard page heap verification for all other allocations by the process.

To use this feature, specify a range that includes the addresses of all functions that call the function with the suspect allocation. The address of the calling function will be on the call stack when the suspect allocation occurs.

*AddressStart* and *AddressEnd* specify the address range searched in allocation stack traces. The addresses are specified in hexadecimal format, such as, 0xAABBCCDD.

On Windows Server 2003 and earlier systems, the **/address** parameter is valid only on *x*86-based computers. On Windows Vista,: it is valid on all supported architectures.

<span id="________dlls_DLL___DLL...__"></span><span id="________dlls_dll___dll...__"></span><span id="________DLLS_DLL___DLL...__"></span> **/dlls** *DLL*\[**,** *DLL*...\]   
Enables full page heap verification for allocations requested by the specified DLLs and standard page heap verification for all other allocations by the process.

*DLL* is the name of a binary file, including its file name extension. The specified file must be a function library that the process loads during execution.

<span id="________debug______"></span><span id="________DEBUG______"></span> **/debug**   
Automatically launches the process specified by the **/enable** parameter under a debugger.

By default, this parameter uses the NTSD debugger with the command line **ntsd -g -G -x** and with page heap enabled, but you can use the *DebuggerCommand* variable to specify a different debugger and command line.

For information about NTSD, see [Debugging Using CDB and NTSD](debugging-using-cdb-and-ntsd.md).

This option is useful for programs that are difficult to start from a command prompt and those that are started by other processes.

<span id="_DebuggerCommand_______"></span><span id="_debuggercommand_______"></span><span id="_DEBUGGERCOMMAND_______"></span>**"**<em>DebuggerCommand</em>**"**   
Specifies a debugger and the command sent to the debugger. This quoted string can include a fully qualified path to the debugger, the debugger name, and command parameters that the debugger interprets. The quotation marks are required.

If the command includes a path to the debugger, the path cannot contain any other quotation marks. If other quotation marks appear, the command shell (*cmd.exe*) will misinterpret the command.

<span id="________kdebug______"></span><span id="________KDEBUG______"></span> **/kdebug**   
Automatically launches the process specified by the **/enable** parameter under the NTSD debugger with the command line **ntsd -g -G -x**, with page heap enabled, and with control of NTSD redirected to the kernel debugger.

For information about NTSD, see [Debugging Using CDB and NTSD](debugging-using-cdb-and-ntsd.md).

<span id="________unaligned______"></span><span id="________UNALIGNED______"></span> **/unaligned**   
Aligns the end of each allocation at an end-of-page boundary, even if doing so means that the starting address is not aligned on an 8-byte block. By default, the heap manager guarantees that the starting address of an allocation is aligned on an 8-byte block.

This option is used to detect off-by-one-byte errors. When this parameter is used with the **/full** parameter, the zone of reserved virtual memory begins just after the last byte of the allocation and an immediate fault occurs when a process tries to read or write even one byte beyond the allocation.

<span id="________decommit______"></span><span id="________DECOMMIT______"></span> **/decommit**   
This option is no longer valid. It is accepted, but ignored.

The PageHeap program (pageheap.exe) included in Windows 2000 implemented full page heap verification by placing an inaccessible page after an allocation. In that tool, the **/decommit** parameter substituted a zone of reserved virtual memory for the inaccessible page. In this version of GFlags, a zone of reserved virtual memory is always used to implement full page heap verification.

<span id="________notraces______"></span><span id="________NOTRACES______"></span> **/notraces**   
Specifies that run-time stack traces are not saved.

This option improves performance slightly, but it makes debugging much more difficult. This parameter is valid, but its use is not recommended.

<span id="________fault______"></span><span id="________FAULT______"></span> **/fault**   
Forces the program's memory allocations to fail at the specified rate and after the specified time-out.

This parameter inserts heap allocation errors into the image file being tested (a practice known as "fault injection") so that some memory allocations fail, as might occur when the program runs in low memory conditions. This test helps to detect errors in handling allocation failure, such as failing to release resources.

<table>
<colgroup>
<col width="50%" />
<col width="50%" />
</colgroup>
<tbody>
<tr class="odd">
<td align="left"><p><em>Rate</em></p></td>
<td align="left"><p>Specifies a decimal integer from 1 (.01%) through 10000 (100%) representing the probability that an allocation will fail. The default is 100 (1%).</p></td>
</tr>
<tr class="even">
<td align="left"><p><em>TimeOut</em></p></td>
<td align="left"><p>Determines the time interval between the start of the program and the start of the fault injection routines.</p>
<p><em>TimeOut</em> is measured in seconds. The default is 5 (seconds).</p></td>
</tr>
</tbody>
</table>

 

<span id="________leaks______"></span><span id="________LEAKS______"></span> **/leaks**   
Checks for heap leaks when a process ends.

The **/leaks** parameter disables full page heap. When **/leaks** is used, the **/full** parameter and parameters that modify the **/full** parameter, such as **/backwards**, are ignored, and GFlags performs standard page heap verification with a leak check.

<span id="________protect______"></span><span id="________PROTECT______"></span> **/protect**   
Protects heap internal structures. This test is used to detect random heap corruptions. It can make execution significantly slower.

<span id="________no_sync______"></span><span id="________NO_SYNC______"></span> **/no\_sync**   
Checks for unsynchronized access. This parameter causes a break if it detects that a heap created with the HEAP\_NO\_SERIALIZE flag is accessed by different threads.

Do not use this flag to debug a program that includes a customized heap manager. Functions that synchronize heap access cause the page heap verifier to report synchronization faults that do not exist.

<span id="________no_lock_checks______"></span><span id="________NO_LOCK_CHECKS______"></span> **/no\_lock\_checks**   
Disables the critical section verifier.

<span id="_______________"></span> **/?**   
Displays help for GFlags. With **/p**, **/?** displays help for the page heap verification options in GFlags.

### <span id="comments"></span><span id="COMMENTS"></span>Comments

Typing **gflags** without parameters opens the **Global Flags** dialog box.

Typing **gflags /p** without additional parameters displays a list of programs that have page heap verification enabled.

To clear all flags, set *Flag* to **-FFFFFFFF**. (Setting *Flag* to 0 adds zero to the current flag value. It does not clear all flags.)

When you set *Flag* for an image file to **FFFFFFFF**, Windows clears all flags and deletes the GlobalFlag entry in the registry subkey for the image file. The subkey remains.

The **/full**, **/random**, **/size**, **/address**, and **/dlls** parameters for the page heap **/enable** operation determine which allocations are subject to page heap verification and the verification method used. You can use only one of these parameters in each command. The default is standard page heap verification of all allocations of the process. The remaining parameters set options for page heap verification.

The page heap features in GFlags only monitor heap memory allocations that use the standard Windows heap manager functions (**HeapAlloc**, **GlobalAlloc**, **LocalAlloc**, **malloc**, **new**, **new\[\]**, or their corresponding deallocation functions), or those that use custom operations that call the standard heap manager functions.

To determine whether full or standard page heap verification is enabled for a program, at the command line, type **gflags /p**. In the resulting display, **traces** indicates that standard page heap verification is enabled for the program and **full traces** indicates that full page heap verification is enabled for the program.

The **/enable** parameter sets the [Enable page heap](enable-page-heap.md) (hpa) flag for the image file in the registry. However, the **/enable** parameter turns on *standard* heap verification for the image file by default, unlike the **/i** parameter with the **+hpa** flag, which turns on *full* heap verification for an image file.

*Standard* page heap verification places random patterns at the end of an allocation and examines the patterns when a heap block is freed. *Full* page heap verification places a zone of reserved virtual memory at the end of each allocation.

Full page heap verification can consume system memory quickly. To enable full page heap verification for memory-intensive processes, use the **/size** or **/dlls** parameter.

After using global flags for debugging, submit a **gflags /p /disable** command to turn off the page heap verification and delete associated registry entries. Otherwise, entries that the debugger reads remain in the registry. You cannot use the **gflags /i hpa** command for this task, because it turns off page heap verification, but does not delete the registry entries.

By default, on Windows Vista and later versions of Windows, program-specific settings (image file flags and page heap verification settings) are stored in the current user account.

This version of GFlags includes the **-v** options, which enable features being developed for GFlags. However, these features are not yet complete and, therefore, are not documented.

 

 





