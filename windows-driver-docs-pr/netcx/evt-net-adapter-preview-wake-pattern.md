---
title: EVT_NET_ADAPTER_PREVIEW_WAKE_PATTERN callback function
topic_type:
- apiref
api_name:
- PFN_NET_ADAPTER_PREVIEW_WAKE_PATTERN
api_location:
- netadapter.h
api_type:
- UserDefined
---

# EVT_NET_ADAPTER_PREVIEW_WAKE_PATTERN callback function


[!include[NetAdapterCx Beta Prerelease](../netcx-beta-prerelease.md)]

Implement this optional callback to reject wake patterns that are not compatible with your hardware.

Syntax
------

```cpp
EVT_NET_ADAPTER_PREVIEW_WAKE_PATTERN EvtNetAdapterPreviewWakePattern;

NTSTATUS EvtNetAdapterPreviewWakePattern(
  _In_ NETADAPTER           Adapter,
  _In_ NETPOWERSETTINGS     ExistingPowerSettings,
  _In_ NDIS_PM_WOL_PACKET   WakePatternType,
  _In_ PNDIS_PM_WOL_PATTERN PatternToBeAdded
)
{ ... }
```

Parameters
----------

*Adapter* [in]  
The network adapter object that the client created in a prior call to [**NetAdapterCreate**](netadaptercreate.md).

*ExistingPowerSettings* [in]  
A handle to the net power settings object.

*WakePatternType* [in]  
An [**NDIS_PM_WOL_PACKET**](https://msdn.microsoft.com/library/windows/hardware/ff566766) enumeration value that specifies the type of the WOL packet.

*PatternToBeAdded* [in]  
A pointer to a structure of type [**NDIS_PM_WOL_PATTERN**](https://msdn.microsoft.com/library/windows/hardware/ff566768) that specifies the wake-on-LAN (WOL) pattern to accept or reject.

Return value
------------

To accept the pattern, the callback function must return STATUS_SUCCESS.

To reject the pattern, return STATUS_NDIS_PM_WOL_PATTERN_LIST_FULL.

Remarks
-------

Drivers are not required to implement EvtNetAdapterPreviewWakePattern, as NetAdapter already blocks wake patterns that are not compatible with the driver's [**NET_ADAPTER_POWER_CAPABILITIES**](net-adapter-power-capabilities.md). However, if your hardware has additional limitations that cannot be expressed in the [**NET_ADAPTER_POWER_CAPABILITIES**](net-adapter-power-capabilities.md) structure, you can provide EvtNetAdapterPreviewWakePattern to enforce those additional limitations.

Register your implementation of this callback function by setting the appropriate member of [**NET_ADAPTER_POWER_CAPABILITIES**](net-adapter-power-capabilities.md) and then calling [**NetAdapterSetPowerCapabilities**](netadaptersetpowercapabilities.md) during [*EVT_NET_ADAPTER_SET_CAPABILITIES*](evt-net-adapter-set-capabilities.md).

In this callback, the driver typically uses the NETPOWERSETTINGS handle it receives in the *ExistingPowerSettings* parameter to iterate through the enabled wake patterns to determine whether to accept or reject *PatternToBeAdded*.  For an example, see [Configuring Power Management](configuring-power-management.md).

The client driver can use the pointer to examine the [**NDIS_PM_WOL_PATTERN**](https://msdn.microsoft.com/library/windows/hardware/ff566768) structure, but should not retain it.  NetAdapterCx will destroy the wake pattern structure once the driver's EvtNetAdapterPreviewWakePattern returns.

In its [*EvtDeviceArmWakeFromS0*](https://msdn.microsoft.com/library/windows/hardware/ff540843) and [*EvtDeviceArmWakeFromSx*](https://msdn.microsoft.com/library/windows/hardware/ff540844) callback functions, the driver can iterate through the enabled wake patterns and protocol offloads to program them into the hardware.

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
<td align="left"><p>1.21</p></td>
</tr>
<tr class="odd">
<td align="left"><p>Minimum NetAdapterCx version</p></td>
<td align="left"><p>1.0</p></td>
</tr>
<tr class="even">
<td align="left"><p>Header</p></td>
<td align="left">Netadapter.h</td>
</tr>
<tr class="odd">
<td align="left"><p>IRQL</p></td>
<td align="left"><p>PASSIVE_LEVEL</p></td>
</tr>
</tbody>
</table>

## See also


[*EVT_NET_ADAPTER_PREVIEW_PROTOCOL_OFFLOAD*](evt-net-adapter-preview-protocol-offload.md)

[**NetAdapterSetPowerCapabilities**](netadaptersetpowercapabilities.md)

 

 






