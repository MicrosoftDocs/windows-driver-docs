---
title: NET_ADAPTER_CONFIG structure
description: Describes the configuration options for a NetAdapterCx client driver. An initialized NET\_ADAPTER\_CONFIG structure is an input parameter to NetAdapterCreate.
ms.assetid: aa938a6d-91f5-4a28-89dd-03e28f4f9cad
keywords: ["NET_ADAPTER_CONFIG structure Network Drivers Starting with Windows Vista", "PNET_ADAPTER_CONFIG structure pointer Network Drivers Starting with Windows Vista"]
topic_type:
- apiref
api_name:
- NET_ADAPTER_CONFIG
api_location:
- netadapter.h
api_type:
- HeaderDef
---

# NET\_ADAPTER\_CONFIG structure


\[Some information relates to pre-released product which may be substantially modified before it's commercially released. Microsoft makes no warranties, express or implied, with respect to the information provided here.\]

Describes the configuration options for a NetAdapterCx client driver. An initialized **NET\_ADAPTER\_CONFIG** structure is an input parameter to [**NetAdapterCreate**](netadaptercreate.md).

Syntax
------

```ManagedCPlusPlus
typedef struct _NET_ADAPTER_CONFIG {
  ULONG                                     Size;
  NET_ADAPTER_DRIVER_TYPE                   Type;
  PFN_NET_ADAPTER_SET_CAPABILITIES          EvtAdapterSetCapabilities;
  PFN_NET_ADAPTER_CREATE_TXQUEUE            EvtAdapterCreateTxQueue;
  PFN_NET_ADAPTER_CREATE_RXQUEUE            EvtAdapterCreateRxQueue;
  WDF_OBJECT_ATTRIBUTES                     NetRequestObjectAttributes;
  WDF_OBJECT_ATTRIBUTES                     NetPowerSettingsObjectAttributes;
} NET_ADAPTER_CONFIG, *PNET_ADAPTER_CONFIG;
```

Members
-------

**Size**  
Size of the **NET\_ADAPTER\_CONFIG** structure.

**Type**  
A [**NET\_ADAPTER\_DRIVER\_TYPE**](net-adapter-driver-type.md)-typed value indicating the type of driver that is creating the NetAdapter object. Currently, the only supported value is **NET\_ADAPTER\_DRIVER\_TYPE\_MINIPORT**.

**EvtAdapterSetCapabilities**  
A pointer to the client's implementation of the [*EVT\_NET\_ADAPTER\_SET\_CAPABILITIES*](evt-net-adapter-set-capabilities.md) event callback.

**EvtAdapterCreateTxQueue**  
A pointer to the client's implementation of the [*EVT\_NET\_ADAPTER\_CREATE\_TXQUEUE*](evt-net-adapter-create-txqueue.md) event callback.

**EvtAdapterCreateRxQueue**  
A pointer to the client's implementation of the [*EVT\_NET\_ADAPTER\_CREATE\_RXQUEUE*](evt-net-adapter-create-rxqueue.md) event callback.

**NetRequestObjectAttributes**  
Optional WDF object attributes associated with the NETREQUESTQUEUE object, or NULL.

**NetPowerSettingsObjectAttributes**  
Optional WDF object attributes associated with the NETPOWERSETTINGS object, or NULL.

Remarks
-------

Call [**NET\_ADAPTER\_CONFIG\_INIT**](net-adapter-config-init.md) to initialize this structure.

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

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bnetvista\netvista%5D:%20NET_ADAPTER_CONFIG%20structure%20%20RELEASE:%20%281/19/2017%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")




