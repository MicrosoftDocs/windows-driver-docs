---
title: NET_ADAPTER_POWER_FLAGS enumeration
topic_type:
- apiref
api_name:
- NET_ADAPTER_POWER_FLAGS
api_location:
- netadapter.h
api_type:
- HeaderDef
---

# NET_ADAPTER_POWER_FLAGS enumeration


[!include[NetAdapterCx Beta Prerelease](../netcx-beta-prerelease.md)]

Specifies a client driver's power capabilities.

Syntax
------

```ManagedCPlusPlus
typedef enum _NET_ADAPTER_POWER_FLAGS { 
  NET_ADAPTER_POWER_WAKE_PACKET_INDICATION  = NDIS_PM_WAKE_PACKET_INDICATION_SUPPORTED,
  NET_ADAPTER_POWER_SELECTIVE_SUSPEND       = NDIS_PM_SELECTIVE_SUSPEND_SUPPORTED
} NET_ADAPTER_POWER_FLAGS;
```

Constants
---------
**NET_ADAPTER_POWER_WAKE_PACKET_INDICATION**  
If this flag is set, the network adapter must be able to save the received packet that caused the adapter to generate a wake-up event.

If this flag is set, the client driver must be able to do the following with this packet after the network adapter transitions to a full-power state:

* The client driver must be able to indicate the packet by calling [**NdisMIndicateReceiveNetBufferLists**](https://msdn.microsoft.com/library/windows/hardware/ff563598). 
* The client driver must be able to issue an NDIS_STATUS_PM_WAKE_REASON status indication and must pass the packet with the indication. To indicate the received packet, the client calls [**NetAdapterWdmGetNdisHandle**](netadapterwdmgetndishandle.md) and then calls [**NdisMIndicateReceiveNetBufferLists**](https://msdn.microsoft.com/library/windows/hardware/ff563598).

For more information about this power management capability, see [NDIS Wake Reason Status Indications](../network/ndis-wake-reason-status-indications.md).

**NET_ADAPTER_POWER_SELECTIVE_SUSPEND**  
Specifies that NetAdapterCx should suspend an idle network adapter by transitioning the adapter to a low-power state.

Remarks
---
The **NET_ADAPTER_POWER_FLAGS** enumeration is used to specify power capabilities in the [**NET_ADAPTER_POWER_CAPABILITIES**](net-adapter-power-capabilities.md) structure.

The client driver passes an initialized **NET_ADAPTER_POWER_CAPABILITIES** structure as an input parameter value to [**NetAdapterSetPowerCapabilities**](netadaptersetpowercapabilities.md).

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

## See also

[**NET_ADAPTER_POWER_CAPABILITIES**](net-adapter-power-capabilities.md)

[**NDIS_PM_CAPABILITIES**](https://msdn.microsoft.com/library/windows/hardware/ff566748)
