---
title: NET_ADAPTER_DATAPATH_CAPABILITIES structure
topic_type:
- apiref
api_name:
- NET_ADAPTER_DATAPATH_CAPABILITIES
api_location:
- netadapter.h
api_type:
- HeaderDef
---

# NET_ADAPTER_DATAPATH_CAPABILITIES structure


[!include[NetAdapterCx Beta Prerelease](../netcx-beta-prerelease.md)]

Describes the data path capabilities of the adapter.

Syntax
------

```cpp
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

The client driver passes an initialized **NET_ADAPTER_DATAPATH_CAPABILITIES** structure as an input parameter value to [**NetAdapterSetDataPathCapabilities**](netadaptersetdatapathcapabilities.md).

Call [**NET_ADAPTER_DATAPATH_CAPABILITIES_INIT**](net-adapter-datapath-capabilities-init.md) to initialize this structure.

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

 

 





