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

```cpp
EVT_NET_ADAPTER_SET_CAPABILITIES EvtNetAdapterSetCapabilities;

NTSTATUS EvtNetAdapterSetCapabilities(
  _In_ NETADAPTER Adapter
)
{ ... }
```

Parameters
----------

*Adapter* [in]  
The network adapter object that the client created in a prior call to [**NetAdapterCreate**](netadaptercreate.md).

Return value
------------

If the operation is successful, the callback function must return STATUS_SUCCESS, or another status value for which NT_SUCCESS(status) equals TRUE.

If this function returns an [NTSTATUS](https://msdn.microsoft.com/library/windows/hardware/ff557697) error code, the device fails to initialize.

Remarks
-------

To register an *EVT_NET_ADAPTER_SET_CAPABILITIES* callback function, the client driver must call [**NetAdapterCreate**](netadaptercreate.md).

NetAdapterCx calls *EVT_NET_ADAPTER_SET_CAPABILITIES* after [*EVT_WDF_DEVICE_PREPARE_HARDWARE*](https://msdn.microsoft.com/library/windows/hardware/ff540880) but before [*EVT_WDF_DEVICE_D0_ENTRY*](https://msdn.microsoft.com/library/windows/hardware/ff540848).

NetAdapterCx calls *EVT_NET_ADAPTER_SET_CAPABILITIES* once per device start.

In this function, the client typically sets the adapter's link and MAC capabilities, power capabilities and MTU size.  To do so, it uses the following methods:

* [**NetAdapterSetLinkLayerMtuSize**](netadaptersetlinklayermtusize.md) 
* [**NetAdapterSetLinkLayerCapabilities**](netadaptersetlinklayercapabilities.md)
* [**NetAdapterSetPowerCapabilities**](netadaptersetpowercapabilities.md)

Optionally the client can also call:

* [**NetAdapterSetCurrentLinkState**](netadaptersetcurrentlinkstate.md)
* [**NetAdapterSetDataPathCapabilities**](netadaptersetdatapathcapabilities.md)

To set an attribute that does not have equivalent NetAdapter functionality, for example to report offload capabilities, call [**NdisMSetMiniportAttributes**](https://msdn.microsoft.com/library/windows/hardware/ff563672) from [*EVT_NET_ADAPTER_SET_CAPABILITIES*](evt-net-adapter-set-capabilities.md).  Use [**NetAdapterWdmGetNdisHandle**](netadapterwdmgetndishandle.md) to get the NDIS handle.

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

 

 






