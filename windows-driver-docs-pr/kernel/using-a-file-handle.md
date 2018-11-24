---
title: Using a File Handle
description: Using a File Handle
ms.assetid: f5a4d3f6-b74f-411e-9fa9-a41d83152fd7
keywords: ["files WDK kernel", "file objects WDK kernel", "objects WDK file objects", "file handles WDK kernel", "handle to file WDK kernel"]
ms.date: 06/16/2017
ms.localizationpriority: medium
---

# Using a File Handle





The following table lists the operations that drivers can perform on a file handle and the corresponding routines that carry out those operations.

<table>
<colgroup>
<col width="50%" />
<col width="50%" />
</colgroup>
<thead>
<tr class="header">
<th>Operation</th>
<th>Routine to call</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><p>Read data from the file.</p></td>
<td><p><a href="https://msdn.microsoft.com/library/windows/hardware/ff567072" data-raw-source="[&lt;strong&gt;ZwReadFile&lt;/strong&gt;](https://msdn.microsoft.com/library/windows/hardware/ff567072)"><strong>ZwReadFile</strong></a></p></td>
</tr>
<tr class="even">
<td><p>Write data to the file.</p></td>
<td><p><a href="https://msdn.microsoft.com/library/windows/hardware/ff567121" data-raw-source="[&lt;strong&gt;ZwWriteFile&lt;/strong&gt;](https://msdn.microsoft.com/library/windows/hardware/ff567121)"><strong>ZwWriteFile</strong></a></p></td>
</tr>
<tr class="odd">
<td><p>Read metadata for the file or file handle.</p></td>
<td><p><a href="https://msdn.microsoft.com/library/windows/hardware/ff567052" data-raw-source="[&lt;strong&gt;ZwQueryInformationFile&lt;/strong&gt;](https://msdn.microsoft.com/library/windows/hardware/ff567052)"><strong>ZwQueryInformationFile</strong></a></p></td>
</tr>
<tr class="even">
<td><p>Write metadata for the file or file handle.</p></td>
<td><p><a href="https://msdn.microsoft.com/library/windows/hardware/ff567096" data-raw-source="[&lt;strong&gt;ZwSetInformationFile&lt;/strong&gt;](https://msdn.microsoft.com/library/windows/hardware/ff567096)"><strong>ZwSetInformationFile</strong></a></p></td>
</tr>
</tbody>
</table>

 

To indicate where in the file to begin reading or writing data, you pass a *ByteOffset* parameter to **ZwReadFile** or **ZwWriteFile**, respectively.

If you opened the handle with FILE\_APPEND\_DATA access, all data is written to the end of the file, and the *ByteOffset* parameter is ignored.

Under certain conditions, the I/O manager maintains a current file-position pointer for the file. You can begin a read or write operation at that position by specifying **NULL** for *ByteOffset*. For more information about when the current file-position pointer exists, see [Using the Current File Position](using-the-current-file-position.md) later in this section.

To examine or change information about a file, call [**ZwQueryInformationFile**](https://msdn.microsoft.com/library/windows/hardware/ff567052) or [**ZwSetInformationFile**](https://msdn.microsoft.com/library/windows/hardware/ff567096), respectively. You specify the particular type of information as the *FileInformationClass* parameter to each routine. For example, setting *FileInformationClass* to **FileBasicInformation** allows you to examine or change a [**FILE\_BASIC\_INFORMATION**](https://msdn.microsoft.com/library/windows/hardware/ff545762) structure, which contains members for the file-creation time and the last-access time, among others. For information about all the possible values for *FileInformationClass*, see [**FILE\_INFORMATION\_CLASS**](https://msdn.microsoft.com/library/windows/hardware/ff728840).

 

 




