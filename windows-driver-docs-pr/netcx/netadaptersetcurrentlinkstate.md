---
title: NetAdapterSetCurrentLinkState method
description: Set the current link state of the of the network adapter.
ms.assetid: ea560091-3ba4-428e-8560-6d75ce0493e6
keywords: ["NetAdapterSetCurrentLinkState method Network Drivers Starting with Windows Vista"]
topic_type:
- apiref
api_name:
- NetAdapterSetCurrentLinkState
api_location:
- netadapter.h
api_type:
- HeaderDef
---

# NetAdapterSetCurrentLinkState method


[!include[NetAdapterCx Beta Prerelease](../netcx-beta-prerelease.md)]

Set the current link state of the of the network adapter.

Syntax
------

```ManagedCPlusPlus
VOID NetAdapterSetCurrentLinkState(
  _In_ NETADAPTER              Adapter,
  _In_ PNET_ADAPTER_LINK_STATE CurrentLinkState
);
```

Parameters
----------

*Adapter* \[in\]  
The NDIS adapter object that the client created in a prior call to [**NetAdapterCreate**](netadaptercreate.md).

*CurrentLinkState* \[in\]  
A pointer to an allocated and initialized [**NET\_ADAPTER\_LINK\_STATE**](net-adapter-link-state.md) structure that describes the current link state of the adapter.

Return value
------------

This method does not return a value.

Remarks
-------

The client driver calls **NetAdapterSetCurrentLinkState** from its [*EVT\_NET\_ADAPTER\_SET\_CAPABILITIES*](evt-net-adapter-set-capabilities.md) implementation, or from a callback function that NetAdapterCx calls after *EVT\_NET\_ADAPTER\_SET\_CAPABILITIES*.

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
<td align="left">Netadapter.h (include Netadaptercx.h)</td>
</tr>
<tr class="odd">
<td align="left"><p>IRQL</p></td>
<td align="left"><p>DISPATCH_LEVEL</p></td>
</tr>
</tbody>
</table>

## See also


[**NET\_ADAPTER\_LINK\_STATE\_INIT**](net-adapter-link-state-init.md)

[**NET\_ADAPTER\_LINK\_STATE\_INIT\_DISCONNECTED**](net-adapter-link-state-init-disconnected.md)

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bnetvista\netvista%5D:%20NetAdapterSetCurrentLinkState%20method%20%20RELEASE:%20%281/19/2017%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")





