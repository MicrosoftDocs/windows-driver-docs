---
title: EVT_NET_ADAPTER_SET_CAPABILITIES callback function
topic_type:
- apiref
api_name:
- PFN_NET_ADAPTER_SET_CAPABILITIES
api_location:
- netadapter.h
api_type:
- UserDefined
---

# EVT_NET_ADAPTER_SET_CAPABILITIES callback function


[!include[NetAdapterCx Beta Prerelease](../netcx-beta-prerelease.md)]

The client driver's implementation of the *EVT_NET_ADAPTER_SET_CAPABILITIES* event callback function that sets the capabilities of the network adapter.

Syntax
------

```ManagedCPlusPlus
EVT_NET_ADAPTER_SET_CAPABILITIES EvtNetAdapterSetCapabilities;

NTSTATUS EvtNetAdapterSetCapabilities(
  _In_ NETADAPTER Adapter
)
{ ... }

typedef EVT_NET_ADAPTER_SET_CAPABILITIES PFN_NET_ADAPTER_SET_CAPABILITIES;
```

Parameters
----------

*Adapter* [in]  
The NDIS adapter object that the client created in a prior call to [**NetAdapterCreate**](netadaptercreate.md).

Return value
------------

If the operation is successful, the callback function must return STATUS_SUCCESS, or another status value for which NT_SUCCESS(status) equals TRUE.

If this function returns an [NTSTATUS](https://msdn.microsoft.com/library/windows/hardware/ff557697) error code, the device fails to initialize.

Remarks
-------

NetAdapterCx calls *EVT_NET_ADAPTER_SET_CAPABILITIES* after [*EVT_WDF_DEVICE_PREPARE_HARDWARE*](https://msdn.microsoft.com/library/windows/hardware/ff540880) but before [*EVT_WDF_DEVICE_D0_ENTRY*](https://msdn.microsoft.com/library/windows/hardware/ff540848).

NetAdapterCx calls *EVT_NET_ADAPTER_SET_CAPABILITIES* once per device arrival.

In this function, the client typically sets the adapter's link and MAC capabilities, and optionally specifies power capabilities and current link state.  To do so, it uses the following methods:

* [**NetAdapterSetCurrentLinkState**](netadaptersetcurrentlinkstate.md)
* [**NetAdapterSetDataPathCapabilities**](netadaptersetdatapathcapabilities.md)
* [**NetAdapterSetLinkLayerCapabilities**](netadaptersetlinklayercapabilities.md)
* [**NetAdapterSetPowerCapabilities**](netadaptersetpowercapabilities.md)

In NetAdapterCx version 1.0, the client driver reports offload capabilities by calling [**NdisMSetMiniportAttributes**](https://msdn.microsoft.com/library/windows/hardware/ff563672) from this callback routine. 

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


[**NetAdapterSetDataPathCapabilities**](netadaptersetdatapathcapabilities.md)

[**NetAdapterSetLinkLayerCapabilities**](netadaptersetlinklayercapabilities.md)

[**NetAdapterSetPowerCapabilities**](netadaptersetpowercapabilities.md)

 

 






