---
title: EVT_NET_ADAPTER_SET_CAPABILITIES callback function
description: The client driver's implementation of the EVT\_NET\_ADAPTER\_SET\_CAPABILITIES event callback function that sets the capabilities of the network adapter.
ms.assetid: 88f2ed30-a4e8-48c4-a6cf-9b5d89cebe0f
keywords: ["EvtNetAdapterSetCapabilities callback function Network Drivers Starting with Windows Vista", "EVT_NET_ADAPTER_SET_CAPABILITIES", "PFN_NET_ADAPTER_SET_CAPABILITIES callback function pointer Network Drivers Starting with Windows Vista"]
topic_type:
- apiref
api_name:
- PFN_NET_ADAPTER_SET_CAPABILITIES
api_location:
- netadapter.h
api_type:
- UserDefined
---

# EVT\_NET\_ADAPTER\_SET\_CAPABILITIES callback function


[!include[NetAdapterCx Beta Prerelease](../netcx-beta-prerelease.md)]

The client driver's implementation of the *EVT\_NET\_ADAPTER\_SET\_CAPABILITIES* event callback function that sets the capabilities of the network adapter.

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

*Adapter* \[in\]  
The NDIS adapter object that the client created in a prior call to [**NetAdapterCreate**](netadaptercreate.md).

Return value
------------

If the operation is successful, the callback function must return STATUS\_SUCCESS, or another status value for which NT\_SUCCESS(status) equals TRUE.

If this function returns an [NTSTATUS](https://msdn.microsoft.com/library/windows/hardware/ff557697) error code, the device fails to initialize.

Remarks
-------

NetAdapterCx calls the client's *EVT\_NET\_ADAPTER\_SET\_CAPABILITIES* event callback function after [*EVT\_WDF\_PREPARE\_HARDWARE*](https://msdn.microsoft.com/library/windows/hardware/ff540880) returns success.

This function must set the adapter's link and MAC capabilities, and can optionally specify power capabilities and current link state.

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

 

 






