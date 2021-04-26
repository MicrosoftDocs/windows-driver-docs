---
title: Disk-Space List Functions
description: Disk-Space List Functions
keywords:
- SetupAPI functions WDK , disk-space lists
- disk-space lists WDK SetupAPI
- calculating disk space WDK SetupAPI
- space calculations WDK SetupAPI
- disk space calculations WDK SetupAPI
- total disk space calculations WDK SetupAPI
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# Disk-Space List Functions





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
<td align="left"><p><a href="/windows/win32/api/setupapi/nf-setupapi-setupaddinstallsectiontodiskspacelista" data-raw-source="[&lt;strong&gt;SetupAddInstallSectionToDiskSpaceList&lt;/strong&gt;](/windows/win32/api/setupapi/nf-setupapi-setupaddinstallsectiontodiskspacelista)"><strong>SetupAddInstallSectionToDiskSpaceList</strong></a></p></td>
<td align="left"><p>Searches for <strong>CopyFile</strong> and <strong>DelFile</strong> directives in a <em>DDInstall</em> section of an INF file, then adds the file operations specified in those sections to a disk-space list.</p></td>
</tr>
<tr class="even">
<td align="left"><p><a href="/windows/win32/api/setupapi/nf-setupapi-setupaddsectiontodiskspacelista" data-raw-source="[&lt;strong&gt;SetupAddSectionToDiskSpaceList&lt;/strong&gt;](/windows/win32/api/setupapi/nf-setupapi-setupaddsectiontodiskspacelista)"><strong>SetupAddSectionToDiskSpaceList</strong></a></p></td>
<td align="left"><p>Adds to a disk-space list all the file copy or delete operations that are listed in a specified section of an INF file.</p></td>
</tr>
<tr class="odd">
<td align="left"><p><a href="/windows/win32/api/setupapi/nf-setupapi-setupaddtodiskspacelista" data-raw-source="[&lt;strong&gt;SetupAddToDiskSpaceList&lt;/strong&gt;](/windows/win32/api/setupapi/nf-setupapi-setupaddtodiskspacelista)"><strong>SetupAddToDiskSpaceList</strong></a></p></td>
<td align="left"><p>Adds a single delete or copy operation to a disk-space list.</p></td>
</tr>
<tr class="even">
<td align="left"><p><a href="/windows/win32/api/setupapi/nf-setupapi-setupcreatediskspacelista" data-raw-source="[&lt;strong&gt;SetupCreateDiskSpaceList&lt;/strong&gt;](/windows/win32/api/setupapi/nf-setupapi-setupcreatediskspacelista)"><strong>SetupCreateDiskSpaceList</strong></a></p></td>
<td align="left"><p>Creates a disk-space list.</p></td>
</tr>
<tr class="odd">
<td align="left"><p><a href="/windows/win32/api/setupapi/nf-setupapi-setupdestroydiskspacelist" data-raw-source="[&lt;strong&gt;SetupDestroyDiskSpaceList&lt;/strong&gt;](/windows/win32/api/setupapi/nf-setupapi-setupdestroydiskspacelist)"><strong>SetupDestroyDiskSpaceList</strong></a></p></td>
<td align="left"><p>Destroys a disk-space list and releases the resources allocated to it.</p></td>
</tr>
<tr class="even">
<td align="left"><p><a href="/windows/win32/api/setupapi/nf-setupapi-setupquerydrivesindiskspacelista" data-raw-source="[&lt;strong&gt;SetupQueryDrivesInDiskSpaceList&lt;/strong&gt;](/windows/win32/api/setupapi/nf-setupapi-setupquerydrivesindiskspacelista)"><strong>SetupQueryDrivesInDiskSpaceList</strong></a></p></td>
<td align="left"><p>Fills a caller-supplied buffer with a list of the drives referenced by the file operations that are listed in the disk-space list.</p></td>
</tr>
<tr class="odd">
<td align="left"><p><a href="/windows/win32/api/setupapi/nf-setupapi-setupqueryspacerequiredondrivea" data-raw-source="[&lt;strong&gt;SetupQuerySpaceRequiredOnDrive&lt;/strong&gt;](/windows/win32/api/setupapi/nf-setupapi-setupqueryspacerequiredondrivea)"><strong>SetupQuerySpaceRequiredOnDrive</strong></a></p></td>
<td align="left"><p>Examines a disk-space list to determine the space that is required to perform all the file operations that are listed for a particular drive.</p></td>
</tr>
<tr class="even">
<td align="left"><p><a href="/windows/win32/api/setupapi/nf-setupapi-setupremovefromdiskspacelista" data-raw-source="[&lt;strong&gt;SetupRemoveFromDiskSpaceList&lt;/strong&gt;](/windows/win32/api/setupapi/nf-setupapi-setupremovefromdiskspacelista)"><strong>SetupRemoveFromDiskSpaceList</strong></a></p></td>
<td align="left"><p>Removes a file copy or delete operation from a disk-space list.</p></td>
</tr>
<tr class="odd">
<td align="left"><p><a href="/windows/win32/api/setupapi/nf-setupapi-setupremoveinstallsectionfromdiskspacelista" data-raw-source="[&lt;strong&gt;SetupRemoveInstallSectionFromDiskSpaceList&lt;/strong&gt;](/windows/win32/api/setupapi/nf-setupapi-setupremoveinstallsectionfromdiskspacelista)"><strong>SetupRemoveInstallSectionFromDiskSpaceList</strong></a></p></td>
<td align="left"><p>Searches for <strong>CopyFiles</strong> and <strong>DelFiles</strong> directives in a <em>DDInstall</em> section of an INF file, and removes the file operations specified in those sections from a disk-space list.</p></td>
</tr>
<tr class="even">
<td align="left"><p><strong>SetupRemoveSectionFromDiskSpaceList</strong></p></td>
<td align="left"><p>Removes from a disk-space list the file copy or delete operations that are listed in a specified section of an INF file.</p></td>
</tr>
</tbody>
</table>

 

