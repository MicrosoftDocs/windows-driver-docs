---
title: GFlags Details
description: GFlags Details
ms.assetid: 97faa63d-b876-4973-812f-f3bdd57c1778
keywords: ["GFlags, details"]
ms.author: domars
ms.date: 05/23/2017
ms.localizationpriority: medium
---

# GFlags Details


## <span id="ddk_gflags_details_dtools"></span><span id="DDK_GFLAGS_DETAILS_DTOOLS"></span>


GFlags enables and disables system features by editing the Windows registry and internal settings. This section explains the operation of GFlags in detail and includes tips for using GFlags most efficiently.

### <span id="general_information"></span><span id="GENERAL_INFORMATION"></span>General Information

-   To display the GFlags dialog box, at the command line, type **gflags** (with no parameters).

-   On Windows Server 2003 and earlier versions of Windows, to set flags in the registry or in kernel mode, you must be a member of the Administrators group on the computer. However, users with at least Guest account access can launch a program from the GFlags dialog box.

-   GFlags system-level registry settings appear in the registry immediately, but do not take effect until you restart the system.

-   GFlags image file registry settings appear in the registry immediately, but do not take effect until you restart the process.

-   The debugger and launch features in the GFlags dialog box are program specific. You can only set them on one image file at a time.

### <span id="flag_details"></span><span id="FLAG_DETAILS"></span>Flag Details

-   To clear all flags, set the flag to -FFFFFFFF. Setting the flag to 0 adds 0 to the current flag value.

-   When you set the flags for an image file to FFFFFFFF (0xFFFFFFFF), Windows clears all flags for the image file and deletes the **GlobalFlag** entry in the image file registry key. The image file registry key is retained.

### <span id="dialog_box_and_command_line"></span><span id="DIALOG_BOX_AND_COMMAND_LINE"></span>Dialog Box and Command Line

You can run GFlags by using its handy dialog box or from the command line. Most features are available in both forms, with the following exceptions.

**Dialog box only**

-   Launch. Start a program using the specified flags.

-   Run the program in a debugger.

-   [Special Pool](special-pool.md) on systems prior to Windows Vista. On Windows Vista and later versions of Windows, you can configure the Special Pool feature at the command line or in the Gflags dialog box.

**Command line only**

-   Set the size of the user mode stack trace database (/tracedb).

-   Set page heap verification options.

### <span id="registry_information"></span><span id="REGISTRY_INFORMATION"></span>Registry Information

GFlags settings that are saved between sessions are stored in the registry. You can use the registry APIs, Regedit, or reg.exe to query or change these values. The following table lists the types of settings and where they are stored in the registry.

<table>
<colgroup>
<col width="50%" />
<col width="50%" />
</colgroup>
<tbody>
<tr class="odd">
<td align="left"><p>Systemwide settings (&quot;Registry&quot;)</p></td>
<td align="left"><p>HKEY_LOCAL_MACHINE\SYSTEM\CurrentControlSet\Control\Session Manager&lt;strong&gt;GlobalFlag</strong></p></td>
</tr>
<tr class="even">
<td align="left"><p>Program-specific settings (&quot;Image file&quot;) for all users of the computer.</p></td>
<td align="left"><p>HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Windows NT\CurrentVersion\Image File Execution Options&lt;em&gt;ImageFileName</em>&lt;strong&gt;GlobalFlag</strong></p></td>
</tr>
<tr class="odd">
<td align="left"><p>Silent exit settings for a specific program (&quot;Silent Process Exit&quot;) for all users of the computer.</p></td>
<td align="left"><p>HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Windows NT\CurrentVersion\SilentProcessExit&lt;em&gt;ImageFileName</em></p></td>
</tr>
<tr class="even">
<td align="left"><p>Page heap options for an image file for all users of the computer</p></td>
<td align="left"><p>HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Windows NT\CurrentVersion\Image File Execution Options&lt;em&gt;ImageFileName</em>&lt;strong&gt;PageHeapFlags</strong></p></td>
</tr>
<tr class="odd">
<td align="left"><p>User mode stack trace database size (<strong>tracedb</strong>)</p></td>
<td align="left"><p>HKLM\SOFTWARE\Microsoft\Windows NT\CurrentVersion\Image File Execution Options&lt;em&gt;ImageFileName</em>&lt;strong&gt;StackTraceDatabaseSizeInMb</strong></p></td>
</tr>
<tr class="even">
<td align="left"><p>Create user mode stack trace database (ust, 0x1000) for an image file</p></td>
<td align="left"><p>Windows adds the image file name to the value of the USTEnabled registry entry (HKLM\SOFTWARE\Microsoft\Windows NT\CurrentVersion\Image File Execution Options&lt;strong&gt;USTEnabled</strong>).</p></td>
</tr>
<tr class="odd">
<td align="left"><p>Load image using large pages if possible</p></td>
<td align="left"><p>HKLM\SOFTWARE\Microsoft\Windows NT\CurrentVersion\Image File Execution Options&lt;em&gt;ImageFileName</em>&lt;strong&gt;UseLargePages</strong>.</p></td>
</tr>
<tr class="even">
<td align="left"><p>Special Pool</p>
<p>(Kernel Special Pool Tag)</p></td>
<td align="left"><p>HKLM\SYSTEM\CurrentControlSet\Control\Session Manager\Memory Management&lt;strong&gt;PoolTag</strong></p></td>
</tr>
<tr class="odd">
<td align="left"><p>Verify Start / Verify End</p></td>
<td align="left"><p>HKLM\SYSTEM\CurrentControlSet\Control\Session Manager\Memory Management\PoolTagOverruns. The <strong>Verify Start</strong> option sets the value to 0. The <strong>Verify End</strong> option sets the value to 1.</p></td>
</tr>
<tr class="even">
<td align="left"><p>Debugger for an image file</p></td>
<td align="left"><p>HKLM\SOFTWARE\Microsoft\Windows NT\CurrentVersion\Image File Execution Options&lt;em&gt;ImageFileName</em>&lt;strong&gt;Debugger</strong></p></td>
</tr>
<tr class="odd">
<td align="left"><p>Object Reference Tracing</p></td>
<td align="left"><p>HKLM\SYSTEM\CurrentControlSet\Control\Session Manager\Kernel&lt;strong&gt;ObTraceProcessName</strong>, <strong>ObTracePermanent</strong> and <strong>ObTracePoolTags</strong></p></td>
</tr>
</tbody>
</table>

 

 

 





