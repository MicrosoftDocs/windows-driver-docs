---
title: Load Order Groups and Altitudes for Minifilter Drivers
description: Load Order Groups and Altitudes for Minifilter Drivers
ms.assetid: be8f18fe-c80b-44a3-b0c3-f2f630142180
keywords:
- altitudes WDK file system minifilter
- load order groups WDK file system
- start types WDK file system
- driver start types WDK file system
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# Load Order Groups and Altitudes for Minifilter Drivers


Windows uses a dedicated set of load order groups for file system filter drivers and minifilter drivers that are loaded at system startup.

Legacy file system filter drivers can attach only to the top of an existing file system driver stack and cannot attach in the middle of a stack. As a result, the start type for a driver and load order group are important to legacy file system filter drivers, because the earlier a filter driver loads, the lower it can attach on the file system driver stack.

Drivers are loaded first based on the start type for the driver, which represents phases of booting a system. For more information about start types, see "Driver Start Types" in [What Determines When a Driver Is Loaded](what-determines-when-a-driver-is-loaded.md). All file system filter drivers and minifilter drivers that specify a start type of SERVICE\_BOOT\_START will be loaded before drivers with a start type of SERVICE\_SYSTEM\_START or SERVICE\_AUTO\_START. The start type is specified by the **StartType** entry in the ServiceInstall Section of an INF file that is used to install the minifilter driver. Within each start type category, the load order group determines when file system filter drivers and minifilter drivers will be loaded.

A minifilter driver can be loaded at any time. The concept of load order groups is still required by minifilter drivers for interoperability with legacy file system filter drivers. Every minifilter driver must have a unique identifier called *altitude*. The altitude of a minifilter driver defines its position relative to other minifilter drivers in the I/O stack when the minifilter driver is loaded. The altitude is an infinite-precision string interpreted as a decimal number. A minifilter driver that has a low numerical altitude is loaded into the I/O stack below a minifilter driver that has a higher numerical value.

Each load order group has a defined range of altitudes. The allocation of altitudes to minifilter drivers is managed by Microsoft. To request an altitude for your minifilter driver, send an email message to <fsfcomm@microsoft.com> asking for one to be assigned.

A minifilter driver must specify an altitude value from an altitude range that represents a load order group. Altitude values for a minifilter driver are specified in the Instance definitions of the Strings Section in the INF file that is used to install the minifilter driver. Instance definitions can also be specified in calls to the [**InstanceSetupCallback**](https://msdn.microsoft.com/library/windows/hardware/ff551096) routine in the [**FLT\_REGISTRATION**](https://msdn.microsoft.com/library/windows/hardware/ff544811) structure. Multiple instances and altitudes can be defined for a minifilter driver. These instance definitions apply across all volumes.

The following rules about start type and load order groups determine when a minifilter driver will be loaded:

-   A minifilter driver that specifies a particular start type and load order group is loaded at the same time as other file system filter drivers and minifilter drivers in that start type and load order group.

-   Within each load order group, file system filter drivers and minifilter drivers are generally loaded in random order. This normally results in drivers being loaded based on the order in which the driver was installed.

-   If a file system filter driver or minifilter driver does not specify a load order group, it is loaded after all the other drivers of the same start type that do specify a load order group.

The following table lists the system-defined load order groups and altitude ranges for minifilter drivers. For each load order group, the Load order group column contains the value that should be specified for that group in the **LoadOrderGroup** entry in the ServiceInstall Section of a minifilter's INF file. The Altitude range column contains the range of altitudes for a particular load order group. A minifilter driver must request an altitude allocation from Microsoft in the appropriate load order group or groups.

Note that the load order groups and altitude ranges are listed as they appear on the stack, which is the reverse of the order in which they are loaded.

<table>
<colgroup>
<col width="33%" />
<col width="33%" />
<col width="33%" />
</colgroup>
<thead>
<tr class="header">
<th align="left">Load order group</th>
<th align="left">Altitude range</th>
<th align="left">Description</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td align="left"><p>Filter</p></td>
<td align="left"><p>420000-429999</p></td>
<td align="left"><p>This group is the same as the Filter load order group that was available on Windows 2000 and earlier. This group loads last and thus attaches furthest from the file system.</p></td>
</tr>
<tr class="even">
<td align="left"><p>FSFilter Top</p></td>
<td align="left"><p>400000-409999</p></td>
<td align="left"><p>This group is provided for filter drivers that must attach above all other FSFilter types.</p></td>
</tr>
<tr class="odd">
<td align="left"><p>FSFilter Activity Monitor</p></td>
<td align="left"><p>360000-389999</p></td>
<td align="left"><p>This group includes filter drivers that observe and report on file I/O.</p></td>
</tr>
<tr class="even">
<td align="left"><p>FSFilter Undelete</p></td>
<td align="left"><p>340000-349999</p></td>
<td align="left"><p>This group includes filters that recover deleted files.</p></td>
</tr>
<tr class="odd">
<td align="left"><p>FSFilter Anti-Virus</p></td>
<td align="left"><p>320000-329999</p></td>
<td align="left"><p>This group includes filter drivers that detect and disinfect viruses during file I/O.</p></td>
</tr>
<tr class="even">
<td align="left"><p>FSFilter Replication</p></td>
<td align="left"><p>300000-309999</p></td>
<td align="left"><p>This group includes filter drivers that replicate file data to remote servers.</p></td>
</tr>
<tr class="odd">
<td align="left"><p>FSFilter Continuous Backup</p></td>
<td align="left"><p>280000-289999</p></td>
<td align="left"><p>This group includes filter drivers that replicate file data to backup media.</p></td>
</tr>
<tr class="even">
<td align="left"><p>FSFilter Content Screener</p></td>
<td align="left"><p>260000-269999</p></td>
<td align="left"><p>This group includes filter drivers that prevent the creation of specific files or file content.</p></td>
</tr>
<tr class="odd">
<td align="left"><p>FSFilter Quota Management</p></td>
<td align="left"><p>240000-249999</p></td>
<td align="left"><p>This group includes filter drivers that provide enhanced file system quotas.</p></td>
</tr>
<tr class="even">
<td align="left"><p>FSFilter System Recovery</p></td>
<td align="left"><p>220000-229999</p></td>
<td align="left"><p>This group includes filter drivers that perform operations to maintain operating system integrity, such as the System Restore (SR) filter.</p></td>
</tr>
<tr class="odd">
<td align="left"><p>FSFilter Cluster File System</p></td>
<td align="left"><p>200000-209999</p></td>
<td align="left"><p>This group includes filter drivers that are used in products that provide file server metadata across a network.</p></td>
</tr>
<tr class="even">
<td align="left"><p>FSFilter HSM</p></td>
<td align="left"><p>180000-189999</p></td>
<td align="left"><p>This group includes filter drivers that perform hierarchical storage management.</p></td>
</tr>
<tr class="odd">
<td align="left"><p>FSFilter Imaging</p></td>
<td align="left"><p>170000-175000</p></td>
<td align="left"><p>This group includes ZIP-like filter drivers that provide a virtual namespace.</p>
<p>This load group is available on Windows Vista and later versions of the operating system.</p></td>
</tr>
<tr class="even">
<td align="left"><p>FSFilter Compression</p></td>
<td align="left"><p>160000-169999</p></td>
<td align="left"><p>This group includes filter drivers that perform file data compression.</p></td>
</tr>
<tr class="odd">
<td align="left"><p>FSFilter Encryption</p></td>
<td align="left"><p>140000-149999</p></td>
<td align="left"><p>This group includes filter drivers that encrypt and decrypt data during file I/O.</p></td>
</tr>
<tr class="even">
<td align="left"><p>FSFilter Virtualization</p></td>
<td align="left"><p>130000- 139999</p></td>
<td align="left"><p>This group includes filter drivers that virtualize the file path, such as the Least Authorized User (LUA) filter driver added in Windows Vista.</p>
<p>This load group is available on Windows Vista and later versions of the operating system.</p></td>
</tr>
<tr class="odd">
<td align="left"><p>FSFilter Physical Quota Management</p></td>
<td align="left"><p>120000-129999</p></td>
<td align="left"><p>This group includes filter drivers that manage quotas by using physical block counts.</p></td>
</tr>
<tr class="even">
<td align="left"><p>FSFilter Open File</p></td>
<td align="left"><p>100000-109999</p></td>
<td align="left"><p>This group includes filter drivers that provide snapshots of already open files.</p></td>
</tr>
<tr class="odd">
<td align="left"><p>FSFilter Security Enhancer</p></td>
<td align="left"><p>80000-89999</p></td>
<td align="left"><p>This group includes filter drivers that apply lockdown and enhanced access control lists (ACLs).</p></td>
</tr>
<tr class="even">
<td align="left"><p>FSFilter Copy Protection</p></td>
<td align="left"><p>60000-69999</p></td>
<td align="left"><p>This group includes filter drivers that check for out-of-band data on media.</p></td>
</tr>
<tr class="odd">
<td align="left"><p>FSFilter Bottom</p></td>
<td align="left"><p>40000-49999</p></td>
<td align="left"><p>This group is provided for filter drivers that must attach below all other FSFilter types.</p></td>
</tr>
<tr class="even">
<td align="left"><p>FSFilter System</p></td>
<td align="left"><p>20000-29999</p></td>
<td align="left"><p>Reserved for internal use.</p></td>
</tr>
<tr class="odd">
<td align="left"><p>FSFilter Infrastructure</p></td>
<td align="left"></td>
<td align="left"><p>Reserved for internal use. This group loads first and thus attaches closest to the file system.</p></td>
</tr>
</tbody>
</table>

 

 

 




