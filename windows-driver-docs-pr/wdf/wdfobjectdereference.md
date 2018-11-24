---
title: WdfObjectDereference macro
description: The WdfObjectDereference macro decrements the reference count for a specified framework object.
ms.assetid: e945202c-7e6b-47b7-9216-d7a3a694489e
keywords:
 - WdfObjectDereference macro
ms.date: 08/23/2017
ms.localizationpriority: medium
---

# WdfObjectDereference macro


\[Applies to KMDF and UMDF\]

The **WdfObjectDereference** macro decrements the reference count for a specified framework object.

Syntax
------

```ManagedCPlusPlus
VOID WdfObjectDereference(
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

If the object's reference count becomes zero, the object might be deleted before **WdfObjectDereference** returns.

A driver can call **WdfObjectDereference** only if it has previously called [**WdfObjectReference**](wdfobjectreference.md).

Instead of calling **WdfObjectDereference**, a driver can call [**WdfObjectDereferenceWithTag**](wdfobjectdereferencewithtag.md) or [**WdfObjectDereferenceActual**](https://msdn.microsoft.com/library/windows/hardware/ff548743).

For more information about object reference counts, see [Framework Object Life Cycle](https://msdn.microsoft.com/library/windows/hardware/ff542889).

Examples
--------

The following code example decrements an object's reference count.

```cpp
WdfObjectDereference(Object); 
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
<td><a href="https://msdn.microsoft.com/library/windows/hardware/ff544957" data-raw-source="[&lt;strong&gt;DriverCreate&lt;/strong&gt;](https://msdn.microsoft.com/library/windows/hardware/ff544957)"><strong>DriverCreate</strong></a>, <a href="https://msdn.microsoft.com/library/windows/hardware/ff549090" data-raw-source="[&lt;strong&gt;MemAfterReqCompletedIntIoctlA&lt;/strong&gt;](https://msdn.microsoft.com/library/windows/hardware/ff549090)"><strong>MemAfterReqCompletedIntIoctlA</strong></a>, <a href="https://msdn.microsoft.com/library/windows/hardware/ff549106" data-raw-source="[&lt;strong&gt;MemAfterReqCompletedIoctlA&lt;/strong&gt;](https://msdn.microsoft.com/library/windows/hardware/ff549106)"><strong>MemAfterReqCompletedIoctlA</strong></a>, <a href="https://msdn.microsoft.com/library/windows/hardware/ff549116" data-raw-source="[&lt;strong&gt;MemAfterReqCompletedReadA&lt;/strong&gt;](https://msdn.microsoft.com/library/windows/hardware/ff549116)"><strong>MemAfterReqCompletedReadA</strong></a>, <a href="https://msdn.microsoft.com/library/windows/hardware/ff549125" data-raw-source="[&lt;strong&gt;MemAfterReqCompletedWriteA&lt;/strong&gt;](https://msdn.microsoft.com/library/windows/hardware/ff549125)"><strong>MemAfterReqCompletedWriteA</strong></a>, <a href="https://msdn.microsoft.com/library/windows/hardware/hh975098" data-raw-source="[&lt;strong&gt;wdfioqueuefindrequestfailed&lt;/strong&gt;](https://msdn.microsoft.com/library/windows/hardware/hh975098)"><strong>wdfioqueuefindrequestfailed</strong></a>, <a href="https://msdn.microsoft.com/library/windows/hardware/hh975099" data-raw-source="[&lt;strong&gt;wdfioqueueretrievefoundrequest&lt;/strong&gt;](https://msdn.microsoft.com/library/windows/hardware/hh975099)"><strong>wdfioqueueretrievefoundrequest</strong></a></td>
</tr>
</tbody>
</table>

## See also


[**WdfObjectDereferenceActual**](https://msdn.microsoft.com/library/windows/hardware/ff548743)

[**WdfObjectDereferenceWithTag**](wdfobjectdereferencewithtag.md)

[**WdfObjectReference**](wdfobjectreference.md)

 

 






