---
title: WdfObjectDereferenceWithTag macro
description: The WdfObjectDereferenceWithTag macro decrements the reference count for a specified framework object and assigns the driver's current file name and line number to the reference. This macro also assigns a tag value to the reference.
ms.assetid: c5cfe516-ad62-4656-a033-d1800d9554a8
keywords:
 - WdfObjectDereferenceWithTag macro
ms.date: 08/23/2017
ms.localizationpriority: medium
---

# WdfObjectDereferenceWithTag macro


\[Applies to KMDF and UMDF\]

The **WdfObjectDereferenceWithTag** macro decrements the reference count for a specified framework object and assigns the driver's current file name and line number to the reference. This macro also assigns a tag value to the reference.

Syntax
------

```ManagedCPlusPlus
VOID WdfObjectDereferenceWithTag(
  [in] WDFOBJECT Handle,
  [in] PVOID     Tag
);
```

Parameters
----------

*Handle* \[in\]  
A handle to a framework object.

*Tag* \[in\]  
A driver-defined value that identifies an object reference. The tag value must match a tag value that the driver previously supplied to [**WdfObjectReferenceWithTag**](wdfobjectreferencewithtag.md).

Return value
------------

None.

A bug check occurs if the driver supplies an invalid object handle.

Remarks
-------

If the object's reference count becomes zero, the object might be deleted before **WdfObjectDereferenceWithTag** returns.

Calling [**WdfObjectDereferenceActual**](https://msdn.microsoft.com/library/windows/hardware/ff548743) or **WdfObjectDereferenceWithTag** instead of [**WdfObjectDereference**](wdfobjectdereference.md) provides additional information (tag string, line number, and file name) to Microsoft debuggers. **WdfObjectDereferenceActual** allows your driver to specify the line number and file name, while **WdfObjectDereferenceWithTag** uses the driver's current line number and file name.

You can view the tag, line number, and file name values by using the **!wdftagtracker** debugger extension. The debugger extension displays the tag value as both a pointer and a series of characters. For more about debugger extensions, see [Debugging a KMDF Driver](https://msdn.microsoft.com/library/windows/hardware/ff540790).

For more information about object reference counts, see [Framework Object Life Cycle](https://msdn.microsoft.com/library/windows/hardware/ff542889).

Examples
--------

The following code example decrements an object's reference count and assigns a tag value to the reference.

```cpp
WdfObjectDereferenceWithTag(
                            object,
                            pTag
                            );
```

Requirements
------------

<table>
<colgroup>
<col width="50%" />
<col width="50%" />
</colgroup>
<tbody>
<tr class="odd">
<td><p>Target platform</p></td>
<td><a href="http://go.microsoft.com/fwlink/p/?linkid=531356" data-raw-source="[Universal](http://go.microsoft.com/fwlink/p/?linkid=531356)">Universal</a></td>
</tr>
<tr class="even">
<td><p>Minimum KMDF version</p></td>
<td><p>1.0</p></td>
</tr>
<tr class="odd">
<td><p>Minimum UMDF version</p></td>
<td><p>2.0</p></td>
</tr>
<tr class="even">
<td><p>Header</p></td>
<td>Wdfobject.h (include Wdf.h)</td>
</tr>
<tr class="odd">
<td><p>Library</p></td>
<td>Wdf01000.sys (KMDF);
WUDFx02000.dll (UMDF)</td>
</tr>
<tr class="even">
<td><p>IRQL</p></td>
<td><p>&lt;= DISPATCH_LEVEL</p></td>
</tr>
</tbody>
</table>

## See also


[**WdfObjectDereference**](wdfobjectdereference.md)

[**WdfObjectReferenceWithTag**](wdfobjectreferencewithtag.md)

 

 






