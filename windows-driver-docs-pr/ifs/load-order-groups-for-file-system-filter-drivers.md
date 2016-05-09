---
title: Load Order Groups for File System Filter Drivers
description: Load Order Groups for File System Filter Drivers
ms.assetid: 57c9e4c6-186c-464f-ac83-c0669d46b189
keywords: ["filter drivers WDK file system , driver loading", "file system filter drivers WDK , driver loading", "driver loading WDK file system", "loading drivers WDK file system", "load order groups WDK file system"]
---

# Load Order Groups for File System Filter Drivers


## <span id="ddk_file_system_filter_driver_load_order_groups_if"></span><span id="DDK_FILE_SYSTEM_FILTER_DRIVER_LOAD_ORDER_GROUPS_IF"></span>


Microsoft Windows XP and later operating systems provide a dedicated set of load order groups for file system filter drivers that are loaded at system startup time. On operating systems before Windows XP, filter drivers could use only the "filter" and "file system" load order groups.

A filter can attach only to the top of an existing file system driver stack and cannot attach in the middle of a stack. As a result, load order groups are important to file system filter drivers, because the earlier a filter driver loads, the lower it can attach on the file system driver stack.

The following rules about load order groups determine when a file system filter driver will be loaded:

-   A file system filter driver that specifies a particular load order group is loaded at the same time as other filter drivers in that group.

-   Within each load order group, filter drivers are loaded in random order.

-   If a file system filter driver does not specify a load order group, it is loaded after all of the other drivers of the same start type that do specify a load order group.

The following table lists the system-defined load order groups for file system filter drivers. For each load order group, the Load Order Group column contains the value that should be specified for that group in the **LoadOrderGroup** entry in the [**Version section**](https://msdn.microsoft.com/library/windows/hardware/ff547502) of a filter's INF file.

Note that the load order groups are listed as they appear on the stack, which is the reverse of the order in which they are loaded.

<table>
<colgroup>
<col width="50%" />
<col width="50%" />
</colgroup>
<thead>
<tr class="header">
<th align="left">Load order group</th>
<th align="left">Description</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td align="left"><p>Filter</p></td>
<td align="left"><p>This group is the same as the &quot;filter&quot; load order group that was available on Windows 2000 and earlier. This group loads last and thus attaches furthest from the file system.</p></td>
</tr>
<tr class="even">
<td align="left"><p>FSFilter Top</p></td>
<td align="left"><p>This group is provided for filter drivers that must attach above all other FSFilter types.</p></td>
</tr>
<tr class="odd">
<td align="left"><p>FSFilter Activity Monitor</p></td>
<td align="left"><p>This group includes filter drivers that observe and report on file I/O.</p></td>
</tr>
<tr class="even">
<td align="left"><p>FSFilter Undelete</p></td>
<td align="left"><p>This group includes filter drivers that recover deleted files.</p></td>
</tr>
<tr class="odd">
<td align="left"><p>FSFilter Anti-Virus</p></td>
<td align="left"><p>This group includes filters that detect and disinfect viruses during file I/O.</p></td>
</tr>
<tr class="even">
<td align="left"><p>FSFilter Replication</p></td>
<td align="left"><p>This group includes filter drivers that replicate file data to remote servers.</p></td>
</tr>
<tr class="odd">
<td align="left"><p>FSFilter Continuous Backup</p></td>
<td align="left"><p>This group includes filter drivers that replicate file data to backup media.</p></td>
</tr>
<tr class="even">
<td align="left"><p>FSFilter Content Screener</p></td>
<td align="left"><p>This group includes filter drivers that prevent the creation of specific files or file content.</p></td>
</tr>
<tr class="odd">
<td align="left"><p>FSFilter Quota Management</p></td>
<td align="left"><p>This group includes filter drivers that provide enhanced file system quotas.</p></td>
</tr>
<tr class="even">
<td align="left"><p>FSFilter System Recovery</p></td>
<td align="left"><p>This group includes filter drivers that perform operations to maintain operating system integrity, such as the System Restore (SR) filter.</p></td>
</tr>
<tr class="odd">
<td align="left"><p>FSFilter Cluster File System</p></td>
<td align="left"><p>This group includes filter drivers that are used in products that provide file server metadata across a network.</p></td>
</tr>
<tr class="even">
<td align="left"><p>FSFilter HSM</p></td>
<td align="left"><p>This group includes filter drivers that perform hierarchical storage management.</p></td>
</tr>
<tr class="odd">
<td align="left"><p>FSFilter Imaging</p></td>
<td align="left"><p>This group includes ZIP-like filter drivers that provide a virtual namespace.</p>
<p>This load group is available on Windows Vista and later versions of the operating system.</p></td>
</tr>
<tr class="even">
<td align="left"><p>FSFilter Compression</p></td>
<td align="left"><p>This group includes filter drivers that perform file data compression.</p></td>
</tr>
<tr class="odd">
<td align="left"><p>FSFilter Encryption</p></td>
<td align="left"><p>This group includes filter drivers that encrypt and decrypt data during file I/O.</p></td>
</tr>
<tr class="even">
<td align="left"><p>FSFilter Virtualization</p></td>
<td align="left"><p>This group includes filter drivers that virtualize the file path, such as the Least Authorized User (LUA) filter driver added in Windows Vista.</p>
<p>This load group is available on Windows Vista and later versions of the operating system.</p></td>
</tr>
<tr class="odd">
<td align="left"><p>FSFilter Physical Quota Management</p></td>
<td align="left"><p>This group includes filter drivers that manage quotas by using physical block counts.</p></td>
</tr>
<tr class="even">
<td align="left"><p>FSFilter Open File</p></td>
<td align="left"><p>This group includes filter drivers that provide snapshots of already open files.</p></td>
</tr>
<tr class="odd">
<td align="left"><p>FSFilter Security Enhancer</p></td>
<td align="left"><p>This group includes filter drivers that apply lockdown and enhanced access control lists (ACLs).</p></td>
</tr>
<tr class="even">
<td align="left"><p>FSFilter Copy Protection</p></td>
<td align="left"><p>This group includes filter drivers that check for out-of-band data on media.</p></td>
</tr>
<tr class="odd">
<td align="left"><p>FSFilter Bottom</p></td>
<td align="left"><p>This group is provided for filter drivers that must attach below all other FSFilter types.</p></td>
</tr>
<tr class="even">
<td align="left"><p>FSFilter System</p></td>
<td align="left"><p>Reserved for internal use. This group includes the HSM and SIS filter drivers.</p></td>
</tr>
<tr class="odd">
<td align="left"><p>FSFilter Infrastructure</p></td>
<td align="left"><p>Reserved for internal use. This group loads first and thus attaches closest to the file system.</p></td>
</tr>
</tbody>
</table>

 

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20[ifsk\ifsk]:%20Load%20Order%20Groups%20for%20File%20System%20Filter%20Drivers%20%20%20RELEASE:%20%285/9/2016%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")




