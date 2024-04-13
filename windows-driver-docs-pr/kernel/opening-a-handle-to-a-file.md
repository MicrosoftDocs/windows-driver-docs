---
title: Opening a Handle to a File
description: Opening a Handle to a File
keywords: ["files WDK kernel", "file objects WDK kernel", "objects WDK file objects", "file handles WDK kernel", "handle to file WDK kernel", "opening handle to file"]
ms.date: 06/16/2017
---

# Opening a Handle to a File





To open a handle to a file, perform the following steps:

1.  Create an [**OBJECT\_ATTRIBUTES**](/windows/win32/api/ntdef/ns-ntdef-_object_attributes) structure, and call the [**InitializeObjectAttributes**](/windows/win32/api/ntdef/nf-ntdef-initializeobjectattributes) macro to initialize the structure. You specify the file's object name as the *ObjectName* parameter to **InitializeObjectAttributes**.

2.  Open a handle to the file by passing the **OBJECT\_ATTRIBUTES** structure to [**IoCreateFile**](/windows-hardware/drivers/ddi/wdm/nf-wdm-iocreatefile), [**ZwCreateFile**](/windows-hardware/drivers/ddi/ntifs/nf-ntifs-ntcreatefile), or [**ZwOpenFile**](/windows-hardware/drivers/ddi/ntifs/nf-ntifs-ntopenfile).

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

 

For more information about the values available for *DesiredAccess*, see [**ZwCreateFile**](/windows-hardware/drivers/ddi/ntifs/nf-ntifs-ntcreatefile).

 

