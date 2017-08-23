---
title: WdfDeviceStopIdleWithTag macro
author: windows-driver-content
description: The WdfDeviceStopIdleWithTag macro increments the power reference count for a specified framework device object and assigns the driver's current file name and line number to the reference. The macro also assigns a tag value to the reference.
ms.assetid: 792A5EA8-5273-4284-B0EE-01BE1DCB9863
keywords:
 - WdfDeviceStopIdleWithTag macro
ms.author: windowsdriverdev
ms.date: 08/23/2017
ms.topic: article
ms.prod: windows-hardware
ms.technology: windows-devices
---

# WdfDeviceStopIdleWithTag macro


\[Applies to KMDF and UMDF\]

The **WdfDeviceStopIdleWithTag** macro increments the power reference count for a specified framework device object and assigns the driver's current file name and line number to the reference. The macro also assigns a tag value to the reference.

Syntax
------

```ManagedCPlusPlus
NTSTATUS WdfDeviceStopIdleWithTag(
  [in] WDFDEVICE Device,
  [in] BOOLEAN   WaitForD0,
  [in] PVOID     Tag
);
```

Parameters
----------

*Device* \[in\]  
A handle to a framework device object.

*WaitForD0* \[in\]  
A Boolean value that indicates when **WdfDeviceStopIdleWithTag** will return. If **TRUE**, it returns only after the specified device has entered the D0 device power state. If **FALSE**, the method returns immediately.

*Tag* \[in\]  
A driver-defined value that the framework stores as an identification tag for the power reference.

Return value
------------

If the operation succeeds, **WdfDeviceStopIdleWithTag** returns STATUS\_SUCCESS. If the driver calls **WdfDeviceStopIdleWithTag** when the device is in its working (D0) state, the method returns STATUS\_SUCCESS, but does not increment the power reference count.

Additional return values include:

<table>
<colgroup>
<col width="50%" />
<col width="50%" />
</colgroup>
<thead>
<tr class="header">
<th>Return code</th>
<th>Description</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><strong>STATUS_PENDING</strong></td>
<td><p>The device is being powered up asynchronously.</p></td>
</tr>
<tr class="even">
<td><strong>STATUS_INVALID_DEVICE_STATE</strong></td>
<td><p>The driver is not the power policy owner for the device.</p></td>
</tr>
<tr class="odd">
<td><strong>STATUS_POWER_STATE_INVALID</strong></td>
<td><p>A device failure occurred and the device cannot enter its D0 power state.</p></td>
</tr>
</tbody>
</table>

 

The method might return other [NTSTATUS values](https://msdn.microsoft.com/library/windows/hardware/ff557697).

A bug check occurs if the driver supplies an invalid object handle.

Remarks
-------

If your driver calls **WdfDeviceStopIdleWithTag** to increment a reference count, the driver must call [**WdfDeviceResumeIdleWithTag**](wdfdeviceresumeidlewithtag.md) to decrement the count.

Calling **WdfDeviceStopIdleWithTag** instead of [**WdfDeviceStopIdle**](https://msdn.microsoft.com/library/windows/hardware/ff546921) provides additional information (tag value, line number, and file name) that you can view in Microsoft debuggers. **WdfDeviceStopIdleWithTag** uses the driver's current line number and file name.

You can view the tag, line number, and file name values by using the [**!wdftagtracker**](https://msdn.microsoft.com/library/windows/hardware/ff566126) debugger extension. The debugger extension displays the tag value as both a pointer and a series of characters.

Use [**!wdfkd.wdfdevice**](https://msdn.microsoft.com/library/windows/hardware/ff565703) with verbose flags on and locate the link to [**!wdftagtracker**](https://msdn.microsoft.com/library/windows/hardware/ff566126) in the output:

```
kd> !wdfdevice <handle> f 
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
<td><p>1.15</p></td>
</tr>
<tr class="odd">
<td><p>Minimum UMDF version</p></td>
<td><p>2.15</p></td>
</tr>
<tr class="even">
<td><p>Header</p></td>
<td>Wdfdevice.h (include Wdf.h)</td>
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


[Debugging Power Reference Leaks in WDF](https://msdn.microsoft.com/library/windows/hardware/dn965441)

[**WdfDeviceResumeIdle**](https://msdn.microsoft.com/library/windows/hardware/ff546838)

[**WdfDeviceResumeIdleWithTag**](wdfdeviceresumeidlewithtag.md)

[**WdfDeviceStopIdle**](https://msdn.microsoft.com/library/windows/hardware/ff546921)

 

 


--------------------
[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bwdf\wdf%5D:%20WdfDeviceStopIdleWithTag%20macro%20%20RELEASE:%20%288/22/2017%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")


