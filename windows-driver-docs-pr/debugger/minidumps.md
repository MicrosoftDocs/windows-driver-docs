---
title: Minidumps
description: Minidumps
ms.assetid: 2cb54df3-2e61-4d5c-9ef6-3c81787d2233
keywords: ["dump file, minidump", "minidump"]
---

# Minidumps


## <span id="ddk_minidumps_dbg"></span><span id="DDK_MINIDUMPS_DBG"></span>


A user-mode dump file that includes only selected parts of the memory associated with a process is called a *minidump*.

The size and contents of a minidump file vary depending on the program being dumped and the application doing the dumping. Sometimes, a minidump file is fairly large and includes the full memory and handle table. Other times, it is much smaller -- for example, it might only contain information about a single thread, or only contain information about modules that are actually referenced in the stack.

The name "minidump" is misleading, because the largest minidump files actually contain more information than the "full" user-mode dump. For example, **.dump /mf** or **.dump /ma** will create a larger and more complete file than **.dump /f**. For this reason, **.dump /m**\[*MiniOptions*\] recommended over **.dump /f** for all user-mode dump file creation.

If you are creating a minidump file with the debugger, you can choose exactly what information to include. A simple **.dump /m** command will include basic information about the loaded modules that make up the target process, thread information, and stack information. This can be modified by using any of the following options:

<table>
<colgroup>
<col width="50%" />
<col width="50%" />
</colgroup>
<thead>
<tr class="header">
<th align="left">.dump option</th>
<th align="left">Effect on dump file</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td align="left"><p><strong>/ma</strong></p></td>
<td align="left"><p>Creates a minidump with all optional additions. The <strong>/ma</strong> option is equivalent to <strong>/mfFhut</strong> -- it adds full memory data, handle data, unloaded module information, basic memory information, and thread time information to the minidump.</p></td>
</tr>
<tr class="even">
<td align="left"><p><strong>/mf</strong></p></td>
<td align="left"><p>Adds full memory data to the minidump. All accessible committed pages owned by the target application will be included.</p></td>
</tr>
<tr class="odd">
<td align="left"><p><strong>/mF</strong></p></td>
<td align="left"><p>Adds all basic memory information to the minidump. This adds a stream to the minidump that contains all basic memory information, not just information about valid memory. This allows the debugger to reconstruct the complete virtual memory layout of the process when the minidump is being debugged.</p></td>
</tr>
<tr class="even">
<td align="left"><p><strong>/mh</strong></p></td>
<td align="left"><p>Adds data about the handles associated with the target application to the minidump.</p></td>
</tr>
<tr class="odd">
<td align="left"><p><strong>/mu</strong></p></td>
<td align="left"><p>Adds unloaded module information to the minidump. This is only available in Windows Server 2003 and later versions of Windows.</p></td>
</tr>
<tr class="even">
<td align="left"><p><strong>/mt</strong></p></td>
<td align="left"><p>Adds additional thread information to the minidump. This includes thread times, which can be displayed by using [<strong>.ttime (Display Thread Times)</strong>](https://msdn.microsoft.com/library/windows/hardware/ff565506) when debugging the minidump.</p></td>
</tr>
<tr class="odd">
<td align="left"><p><strong>/mi</strong></p></td>
<td align="left"><p>Adds <em>secondary memory</em> to the minidump. Secondary memory is any memory referenced by a pointer on the stack or backing store, plus a small region surrounding this address.</p></td>
</tr>
<tr class="even">
<td align="left"><p><strong>/mp</strong></p></td>
<td align="left"><p>Adds process environment block (PEB) and thread environment block (TEB) data to the minidump. This can be useful if you need access to Windows system information regarding the application's processes and threads.</p></td>
</tr>
<tr class="odd">
<td align="left"><p><strong>/mw</strong></p></td>
<td align="left"><p>Adds all committed read-write private pages to the minidump.</p></td>
</tr>
<tr class="even">
<td align="left"><p><strong>/md</strong></p></td>
<td align="left"><p>Adds all read-write data segments within the executable image to the minidump.</p></td>
</tr>
<tr class="odd">
<td align="left"><p><strong>/mc</strong></p></td>
<td align="left"><p>Adds code sections within images.</p></td>
</tr>
<tr class="even">
<td align="left"><p><strong>/mr</strong></p></td>
<td align="left"><p>Deletes from the minidump those portions of the stack and store memory that are not useful for recreating the stack trace. Local variables and other data type values are deleted as well. This option does not make the minidump smaller (since these memory sections are simply zeroed), but it is useful if you wish to protect the privacy of other applications.</p></td>
</tr>
<tr class="odd">
<td align="left"><p><strong>/mR</strong></p></td>
<td align="left"><p>Deletes the full module paths from the minidump. Only the module <em>names</em> will be included. This is a useful option if you wish to protect the privacy of the user's directory structure.</p></td>
</tr>
<tr class="even">
<td align="left"><p><strong>/mk &quot;</strong> <em>FileName</em> <strong>&quot;</strong></p></td>
<td align="left"><p>(Windows Vista only) Creates a kernel-mode minidump in addition to the user-mode minidump. The kernel-mode minidump will be restricted to the same threads that are stored in the user-mode minidump. <em>FileName</em> must be enclosed in quotation marks.</p></td>
</tr>
</tbody>
</table>

 

These options can be combined. For example, the command **.dump /mfiu** can be used to create a fairly large minidump, or the command **.dump /mrR** can be used to create a minidump that preserves the user's privacy. For full syntax details, see [**.dump (Create Dump File)**](https://msdn.microsoft.com/library/windows/hardware/ff562428).

For details on the internals of minidump files, see the DbgHelp Reference in the Microsoft Windows SDK.

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20[debugger\debugger]:%20Minidumps%20%20RELEASE:%20%284/24/2017%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")




