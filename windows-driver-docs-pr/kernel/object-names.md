---
title: Object Names
author: windows-driver-content
description: Object Names
ms.assetid: b30e7475-7f94-4993-b373-8e4a8b1bcb4c
keywords: ["object names WDK kernel", "named objects WDK kernel", "unnamed objects WDK kernel", "object names WDK user-mode", "object handles WDK user-mode", "object handles WDK kernel", "handles WDK user-mode", "handles WDK kernel"]
ms.author: windowsdriverdev
ms.date: 06/16/2017
ms.topic: article
ms.prod: windows-hardware
ms.technology: windows-devices
---

# Object Names


## <a href="" id="ddk-object-names-kg"></a>


Kernel-mode objects are either named or unnamed. The *object name* is a Unicode string that both user-mode and kernel-mode components can use to refer to the object. For example, **\\KernelObjects\\LowMemoryCondition** is the name of the standard event object that signals when the amount of free memory in the system is low.

Both user-mode and kernel-mode components use the object name to open a handle to an object. All subsequent operations are performed by using the handle.

If an object is unnamed, a user-mode component cannot open a handle to it. Kernel-mode components can refer to an unnamed object by either a pointer or a handle.

Named objects are organized into a hierarchy. Each object is named relative to a parent object. Each component of the object's name begins with a backslash character. For example, **\\KernelObjects** is the parent object for **\\KernelObjects\\LowMemoryCondition**.

Only some types of objects can have child objects. The following are some examples:

-   Object directories have child objects. The object manager uses object directories to organize objects. For example **\\KernelObjects** is an object directory that holds standard event objects. Object directories do not correspond to actual directories on a disk. For more information, see [Object Directories](object-directories.md).

-   Device objects for disk drives have child objects that correspond to files on the disk.

-   File objects that represent directories have child objects corresponding to files within the directory.

-   Device objects for WDM drivers have their own namespace that can be used in a driver-defined fashion. For more information, see [Controlling Device Namespace Access](controlling-device-namespace-access.md).

Files have object names that are relative to **\\DosDevices**. For example, the file C:\\Directory\\File can be specified as **\\DosDevices\\C:\\***Directory\\File*.

For example, the components of the object name can be described as follows.

<table>
<colgroup>
<col width="50%" />
<col width="50%" />
</colgroup>
<thead>
<tr class="header">
<th>Object Name</th>
<th>Description</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><p><strong>\DosDevices</strong></p></td>
<td><p>Object directory.</p></td>
</tr>
<tr class="even">
<td><p><strong>\DosDevices\C:</strong></p></td>
<td><p>Device object representing the C: drive.</p></td>
</tr>
<tr class="odd">
<td><p><strong>\DosDevices\C:\\</strong> <em>Directory</em></p></td>
<td><p>File object representing the directory named C:\Directory.</p></td>
</tr>
<tr class="even">
<td><p><strong>\DosDevices\C:\\</strong> <em>Directory</em> \ <em>File</em></p></td>
<td><p>File object representing the file named C:\Directory\File.</p></td>
</tr>
</tbody>
</table>

 

Drivers that create named objects do so in specific object directories. For more information, see [Object Directories](object-directories.md).

 

 


--------------------
[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bkernel\kernel%5D:%20Object%20Names%20%20RELEASE:%20%286/14/2017%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")


