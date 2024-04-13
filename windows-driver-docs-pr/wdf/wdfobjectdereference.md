---
title: WdfObjectDereference Macro
description: The WdfObjectDereference macro decrements the reference count for a specified framework object.
keywords:
 - WdfObjectDereference macro
ms.date: 08/23/2017
ms.topic: reference
---

# WdfObjectDereference macro


\[Applies to KMDF and UMDF\]

The **WdfObjectDereference** macro decrements the reference count for a specified framework object.

## Syntax

```ManagedCPlusPlus
VOID WdfObjectDereference(
  [in] WDFOBJECT Handle
);
```

## Parameters

*Handle* \[in\]  
A handle to a framework object.

## Return value

None.

A bug check occurs if the driver supplies an invalid object handle.

## Remarks

If the object's reference count becomes zero, the object might be deleted before **WdfObjectDereference** returns.

A driver can call **WdfObjectDereference** only if it has previously called [**WdfObjectReference**](wdfobjectreference.md).

Instead of calling **WdfObjectDereference**, a driver can call [**WdfObjectDereferenceWithTag**](wdfobjectdereferencewithtag.md) or [**WdfObjectDereferenceActual**](/windows-hardware/drivers/ddi/wdfobject/nf-wdfobject-wdfobjectdereferenceactual).

For more information about object reference counts, see [Framework Object Life Cycle](./framework-object-life-cycle.md).

## Examples

The following code example decrements an object's reference count.

```cpp
WdfObjectDereference(Object); 
```

## Requirements

<table>
<colgroup>
<col width="50%" />
<col width="50%" />
</colgroup>
<tbody>
<tr class="odd">
<td><p>Target platform</p></td>
<td><a href="https://go.microsoft.com/fwlink/p/?linkid=531356" data-raw-source="[Universal](https://go.microsoft.com/fwlink/p/?linkid=531356)">Universal</a></td>
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
<td><a href="/windows-hardware/drivers/devtest/kmdf-drivercreate" data-raw-source="[&lt;strong&gt;DriverCreate&lt;/strong&gt;](../devtest/kmdf-drivercreate.md)"><strong>DriverCreate</strong></a>, <a href="/windows-hardware/drivers/devtest/kmdf-memafterreqcompletedintioctla" data-raw-source="[&lt;strong&gt;MemAfterReqCompletedIntIoctlA&lt;/strong&gt;](../devtest/kmdf-memafterreqcompletedintioctla.md)"><strong>MemAfterReqCompletedIntIoctlA</strong></a>, <a href="/windows-hardware/drivers/devtest/kmdf-memafterreqcompletedioctla" data-raw-source="[&lt;strong&gt;MemAfterReqCompletedIoctlA&lt;/strong&gt;](../devtest/kmdf-memafterreqcompletedioctla.md)"><strong>MemAfterReqCompletedIoctlA</strong></a>, <a href="/windows-hardware/drivers/devtest/kmdf-memafterreqcompletedreada" data-raw-source="[&lt;strong&gt;MemAfterReqCompletedReadA&lt;/strong&gt;](../devtest/kmdf-memafterreqcompletedreada.md)"><strong>MemAfterReqCompletedReadA</strong></a>, <a href="/windows-hardware/drivers/devtest/kmdf-memafterreqcompletedwritea" data-raw-source="[&lt;strong&gt;MemAfterReqCompletedWriteA&lt;/strong&gt;](../devtest/kmdf-memafterreqcompletedwritea.md)"><strong>MemAfterReqCompletedWriteA</strong></a>, <a href="/windows-hardware/drivers/devtest/kmdf-wdfioqueuefindrequestfailed" data-raw-source="[&lt;strong&gt;wdfioqueuefindrequestfailed&lt;/strong&gt;](../devtest/kmdf-wdfioqueuefindrequestfailed.md)"><strong>wdfioqueuefindrequestfailed</strong></a>, <a href="/windows-hardware/drivers/devtest/kmdf-wdfioqueueretrievefoundrequest" data-raw-source="[&lt;strong&gt;wdfioqueueretrievefoundrequest&lt;/strong&gt;](../devtest/kmdf-wdfioqueueretrievefoundrequest.md)"><strong>wdfioqueueretrievefoundrequest</strong></a></td>
</tr>
</tbody>
</table>

## See also


[**WdfObjectDereferenceActual**](/windows-hardware/drivers/ddi/wdfobject/nf-wdfobject-wdfobjectdereferenceactual)

[**WdfObjectDereferenceWithTag**](wdfobjectdereferencewithtag.md)

[**WdfObjectReference**](wdfobjectreference.md)

