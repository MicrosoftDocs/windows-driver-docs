---
title: NetPowerSettingsIsWakePatternEnabled method
topic_type:
- apiref
api_name:
- NetPowerSettingsIsWakePatternEnabled
api_location:
- NetAdapterCxStub.lib
- NetAdapterCxStub.dll
api_type:
- LibDef
---

# NetPowerSettingsIsWakePatternEnabled method


[!include[NetAdapterCx Beta Prerelease](../netcx-beta-prerelease.md)]

Determines if a wake-on-LAN (WoL) pattern is enabled for a network adapter.

Syntax
------

```cpp
BOOLEAN NetPowerSettingsIsWakePatternEnabled(
  _In_ NETPOWERSETTINGS     NetPowerSettings,
  _In_ PNDIS_PM_WOL_PATTERN NdisPmWolPattern
);
```

Parameters
----------

*NetPowerSettings* [in]  
A handle to the NETPOWERSETTINGS object associated with the net adapter. To retrieve the handle, call [**NetAdapterGetPowerSettings**](netadaptergetpowersettings.md).

*NdisPmWolPattern* [in]  
A pointer to a [**NDIS_PM_WOL_PATTERN**](https://msdn.microsoft.com/library/windows/hardware/ff566768) structure obtained by calling [**NetPowerSettingsGetWakePattern**](netpowersettingsgetwakepattern.md).

Return value
------------

Returns **TRUE** if the WoL pattern is enabled, and **FALSE** otherwise.

Remarks
-------

The client driver calls **NetPowerSettingsIsWakePatternEnabled** during a power transition, typically from its [*EVT_WDF_DEVICE_ARM_WAKE_FROM_SX*](https://msdn.microsoft.com/library/windows/hardware/ff540844) or [*EVT_WDF_DEVICE_ARM_WAKE_FROM_S0*](https://msdn.microsoft.com/library/windows/hardware/ff540843) callback function, or from the [*EVT_NET_ADAPTER_PREVIEW_WAKE_PATTERN*](evt-net-adapter-preview-wake-pattern.md) callback function.

If the wake pattern is enabled, the driver programs its hardware to enable the pattern during a power down transition.

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


[**NDIS_PM_WOL_PATTERN**](https://msdn.microsoft.com/library/windows/hardware/ff566768)

 

 






