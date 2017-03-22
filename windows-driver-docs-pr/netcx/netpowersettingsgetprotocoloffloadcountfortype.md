---
title: NetPowerSettingsGetProtocolOffloadCountForType method
topic_type:
- apiref
api_name:
- NetPowerSettingsGetProtocolOffloadCountForType
api_location:
- NetAdapterCxStub.lib
- NetAdapterCxStub.dll
api_type:
- LibDef
---

# NetPowerSettingsGetProtocolOffloadCountForType method


[!include[NetAdapterCx Beta Prerelease](../netcx-beta-prerelease.md)]

Retrieves the number of protocol offload structures in the NETPOWERSETTINGS object for the particular offload type.

Syntax
------

```cpp
ULONG NetPowerSettingsGetProtocolOffloadCountForType(
  _In_ NETPOWERSETTINGS              NetPowerSettings,
  _In_ NDIS_PM_PROTOCOL_OFFLOAD_TYPE ProtocolOffloadType
);
```

Parameters
----------

*NetPowerSettings* [in]  
A handle to the NETPOWERSETTINGS object associated with the net adapter. To retrieve the handle, call [**NetAdapterGetPowerSettings**](netadaptergetpowersettings.md).

*ProtocolOffloadType* [in]  
An [**NDIS_PM_PROTOCOL_OFFLOAD_TYPE**](https://msdn.microsoft.com/library/windows/hardware/ff566765) value that contains the type of protocol offload to count.

Return value
------------

Returns the total number of enabled and disabled protocol offloads in the NETPOWERSETTINGS object for the specified protocol offload type.

Remarks
-------

The client driver must only call **NetPowerSettingsGetProtocolOffloadCountForType** during a power transition, typically from its [*EVT_WDF_DEVICE_ARM_WAKE_FROM_SX*](https://msdn.microsoft.com/library/windows/hardware/ff540844) or [*EVT_WDF_DEVICE_ARM_WAKE_FROM_S0*](https://msdn.microsoft.com/library/windows/hardware/ff540843) callback function, or from the [*EVT_NET_ADAPTER_PREVIEW_PROTOCOL_OFFLOAD*](evt-net-adapter-preview-protocol-offload.md) callback function.  Otherwise, the call results in a system bugcheck.

To determine if a specific protocol offload is enabled, call [**NetPowerSettingsIsProtocolOffloadEnabled**](netpowersettingsisprotocoloffloadenabled.md).

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


[**NDIS_PM_PROTOCOL_OFFLOAD_TYPE**](https://msdn.microsoft.com/library/windows/hardware/ff566765)

 

 






