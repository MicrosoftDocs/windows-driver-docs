---
title: EVT_NET_ADAPTER_PREVIEW_PROTOCOL_OFFLOAD callback function
topic_type:
- apiref
api_name:
- PFN_NET_ADAPTER_PREVIEW_PROTOCOL_OFFLOAD
api_location:
- netadapter.h
api_type:
- UserDefined
---

# EVT_NET_ADAPTER_PREVIEW_PROTOCOL_OFFLOAD callback function

[!include[NetAdapterCx Beta Prerelease](../netcx-beta-prerelease.md)]

The client driver's implementation of the *EVT_NET_ADAPTER_PREVIEW_PROTOCOL_OFFLOAD* event callback function that accepts or rejects an incoming protocol offload.

Syntax
------

```cpp
EVT_NET_ADAPTER_PREVIEW_PROTOCOL_OFFLOAD EvtNetAdapterPreviewProtocolOffload;

NTSTATUS EvtNetAdapterPreviewProtocolOffload(
  _In_ NETADAPTER                    Adapter,
  _In_ NETPOWERSETTINGS              ExistingPowerSettings,
  _In_ NDIS_PM_PROTOCOL_OFFLOAD_TYPE ProtocolOffloadType,
  _In_ PNDIS_PM_PROTOCOL_OFFLOAD     ProtocolOffloadToBeAdded
)
{ ... }

typedef EVT_NET_ADAPTER_PREVIEW_PROTOCOL_OFFLOAD PFN_NET_ADAPTER_PREVIEW_PROTOCOL_OFFLOAD;
```

Parameters
----------

*Adapter* [in]  
The NDIS adapter object that the client created in a prior call to [**NetAdapterCreate**](netadaptercreate.md).

*ExistingPowerSettings* [in]  
A handle to the net wake settings object.

*ProtocolOffloadType* [in]  
An [**NDIS_PM_PROTOCOL_OFFLOAD_TYPE**](https://msdn.microsoft.com/library/windows/hardware/ff566765) enumeration value that specifies the type of protocol offload.

*ProtocolOffloadToBeAdded* [in]  
A pointer to a structure of type [**NDIS_PM_PROTOCOL_OFFLOAD**](https://msdn.microsoft.com/library/windows/hardware/ff566760) that specifies the protocol offload to accept or reject.

Return value
------------

To accept the pattern, the callback function must return STATUS_SUCCESS, or another status value for which NT_SUCCESS(status) equals TRUE.

To reject the pattern, return STATUS_NDIS_PM_PROTOCOL_OFFLOAD_LIST_FULL.

Remarks
-------

Register your implementation of this callback function by setting the appropriate member of [**NET_ADAPTER_POWER_CAPABILITIES**](net-adapter-power-capabilities.md) and then calling [**NetAdapterSetPowerCapabilities**](netadaptersetpowercapabilities.md).

In this callback, the driver typically iterates through the *ExistingPowerSettings* to determine whether to accept or reject *ProtocolOffloadToBeAdded*.

For more info, see [Configuring Power Management](configuring-power-managementE.md).

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
<td align="left">Netadapter.h</td>
</tr>
<tr class="odd">
<td align="left"><p>IRQL</p></td>
<td align="left"><p>PASSIVE_LEVEL</p></td>
</tr>
</tbody>
</table>

## See also


[*EVT_NET_ADAPTER_PREVIEW_WAKE_PATTERN*](evt-net-adapter-preview-wake-pattern.md)

[**NetAdapterSetPowerCapabilities**](netadaptersetpowercapabilities.md)

 

 






