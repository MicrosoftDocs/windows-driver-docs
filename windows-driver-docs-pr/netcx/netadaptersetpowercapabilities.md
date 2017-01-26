---
title: NetAdapterSetPowerCapabilities method
description: Sets the power capabilities of the network adapter.
ms.assetid: 23eb3d91-d635-4be5-8b34-ccb60cda49be
keywords: ["NetAdapterSetPowerCapabilities method Network Drivers Starting with Windows Vista"]
topic_type:
- apiref
api_name:
- NetAdapterSetPowerCapabilities
api_location:
- netadapter.h
api_type:
- HeaderDef
---

# NetAdapterSetPowerCapabilities method


[!include[NetAdapterCx Beta Prerelease](../netcx-beta-prerelease.md)]

Sets the power capabilities of the network adapter.

Syntax
------

```ManagedCPlusPlus
void NetAdapterSetPowerCapabilities(
  _In_ NETADAPTER                      Adapter,
  _In_ PNET_ADAPTER_POWER_CAPABILITIES PowerCapabilities
);
```

Parameters
----------

*Adapter* \[in\]  
The NDIS adapter object that the client created in a prior call to [**NetAdapterCreate**](netadaptercreate.md).

*PowerCapabilities* \[in\]  
A pointer to an allocated and initialized [**NET\_ADAPTER\_POWER\_CAPABILITIES**](net-adapter-power-capabilities.md) structure.

Return value
------------

This method does not return a value.

Remarks
-------

The client driver sets capabilities by calling the following methods from its [*EVT\_NET\_ADAPTER\_SET\_CAPABILITIES*](evt-net-adapter-set-capabilities.md) event callback routine.

-   [**NetAdapterSetDataPathCapabilities**](netadaptersetdatapathcapabilities.md)
-   [**NetAdapterSetLinkLayerCapabilities**](netadaptersetlinklayercapabilities.md)
-   **NetAdapterSetPowerCapabilities**

Alternatively, the client can call **NetAdapterSetPowerCapabilities** in a callback that NdisCx calls after [*EVT\_NET\_ADAPTER\_SET\_CAPABILITIES*](evt-net-adapter-set-capabilities.md). If it does, it must not change the [*EVT\_NET\_ADAPTER\_PREVIEW\_WAKE\_PATTERN*](evt-net-adapter-preview-wake-pattern.md) event callback function.

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


[**NdisMIndicateStatusEx**](https://msdn.microsoft.com/library/windows/hardware/ff563600)

[**NdisMSetMiniportAttributes**](https://msdn.microsoft.com/library/windows/hardware/ff563672)

[**NetAdapterSetDataPathCapabilities**](netadaptersetdatapathcapabilities.md)

[**NetAdapterSetLinkLayerCapabilities**](netadaptersetlinklayercapabilities.md)
 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bnetvista\netvista%5D:%20NetAdapterSetPowerCapabilities%20method%20%20RELEASE:%20%281/19/2017%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")





