---
title: Storage Kernel Debugger Extensions
description: The storage kernel debugger extensions (storagekd) are used for debugging the storage drivers on Windows 8 and above operating system (OS) targets.
ms.assetid: 8EF83BC8-6ABB-496C-98A6-EF0298D78F76
ms.author: domars
ms.date: 11/28/2017
ms.localizationpriority: medium
---

# Storage Kernel Debugger Extensions


The storage kernel debugger extensions (storagekd) are used for debugging the storage drivers on Windows 8 and above operating system (OS) targets.

Extension commands that are useful for debugging storage drivers, via classpnp managed storage class drivers and Storport managed storage miniport drivers, can be found in **Storagekd.dll**.

Please refer to [SCSI Miniport Extensions (Scsikd.dll and Minipkd.dll)](scsi-miniport-extensions--scsikd-dll-and-minipkd-dll-.md) for debugging needs for Windows 7 and below version of OS targets.

**Important**  You need special symbols to use this extension. For more information, see [Debugging Tools for Windows](index.md).

 

## <span id="Storage_kernel_debugger_extension_commands"></span><span id="storage_kernel_debugger_extension_commands"></span><span id="STORAGE_KERNEL_DEBUGGER_EXTENSION_COMMANDS"></span>Storage kernel debugger extension commands


<table>
<colgroup>
<col width="50%" />
<col width="50%" />
</colgroup>
<thead>
<tr class="header">
<th align="left">Command</th>
<th align="left">Description</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td align="left"><p><span id="_storagekd.storhelp"></span><span id="_STORAGEKD.STORHELP"></span><strong><a href="-storagekd-storhelp.md" data-raw-source="[!storagekd.storhelp](-storagekd-storhelp.md)">!storagekd.storhelp</a></strong></p></td>
<td align="left"><p>Displays help text for <strong>Storagekd.dll</strong> extension commands.</p></td>
</tr>
<tr class="even">
<td align="left"><p><span id="_storagekd.storclass"></span><span id="_STORAGEKD.STORCLASS"></span><strong><a href="-storagekd-storclass.md" data-raw-source="[!storagekd.storclass](-storagekd-storclass.md)">!storagekd.storclass</a></strong></p></td>
<td align="left"><p>Displays information about the specified <em>classpnp</em> device.</p></td>
</tr>
<tr class="odd">
<td align="left"><p><span id="_storagekd.storadapter"></span><span id="_STORAGEKD.STORADAPTER"></span><strong><a href="-storagekd-storadapter.md" data-raw-source="[!storagekd.storadapter](-storagekd-storadapter.md)">!storagekd.storadapter</a></strong></p></td>
<td align="left"><p>Displays information about the specified <em>Storport</em> adapter.</p></td>
</tr>
<tr class="even">
<td align="left"><p><span id="_storagekd.storunit"></span><span id="_STORAGEKD.STORUNIT"></span><strong><a href="-storagekd-storunit.md" data-raw-source="[!storagekd.storunit](-storagekd-storunit.md)">!storagekd.storunit</a></strong></p></td>
<td align="left"><p>Displays information about the specified <em>Storport</em> logical unit.</p></td>
</tr>
<tr class="odd">
<td align="left"><p><span id="_storagekd.storloglist"></span><span id="_STORAGEKD.STORLOGLIST"></span><strong><a href="-storagekd-storloglist.md" data-raw-source="[!storagekd.storloglist](-storagekd-storloglist.md)">!storagekd.storloglist</a></strong></p></td>
<td align="left"><p>Displays the <em>Storport</em> adapter’s internal log entries.</p></td>
</tr>
<tr class="even">
<td align="left"><p><span id="_storagekd.storlogirp"></span><span id="_STORAGEKD.STORLOGIRP"></span><strong><a href="-storagekd-storlogirp.md" data-raw-source="[!storagekd.storlogirp](-storagekd-storlogirp.md)">!storagekd.storlogirp</a></strong></p></td>
<td align="left"><p>Displays the <em>Storport’s</em> internal log entries for the adapter filtered for the IRP provided.</p></td>
</tr>
<tr class="odd">
<td align="left"><p><span id="_storagekd.storlogsrb"></span><span id="_STORAGEKD.STORLOGSRB"></span><strong><a href="-storagekd-storlogsrb.md" data-raw-source="[!storagekd.storlogsrb](-storagekd-storlogsrb.md)">!storagekd.storlogsrb</a></strong></p></td>
<td align="left"><p>Displays the <em>Storport’s</em> internal log entries for the adapter filtered for the Storage (or SCSI) Request Block (SRB) provided.</p></td>
</tr>
<tr class="even">
<td align="left"><p><span id="_storagekd.storsrb"></span><span id="_STORAGEKD.STORSRB"></span><strong><a href="-storagekd-storsrb.md" data-raw-source="[!storagekd.storsrb](-storagekd-storsrb.md)">!storagekd.storsrb</a></strong></p></td>
<td align="left"><p>Displays information about the specified Storage (or SCSI) Request Block (SRB).</p></td>
</tr>
</tbody>
</table>

 

 

 





