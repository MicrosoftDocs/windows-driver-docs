---
title: OID_WDI_TASK_CREATE_PORT
description: OID_WDI_TASK_CREATE_PORT requests that a new 802.11 entity is created by the IHV component.
ms.assetid: e1a03a97-608f-42af-bd39-37a7eb9ad5b7
ms.date: 07/18/2017
keywords:
 - OID_WDI_TASK_CREATE_PORT Network Drivers Starting with Windows Vista
ms.localizationpriority: medium
---

# OID\_WDI\_TASK\_CREATE\_PORT


OID\_WDI\_TASK\_CREATE\_PORT requests that a new 802.11 entity is created by the IHV component.

| Object  | Abort capable | Default priority (host driver policy) | Normal execution time (seconds) |
|---------|---------------|---------------------------------------|---------------------------------|
| Adapter | No            | 6                                     | 1                               |

 

The operation mode of the created port is set to **WDI\_OPERATION\_MODE\_STA** unless it has been specified in the task parameters.

If the MAC is to function as a Wi-Fi Direct device port, **uOpmodeMask** contains **WDI\_OPERATION\_MODE\_P2P\_DEVICE**. In this case, the IHV component driver must assign the MAC address reserved for the Wi-Fi Direct Device to this port and return it in the request completion indication.

## Task parameters


<table>
<colgroup>
<col width="25%" />
<col width="25%" />
<col width="25%" />
<col width="25%" />
</colgroup>
<thead>
<tr class="header">
<th>TLV</th>
<th>Multiple TLV instances allowed</th>
<th>Optional</th>
<th>Description</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><a href="https://msdn.microsoft.com/library/windows/hardware/dn926273" data-raw-source="[&lt;strong&gt;WDI_TLV_CREATE_PORT_PARAMETERS&lt;/strong&gt;](https://msdn.microsoft.com/library/windows/hardware/dn926273)"><strong>WDI_TLV_CREATE_PORT_PARAMETERS</strong></a></td>
<td></td>
<td></td>
<td>Parameters for port creation.</td>
</tr>
<tr class="even">
<td><a href="https://msdn.microsoft.com/library/windows/hardware/dn926270" data-raw-source="[&lt;strong&gt;WDI_TLV_CREATE_PORT_MAC_ADDRESS&lt;/strong&gt;](https://msdn.microsoft.com/library/windows/hardware/dn926270)"><strong>WDI_TLV_CREATE_PORT_MAC_ADDRESS</strong></a></td>
<td></td>
<td>X</td>
<td><p>This TLV is used when the UE recreates the non-primary port during resume from hibernation. When this TLV is present, the firmware must use this MAC address to create the port. This MAC address is guaranteed to be the MAC address that the firmware created for the port type prior to hibernation.</p>
<p>The goal is to use the same NDIS port number and MAC address in order to match the states of the upper layers. Note that the WFC_PORT_ID can be different at recreation, but the port ID should not collide with any port ID of an existing port. This information is only used between the UE and LE/firmware.</p></td>
</tr>
</tbody>
</table>

 

## Task completion indication


[NDIS\_STATUS\_WDI\_INDICATION\_CREATE\_PORT\_COMPLETE](ndis-status-wdi-indication-create-port-complete.md)
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

 

 




