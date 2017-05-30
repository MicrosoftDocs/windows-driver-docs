---
title: NET_ADAPTER_WAKEUP_EVENTS_FLAGS enumeration
topic_type:
- apiref
api_name:
- NET_ADAPTER_WAKEUP_EVENTS_FLAGS
api_location:
- netadapter.h
api_type:
- HeaderDef
---

# NET_ADAPTER_WAKEUP_EVENTS_FLAGS enumeration

[!include[NetAdapterCx Beta Prerelease](../netcx-beta-prerelease.md)]

Specifies the media-independent wake-up events that a network adapter supports.

Syntax
------

```cpp
typedef enum _NET_ADAPTER_WAKEUP_EVENTS_FLAGS { 
  NET_ADAPTER_WAKE_ON_MEDIA_CONNECT     = NDIS_PM_WAKE_ON_MEDIA_CONNECT_SUPPORTED,
  NET_ADAPTER_WAKE_ON_MEDIA_DISCONNECT  = NDIS_PM_WAKE_ON_MEDIA_DISCONNECT_SUPPORTED
} NET_ADAPTER_WAKEUP_EVENTS_FLAGS;
```

Constants
---------

**NET_ADAPTER_WAKE_ON_MEDIA_CONNECT**  
If this flag is set, the network adapter can generate a wake-up event when it becomes connected to the networking interface.

**NET_ADAPTER_WAKE_ON_MEDIA_DISCONNECT**  
If this flag is set, the network adapter can generate a wake-up event when it becomes disconnected to the networking interface.

Remarks
-------
The **NET_ADAPTER_WAKEUP_EVENTS_FLAGS** enumeration is used to specify media-independent wake-up events in the [**NET_ADAPTER_POWER_CAPABILITIES**](net-adapter-power-capabilities.md) structure.

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

[**NDIS_PM_CAPABILITIES**](https://msdn.microsoft.com/library/windows/hardware/ff566748)

 

 






