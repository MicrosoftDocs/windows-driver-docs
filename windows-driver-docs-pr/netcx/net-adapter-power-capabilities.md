---
title: NET_ADAPTER_POWER_CAPABILITIES structure
---

# NET_ADAPTER_POWER_CAPABILITIES structure


[!include[NetAdapterCx Beta Prerelease](../netcx-beta-prerelease.md)]

Describes the power capabilities of the adapter.

Syntax
------

```cpp
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
Bitwise OR of [**NET_ADAPTER_POWER_FLAGS**](net-adapter-power-flags.md)-typed flags.

**SupportedWakePatterns**  
Bitwise OR of [**NET_ADAPTER_WAKE_PATTERN_FLAGS**](net-adapter-wake-pattern-flags.md)-typed flags that specify the wake-on-LAN (WOL) patterns that a network adapter supports.

**NumTotalWakePatterns**  
The total number of wake patterns that a network adapter supports. This is the sum of the number of supported wake protocol patterns and the number of supported wake bitmap patterns.

**MaxWakePatternSize**  
The maximum number of bytes that can be compared with a pattern.

**MaxWakePatternOffset**  
The number of bytes in a packet that can be examined, starting at the beginning of the MAC header.

**MaxWakePacketSaveBuffer**  
The number of bytes of a wake packet that the client can save to a buffer and indicate up the driver stack. This value must be less than or equal to the size, in bytes, of the maximum transmission unit (MTU) for the network media.

**SupportedProtocolOffloads**  
Bitwise OR of [**NET_ADAPTER_PROTOCOL_OFFLOADS_FLAGS**](net-adapter-protocol-offloads-flags.md)-typed flags that specify the protocol offload features that a network adapter supports.

**NumArpOffloadIPv4Addresses**  
The number of IPv4 addresses that the adapter supports for ARP offload.

**NumNSOffloadIPv6Addresses**  
The number of IPv6 NS offload requests that the adapter supports. This should be at least 2.

**SupportedWakeUpEvents**  
Bitwise OR of [**NET_ADAPTER_WAKEUP_EVENTS_FLAGS**](net-adapter-wakeup-events-flags.md)-typed flags that specify the media-independent wake-up events that a network adapter supports.

**SupportedMediaSpecificWakeUpEvents**  
Bitwise OR of [**NET_ADAPTER_MEDIA_SPECIFIC_WAKEUP_EVENTS_FLAGS**](net-adapter-media-specific-wakeup-events-flags.md)-typed flags that specify the media-specific wake-up events that a network adapter supports.

**EvtAdapterPreviewWakePattern**  
A pointer to the client's implementation of the [*EVT_NET_ADAPTER_PREVIEW_WAKE_PATTERN*](evt-net-adapter-preview-wake-pattern.md) event callback.

**EvtAdapterPreviewProtocolOffload**  
A pointer to the client's implementation of the [*EVT_NET_ADAPTER_PREVIEW_PROTOCOL_OFFLOAD*](evt-net-adapter-preview-protocol-offload.md) event callback.

**ManageS0IdlePowerReferences**  
A [**WDF_TRI_STATE**](https://msdn.microsoft.com/library/windows/hardware/ff552533)-typed enumerator that indicates whether NetAdapterCx should manage power references for scenarios such as modern standby (AoAC).  See more info in the **Remarks** section.  This member can have one of the following values:

**WdfTrue** - NetAdapterCx manages power references. The client driver must be the power policy owner to specify **WdfTrue**.  
**WdfFalse** - NetAdapterCx does not manage power references.  
**WdfUseDefault** : if driver is the power policy owner, then use **WdfTrue**, otherwise use **WdfFalse**.

Remarks
-------

The client driver passes an initialized **NET_ADAPTER_POWER_CAPABILITIES** structure as an input parameter value to [**NetAdapterSetPowerCapabilities**](netadaptersetpowercapabilities.md).

Call [**NET_ADAPTER_POWER_CAPABILITIES_INIT**](net-adapter-power-capabilities-init.md) to initialize this structure.

The client driver configures its S0-Idle policy like any other WDF driver, by calling [**WdfDeviceAssignS0IdleSettings**](https://msdn.microsoft.com/library/windows/hardware/ff545903).

 When power reference management is enabled via **ManageS0IdlePowerReferences**,  NetAdapterCx manages power references that result in the WDFDEVICE being powered up/down as necessary. For example, the class extension acquires and releases power references so the device maintains power state as necessary to support modern standby (AoAC). Additionally, the client driver can set the **NET_ADAPTER_POWER_SELECTIVE_SUSPEND** flag in the [**NET_ADAPTER_POWER_FLAGS**](net-adapter-power-flags.md) enumeration to cause NetAdapterCx to manage power references for the data and control path. This will result in the device being powered down when it is idle. Note that the **NET_ADAPTER_POWER_SELECTIVE_SUSPEND** option results in improved power efficiency at the cost of some performance.

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

 See Also
----
[Power Policy Ownership](../wdf/power-policy-ownership.md)


 





