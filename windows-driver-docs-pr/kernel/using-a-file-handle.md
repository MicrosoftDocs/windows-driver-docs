---
title: Using a File Handle
description: Using a File Handle
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
<td><p><a href="/windows-hardware/drivers/ddi/ntifs/nf-ntifs-ntreadfile" data-raw-source="[&lt;strong&gt;ZwReadFile&lt;/strong&gt;](/windows-hardware/drivers/ddi/ntifs/nf-ntifs-ntreadfile)"><strong>ZwReadFile</strong></a></p></td>
</tr>
<tr class="even">
<td><p>Write data to the file.</p></td>
<td><p><a href="/windows-hardware/drivers/ddi/ntifs/nf-ntifs-ntwritefile" data-raw-source="[&lt;strong&gt;ZwWriteFile&lt;/strong&gt;](/windows-hardware/drivers/ddi/ntifs/nf-ntifs-ntwritefile)"><strong>ZwWriteFile</strong></a></p></td>
</tr>
<tr class="odd">
<td><p>Read metadata for the file or file handle.</p></td>
<td><p><a href="/windows-hardware/drivers/ddi/ntifs/nf-ntifs-ntqueryinformationfile" data-raw-source="[&lt;strong&gt;ZwQueryInformationFile&lt;/strong&gt;](/windows-hardware/drivers/ddi/ntifs/nf-ntifs-ntqueryinformationfile)"><strong>ZwQueryInformationFile</strong></a></p></td>
</tr>
<tr class="even">
<td><p>Write metadata for the file or file handle.</p></td>
<td><p><a href="/windows-hardware/drivers/ddi/ntifs/nf-ntifs-ntsetinformationfile" data-raw-source="[&lt;strong&gt;ZwSetInformationFile&lt;/strong&gt;](/windows-hardware/drivers/ddi/ntifs/nf-ntifs-ntsetinformationfile)"><strong>ZwSetInformationFile</strong></a></p></td>
</tr>
</tbody>
</table>

 

To indicate where in the file to begin reading or writing data, you pass a *ByteOffset* parameter to **ZwReadFile** or **ZwWriteFile**, respectively.

If you opened the handle with FILE\_APPEND\_DATA access, all data is written to the end of the file, and the *ByteOffset* parameter is ignored.

Under certain conditions, the I/O manager maintains a current file-position pointer for the file. You can begin a read or write operation at that position by specifying **NULL** for *ByteOffset*. For more information about when the current file-position pointer exists, see [Using the Current File Position](using-the-current-file-position.md) later in this section.

To examine or change information about a file, call [**ZwQueryInformationFile**](/windows-hardware/drivers/ddi/ntifs/nf-ntifs-ntqueryinformationfile) or [**ZwSetInformationFile**](/windows-hardware/drivers/ddi/ntifs/nf-ntifs-ntsetinformationfile), respectively. You specify the particular type of information as the *FileInformationClass* parameter to each routine. For example, setting *FileInformationClass* to **FileBasicInformation** allows you to examine or change a [**FILE\_BASIC\_INFORMATION**](/windows-hardware/drivers/ddi/wdm/ns-wdm-_file_basic_information) structure, which contains members for the file-creation time and the last-access time, among others. For information about all the possible values for *FileInformationClass*, see [**FILE\_INFORMATION\_CLASS**](/windows-hardware/drivers/ddi/wdm/ne-wdm-_file_information_class).

