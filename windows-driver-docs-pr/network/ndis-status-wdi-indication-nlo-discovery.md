---
title: NDIS_STATUS_WDI_INDICATION_NLO_DISCOVERY
description: Miniport drivers use NDIS_STATUS_WDI_INDICATION_NLO_DISCOVERY to indicate Network List Offload (NLO) discovery.
ms.assetid: 1a789bd8-8601-45f3-a9bf-5220c20379cb
ms.date: 07/18/2017
keywords:
 - NDIS_STATUS_WDI_INDICATION_NLO_DISCOVERY Network Drivers Starting with Windows Vista
ms.localizationpriority: medium
---

# NDIS\_STATUS\_WDI\_INDICATION\_NLO\_DISCOVERY


Miniport drivers use NDIS\_STATUS\_WDI\_INDICATION\_NLO\_DISCOVERY to indicate Network List Offload (NLO) discovery.

| Object |
|--------|
| Port   |

 

The firmware detects APs for SSIDs pushed down in NLO. NLO is used in non-AOAC systems for fast connection when resuming from system sleep. It is also used in AOAC systems to scan APs for SSIDs that are pushed to the firmware.

The OS does not request periodic background scans when in CS. NLO scan is the preferred method in CS because the screen is off when users don’t need to see all visible APs but those for SSIDs that users have auto-connect profiles to auto connect to. The list of SSIDs to offload from the OS has a preferred authentication and cipher pair and up to 4 channel hints. When the list has at least one SSID, the firmware should start an NLO scan autonomously following the schedule of fast scan and slow scan phases. The class driver translates the OS request to a firmware request. The firmware is expected to do NLO scan according the schedule for the APs that support the preferred authentication and cipher pair associated with the SSIDs.

In each scan period, the firmware scans for SSIDs that match the criteria on the list of channels but not necessary constrained on the list of channels. The discovered AP information should be cached for indication.

When any matches are found, the firmware indicates NLO discovery and caches the list of discovered AP information for the host to retrieve.

The indication of NLO discovery happens in the following two cases.

-   When the NIC is in Dx:
    1.  Trigger the wake interrupt and wait for set power to D0 to continue the following steps.
    2.  Indicate NLO discovery.
    3.  Indicate that the firmware woke the stack with the reason of NLO discovery.
-   When the NIC is in D0:
    -   Indicate NLO discovery.

## Payload data


| Type                                                   | Multiple TLV instances allowed | Optional | Description                                                                                      |
|--------------------------------------------------------|--------------------------------|----------|--------------------------------------------------------------------------------------------------|
| [**WDI\_TLV\_BSS\_ENTRY**](https://msdn.microsoft.com/library/windows/hardware/dn926162) | X                              |          | A list of BSSIDs. The list must at least contain the entry that triggered this discovery status. |

 

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

 

 




