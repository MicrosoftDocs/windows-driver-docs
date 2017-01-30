---
title: NetPowerSettingsGetWakePattern method
description: Retrieves a wake-on-LAN (WoL) pattern structure.
ms.assetid: 31cffe3b-7d39-4ae3-9ae6-5eedce49910b
keywords: ["NetPowerSettingsGetWakePattern method Network Drivers Starting with Windows Vista"]
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

Retrieves a wake-on-LAN (WoL) pattern structure.

Syntax
------

```ManagedCPlusPlus
PNDIS_PM_WOL_PATTERN NetPowerSettingsGetWakePattern(
  _In_ NETPOWERSETTINGS NetPowerSettings,
  _In_ ULONG            Index
);
```

Parameters
----------

*NetPowerSettings* \[in\]  
A handle to the NETPOWERSETTINGS object associated with the net adapter. To retrieve the handle, call [**NetAdapterGetPowerSettings**](netadaptergetpowersettings.md).

*Index* \[in\]  
A zero-based value that is used as an index into the WoL patterns stored in the NETPOWERSETTINGS object. This value must be less than the value returned by [**NetPowerSettingsGetWakePatternCount**](netpowersettingsgetwakepatterncount.md).

Return value
------------

Returns a pointer to the [**NDIS\_PM\_WOL\_PATTERN**](https://msdn.microsoft.com/library/windows/hardware/ff566768) structure at the specified index, or **NULL** if the index value is invalid.

Remarks
-------

The client driver calls **NetPowerSettingsGetWakePattern** during a power transition, typically from its [*EVT\_WDF\_DEVICE\_ARM\_WAKE\_FROM\_SX*](https://msdn.microsoft.com/library/windows/hardware/ff540844) or [*EVT\_WDF\_DEVICE\_ARM\_WAKE\_FROM\_S0*](https://msdn.microsoft.com/library/windows/hardware/ff540843) callback function, or from the [*EVT\_NET\_ADAPTER\_PREVIEW\_WAKE\_PATTERN*](evt-net-adapter-preview-wake-pattern.md) callback function.

The client driver can use the pointer to examine the [**NDIS\_PM\_WOL\_PATTERN**](https://msdn.microsoft.com/library/windows/hardware/ff566768) structure, but should not retain it. NetAdapterCx automatically releases the pattern structure during WoL pattern removal.

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
<td align="left">[Universal](http://go.microsoft.com/fwlink/p/?linkid=531356)</td>
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


[**NDIS\_PM\_WOL\_PATTERN**](https://msdn.microsoft.com/library/windows/hardware/ff566768)

 

 






