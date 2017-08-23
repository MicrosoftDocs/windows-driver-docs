---
title: WdfObjectReferenceWithTag macro
author: windows-driver-content
description: The WdfObjectReferenceWithTag macro increments the reference count for a specified framework object and assigns the driver's current file name and line number to the reference. The macro also assigns a tag value to the reference.
ms.assetid: f0206238-c745-48b3-84d0-9f6d6ec9c2e0
keywords:
 - WdfObjectReferenceWithTag macro
ms.author: windowsdriverdev
ms.date: 08/23/2017
ms.topic: article
ms.prod: windows-hardware
ms.technology: windows-devices
---

# WdfObjectReferenceWithTag macro


\[Applies to KMDF and UMDF\]

The **WdfObjectReferenceWithTag** macro increments the reference count for a specified framework object and assigns the driver's current file name and line number to the reference. The macro also assigns a tag value to the reference.

Syntax
------

```ManagedCPlusPlus
VOID WdfObjectReferenceWithTag(
  [in] WDFOBJECT Handle,
  [in] PVOID     Tag
);
```

Parameters
----------

*Handle* \[in\]  
A handle to a framework object.

*Tag* \[in\]  
A driver-defined value that the framework stores as an identification tag for the object reference.

Return value
------------

None.

A bug check occurs if the driver supplies an invalid object handle.

Remarks
-------

If your driver calls **WdfObjectReferenceWithTag** to increment a reference count, the driver must call [**WdfObjectDereferenceWithTag**](wdfobjectdereferencewithtag.md) to decrement the count.

Calling [**WdfObjectReferenceActual**](https://msdn.microsoft.com/library/windows/hardware/ff548760) or **WdfObjectReferenceWithTag** instead of [**WdfObjectReference**](wdfobjectreference.md) provides additional information (tag value, line number, and file name) to Microsoft debuggers. **WdfObjectReferenceActual** allows your driver to specify the line number and file name, while **WdfObjectReferenceWithTag** uses the driver's current line number and file name.

You can view the tag, line number, and file name values by using the **!wdftagtracker** debugger extension. The debugger extension displays the tag value as both a pointer and a series of characters. For more about debugger extensions, see [Debugging a KMDF Driver](https://msdn.microsoft.com/library/windows/hardware/ff540790).

For more information about object reference counts, see [Framework Object Life Cycle](https://msdn.microsoft.com/library/windows/hardware/ff542889).

Examples
--------

The following code example increments an object's reference count and assigns a tag value to the reference.

```
WdfObjectReferenceWithTag(
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
<td>[Universal](http://go.microsoft.com/fwlink/p/?linkid=531356)</td>
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


[**WdfObjectReference**](wdfobjectreference.md)

 

 


--------------------
[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bwdf\wdf%5D:%20WdfObjectReferenceWithTag%20macro%20%20RELEASE:%20%288/22/2017%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")


