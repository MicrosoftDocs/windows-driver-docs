---
title: NET_ADAPTER_POWER_CAPABILITIES structure
description: Describes the power capabilities of the adapter.
ms.assetid: de2bd967-6e72-466a-8f5b-d669c324d155
keywords: ["NET_ADAPTER_POWER_CAPABILITIES structure Network Drivers Starting with Windows Vista", "PNET_ADAPTER_POWER_CAPABILITIES structure pointer Network Drivers Starting with Windows Vista"]
---

# NET\_ADAPTER\_POWER\_CAPABILITIES structure


[!include[NetAdapterCx Beta Prerelease](../netcx-beta-prerelease.md)]

Describes the power capabilities of the adapter.

Syntax
------

```ManagedCPlusPlus
typedef struct _NET_ADAPTER_POWER_CAPABILITIES {
  ULONG                                          Size;
  NET_ADAPTER_POWER_FLAGS                        Flags;
  NET_ADAPTER_WAKE_PATTERN_FLAGS                 SupportedWakePatterns;
  ULONG                                          NumTotalWakePatterns;
  ULONG                                          MaxWakePatternSize;
  ULONG                                          MaxWakePatternOffset;
  ULONG                                          MaxWakePacketSaveBuffer;
  NET_ADAPTER_PROTOCOL_OFFLOADS_FLAGS            SupportedProtocolOffloads;
  ULONG                                          NumArpOffloadIPv4Addresses;
  ULONG                                          NumNSOffloadIPv6Addresses;
  NET_ADAPTER_WAKEUP_EVENTS_FLAGS                SupportedWakeUpEvents;
  NET_ADAPTER_MEDIA_SPECIFIC_WAKEUP_EVENTS_FLAGS SupportedMediaSpecificWakeUpEvents;
  PFN_NET_ADAPTER_PREVIEW_WAKE_PATTERN           EvtAdapterPreviewWakePattern;
  PFN_NET_ADAPTER_PREVIEW_PROTOCOL_OFFLOAD       EvtAdapterPreviewProtocolOffload;
  WDF_TRI_STATE                                  ManageS0IdlePowerReferences;
} NET_ADAPTER_POWER_CAPABILITIES, *PNET_ADAPTER_POWER_CAPABILITIES;
```

Members
-------

**Size**  
Size of this structure in bytes.

**Flags**  
Bitwise OR of [**NET\_ADAPTER\_POWER\_FLAGS**](net-adapter-power-flags.md)-typed flags.

**SupportedWakePatterns**  
Bitwise OR of [**NET\_ADAPTER\_WAKE\_PATTERN\_FLAGS**](net-adapter-wake-pattern-flags.md)-typed flags that specify the wake-on-LAN (WOL) patterns that a network adapter supports.

**NumTotalWakePatterns**  
The total number of wake patterns that a network adapter supports. This is the sum of the number of supported wake protocol patterns and the number of supported wake bitmap patterns.

**MaxWakePatternSize**  
The maximum number of bytes that can be compared with a pattern.

**MaxWakePatternOffset**  
The number of bytes in a packet that can be examined, starting at the beginning of the MAC header.

**MaxWakePacketSaveBuffer**  
The number of bytes of a wake packet that the client can save to a buffer and indicate up the driver stack. This value must be less than or equal to the size, in bytes, of the maximum transmission unit (MTU) for the network media.

**SupportedProtocolOffloads**  
Bitwise OR of [**NET\_ADAPTER\_PROTOCOL\_OFFLOADS\_FLAGS**](net-adapter-protocol-offloads-flags.md)-typed flags that specify the protocol offload features that a network adapter supports.

**NumArpOffloadIPv4Addresses**  
The number of IPv4 addresses that the adapter supports for ARP offload.

**NumNSOffloadIPv6Addresses**  
The number of IPv6 NS offload requests that the adapter supports. This should be at least 2.

**SupportedWakeUpEvents**  
Bitwise OR of [**NET\_ADAPTER\_WAKEUP\_EVENTS\_FLAGS**](net-adapter-wakeup-events-flags.md)-typed flags that specify the media-independent wake-up events that a network adapter supports.

**SupportedMediaSpecificWakeUpEvents**  
Bitwise OR of [**NET\_ADAPTER\_MEDIA\_SPECIFIC\_WAKEUP\_EVENTS\_FLAGS**](net-adapter-media-specific-wakeup-events-flags.md)-typed flags that specify the media-specific wake-up events that a network adapter supports.

**EvtAdapterPreviewWakePattern**  
A pointer to the client's implementation of the [*EVT\_NET\_ADAPTER\_PREVIEW\_WAKE\_PATTERN*](evt-net-adapter-preview-wake-pattern.md) event callback.

**EvtAdapterPreviewProtocolOffload**  
A pointer to the client's implementation of the [*EVT\_NET\_ADAPTER\_PREVIEW\_PROTOCOL\_OFFLOAD*](evt-net-adapter-preview-protocol-offload.md) event callback.

**ManageS0IdlePowerReferences**  
TBD

Remarks
-------

The client driver passes an initialized **NET\_ADAPTER\_POWER\_CAPABILITIES** structure as an input parameter value to [**NetAdapterSetPowerCapabilities**](netadaptersetpowercapabilities.md).

Call [**NET\_ADAPTER\_POWER\_CAPABILITIES\_INIT**](net-adapter-power-capabilities-init.md) to initialize this structure.

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

 

 





