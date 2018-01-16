---
title: RxNewMapUserBuffer function
description: RxNewMapUserBuffer returns the user buffer address used for low I/O.
ms.assetid: 90ab7793-55ed-47f7-b55d-f4205488796c
keywords: ["RxNewMapUserBuffer function Installable File System Drivers"]
topic_type:
- apiref
api_name:
- RxNewMapUserBuffer
api_location:
- rxprocs.h
api_type:
- HeaderDef
ms.author: windowsdriverdev
ms.date: 11/28/2017
ms.topic: article
ms.prod: windows-hardware
ms.technology: windows-devices
---

# RxNewMapUserBuffer function


**RxNewMapUserBuffer** returns the user buffer address used for low I/O.

Syntax
------

```ManagedCPlusPlus
PVOID RxNewMapUserBuffer(
  _In_ PRX_CONTEXT RxContext
);
```

Parameters
----------

*RxContext* \[in\]  
A pointer to the RX\_CONTEXT structure for this request.

Return value
------------

**RxNewMapUserBuffer** returns a mapped address pointer on success or **NULL** on failure.

Remarks
-------

If an MDL exists, then the assumption is that the MDL describes the user buffer, and the system address for the MDL is returned by **RxNewMapUserBuffer**. Otherwise, the user buffer is returned directly by **RxNewMapUserBuffer**.

The **RxNewMapUserBuffer** routine checks if the **CurrentIrp**-&gt;**MdlAddress** member of the *RxContext* variable is **NULL** and returns the **CurrentIrp**-&gt;**UserBuffer** member of the *RxContext* variable when this is the case. If the **CurrentIrp**-&gt;**MdlAddress** member is not **NULL**, then **RxNewMapUserBuffer** will call [**MmGetSystemAddressForMdlSafe**](https://msdn.microsoft.com/library/windows/hardware/ff554559) to return the MDL from the IRP.

Note that the **RxNewMapUserBuffer** routine is only available on Windows XP and Windows 2000.

Requirements
------------

<table>
<colgroup>
<col width="50%" />
<col width="50%" />
</colgroup>
<tbody>
<tr class="odd">
<td align="left"><p>Target platform</p></td>
<td align="left">Desktop</td>
</tr>
<tr class="even">
<td align="left"><p>Version</p></td>
<td align="left"><p>The RxNewMapUserBuffer routine is only available on Windows XP and Windows 2000.</p></td>
</tr>
<tr class="odd">
<td align="left"><p>Header</p></td>
<td align="left">Rxprocs.h (include Rxcontx.h or Rxprocs.h)</td>
</tr>
<tr class="even">
<td align="left"><p>IRQL</p></td>
<td align="left"><p>&lt;= APC_LEVEL</p></td>
</tr>
</tbody>
</table>

## See also


[**MmGetSystemAddressForMdlSafe**](https://msdn.microsoft.com/library/windows/hardware/ff554559)

[**RxLowIoCompletion**](https://msdn.microsoft.com/library/windows/hardware/ff554525)

[**RxLowIoGetBufferAddress**](https://msdn.microsoft.com/library/windows/hardware/ff554529)

[**RxMapSystemBuffer**](https://msdn.microsoft.com/library/windows/hardware/ff554549)

[**RX\_CONTEXT**](https://msdn.microsoft.com/library/windows/hardware/ff554751)

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bifsk\ifsk%5D:%20RxNewMapUserBuffer%20function%20%20RELEASE:%20%281/9/2018%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")





