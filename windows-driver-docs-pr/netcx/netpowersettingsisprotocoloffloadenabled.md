---
title: NetPowerSettingsIsProtocolOffloadEnabled method
topic_type:
- apiref
api_name:
- NetPowerSettingsIsProtocolOffloadEnabled
api_location:
- NetAdapterCxStub.lib
- NetAdapterCxStub.dll
api_type:
- LibDef
---

# NetPowerSettingsIsProtocolOffloadEnabled method


[!include[NetAdapterCx Beta Prerelease](../netcx-beta-prerelease.md)]

Determines if a protocol offload structure is enabled.

Syntax
------

```ManagedCPlusPlus
BOOLEAN NetPowerSettingsIsProtocolOffloadEnabled(
  _In_ NETPOWERSETTINGS          NetPowerSettings,
  _In_ PNDIS_PM_PROTOCOL_OFFLOAD NdisProtocolOffload
);
```

Parameters
----------

*NetPowerSettings* [in]  
A handle to the NETPOWERSETTINGS object associated with the net adapter. To retrieve the handle, call [**NetAdapterGetPowerSettings**](netadaptergetpowersettings.md).

*NdisProtocolOffload* [in]  
A pointer to a [**NDIS_PM_PROTOCOL_OFFLOAD**](https://msdn.microsoft.com/library/windows/hardware/ff566760) structure obtained by calling [**NetPowerSettingsGetProtocolOffload**](netpowersettingsgetprotocoloffload.md).

Return value
------------

Returns **TRUE** if the protocol offload is enabled, and **FALSE** otherwise.

Remarks
-------

The client driver calls **NetPowerSettingsIsProtocolOffloadEnabled** during a power transition, typically from its [*EVT_WDF_DEVICE_ARM_WAKE_FROM_SX*](https://msdn.microsoft.com/library/windows/hardware/ff540844) or [*EVT_WDF_DEVICE_ARM_WAKE_FROM_S0*](https://msdn.microsoft.com/library/windows/hardware/ff540843) callback function, or from the [*EVT_NET_ADAPTER_PREVIEW_PROTOCOL_OFFLOAD*](evt-net-adapter-preview-protocol-offload.md) callback function.

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


[**NDIS_PM_PROTOCOL_OFFLOAD**](https://msdn.microsoft.com/library/windows/hardware/ff566760)

 

 






