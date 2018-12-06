---
title: OID_WDI_SET_NETWORK_LIST_OFFLOAD
description: OID_WDI_SET_NETWORK_LIST_OFFLOAD sets a list of preferred SSIDs for the firmware to scan for APs.
ms.assetid: 2df9ee2b-78df-4f92-9b40-5945ecc81c7e
ms.date: 07/18/2017
keywords:
 - OID_WDI_SET_NETWORK_LIST_OFFLOAD Network Drivers Starting with Windows Vista
ms.localizationpriority: medium
---

# OID\_WDI\_SET\_NETWORK\_LIST\_OFFLOAD


OID\_WDI\_SET\_NETWORK\_LIST\_OFFLOAD sets a list of preferred SSIDs for the firmware to scan for APs.

| Scope        | Set serialized with task | Normal execution time (seconds) |
|--------------|--------------------------|---------------------------------|
| Primary port | Yes                      | 1                               |

 

There are two types of Network List Offload (NLO). One type is offload to NICs on Always On Always Connected (AOAC) systems. The other is Instant Connect NLO which, in Windows 8 and Windows 8.1, was only used for non-AOAC systems to quickly reconnect Wi-Fi at resume from hibernation. For Instant Connect, the list is sent down before the system goes into hibernation. Going forward, Instant Connect is used for resume from hibernation on AOAC systems that support it.

## Instant Connect


WDI handles Instant Connect NLO and uses a combination of targeted scans to fulfill the request from the OS. IHV drivers do not need to handle this Instant Connect OS request.

When the OS resumes from hibernation, the OS sends an Instant Connect NLO. WDI makes a union of all channel hints for a targeted scan OID. IHV drivers should support such a targeted scan as defined in [OID\_WDI\_TASK\_SCAN](oid-wdi-task-scan.md). The following section applies to Network List Offload to capable NICs on AOAC systems.

## Network List Offload


The OS does not request periodic background scans when in CS. A NLO scan is the preferred method in CS because the screen is off when users do not need to see all visible APs. SSIDs that users have auto-connect profiles set to auto-connect are the only useful APs. The list of SSIDs to offload from the OS has a preferred authentication and cipher pair, and up to four channel hints. When the list has a least one SSID, the firmware should start to do a NLO scan autonomously, following the schedule of fast scan and slow scan phases. The WDI compliant driver translates the operating system request to a firmware request. The firmware is expected to do a NLO scan according the schedule for the APs. The APs should support the preferred authentication and cipher pair associated with the SSIDs.

The request to the firmware has a list of channel hints for all offload SSIDs. The WDI compliant driver combines them for the firmware. For example, if SSID1\[auth1, cipher1\] has channel hints of 1 and 6, and SSID2\[auth2, cipher2\] has channel hints of 6 and 11, the request to the firmware is a list of SSIDs { SSID1\[auth1, cipher1\], SSID2\[auth2, cipher2\] } and list of channels to scan { 1, 6, 11 }.

In each scan period, the firmware scans for SSIDs that match the criteria on the list of channels, but not necessary constrained on the list of channels. The discovered AP information should be cached for the host to retrieve. The firmware indicates NLO discovery when at least one BSSID matches the SSID, algorithm, and cipher, but the channel match is not required.

Each OID\_WDI\_SET\_NETWORK\_LIST\_OFFLOAD that the UE sends to the LE represents a fresh NLO scan request. Any previous such requests or states are renewed. LE scans for NLO and only indicates once for a found AP per request. The UE replumbs (12 times; this is subject to change) NLO at Dx transitions if a found AP is not connected successfully (due to reasons such as: an AP is found but devices move around, the AP signal fades, and the connection fails; or prolong EAP authentication fails partway through). The LE and firmware should delay the NLO scan schedule based on the delay configuration in [**WDI\_TLV\_NETWORK\_LIST\_OFFLOAD\_CONFIG**](https://msdn.microsoft.com/library/windows/hardware/dn897851). This is a number that the UE uses to conform to the schedule of the operating system's original NLO command.

The default scan type for NLO is WDI\_SCAN\_TYPE\_AUTO. When actively scanning a channel, the firmware should use the wildcard SSID. Visible APs should be compared with SSIDs on the offload list to decide a match. This is to reduce privacy exposure.

Indicating NLO discovery has two cases.

1.  When the NIC is in D2, it must do the following steps.
    -   Trigger the wake interrupt and wait for set power to D0 before continuing to the following steps.
    -   Indicate that the firmware woke the stack with the reason of NLO discovery.
    -   Return D0 command.
    -   Indicate NLO discovery with all of the found AP information.

2.  When the NIC is in D0, it must do the following step.
    -   Indicate NLO discovery with all of the found AP information.

## Set property parameters


| TLV                                                                                                  | Multiple TLV instances allowed | Optional | Description         |
|------------------------------------------------------------------------------------------------------|--------------------------------|----------|---------------------|
| [**WDI\_TLV\_NETWORK\_LIST\_OFFLOAD\_PARAMETERS**](https://msdn.microsoft.com/library/windows/hardware/dn897852) |                                |          | The NLO parameters. |

 

## Set property results


No additional data. The data in the header is sufficient.
Requirements
------------

<table>
<colgroup>
<col width="50%" />
<col width="50%" />
</colgroup>
<tbody>
<tr class="odd">
<td><p>Minimum supported client</p></td>
<td><p>Windows 10</p></td>
</tr>
<tr class="even">
<td><p>Minimum supported server</p></td>
<td><p>Windows Server 2016</p></td>
</tr>
<tr class="odd">
<td><p>Header</p></td>
<td>Dot11wdi.h</td>
</tr>
</tbody>
</table>

 

 




