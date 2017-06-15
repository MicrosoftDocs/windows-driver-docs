---
title: Using a File Handle
author: windows-driver-content
description: Using a File Handle
MS-HAID:
- 'Other\_bebd0839-cc3a-4771-a8ad-051f73a43eaa.xml'
- 'kernel.using\_a\_file\_handle'
MSHAttr:
- 'PreferredSiteName:MSDN'
- 'PreferredLib:/library/windows/hardware'
ms.assetid: f5a4d3f6-b74f-411e-9fa9-a41d83152fd7
keywords: ["files WDK kernel", "file objects WDK kernel", "objects WDK file objects", "file handles WDK kernel", "handle to file WDK kernel"]
---

# Using a File Handle


## <a href="" id="ddk-using-a-file-handle-kg"></a>


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
<td><p>[<strong>ZwReadFile</strong>](https://msdn.microsoft.com/library/windows/hardware/ff567072)</p></td>
</tr>
<tr class="even">
<td><p>Write data to the file.</p></td>
<td><p>[<strong>ZwWriteFile</strong>](https://msdn.microsoft.com/library/windows/hardware/ff567121)</p></td>
</tr>
<tr class="odd">
<td><p>Read metadata for the file or file handle.</p></td>
<td><p>[<strong>ZwQueryInformationFile</strong>](https://msdn.microsoft.com/library/windows/hardware/ff567052)</p></td>
</tr>
<tr class="even">
<td><p>Write metadata for the file or file handle.</p></td>
<td><p>[<strong>ZwSetInformationFile</strong>](https://msdn.microsoft.com/library/windows/hardware/ff567096)</p></td>
</tr>
</tbody>
</table>

 

To indicate where in the file to begin reading or writing data, you pass a *ByteOffset* parameter to **ZwReadFile** or **ZwWriteFile**, respectively.

If you opened the handle with FILE\_APPEND\_DATA access, all data is written to the end of the file, and the *ByteOffset* parameter is ignored.

Under certain conditions, the I/O manager maintains a current file-position pointer for the file. You can begin a read or write operation at that position by specifying **NULL** for *ByteOffset*. For more information about when the current file-position pointer exists, see [Using the Current File Position](using-the-current-file-position.md) later in this section.

To examine or change information about a file, call [**ZwQueryInformationFile**](https://msdn.microsoft.com/library/windows/hardware/ff567052) or [**ZwSetInformationFile**](https://msdn.microsoft.com/library/windows/hardware/ff567096), respectively. You specify the particular type of information as the *FileInformationClass* parameter to each routine. For example, setting *FileInformationClass* to **FileBasicInformation** allows you to examine or change a [**FILE\_BASIC\_INFORMATION**](https://msdn.microsoft.com/library/windows/hardware/ff545762) structure, which contains members for the file-creation time and the last-access time, among others. For information about all the possible values for *FileInformationClass*, see [**FILE\_INFORMATION\_CLASS**](https://msdn.microsoft.com/library/windows/hardware/ff728840).

 

 


--------------------
[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bkernel\kernel%5D:%20Using%20a%20File%20Handle%20%20RELEASE:%20%286/14/2017%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")


