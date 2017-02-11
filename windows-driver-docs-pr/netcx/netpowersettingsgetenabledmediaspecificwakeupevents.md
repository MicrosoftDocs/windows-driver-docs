---
title: NetPowerSettingsGetEnabledMediaSpecificWakeUpEvents method
topic_type:
- apiref
api_name:
- NetPowerSettingsGetEnabledMediaSpecificWakeUpEvents
api_location:
- NetAdapterCxStub.lib
- NetAdapterCxStub.dll
api_type:
- LibDef
---

# NetPowerSettingsGetEnabledMediaSpecificWakeUpEvents method


[!include[NetAdapterCx Beta Prerelease](../netcx-beta-prerelease.md)]

Retrieves the media-specific wake-up events that a network adapter supports.

Syntax
------

```ManagedCPlusPlus
ULONG NetPowerSettingsGetEnabledMediaSpecificWakeUpEvents(
  _In_ NETPOWERSETTINGS NetPowerSettings
);
```

Parameters
----------

*NetPowerSettings* \[in\]  
A handle to the NETPOWERSETTINGS object associated with the net adapter. To retrieve the handle, call [**NetAdapterGetPowerSettings**](netadaptergetpowersettings.md).

Return value
------------

A ULONG value that contains a bitwise **OR** of flags that correspond to events that the client driver reported in the **SupportedMediaSpecificWakeUpEvents** member of the [**NET_ADAPTER_POWER_CAPABILITIES**](net-adapter-power-capabilities.md) structure. The flags represent the media-specific wake-up events that the driver must enable in the hardware to arm the device for wake.

For more information, see the **MediaSpecificWakeUpEvents** member of [**NDIS_PM_PARAMETERS**](https://msdn.microsoft.com/library/windows/hardware/ff566759).

Remarks
-------

The client driver calls **NetPowerSettingsGetEnabledMediaSpecificWakeUpEvents** during a power transition, typically from its [*EVT_WDF_DEVICE_ARM_WAKE_FROM_SX*](https://msdn.microsoft.com/library/windows/hardware/ff540844) or [*EVT_WDF_DEVICE_ARM_WAKE_FROM_S0*](https://msdn.microsoft.com/library/windows/hardware/ff540843) callback function.

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
<td align="left">Netpowersettings.h (include Netadaptercx.h)</td>
</tr>
<tr class="odd">
<td align="left"><p>Library</p></td>
<td align="left">NetAdapterCxStub.lib</td>
</tr>
<tr class="even">
<td align="left"><p>IRQL</p></td>
<td align="left"><p>DISPATCH_LEVEL</p></td>
</tr>
</tbody>
</table>

## See also


[**NDIS_PM_PARAMETERS**](https://msdn.microsoft.com/library/windows/hardware/ff566759)

 

 






