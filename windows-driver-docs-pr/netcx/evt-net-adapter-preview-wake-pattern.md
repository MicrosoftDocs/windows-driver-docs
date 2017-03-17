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

The client driver's implementation of the *EVT_NET_ADAPTER_PREVIEW_WAKE_PATTERN* event callback function that accepts or rejects an incoming wake-on-LAN (WOL) pattern.

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

typedef EVT_NET_ADAPTER_PREVIEW_WAKE_PATTERN PFN_NET_ADAPTER_PREVIEW_WAKE_PATTERN;
```

Parameters
----------

*Adapter* [in]  
The NDIS adapter object that the client created in a prior call to [**NetAdapterCreate**](netadaptercreate.md).

*ExistingPowerSettings* [in]  
A handle to the net wake settings object.

*WakePatternType* [in]  
An [**NDIS_PM_WOL_PACKET**](https://msdn.microsoft.com/library/windows/hardware/ff566766) enumeration value that specifies the type of the WOL packet.

*PatternToBeAdded* [in]  
A pointer to a structure of type [**NDIS_PM_WOL_PATTERN**](https://msdn.microsoft.com/library/windows/hardware/ff566768) that specifies the wake-on-LAN (WOL) pattern to accept or reject.

Return value
------------

To accept the pattern, the callback function must return STATUS_SUCCESS, or another status value for which NT_SUCCESS(status) equals TRUE.

To reject the pattern, return STATUS_NDIS_PM_WOL_PATTERN_LIST_FULL.

Remarks
-------

Register your implementation of this callback function by setting the appropriate member of [**NET_ADAPTER_POWER_CAPABILITIES**](net-adapter-power-capabilities.md) and then calling [**NetAdapterSetPowerCapabilities**](netadaptersetpowercapabilities.md).

In this callback, the driver typically uses the NETPOWERSETTINGS handle it receives in the *ExistingPowerSettings* parameter to iterate through the enabled wake patterns to determine whether to accept or reject *PatternToBeAdded*.  For an example, see [Configuring Power Management](configuring-power-management.md).

The client driver can use the pointer to examine the [**NDIS_PM_WOL_PATTERN**](https://msdn.microsoft.com/library/windows/hardware/ff566768) structure, but should not retain it. NetAdapterCx can release the wake pattern structure without notification to the driver.

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

 

 






