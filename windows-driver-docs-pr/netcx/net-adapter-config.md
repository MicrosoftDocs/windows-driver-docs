---
title: NET_ADAPTER_CONFIG structure
topic_type:
- apiref
api_name:
- NET_ADAPTER_CONFIG
api_location:
- netadapter.h
api_type:
- HeaderDef
---

# NET_ADAPTER_CONFIG structure


[!include[NetAdapterCx Beta Prerelease](../netcx-beta-prerelease.md)]

Describes the configuration options for a NetAdapterCx client driver. An initialized **NET_ADAPTER_CONFIG** structure is an input parameter to [**NetAdapterCreate**](netadaptercreate.md).

Syntax
------

```cpp
typedef struct _NET_ADAPTER_CONFIG {
  ULONG                                     Size;
  PFN_NET_ADAPTER_SET_CAPABILITIES          EvtAdapterSetCapabilities;
  PFN_NET_ADAPTER_CREATE_TXQUEUE            EvtAdapterCreateTxQueue;
  PFN_NET_ADAPTER_CREATE_RXQUEUE            EvtAdapterCreateRxQueue;
  PWDF_OBJECT_ATTRIBUTES                    NetRequestObjectAttributes;
  PWDF_OBJECT_ATTRIBUTES                    NetPowerSettingsObjectAttributes;
} NET_ADAPTER_CONFIG, *PNET_ADAPTER_CONFIG;
```

Members
-------

**Size**  
Size of the **NET_ADAPTER_CONFIG** structure.

**EvtAdapterSetCapabilities**  
A pointer to the client's implementation of the [*EVT_NET_ADAPTER_SET_CAPABILITIES*](evt-net-adapter-set-capabilities.md) event callback.

**EvtAdapterCreateTxQueue**  
A pointer to the client's implementation of the [*EVT_NET_ADAPTER_CREATE_TXQUEUE*](evt-net-adapter-create-txqueue.md) event callback.

**EvtAdapterCreateRxQueue**  
A pointer to the client's implementation of the [*EVT_NET_ADAPTER_CREATE_RXQUEUE*](evt-net-adapter-create-rxqueue.md) event callback.

**NetRequestObjectAttributes**  
Optional WDF object attributes associated with the NETREQUEST objects, or NULL.  If non-NULL, all NETREQUESTs created by the framework will have these attributes.

**NetPowerSettingsObjectAttributes**  
Optional WDF object attributes associated with the NETPOWERSETTINGS object, or NULL.

Remarks
-------

Call [**NET_ADAPTER_CONFIG_INIT**](net-adapter-config-init.md) to initialize this structure.

In NetAdapterCx version 1.1, the **Type** member from version 1.0 was removed.

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
<td align="left"><p>1.23</p></td>
</tr>
<tr class="even">
<td align="left"><p>Minimum NetAdapterCx version</p></td>
<td align="left"><p>1.1</p></td>
</tr>
<tr class="odd">
<td align="left"><p>Header</p></td>
<td align="left">Netadapter.h (include NetAdapterCx.h) </td>
</tr>
</tbody>
</table>

 

 





