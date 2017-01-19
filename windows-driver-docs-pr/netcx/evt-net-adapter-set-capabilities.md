---
title: EVT\_NET\_ADAPTER\_SET\_CAPABILITIES callback function
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


\[Some information relates to pre-released product which may be substantially modified before it's commercially released. Microsoft makes no warranties, express or implied, with respect to the information provided here.\]

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

NetAdapterCx calls the client's *EVT\_NET\_ADAPTER\_SET\_CAPABILITIES* event callback function after [*EVT\_WDF\_PREPARE\_HARDWARE*](wdf-evtdevicepreparehardware) returns success.

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

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bnetvista\netvista%5D:%20EVT_NET_ADAPTER_SET_CAPABILITIES%20callback%20function%20%20RELEASE:%20%281/19/2017%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")





