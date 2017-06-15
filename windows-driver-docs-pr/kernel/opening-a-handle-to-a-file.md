---
title: Opening a Handle to a File
author: windows-driver-content
description: Opening a Handle to a File
MS-HAID:
- 'Other\_c81e36e0-df88-46cf-a80e-a377ee0de186.xml'
- 'kernel.opening\_a\_handle\_to\_a\_file'
MSHAttr:
- 'PreferredSiteName:MSDN'
- 'PreferredLib:/library/windows/hardware'
ms.assetid: 9378282a-ee29-44b6-b206-602eee94ec3b
keywords: ["files WDK kernel", "file objects WDK kernel", "objects WDK file objects", "file handles WDK kernel", "handle to file WDK kernel", "opening handle to file"]
---

# Opening a Handle to a File


## <a href="" id="ddk-opening-a-handle-to-a-file-kg"></a>


To open a handle to a file, perform the following steps:

1.  Create an [**OBJECT\_ATTRIBUTES**](https://msdn.microsoft.com/library/windows/hardware/ff557749) structure, and call the [**InitializeObjectAttributes**](https://msdn.microsoft.com/library/windows/hardware/ff547804) macro to initialize the structure. You specify the file's object name as the *ObjectName* parameter to **InitializeObjectAttributes**.

2.  Open a handle to the file by passing the **OBJECT\_ATTRIBUTES** structure to [**IoCreateFile**](https://msdn.microsoft.com/library/windows/hardware/ff548418), [**ZwCreateFile**](https://msdn.microsoft.com/library/windows/hardware/ff566424), or [**ZwOpenFile**](https://msdn.microsoft.com/library/windows/hardware/ff567011).

    If the file does not exist, **IoCreateFile** and **ZwCreateFile** will create it, whereas **ZwOpenFile** will return STATUS\_OBJECT\_NAME\_NOT\_FOUND.

Note that drivers almost always use **ZwCreateFile** or **ZwOpenFile** rather than **IoCreateFile**.

When you call **IoCreateFile**, **ZwCreateFile**, or **ZwOpenFile**, the Windows executive creates a new file object to represent the file, and it provides an open handle to the object. This file object persists until you close all the open handles to it.

Whichever routine you call, you must pass the access rights you need as the *DesiredAccess* parameter. These rights must cover all the operations that your driver will perform. The following table lists these operations and the corresponding access right to request.

<table>
<colgroup>
<col width="50%" />
<col width="50%" />
</colgroup>
<thead>
<tr class="header">
<th>Operation</th>
<th>Required access right</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><p>Read from the file.</p></td>
<td><p>FILE_READ_DATA or GENERIC_READ</p></td>
</tr>
<tr class="even">
<td><p>Write to the file.</p></td>
<td><p>FILE_WRITE_DATA or GENERIC_WRITE</p></td>
</tr>
<tr class="odd">
<td><p>Write only to the end of the file.</p></td>
<td><p>FILE_APPEND_DATA</p></td>
</tr>
<tr class="even">
<td><p>Read the file's metadata, such as the file's creation time.</p></td>
<td><p>FILE_READ_ATTRIBUTES or GENERIC_READ</p></td>
</tr>
<tr class="odd">
<td><p>Write the file's metadata, such as the file's creation time.</p></td>
<td><p>FILE_WRITE_ATTRIBUTES or GENERIC_WRITE</p></td>
</tr>
</tbody>
</table>

 

For more information about the values available for *DesiredAccess*, see [**ZwCreateFile**](https://msdn.microsoft.com/library/windows/hardware/ff566424).

 

 


--------------------
[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bkernel\kernel%5D:%20Opening%20a%20Handle%20to%20a%20File%20%20RELEASE:%20%286/14/2017%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")


