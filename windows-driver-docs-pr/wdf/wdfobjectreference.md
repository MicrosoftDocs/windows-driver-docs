---
title: WdfObjectReference macro
description: The WdfObjectReference macro increments the reference count for a specified framework object.
ms.assetid: 8e024197-d366-4665-994b-4e03f559e017
keywords:
 - WdfObjectReference macro
ms.date: 08/23/2017
ms.localizationpriority: medium
---

# WdfObjectReference macro


\[Applies to KMDF and UMDF\]

The **WdfObjectReference** macro increments the reference count for a specified framework object.

Syntax
------

```ManagedCPlusPlus
VOID WdfObjectReference(
  [in] WDFOBJECT Handle
);
```

Parameters
----------

*Handle* \[in\]  
A handle to a framework object.

Return value
------------

None.

A bug check occurs if the driver supplies an invalid object handle.

Remarks
-------

If your driver calls **WdfObjectReference** to increment a reference count, the driver must call [**WdfObjectDereference**](wdfobjectdereference.md) to decrement the count.

Instead of calling **WdfObjectReference**, a driver can call [**WdfObjectReferenceWithTag**](wdfobjectreferencewithtag.md) or [**WdfObjectReferenceActual**](https://msdn.microsoft.com/library/windows/hardware/ff548760).

For more information about object reference counts, see [Framework Object Life Cycle](https://msdn.microsoft.com/library/windows/hardware/ff542889).

Examples
--------

The following code example increments an object's reference count.

```cpp
WdfObjectReference(Object); 
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
<tr class="odd">
<td><p>DDI compliance rules</p></td>
<td><a href="https://msdn.microsoft.com/library/windows/hardware/ff544957" data-raw-source="[&lt;strong&gt;DriverCreate&lt;/strong&gt;](https://msdn.microsoft.com/library/windows/hardware/ff544957)"><strong>DriverCreate</strong></a>, <a href="https://msdn.microsoft.com/library/windows/hardware/ff549090" data-raw-source="[&lt;strong&gt;MemAfterReqCompletedIntIoctlA&lt;/strong&gt;](https://msdn.microsoft.com/library/windows/hardware/ff549090)"><strong>MemAfterReqCompletedIntIoctlA</strong></a>, <a href="https://msdn.microsoft.com/library/windows/hardware/ff549106" data-raw-source="[&lt;strong&gt;MemAfterReqCompletedIoctlA&lt;/strong&gt;](https://msdn.microsoft.com/library/windows/hardware/ff549106)"><strong>MemAfterReqCompletedIoctlA</strong></a>, <a href="https://msdn.microsoft.com/library/windows/hardware/ff549116" data-raw-source="[&lt;strong&gt;MemAfterReqCompletedReadA&lt;/strong&gt;](https://msdn.microsoft.com/library/windows/hardware/ff549116)"><strong>MemAfterReqCompletedReadA</strong></a>, <a href="https://msdn.microsoft.com/library/windows/hardware/ff549125" data-raw-source="[&lt;strong&gt;MemAfterReqCompletedWriteA&lt;/strong&gt;](https://msdn.microsoft.com/library/windows/hardware/ff549125)"><strong>MemAfterReqCompletedWriteA</strong></a></td>
</tr>
</tbody>
</table>

## See also


[**WdfObjectReferenceActual**](https://msdn.microsoft.com/library/windows/hardware/ff548760)

[**WdfObjectReferenceWithTag**](wdfobjectreferencewithtag.md)

 

 






