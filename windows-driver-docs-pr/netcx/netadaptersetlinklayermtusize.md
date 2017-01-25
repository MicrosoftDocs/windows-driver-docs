---
title: NetAdapterSetLinkLayerMtuSize method
description: Overrides the maximum transfer unit (MTU) size that the client driver provided to NetAdapterSetLinkLayerCapabilities.
ms.assetid: c3303fe1-18cd-4fd0-bdc9-6da9c0a95769
keywords: ["NetAdapterSetLinkLayerMtuSize method Network Drivers Starting with Windows Vista"]
topic_type:
- apiref
api_name:
- NetAdapterSetLinkLayerMtuSize
api_location:
- NetAdapterCxStub.lib
- NetAdapterCxStub.dll
api_type:
- LibDef
---

# NetAdapterSetLinkLayerMtuSize method


[!include[NetAdapterCx Beta Prerelease](../netcx-beta-prerelease.md)]

Overrides the maximum transfer unit (MTU) size that the client driver provided to [**NetAdapterSetLinkLayerCapabilities**](netadaptersetlinklayercapabilities.md).

Syntax
------

```ManagedCPlusPlus
void NetAdapterSetLinkLayerMtuSize(
  _In_ NETADAPTER Adapter,
  _In_ ULONG      MtuSize
);
```

Parameters
----------

*Adapter* \[in\]  
The NDIS adapter object that the client created in a prior call to [**NetAdapterCreate**](netadaptercreate.md).

*MtuSize* \[in\]  
The new size of the adapter's MTU, in bytes.

Return value
------------

This method does not return a value.

Remarks
-------

The client driver first sets MTU size by calling [**NetAdapterSetLinkLayerCapabilities**](netadaptersetlinklayercapabilities.md) from its [*EVT\_NET\_ADAPTER\_SET\_CAPABILITIES*](evt-net-adapter-set-capabilities.md) implementation.

The client driver can change MTU size after returning from [*EVT\_NET\_ADAPTER\_SET\_CAPABILITIES*](evt-net-adapter-set-capabilities.md) by calling **NetAdapterSetLinkLayerMtuSize**. Doing so causes all of the adapter's Tx and Rx queues to be recreated.

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
<td align="left"><p>Library</p></td>
<td align="left">NetAdapterCxStub.lib</td>
</tr>
<tr class="even">
<td align="left"><p>IRQL</p></td>
<td align="left"><p>PASSIVE_LEVEL</p></td>
</tr>
</tbody>
</table>

## See also


[**NetAdapterSetLinkLayerCapabilities**](netadaptersetlinklayercapabilities.md)

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bnetvista\netvista%5D:%20NetAdapterSetLinkLayerMtuSize%20method%20%20RELEASE:%20%281/19/2017%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")





