---
title: NetPowerSettingsGetWakePattern method
topic_type:
- apiref
api_name:
- NetPowerSettingsGetWakePattern
api_location:
- NetAdapterCxStub.lib
- NetAdapterCxStub.dll
api_type:
- LibDef
---

# NetPowerSettingsGetWakePattern method


[!include[NetAdapterCx Beta Prerelease](../netcx-beta-prerelease.md)]

Retrieves the wake pattern structure at the specified index.

Syntax
------

```cpp
PNDIS_PM_WOL_PATTERN NetPowerSettingsGetWakePattern(
  _In_ NETPOWERSETTINGS NetPowerSettings,
  _In_ ULONG            Index
);
```

Parameters
----------

*NetPowerSettings* [in]  
A handle to the NETPOWERSETTINGS object associated with the NETADAPTER. To retrieve the handle, call [**NetAdapterGetPowerSettings**](netadaptergetpowersettings.md).

*Index* [in]  
A zero-based value that is used as an index into the WoL patterns stored in the NETPOWERSETTINGS object. This value must be less than the value returned by [**NetPowerSettingsGetWakePatternCount**](netpowersettingsgetwakepatterncount.md).

Return value
------------

Returns a pointer to the [**NDIS_PM_WOL_PATTERN**](https://msdn.microsoft.com/library/windows/hardware/ff566768) structure at the specified index, or **NULL** if the index value is invalid.

Remarks
-------

The client driver must only call **NetPowerSettingsGetWakePattern** during a power transition, typically [*EVT_WDF_DEVICE_ARM_WAKE_FROM_SX*](https://msdn.microsoft.com/library/windows/hardware/ff540844), or from [*EVT_WDF_DEVICE_ARM_WAKE_FROM_S0*](https://msdn.microsoft.com/library/windows/hardware/ff540843) or [*EVT_NET_ADAPTER_PREVIEW_WAKE_PATTERN*](evt-net-adapter-preview-wake-pattern.md).  Otherwise, the call results in a system bugcheck.

The client can check if this pattern is enabled by calling [**NetPowerSettingsIsWakePatternEnabled**](netpowersettingsiswakepatternenabled.md).

The client driver can use the pointer to examine the [**NDIS_PM_WOL_PATTERN**](https://msdn.microsoft.com/library/windows/hardware/ff566768) structure, but should not retain it. NetAdapterCx automatically releases the pattern structure during WoL pattern removal.

In NetAdapterCx version 1.1, the IRQL of this method was changed from DISPATCH_LEVEL to PASSIVE_LEVEL.

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
<td align="left"><p>1.23</p></td>
</tr>
<tr class="odd">
<td align="left"><p>Minimum NetAdapterCx version</p></td>
<td align="left"><p>1.1</p></td>
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
<td align="left"><p>PASSIVE_LEVEL</p></td>
</tr>
</tbody>
</table>

## See also


[**NDIS_PM_WOL_PATTERN**](https://msdn.microsoft.com/library/windows/hardware/ff566768)

 

 






