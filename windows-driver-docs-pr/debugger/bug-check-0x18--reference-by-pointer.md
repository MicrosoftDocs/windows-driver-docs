---
title: Bug Check 0x18 REFERENCE_BY_POINTER
description: The REFERENCE_BY_POINTER bug check has a value of 0x00000018. This indicates that the reference count of an object is illegal for the current state of the object.
ms.assetid: 911fa821-5e59-4f20-a31b-148064e6c113
keywords: ["Bug Check 0x18 REFERENCE_BY_POINTER", "REFERENCE_BY_POINTER"]
ms.author: domars
ms.date: 05/23/2017
topic_type:
- apiref
api_name:
- REFERENCE_BY_POINTER
api_type:
- NA
ms.localizationpriority: medium
---

# Bug Check 0x18: REFERENCE\_BY\_POINTER


The REFERENCE\_BY\_POINTER bug check has a value of 0x00000018. This indicates that the reference count of an object is illegal for the current state of the object.

**Important** This topic is for programmers. If you are a customer who has received a blue screen error code while using your computer, see [Troubleshoot blue screen errors](https://windows.microsoft.com/windows-10/troubleshoot-blue-screen-errors).

## REFERENCE\_BY\_POINTER Parameters


<table>
<colgroup>
<col width="50%" />
<col width="50%" />
</colgroup>
<thead>
<tr class="header">
<th align="left">Parameter</th>
<th align="left">Description</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td align="left"><p>1</p></td>
<td align="left"><p>Object type of the object whose reference count is being lowered.</p></td>
</tr>
<tr class="even">
<td align="left"><p>2</p></td>
<td align="left"><p>Object whose reference count is being lowered.</p></td>
</tr>
<tr class="odd">
<td align="left"><p>3</p></td>
<td align="left"><p>Reserved</p></td>
</tr>
<tr class="even">
<td align="left"><p>4</p></td>
<td align="left"><p>Reserved</p></td>
</tr>
</tbody>
</table>

 

Cause
-----

The reference count of an object is illegal for the current state of the object. Each time a driver uses a pointer to an object, the driver calls a kernel routine to increase the reference count of the object by one. When the driver is done with the pointer, the driver calls another kernel routine to decrease the reference count by one.

Drivers must match calls to the routines that increase (*reference*) and decrease (*dereference*) the reference count. This bug check is caused by an inconsistency in the object's reference count. Typically, the inconsistency is caused by a driver that decreases the reference count of an object too many times, making extra calls that dereference the object. This bug check can occur because an object's reference count goes to zero while there are still open handles to the object. It might also occur when the object's reference count drops below zero, whether or not there are open handles to the object.

Resolution
----------

Make sure that the driver matches calls to the routines that increase and decrease the reference count of the object. Make sure that your driver does not make extra calls to routines that dereference the object (see Parameter 2).

You can use a debugger to help analyze this problem. For more information, see [Crash dump analysis using the Windows debuggers (WinDbg)](crash-dump-files.md). The [**!analyze**](-analyze.md) debug extension displays information about the bug check and can be very helpful in determining the root cause.

To find the handle and pointer count on the object, use the **!object** debugger command.

kd&gt; !object *address*

Where *address* is the address of the object given in Parameter 2.

You can also set a breakpoint in the code leading up to this stop code and attempt to single step forward into the faulting code.

If you are not equipped to use the Windows debugger to work on this problem, you can use some basic troubleshooting techniques.

-   Check the System Log in Event Viewer for additional error messages that might help identify the device or driver that is causing this bug check.

-   If a driver is identified in the bug check message, disable the driver or check with the manufacturer for driver updates.

-   Confirm that any new hardware that is installed is compatible with the installed version of Windows. For example, you can get information about required hardware at [Windows 10 Specifications](https://www.microsoft.com/windows/windows-10-specifications).

-   For additional general troubleshooting information, see [**Blue Screen Data**](blue-screen-data.md).

 

 




