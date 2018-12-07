---
title: Object Names
description: Object Names
ms.assetid: b30e7475-7f94-4993-b373-8e4a8b1bcb4c
keywords: ["object names WDK kernel", "named objects WDK kernel", "unnamed objects WDK kernel", "object names WDK user-mode", "object handles WDK user-mode", "object handles WDK kernel", "handles WDK user-mode", "handles WDK kernel"]
ms.date: 06/16/2017
ms.localizationpriority: medium
---

# Object Names





Kernel-mode objects are either named or unnamed. The *object name* is a Unicode string that both user-mode and kernel-mode components can use to refer to the object. For example, **\\KernelObjects\\LowMemoryCondition** is the name of the standard event object that signals when the amount of free memory in the system is low.

Both user-mode and kernel-mode components use the object name to open a handle to an object. All subsequent operations are performed by using the handle.

If an object is unnamed, a user-mode component cannot open a handle to it. Kernel-mode components can refer to an unnamed object by either a pointer or a handle.

Named objects are organized into a hierarchy. Each object is named relative to a parent object. Each component of the object's name begins with a backslash character. For example, **\\KernelObjects** is the parent object for **\\KernelObjects\\LowMemoryCondition**.

Only some types of objects can have child objects. The following are some examples:

-   Object directories have child objects. The object manager uses object directories to organize objects. For example **\\KernelObjects** is an object directory that holds standard event objects. Object directories do not correspond to actual directories on a disk. For more information, see [Object Directories](object-directories.md).

-   Device objects for disk drives have child objects that correspond to files on the disk.

-   File objects that represent directories have child objects corresponding to files within the directory.

-   Device objects for WDM drivers have their own namespace that can be used in a driver-defined fashion. For more information, see [Controlling Device Namespace Access](controlling-device-namespace-access.md).

Files have object names that are relative to **\\DosDevices**. For example, the file C:\\Directory\\File can be specified as **\\DosDevices\\C:\\**<em>Directory\\File</em>.

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
<td><p><strong>\DosDevices\C:&lt;/strong&gt; <em>Directory</em></p></td>
<td><p>File object representing the directory named C:\Directory.</p></td>
</tr>
<tr class="even">
<td><p><strong>\DosDevices\C:&lt;/strong&gt; <em>Directory</em> \ <em>File</em></p></td>
<td><p>File object representing the file named C:\Directory\File.</p></td>
</tr>
</tbody>
</table>

 

Drivers that create named objects do so in specific object directories. For more information, see [Object Directories](object-directories.md).

 

 




