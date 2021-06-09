---
title: WdfObjectDereferenceWithTag macro
description: The WdfObjectDereferenceWithTag macro decrements the reference count for a specified framework object and assigns the driver's current file name and line number to the reference. This macro also assigns a tag value to the reference.
keywords:
 - WdfObjectDereferenceWithTag macro
ms.date: 08/23/2017
ms.localizationpriority: medium
---

# WdfObjectDereferenceWithTag macro


\[Applies to KMDF and UMDF\]

The **WdfObjectDereferenceWithTag** macro decrements the reference count for a specified framework object and assigns the driver's current file name and line number to the reference. This macro also assigns a tag value to the reference.

## Syntax

```ManagedCPlusPlus
VOID WdfObjectDereferenceWithTag(
  [in] WDFOBJECT Handle,
  [in] PVOID     Tag
);
```

## Parameters

*Handle* \[in\]  
A handle to a framework object.

*Tag* \[in\]  
A driver-defined value that identifies an object reference. The tag value must match a tag value that the driver previously supplied to [**WdfObjectReferenceWithTag**](wdfobjectreferencewithtag.md).

## Return value

None.

A bug check occurs if the driver supplies an invalid object handle.

## Remarks

If the object's reference count becomes zero, the object might be deleted before **WdfObjectDereferenceWithTag** returns.

Calling [**WdfObjectDereferenceActual**](/windows-hardware/drivers/ddi/wdfobject/nf-wdfobject-wdfobjectdereferenceactual) or **WdfObjectDereferenceWithTag** instead of [**WdfObjectDereference**](wdfobjectdereference.md) provides additional information (tag string, line number, and file name) to Microsoft debuggers. **WdfObjectDereferenceActual** allows your driver to specify the line number and file name, while **WdfObjectDereferenceWithTag** uses the driver's current line number and file name.

You can view the tag, line number, and file name values by using the **!wdftagtracker** debugger extension. The debugger extension displays the tag value as both a pointer and a series of characters. For more about debugger extensions, see [Debugging a KMDF Driver](../debugger/debug-universal-drivers---step-by-step-lab--echo-kernel-mode-.md).

For more information about object reference counts, see [Framework Object Life Cycle](./framework-object-life-cycle.md).

## Examples

The following code example decrements an object's reference count and assigns a tag value to the reference.

```cpp
WdfObjectDereferenceWithTag(
                            object,
                            pTag
                            );
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
</tbody>
</table>

## See also


[**WdfObjectDereference**](wdfobjectdereference.md)

[**WdfObjectReferenceWithTag**](wdfobjectreferencewithtag.md)

 

