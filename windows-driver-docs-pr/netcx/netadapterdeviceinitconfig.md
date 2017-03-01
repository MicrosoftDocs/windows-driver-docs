---
title: NetAdapterDeviceInitConfig method
topic_type:
- apiref
api_name:
- NetAdapterDeviceInitConfig
api_location:
- netadapter.h
api_type:
- HeaderDef
---

# NetAdapterDeviceInitConfig method


[!include[NetAdapterCx Beta Prerelease](../netcx-beta-prerelease.md)]

Initializes device initialization operations when the Plug and Play (PnP) manager reports the existence of a device.

Syntax
------

```cpp
NTSTATUS NetAdapterDeviceInitConfig(
  _Inout_ PWDFDEVICE_INIT DeviceInit
);
```

Parameters
----------

*DeviceInit* [in, out]  
The DeviceInit value passed in to the client by WDF in its [*EvtDriverDeviceAdd*](https://msdn.microsoft.com/library/windows/hardware/ff541693) routine.

Return value
------------

The method returns STATUS_SUCCESS if the operation succeeds. Otherwise, this method may return an appropriate NTSTATUS error code.

Remarks
-------

The client driver calls this method in its [*EVT_WDF_DRIVER_DEVICE_ADD*](https://msdn.microsoft.com/library/windows/hardware/ff541693) callback before it calls [**WdfDeviceCreate**](https://msdn.microsoft.com/library/windows/hardware/ff545926).

When a client driver calls **NetAdapterDeviceInitConfig**, the system-supplied NetAdapterCx.sys driver calls the following methods on behalf of the client. The client driver does not need to call these methods.

-   [**WdfDeviceInitSetReleaseHardwareOrderOnFailure**](https://msdn.microsoft.com/library/windows/hardware/hh706196)
-   [**WdfDeviceInitSetDeviceType**](https://msdn.microsoft.com/library/windows/hardware/ff546090)
-   [**WdfDeviceInitSetCharacteristics**](https://msdn.microsoft.com/library/windows/hardware/ff546074)
-   [**WdfDeviceInitSetIoType**](https://msdn.microsoft.com/library/windows/hardware/ff546128)
-   [**WdfDeviceInitSetPowerPageable**](https://msdn.microsoft.com/library/windows/hardware/ff546766)

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
<td align="left">Universal</td>
</tr>
<tr class="even">
<td align="left"><p>Minimum KMDF version</p></td>
<td align="left"><p>1.21</p></td>
</tr>
<tr class="odd">
<td align="left"><p>Minimum NetAdapterCx version</p></td>
<td align="left"><p>1.0</p></td>
</tr>
<tr class="even">
<td align="left"><p>Header</p></td>
<td align="left">Netadapter.h (include Netadaptercx.h)</td>
</tr>
<tr class="odd">
<td align="left"><p>IRQL</p></td>
<td align="left"><p>PASSIVE_LEVEL</p></td>
</tr>
</tbody>
</table>

 

 





