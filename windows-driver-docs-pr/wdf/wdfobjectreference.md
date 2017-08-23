---
title: WdfObjectReference macro
author: windows-driver-content
description: The WdfObjectReference macro increments the reference count for a specified framework object.
ms.assetid: 8e024197-d366-4665-994b-4e03f559e017
keywords:
 - WdfObjectReference macro
ms.author: windowsdriverdev
ms.date: 08/23/2017
ms.topic: article
ms.prod: windows-hardware
ms.technology: windows-devices
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

```
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
<tr class="odd">
<td><p>DDI compliance rules</p></td>
<td>[<strong>DriverCreate</strong>](https://msdn.microsoft.com/library/windows/hardware/ff544957), [<strong>MemAfterReqCompletedIntIoctlA</strong>](https://msdn.microsoft.com/library/windows/hardware/ff549090), [<strong>MemAfterReqCompletedIoctlA</strong>](https://msdn.microsoft.com/library/windows/hardware/ff549106), [<strong>MemAfterReqCompletedReadA</strong>](https://msdn.microsoft.com/library/windows/hardware/ff549116), [<strong>MemAfterReqCompletedWriteA</strong>](https://msdn.microsoft.com/library/windows/hardware/ff549125)</td>
</tr>
</tbody>
</table>

## See also


[**WdfObjectReferenceActual**](https://msdn.microsoft.com/library/windows/hardware/ff548760)

[**WdfObjectReferenceWithTag**](wdfobjectreferencewithtag.md)

 

 


--------------------
[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bwdf\wdf%5D:%20WdfObjectReference%20macro%20%20RELEASE:%20%288/22/2017%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")


