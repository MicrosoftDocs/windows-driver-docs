---
title: EVENT\_TYPES\_QUALIFIERS
description: EVENT\_TYPES\_QUALIFIERS
ms.assetid: 528e5eaa-aaeb-4e5b-a4b2-0f518fcd79ee
ms.localizationpriority: medium
ms.date: 10/17/2018
---

# EVENT\_TYPES\_QUALIFIERS


## <span id="ddk_event_type_qualifiers_kr"></span><span id="DDK_EVENT_TYPE_QUALIFIERS_KR"></span>


The EVENT\_TYPES\_QUALIFIERS WMI class qualifier contains a list of the types of events that are reported by an HBA miniport driver that supports the T11 committee's *Fibre Channel HBA API* specification.

<table>
<colgroup>
<col width="50%" />
<col width="50%" />
</colgroup>
<thead>
<tr class="header">
<th align="left">Value</th>
<th align="left">Meaning</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td align="left"><p>HBA_EVENT_ADAPTER_UNKNOWN</p></td>
<td align="left"><p>Indicates that the adapter event is unknown.</p></td>
</tr>
<tr class="even">
<td align="left"><p>HBA_EVENT_ADAPTER_ADD</p></td>
<td align="left"><p>Indicates that an HBA has been added to the local system.</p></td>
</tr>
<tr class="odd">
<td align="left"><p>HBA_EVENT_ADAPTER_REMOVE</p></td>
<td align="left"><p>Indicates that an HBA has been removed from the local system.</p></td>
</tr>
<tr class="even">
<td align="left"><p>HBA_EVENT_ADAPTER_CHANGE</p></td>
<td align="left"><p>Indicates that there has been a configuration change to an HBA on the local system.</p></td>
</tr>
<tr class="odd">
<td align="left"><p>HBA_EVENT_PORT_UNKNOWN</p></td>
<td align="left"><p>Indicates that the port event is unknown.</p></td>
</tr>
<tr class="even">
<td align="left"><p>HBA_EVENT_PORT_OFFLINE</p></td>
<td align="left"><p>Indicates that a local port has gone offline.</p></td>
</tr>
<tr class="odd">
<td align="left"><p>HBA_EVENT_PORT_ONLINE</p></td>
<td align="left"><p>Indicates that a local port has come online.</p></td>
</tr>
<tr class="even">
<td align="left"><p>HBA_EVENT_PORT_NEW_TARGETS</p></td>
<td align="left"><p>Indicates that a local port has added target devices to its discovered remote ports.</p></td>
</tr>
<tr class="odd">
<td align="left"><p>HBA_EVENT_PORT_FABRIC</p></td>
<td align="left"><p>Indicates that a local port has received a registered state change notification (RSCN) command.</p></td>
</tr>
<tr class="even">
<td align="left"><p>HBA_EVENT_PORT_STAT_THRESHOLD</p></td>
<td align="left"><p>Indicates that a statistical counter has reached a registered level.</p></td>
</tr>
<tr class="odd">
<td align="left"><p>HBA_EVENT_PORT_STAT_GROWTH</p></td>
<td align="left"><p>Indicates that a statistical counter has increased at a rate equal to or in excess of a registered rate.</p></td>
</tr>
<tr class="even">
<td align="left"><p>HBA_EVENT_TARGET_UNKNOWN</p></td>
<td align="left"><p>Indicates that the target event is unknown.</p></td>
</tr>
<tr class="odd">
<td align="left"><p>HBA_EVENT_TARGET_OFFLINE</p></td>
<td align="left"><p>Indicates that operational use of a target port has become impossible.</p></td>
</tr>
<tr class="even">
<td align="left"><p>HBA_EVENT_TARGET_ONLINE</p></td>
<td align="left"><p>Indicates that operational use of a target port has been restored.</p></td>
</tr>
<tr class="odd">
<td align="left"><p>HBA_EVENT_TARGET_REMOVED</p></td>
<td align="left"><p>Indicates that a target port has been removed from the fabric.</p></td>
</tr>
<tr class="even">
<td align="left"><p>HBA_EVENT_LINK_UNKNOWN</p></td>
<td align="left"><p>Indicates that the link event is unknown.</p></td>
</tr>
<tr class="odd">
<td align="left"><p>HBA_EVENT_LINK_INCIDENT</p></td>
<td align="left"><p>Indicates that a local HBA has received a register link incident command.</p></td>
</tr>
</tbody>
</table>

 

By including *Hbaapi.h* your software will have access to a series of symbolic constants that correspond to the type names in the previous table. The definitions for these symbolic constants is not included in *Hbapiwmi.h* (the file that the WMI tool suite generates when it compiles).

 

 





