---
title: .dump (Create Dump File)
description: The .dump command creates a user-mode or kernel-mode crash dump file.
ms.assetid: df6bcf7f-eb2e-4605-87a0-c0a7e9e4776b
keywords: ["Create Dump File (.dump) command", "dump file, Create Dump File (.dump) command", ".dump (Create Dump File) Windows Debugging"]
ms.author: domars
ms.date: 08/01/2018
topic_type:
- apiref
api_name:
- .dump (Create Dump File)
api_type:
- NA
ms.localizationpriority: medium
---

# .dump (Create Dump File)


The **.dump** command creates a user-mode or kernel-mode crash dump file.

```dbgcmd
.dump Options FileName 
.dump /?
```

## <span id="ddk_meta_create_dump_file_dbg"></span><span id="DDK_META_CREATE_DUMP_FILE_DBG"></span>Parameters


<span id="_______Options______"></span><span id="_______options______"></span><span id="_______OPTIONS______"></span> *Options*   
Represents one or more of the following options

<span id="_o"></span><span id="_O"></span>**/o**  
Overwrites an existing dump file with the same name. If this option is not used and there is a file with the same file name, the dump file is not written.

<span id="_f_FullOptions_"></span><span id="_f_fulloptions_"></span><span id="_F_FULLOPTIONS_"></span>**/f\[**<em>FullOptions</em>**\]**  
(Kernel mode:) Creates a [complete memory dump](complete-memory-dump.md).

(User mode:) Creates a *full user-mode dump*. For more information, see [Varieties of User-Mode Dump Files](user-mode-dump-files.md#varieties). Despite their names, the largest minidump file actually contains more information than a full user-mode dump. For example, **.dump /mf** or **.dump /ma** creates a larger and more complete file than **.dump /f**. In user mode, **.dump** **/m\[**<em>MiniOptions</em>**\]** is always preferable to **.dump /f**.

You can add the following *FullOptions* to change the contents of the dump file; the option is case-sensitive.

<table>
<colgroup>
<col width="50%" />
<col width="50%" />
</colgroup>
<tbody>
<tr class="odd">
<td align="left">FullOption</td>
<td align="left">Effect</td>
</tr>
<tr class="even">
<td align="left"><p><strong>y</strong></p></td>
<td align="left">Adds AVX register information to the dump file.</td>
</tr>
</tbody>
</table>

 

<span id="_m_MiniOptions_"></span><span id="_m_minioptions_"></span><span id="_M_MINIOPTIONS_"></span>**/m\[**<em>MiniOptions</em>**\]**  
Creates a *small memory dump* (in kernel mode) or a *minidump* (in user mode) For more information, see [User-Mode Dump Files](user-mode-dump-files.md). If neither **/f** nor **/m** is specified, **/m** is the default.

In user mode, **/m** can be followed with additional *MiniOptions* specifying extra data that is to be included in the dump. If no *MiniOptions* are included, the dump will include module, thread, and stack information, but no additional data. You can add any of the following *MiniOptions* to change the contents of the dump file; they are case-sensitive.

<table>
<colgroup>
<col width="50%" />
<col width="50%" />
</colgroup>
<thead>
<tr class="header">
<th align="left">MiniOption</th>
<th align="left">Effect</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td align="left"><p><strong>a</strong></p></td>
<td align="left"><p>Creates a minidump with all optional additions. The <strong>/ma</strong> option is equivalent to <strong>/mfFhut</strong> -- it adds full memory data, handle data, unloaded module information, basic memory information, and thread time information to the minidump. Any failure to read inaccessable memory results in termination of the minidump generation.</p></td>
</tr>
<tr class="even">
<td align="left"><p><strong>A</strong></p></td>
<td align="left"><p>The <strong>/mA</strong> option is equivalent to <strong>/ma</strong> except that it ignores any failure to read inaccessable memory and continues generating the minidump.</p></td>
</tr>
<tr class="odd">
<td align="left"><p><strong>f</strong></p></td>
<td align="left"><p>Adds full memory data to the minidump. All accessible committed pages owned by the target application will be included.</p></td>
</tr>
<tr class="even">
<td align="left"><p><strong>F</strong></p></td>
<td align="left"><p>Adds all basic memory information to the minidump. This adds a stream to the minidump that contains all basic memory information, not just information about valid memory. This allows the debugger to reconstruct the complete virtual memory layout of the process when the minidump is being debugged.</p></td>
</tr>
<tr class="odd">
<td align="left"><p><strong>h</strong></p></td>
<td align="left"><p>Adds data about the handles associated with the target application to the minidump.</p></td>
</tr>
<tr class="even">
<td align="left"><p><strong>u</strong></p></td>
<td align="left"><p>Adds unloaded module information to the minidump. This is available only in Windows Server 2003 and later versions of Windows.</p></td>
</tr>
<tr class="odd">
<td align="left"><p><strong>t</strong></p></td>
<td align="left"><p>Adds additional thread information to the minidump. This includes thread times, which can be displayed by using the <strong><a href="-runaway.md" data-raw-source="[!runaway](-runaway.md)">!runaway</a></strong> extension or the <strong><a href="-ttime--display-thread-times-.md" data-raw-source="[.ttime (Display Thread Times)](-ttime--display-thread-times-.md)">.ttime (Display Thread Times)</a></strong> command when debugging the minidump.</p></td>
</tr>
<tr class="even">
<td align="left"><p><strong>i</strong></p></td>
<td align="left"><p>Adds <em>secondary memory</em> to the minidump. Secondary memory is any memory referenced by a pointer on the stack or backing store, plus a small region surrounding this address.</p></td>
</tr>
<tr class="odd">
<td align="left"><p><strong>p</strong></p></td>
<td align="left"><p>Adds process environment block (PEB) and thread environment block (TEB) data to the minidump. This can be useful if you need access to Windows system information regarding the application&#39;s processes and threads.</p></td>
</tr>
<tr class="even">
<td align="left"><p><strong>w</strong></p></td>
<td align="left"><p>Adds all committed read-write private pages to the minidump.</p></td>
</tr>
<tr class="odd">
<td align="left"><p><strong>d</strong></p></td>
<td align="left"><p>Adds all read-write data segments within the executable image to the minidump.</p></td>
</tr>
<tr class="even">
<td align="left"><p><strong>c</strong></p></td>
<td align="left"><p>Adds code sections within images.</p></td>
</tr>
<tr class="odd">
<td align="left"><p><strong>r</strong></p></td>
<td align="left"><p>Deletes from the minidump those portions of the stack and store memory that are not useful for recreating the stack trace. Local variables and other data type values are deleted as well. This option does not make the minidump smaller (because these memory sections are simply zeroed), but it is useful if you want to protect the privacy of other applications.</p></td>
</tr>
<tr class="even">
<td align="left"><p><strong>R</strong></p></td>
<td align="left"><p>Deletes the full module paths from the minidump. Only the module names will be included. This is a useful option if you want to protect the privacy of the user&#39;s directory structure.</p></td>
</tr>
<tr class="odd">
<td align="left"><p><strong>y</strong></p></td>
<td align="left"><p>Adds AVX register information to the dump file.</p></td>
</tr>
</tbody>
</table>

 

These *MiniOptions* can only be used when creating a user-mode minidump. They should follow the **/m** specifier.

<span id="_u"></span><span id="_U"></span>**/u**  
Appends the date, time, and PID to the dump file names. This ensures that dump file names are unique.

<span id="_a"></span><span id="_A"></span>**/a**  
Generates dumps for all currently-debugged processes. If **/a** is used, the **/u** option should also be used to ensure that each file has a unique name.

<span id="_ba"></span><span id="_BA"></span>**/b**\[**a**\]  
Creates a .cab file. If this option is included, *FileName* is interpreted as the CAB file name, not the dump file name. A temporary dump file will be created, this file will be packaged into a CAB, and then the dump file will be deleted. If the **b** option is followed by **a**, all symbol and image files also will be packaged into the CAB.

<span id="_c__Comment_"></span><span id="_c__comment_"></span><span id="_C__COMMENT_"></span>**/c "**<em>Comment</em>**"**  
Specifies a comment string that will be written to the dump file. If *Comment* contains spaces, it must be enclosed in double quotes. When the dump file is loaded, the *Comment* string will be displayed.

<span id="_xc_Address"></span><span id="_xc_address"></span><span id="_XC_ADDRESS"></span>**/xc** *Address*  
(User mode minidumps only) Adds a context record to the dump file. *Address* must specify the address of the context record.

<span id="_xr_Address"></span><span id="_xr_address"></span><span id="_XR_ADDRESS"></span>**/xr** *Address*  
(User mode minidumps only) Adds an exception record to the dump file. *Address* must specify the address of the exception record.

<span id="_xp_Address"></span><span id="_xp_address"></span><span id="_XP_ADDRESS"></span>**/xp** *Address*  
(User mode minidumps only) Adds a context record and an exception record to the dump file. *Address* must specify the address of an EXCEPTION\_POINTERS structure which contains pointers to the context record and the exception record.

<span id="_xt_ThreadID"></span><span id="_xt_threadid"></span><span id="_XT_THREADID"></span>**/xt** *ThreadID*  
(User mode minidumps only) Specifies the thread ID of the system thread that will be used as the exception thread for this dump file.

<span id="_kpmf_File"></span><span id="_kpmf_file"></span><span id="_KPMF_FILE"></span>**/kpmf** *File*  
(Only when creating a kernel-mode Complete Memory Dump) Specifies a file that contains physical memory page data.

<span id="_j_Address"></span><span id="_j_address"></span><span id="_J_ADDRESS"></span>**/j** *Address*  
Adds the JIT\_DEBUG\_INFO structure to the dump file in user mode. *Address* must specify the address of the JIT\_DEBUG\_INFO structure. This address is normally provided via the %p parameter when the .jdinfo command is used as part of a just in time postmortem debugging process. For more information, see [**.jdinfo (Use JIT\_DEBUG\_INFO)**](-jdinfo--use-jit-debug-info-.md) and [Enabling Postmortem Debugging](enabling-postmortem-debugging.md).

<span id="_______FileName______"></span><span id="_______filename______"></span><span id="_______FILENAME______"></span> *FileName*   
Specifies the name of the dump file. You can specify a full path and file name or just the file name. If the file name contains spaces, *FileName* should be enclosed in quotation marks. If no path is specified, the current directory is used.

<span id="_______-_______"></span> **-?**   
Displays help for this command. This text is different in kernel mode and in user mode.

### <span id="Environment"></span><span id="environment"></span><span id="ENVIRONMENT"></span>Environment

<table>
<colgroup>
<col width="50%" />
<col width="50%" />
</colgroup>
<tbody>
<tr class="odd">
<td align="left"><p><strong>Modes</strong></p></td>
<td align="left"><p>user mode, kernel mode</p></td>
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

For a description of kernel-mode dump files and an explanation of their use, see [Kernel-Mode Dump Files](kernel-mode-dump-files.md). For a description of user-mode dump files and an explanation of their use, see [User-Mode Dump Files](user-mode-dump-files.md).

Remarks
-------

This command can be used in a variety of situations:

-   During live user-mode debugging, this command directs the target application to generate a dump file, but the target application does not terminate.

-   During live kernel-mode debugging, this command directs the target computer to generate a dump file, but the target computer does not crash.

-   During crash dump debugging, this command creates a new crash dump file from the old one. This is useful if you have a large crash dump file and want to create a smaller one.

You can control what type of dump file will be produced:

- In kernel mode, to produce a [complete memory dump](complete-memory-dump.md), use the **/f** option. To produce a [small memory dump](small-memory-dump.md), use the **/m** option (or no options). The .dump command cannot produce a [kernel memory dump](kernel-memory-dump.md).

- In user mode, **.dump** **/m\[**<em>MiniOptions</em>**\]** is the best choice. Although "m" stands for "minidump", the dump files created by using this *MiniOption* can vary in size from very small to very large. By specifying the proper *MiniOptions* you can control exactly what information is included. For example, **.dump /ma** produces a dump with a great deal of information. The older command, **.dump /f**, produces a moderately large "standard dump" file and cannot be customized.

You cannot specify which process is dumped. All running processes will be dumped.

The **/xc**, **/xr**, **/xp**, and **/xt** options are used to store exception and context information in the dump file. This allows the [**.ecxr (Display Exception Context Record)**](-ecxr--display-exception-context-record-.md) command to be run on this dump file.

The following example will create a user-mode minidump, containing full memory and handle information:

```dbgcmd
0:000> .dump /mfh myfile.dmp 
```

Handle information can be read by using the [**!handle**](-handle.md) extension command.

 

 





