---
title: NetConfigurationQueryLinkLayerAddress method
topic_type:
- apiref
api_name:
- NetConfigurationQueryLinkLayerAddress
api_location:
- netconfiguration.h
api_type:
- HeaderDef
---

# NetConfigurationQueryLinkLayerAddress method

[!include[NetAdapterCx Beta Prerelease](../netcx-beta-prerelease.md)]

The NetConfigurationQueryLinkLayerAddress retrieves the software-configurable link layer address address that was stored in the registry for a NIC.

Syntax
------

```cpp
NTSTATUS NetConfigurationQueryLinkLayerAddress(
  _In_  NETCONFIGURATION                Configuration,
  _Out_ PNET_ADAPTER_LINK_LAYER_ADDRESS LinkLayerAddress
);
```

Parameters
----------

*Configuration* [in]  
Handle to a NETCONFIGURATION object that represents an opened registry key.

*LinkLayerAddress* [out]  
A pointer to a NET_ADAPTER_LINK_LAYER_ADDRESS object that represents the link layer address stored in the registry key.

Return value
------------
Returns one of the following status values:

|Return Code|Description|
|---|---|
| STATUS_SUCCESS | The operation succeeded.|
| STATUS_FAILURE | The operation failed. |

Remarks
-----
The client driver obtains a handle to a NETCONFIGURATION object by calling  [**NetAdapterOpenConfiguration**](netadapteropenconfiguration.md) or [**NetConfigurationOpenSubConfiguration**](netconfigurationopensubconfiguration.md).

In NetAdapterCx 1.0, this method was called **NetConfigurationQueryNetworkAddress**. It was renamed to **NetConfigurationQueryLinkLayerAddress** in NetAdapterCx 1.1.

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
<td align="left"><p>1.23</p></td>
</tr>
<tr class="odd">
<td align="left"><p>Minimum NetAdapterCx version</p></td>
<td align="left"><p>1.1</p></td>
</tr>
<tr class="even">
<td align="left"><p>Header</p></td>
<td align="left">Netconfiguration.h (include Netadaptercx.h)</td>
</tr>
<tr class="odd">
<td align="left"><p>IRQL</p></td>
<td align="left"><p>PASSIVE_LEVEL</p></td>
</tr>
</tbody>
</table>

 

 





