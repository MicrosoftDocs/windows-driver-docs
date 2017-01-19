---
title: NetAdapterSetDataPathCapabilities method
description: Sets the data path capabilities of the network adapter.
ms.assetid: 935f53c6-426d-4ec3-b4d8-43a35de2a87c
keywords: ["NetAdapterSetDataPathCapabilities method Network Drivers Starting with Windows Vista"]
topic_type:
- apiref
api_name:
- NetAdapterSetDataPathCapabilities
api_location:
- netadapter.h
api_type:
- HeaderDef
---

# NetAdapterSetDataPathCapabilities method


\[Some information relates to pre-released product which may be substantially modified before it's commercially released. Microsoft makes no warranties, express or implied, with respect to the information provided here.\]

Sets the data path capabilities of the network adapter.

Syntax
------

```ManagedCPlusPlus
VOID NetAdapterSetDataPathCapabilities(
  _In_ NETADAPTER                         Adapter,
  _In_ PNET_ADAPTER_DATAPATH_CAPABILITIES DataPathCapabilities
);
```

Parameters
----------

*Adapter* \[in\]  
The NDIS adapter object that the client created in a prior call to [**NetAdapterCreate**](netadaptercreate.md).

*DataPathCapabilities* \[in\]  
A pointer to an allocated and initialized [**NET\_ADAPTER\_DATAPATH\_CAPABILITIES**](net-adapter-datapath-capabilities.md) structure.

Return value
------------

This method does not return a value.

Remarks
-------

The client driver must call this method from its [*EVT\_NET\_ADAPTER\_SET\_CAPABILITIES*](evt-net-adapter-set-capabilities.md) event callback routine.

This method along with a few other set capability methods (see below) is the replacement for the [**NDIS\_MINIPORT\_ADAPTER\_GENERAL\_ATTRIBUTES**](https://msdn.microsoft.com/library/windows/hardware/ff565923) union that a (non-WDF) client of Ndis.sys sets by calling [**NdisMSetMiniportAttributes**](https://msdn.microsoft.com/library/windows/hardware/ff563672).

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
<td align="left"><p>PASSIVE_LEVEL</p></td>
</tr>
</tbody>
</table>

## See also


[**NetAdapterSetLinkLayerCapabilities**](netadaptersetlinklayercapabilities.md)

[**NetAdapterSetPowerCapabilities**](netadaptersetpowercapabilities.md)

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bnetvista\netvista%5D:%20NetAdapterSetDataPathCapabilities%20method%20%20RELEASE:%20%281/19/2017%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")





