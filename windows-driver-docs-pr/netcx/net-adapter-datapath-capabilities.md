---
title: NET\_ADAPTER\_DATAPATH\_CAPABILITIES structure
description: Describes the data path capabilities of the adapter.
ms.assetid: 85fac4c9-4a91-4c6f-b906-6b6a38d360d8
keywords: ["NET_ADAPTER_DATAPATH_CAPABILITIES structure Network Drivers Starting with Windows Vista", "PNET_ADAPTER_DATAPATH_CAPABILITIES structure pointer Network Drivers Starting with Windows Vista"]
topic_type:
- apiref
api_name:
- NET_ADAPTER_DATAPATH_CAPABILITIES
api_location:
- netadapter.h
api_type:
- HeaderDef
---

# NET\_ADAPTER\_DATAPATH\_CAPABILITIES structure


[!include[NetAdapterCx Beta Prerelease](../netcx-beta-prerelease.md)]

Describes the data path capabilities of the adapter.

Syntax
------

```ManagedCPlusPlus
typedef struct _NET_ADAPTER_DATAPATH_CAPABILITIES {
  ULONG Size;
  ULONG NumTxQueues;
  ULONG NumRxQueues;
} NET_ADAPTER_DATAPATH_CAPABILITIES, *PNET_ADAPTER_DATAPATH_CAPABILITIES;
```

Members
-------

**Size**  
Size of this structure in bytes.

**NumTxQueues**  
Maximum number of transmit queues supported by the adapter.

**NumRxQueues**  
Maximum number of receive queues supported by the adapter.

Remarks
-------

The client driver passes an initialized **NET\_ADAPTER\_DATAPATH\_CAPABILITIES** structure as an input parameter value to [**NetAdapterSetDataPathCapabilities**](netadaptersetdatapathcapabilities.md).

Call [**NET\_ADAPTER\_DATAPATH\_CAPABILITIES\_INIT**](net-adapter-datapath-capabilities-init.md) to initialize this structure.

Requirements
------------

<table>
<colgroup>
<col width="50%" />
<col width="50%" />
</colgroup>
<tbody>
<tr class="odd">
<td align="left"><p>Minimum KMDF version</p></td>
<td align="left"><p>1.21</p></td>
</tr>
<tr class="even">
<td align="left"><p>Minimum NetAdapterCx version</p></td>
<td align="left"><p>1.0</p></td>
</tr>
<tr class="odd">
<td align="left"><p>Header</p></td>
<td align="left">Netadapter.h</td>
</tr>
</tbody>
</table>

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bnetvista\netvista%5D:%20NET_ADAPTER_DATAPATH_CAPABILITIES%20structure%20%20RELEASE:%20%281/19/2017%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")




