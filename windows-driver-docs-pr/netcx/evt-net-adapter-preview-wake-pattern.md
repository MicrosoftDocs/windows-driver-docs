---
title: EVT_NET_ADAPTER_PREVIEW_WAKE_PATTERN callback function
description: The client driver's implementation of the EVT\_NET\_ADAPTER\_PREVIEW\_WAKE\_PATTERN event callback function that accepts or rejects an incoming wake-on-LAN (WOL) pattern.
ms.assetid: 21049f7f-e066-4b01-b354-5b904385ef49
keywords: ["EvtNetAdapterPreviewWakePattern callback function Network Drivers Starting with Windows Vista", "EVT_NET_ADAPTER_PREVIEW_WAKE_PATTERN", "PFN_NET_ADAPTER_PREVIEW_WAKE_PATTERN callback function pointer Network Drivers Starting with Windows Vista"]
topic_type:
- apiref
api_name:
- PFN_NET_ADAPTER_PREVIEW_WAKE_PATTERN
api_location:
- netadapter.h
api_type:
- UserDefined
---

# EVT\_NET\_ADAPTER\_PREVIEW\_WAKE\_PATTERN callback function


[!include[NetAdapterCx Beta Prerelease](../netcx-beta-prerelease.md)]

The client driver's implementation of the *EVT\_NET\_ADAPTER\_PREVIEW\_WAKE\_PATTERN* event callback function that accepts or rejects an incoming wake-on-LAN (WOL) pattern.

Syntax
------

```ManagedCPlusPlus
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

*Adapter* \[in\]  
The NDIS adapter object that the client created in a prior call to [**NetAdapterCreate**](netadaptercreate.md).

*ExistingPowerSettings* \[in\]  
A handle to the net wake settings object.

*WakePatternType* \[in\]  
An [**NDIS\_PM\_WOL\_PACKET**](https://msdn.microsoft.com/library/windows/hardware/ff566766) enumeration value that specifies the type of the WOL packet.

*PatternToBeAdded* \[in\]  
A pointer to a structure of type [**NDIS\_PM\_WOL\_PATTERN**](https://msdn.microsoft.com/library/windows/hardware/ff566768) that specifies the wake-on-LAN (WOL) pattern to accept or reject.

Return value
------------

To accept the pattern, the callback function must return STATUS\_SUCCESS, or another status value for which NT\_SUCCESS(status) equals TRUE.

To reject the pattern, return STATUS\_NDIS\_PM\_WOL\_PATTERN\_LIST\_FULL.

Remarks
-------

Register your implementation of this callback function by setting the appropriate member of [**NET\_ADAPTER\_POWER\_CAPABILITIES**](net-adapter-power-capabilities.md) and then calling [**NetAdapterSetPowerCapabilities**](netadaptersetpowercapabilities.md).

In this callback, the driver typically iterates through the *ExistingPowerSettings* to determine whether to accept or reject *PatternToBeAdded*.

The client driver can use the pointer to examine the [**NDIS\_PM\_WOL\_PATTERN**](https://msdn.microsoft.com/library/windows/hardware/ff566768) structure, but should not retain it. NetAdapterCx can release the wake pattern structure without notification to the driver.

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
<td align="left">Netadapter.h</td>
</tr>
<tr class="odd">
<td align="left"><p>IRQL</p></td>
<td align="left"><p>PASSIVE_LEVEL</p></td>
</tr>
</tbody>
</table>

## See also


[*EVT\_NET\_ADAPTER\_PREVIEW\_PROTOCOL\_OFFLOAD*](evt-net-adapter-preview-protocol-offload.md)

[**NetAdapterSetPowerCapabilities**](netadaptersetpowercapabilities.md)

 

 






