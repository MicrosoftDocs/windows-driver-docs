---
title: NetPowerSettingsIsWakePatternEnabled method
description: Determines if a wake-on-LAN (WoL) pattern is enabled for a network adapter.
ms.assetid: 7ea019d7-8d06-4e29-8da1-bd40b19b95d6
keywords: ["NetPowerSettingsIsWakePatternEnabled method Network Drivers Starting with Windows Vista"]
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

```ManagedCPlusPlus
BOOLEAN NetPowerSettingsIsWakePatternEnabled(
  _In_ NETPOWERSETTINGS     NetPowerSettings,
  _In_ PNDIS_PM_WOL_PATTERN NdisPmWolPattern
);
```

Parameters
----------

*NetPowerSettings* \[in\]  
A handle to the NETPOWERSETTINGS object associated with the net adapter. To retrieve the handle, call [**NetAdapterGetPowerSettings**](netadaptergetpowersettings.md).

*NdisPmWolPattern* \[in\]  
A pointer to a [**NDIS\_PM\_WOL\_PATTERN**](https://msdn.microsoft.com/library/windows/hardware/ff566768) structure obtained by calling [**NetPowerSettingsGetWakePattern**](netpowersettingsgetwakepattern.md).

Return value
------------

Returns **TRUE** if the WoL pattern is enabled, and **FALSE** otherwise.

Remarks
-------

The client driver calls **NetPowerSettingsIsWakePatternEnabled** during a power transition, typically from its [*EVT\_WDF\_DEVICE\_ARM\_WAKE\_FROM\_SX*](https://msdn.microsoft.com/library/windows/hardware/ff540844) or [*EVT\_WDF\_DEVICE\_ARM\_WAKE\_FROM\_S0*](https://msdn.microsoft.com/library/windows/hardware/ff540843) callback function, or from the [*EVT\_NET\_ADAPTER\_PREVIEW\_WAKE\_PATTERN*](evt-net-adapter-preview-wake-pattern.md) callback function.

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

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bnetvista\netvista%5D:%20NetPowerSettingsIsWakePatternEnabled%20method%20%20RELEASE:%20%281/19/2017%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")





