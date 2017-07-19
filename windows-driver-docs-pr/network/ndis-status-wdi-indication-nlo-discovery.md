---
title: NDIS\_STATUS\_WDI\_INDICATION\_NLO\_DISCOVERY
author: windows-driver-content
description: Miniport drivers use NDIS\_STATUS\_WDI\_INDICATION\_NLO\_DISCOVERY to indicate Network List Offload (NLO) discovery.
ms.assetid: 1a789bd8-8601-45f3-a9bf-5220c20379cb
ms.author: windowsdriverdev 
ms.date: 0718/2017 
ms.topic: article 
ms.prod: windows-hardware 
ms.technology: windows-devices 
keywords:
 - NDIS_STATUS_WDI_INDICATION_NLO_DISCOVERY Network Drivers Starting with Windows Vista
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

 

 


--------------------
[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bnetvista\netvista%5D:%20NDIS_STATUS_WDI_INDICATION_NLO_DISCOVERY%20%20RELEASE:%20%286/30/2017%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")


