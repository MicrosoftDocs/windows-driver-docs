---
title: Object Handles
description: Object Handles
ms.assetid: deeeb3c0-54e4-4727-ac43-6da79be515d7
keywords: ["object handles WDK user-mode", "object handles WDK kernel", "handles WDK user-mode", "handles WDK kernel", "private object handles WDK", "shared object handles WDK"]
ms.date: 06/16/2017
ms.localizationpriority: medium
---

# Object Handles





Drivers and user-mode components access most system-defined objects through *handles*. Handles are represented by the HANDLE opaque data type. (Note that handles are not used to access [device objects](https://msdn.microsoft.com/library/windows/hardware/ff556277#wdkgloss-device-object) or [driver objects](https://msdn.microsoft.com/library/windows/hardware/ff556277#wdkgloss-driver-object).)

For most object types, the kernel-mode routine that creates or opens the object provides a handle to the caller. The caller then uses that handle in subsequent operations on the object.

Here is a list of object types that drivers typically use, and the routines that provide handles to objects of that type.

<table>
<colgroup>
<col width="50%" />
<col width="50%" />
</colgroup>
<thead>
<tr class="header">
<th>Object type</th>
<th>Corresponding create/open routine</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><p>File</p></td>
<td><p><a href="https://msdn.microsoft.com/library/windows/hardware/ff548418" data-raw-source="[&lt;strong&gt;IoCreateFile&lt;/strong&gt;](https://msdn.microsoft.com/library/windows/hardware/ff548418)"><strong>IoCreateFile</strong></a>, <a href="https://msdn.microsoft.com/library/windows/hardware/ff566424" data-raw-source="[&lt;strong&gt;ZwCreateFile&lt;/strong&gt;](https://msdn.microsoft.com/library/windows/hardware/ff566424)"><strong>ZwCreateFile</strong></a>, <a href="https://msdn.microsoft.com/library/windows/hardware/ff567011" data-raw-source="[&lt;strong&gt;ZwOpenFile&lt;/strong&gt;](https://msdn.microsoft.com/library/windows/hardware/ff567011)"><strong>ZwOpenFile</strong></a></p></td>
</tr>
<tr class="even">
<td><p>Registry keys</p></td>
<td><p><a href="https://msdn.microsoft.com/library/windows/hardware/ff549433" data-raw-source="[&lt;strong&gt;IoOpenDeviceInterfaceRegistryKey&lt;/strong&gt;](https://msdn.microsoft.com/library/windows/hardware/ff549433)"><strong>IoOpenDeviceInterfaceRegistryKey</strong></a>, <a href="https://msdn.microsoft.com/library/windows/hardware/ff549443" data-raw-source="[&lt;strong&gt;IoOpenDeviceRegistryKey&lt;/strong&gt;](https://msdn.microsoft.com/library/windows/hardware/ff549443)"><strong>IoOpenDeviceRegistryKey</strong></a>, <a href="https://msdn.microsoft.com/library/windows/hardware/ff566425" data-raw-source="[&lt;strong&gt;ZwCreateKey&lt;/strong&gt;](https://msdn.microsoft.com/library/windows/hardware/ff566425)"><strong>ZwCreateKey</strong></a>, <a href="https://msdn.microsoft.com/library/windows/hardware/ff567014" data-raw-source="[&lt;strong&gt;ZwOpenKey&lt;/strong&gt;](https://msdn.microsoft.com/library/windows/hardware/ff567014)"><strong>ZwOpenKey</strong></a></p></td>
</tr>
<tr class="odd">
<td><p>Threads</p></td>
<td><p><a href="https://msdn.microsoft.com/library/windows/hardware/ff559932" data-raw-source="[&lt;strong&gt;PsCreateSystemThread&lt;/strong&gt;](https://msdn.microsoft.com/library/windows/hardware/ff559932)"><strong>PsCreateSystemThread</strong></a></p></td>
</tr>
<tr class="even">
<td><p>Events</p></td>
<td><p><a href="https://msdn.microsoft.com/library/windows/hardware/ff549045" data-raw-source="[&lt;strong&gt;IoCreateSynchronizationEvent&lt;/strong&gt;](https://msdn.microsoft.com/library/windows/hardware/ff549045)"><strong>IoCreateSynchronizationEvent</strong></a>, <a href="https://msdn.microsoft.com/library/windows/hardware/ff549039" data-raw-source="[&lt;strong&gt;IoCreateNotificationEvent&lt;/strong&gt;](https://msdn.microsoft.com/library/windows/hardware/ff549039)"><strong>IoCreateNotificationEvent</strong></a></p></td>
</tr>
<tr class="odd">
<td><p>Symbolic links</p></td>
<td><p><a href="https://msdn.microsoft.com/library/windows/hardware/ff567030" data-raw-source="[&lt;strong&gt;ZwOpenSymbolicLinkObject&lt;/strong&gt;](https://msdn.microsoft.com/library/windows/hardware/ff567030)"><strong>ZwOpenSymbolicLinkObject</strong></a></p></td>
</tr>
<tr class="even">
<td><p>Directory objects</p></td>
<td><p><a href="https://msdn.microsoft.com/library/windows/hardware/ff566421" data-raw-source="[&lt;strong&gt;ZwCreateDirectoryObject&lt;/strong&gt;](https://msdn.microsoft.com/library/windows/hardware/ff566421)"><strong>ZwCreateDirectoryObject</strong></a></p></td>
</tr>
<tr class="odd">
<td><p>Section objects</p></td>
<td><p><a href="https://msdn.microsoft.com/library/windows/hardware/ff567029" data-raw-source="[&lt;strong&gt;ZwOpenSection&lt;/strong&gt;](https://msdn.microsoft.com/library/windows/hardware/ff567029)"><strong>ZwOpenSection</strong></a></p></td>
</tr>
</tbody>
</table>

 

When the driver no longer requires access to the object, it calls the [**ZwClose**](https://msdn.microsoft.com/library/windows/hardware/ff566417) routine to close the handle. This works for all of the object types listed in the table above.

Most of the routines that provide handles take an [**OBJECT\_ATTRIBUTES**](https://msdn.microsoft.com/library/windows/hardware/ff557749) structure as a parameter. This structure can be used to specify attributes for the handle.

Drivers can specify the following handle attributes:

-   OBJ\_KERNEL\_HANDLE

    The handle can only be accessed from kernel mode.

-   OBJ\_INHERIT

    Any children of the current process receive a copy of the handle when they are created.

-   OBJ\_FORCE\_ACCESS\_CHECK

    This attribute specifies that the system performs all access checks on the handle. By default, the system bypasses all access checks on handles created in kernel mode.

Use the [**InitializeObjectAttributes**](https://msdn.microsoft.com/library/windows/hardware/ff547804) routine to set these attributes in an **OBJECT\_ATTRIBUTES** structure.

For information about validating object handles, see [Failure to Validate Object Handles](failure-to-validate-object-handles.md).

### Private Object Handles

Whenever a driver creates an object handle for its private use, the driver must specify the OBJ\_KERNEL\_HANDLE attribute. This ensures that the handle is inaccessible to user-mode applications.

### Shared Object Handles

A driver that shares object handles between kernel mode and user mode must be carefully written to avoid accidentally creating security holes. Here are some guidelines:

1.  Create handles in kernel mode and pass them to user mode, instead of the other way around. Handles created by a user-mode component and passed to the driver should not be trusted.

2.  If the driver must manipulate handles on behalf of user-mode applications, use the OBJ\_FORCE\_ACCESS\_CHECK attribute to verify that the application has the necessary access.

3.  Use [**ObReferenceObjectByPointer**](https://msdn.microsoft.com/library/windows/hardware/ff558686) to keep a kernel-mode reference on a shared handle. Otherwise, if a user-mode component closes the handle, the reference count goes to zero, and if the driver then tries to use or close the handle the system will crash.

If a user-mode application creates an event object, a driver can safely wait for that event to be signaled, but only if the application passes a handle to the event object to the driver through an IOCTL. The driver must handle the IOCTL in the context of the process that created the event and must validate that the handle is an event handle by calling [**ObReferenceObjectByHandle**](https://msdn.microsoft.com/library/windows/hardware/ff558679).

 

 




