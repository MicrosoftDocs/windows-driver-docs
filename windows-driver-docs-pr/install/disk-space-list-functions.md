---
title: Disk-Space List Functions
description: Disk-Space List Functions
ms.assetid: 850e9f41-b534-49f3-891d-c12c1126e52f
keywords:
- SetupAPI functions WDK , disk-space lists
- disk-space lists WDK SetupAPI
- calculating disk space WDK SetupAPI
- space calculations WDK SetupAPI
- disk space calculations WDK SetupAPI
- total disk space calculations WDK SetupAPI
ms.author: windowsdriverdev
ms.date: 04/20/2017
ms.topic: article
ms.prod: windows-hardware
ms.technology: windows-devices
---

# Disk-Space List Functions


## <a href="" id="ddk-disk-space-list-functions-dg"></a>


Disk-space list functions are used to create and modify disk-space lists. These lists can be used to calculate the total disk space that is required to handle the files that will be copied or deleted during the installation procedure.

The following table lists the functions that can be used to manipulate disk-space lists. For detailed function descriptions, see the Microsoft Windows SDK documentation.

<table>
<colgroup>
<col width="50%" />
<col width="50%" />
</colgroup>
<thead>
<tr class="header">
<th align="left">Function</th>
<th align="left">Description</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td align="left"><p>[<strong>SetupAddInstallSectionToDiskSpaceList</strong>](https://msdn.microsoft.com/library/windows/desktop/aa376978)</p></td>
<td align="left"><p>Searches for <strong>CopyFile</strong> and <strong>DelFile</strong> directives in a <em>DDInstall</em> section of an INF file, then adds the file operations specified in those sections to a disk-space list.</p></td>
</tr>
<tr class="even">
<td align="left"><p>[<strong>SetupAddSectionToDiskSpaceList</strong>](https://msdn.microsoft.com/library/windows/desktop/aa376979)</p></td>
<td align="left"><p>Adds to a disk-space list all the file copy or delete operations that are listed in a specified section of an INF file.</p></td>
</tr>
<tr class="odd">
<td align="left"><p>[<strong>SetupAddToDiskSpaceList</strong>](https://msdn.microsoft.com/library/windows/desktop/aa376980)</p></td>
<td align="left"><p>Adds a single delete or copy operation to a disk-space list.</p></td>
</tr>
<tr class="even">
<td align="left"><p>[<strong>SetupCreateDiskSpaceList</strong>](https://msdn.microsoft.com/library/windows/desktop/aa376991)</p></td>
<td align="left"><p>Creates a disk-space list.</p></td>
</tr>
<tr class="odd">
<td align="left"><p>[<strong>SetupDestroyDiskSpaceList</strong>](https://msdn.microsoft.com/library/windows/desktop/aa376995)</p></td>
<td align="left"><p>Destroys a disk-space list and releases the resources allocated to it.</p></td>
</tr>
<tr class="even">
<td align="left"><p>[<strong>SetupQueryDrivesInDiskSpaceList</strong>](https://msdn.microsoft.com/library/windows/desktop/aa377414)</p></td>
<td align="left"><p>Fills a caller-supplied buffer with a list of the drives referenced by the file operations that are listed in the disk-space list.</p></td>
</tr>
<tr class="odd">
<td align="left"><p>[<strong>SetupQuerySpaceRequiredOnDrive</strong>](https://msdn.microsoft.com/library/windows/desktop/aa377420)</p></td>
<td align="left"><p>Examines a disk-space list to determine the space that is required to perform all the file operations that are listed for a particular drive.</p></td>
</tr>
<tr class="even">
<td align="left"><p>[<strong>SetupRemoveFromDiskSpaceList</strong>](https://msdn.microsoft.com/library/windows/desktop/aa377430)</p></td>
<td align="left"><p>Removes a file copy or delete operation from a disk-space list.</p></td>
</tr>
<tr class="odd">
<td align="left"><p>[<strong>SetupRemoveInstallSectionFromDiskSpaceList</strong>](https://msdn.microsoft.com/library/windows/desktop/aa377432)</p></td>
<td align="left"><p>Searches for <strong>CopyFiles</strong> and <strong>DelFiles</strong> directives in a <em>DDInstall</em> section of an INF file, and removes the file operations specified in those sections from a disk-space list.</p></td>
</tr>
<tr class="even">
<td align="left"><p><strong>SetupRemoveSectionFromDiskSpaceList</strong></p></td>
<td align="left"><p>Removes from a disk-space list the file copy or delete operations that are listed in a specified section of an INF file.</p></td>
</tr>
</tbody>
</table>

 

 

 





