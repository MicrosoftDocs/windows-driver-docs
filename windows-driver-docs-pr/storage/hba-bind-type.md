---
title: HBA\_BIND\_TYPE
description: HBA\_BIND\_TYPE
ms.assetid: a5388574-f48a-4bdc-9ffe-408fa6de1eeb
ms.localizationpriority: medium
ms.date: 10/17/2018
---

# HBA\_BIND\_TYPE


## <span id="ddk_hba_bind_type_kr"></span><span id="DDK_HBA_BIND_TYPE_KR"></span>


The HBA\_BIND\_TYPE WMI class qualifier indicates the ability of an HBA and its miniport driver to provide a specific set of features related to persistent binding.

The following table lists the qualifier names and the meaning of each name:

<table>
<colgroup>
<col width="50%" />
<col width="50%" />
</colgroup>
<thead>
<tr class="header">
<th align="left">Types</th>
<th align="left">Meaning</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td align="left"><p>HBA_CAN_BIND_TO_D_ID</p></td>
<td align="left"><p>Indicates the ability of an HBA and its miniport driver to accept a persistent binding that identifies the Fibre Channel target port by its address identifier.</p></td>
</tr>
<tr class="even">
<td align="left"><p>HBA_CAN_BIND_TO_WWPN</p></td>
<td align="left"><p>Indicates the ability of an HBA and its miniport driver to accept a persistent binding that identifies the Fibre Channel target port by its worldwide port name (WWPN).</p></td>
</tr>
<tr class="odd">
<td align="left"><p>HBA_CAN_BIND_TO_WWNN</p></td>
<td align="left"><p>Indicates the ability of an HBA and its miniport driver to accept a persistent binding that identifies a Fibre Channel target device (not a target port) by its worldwide node name (WWNN). The implicit ambiguity in this means of identifying devices on multiport devices is intentional. It allows the HBA and/or the fabric to resolve the ambiguity in a vendor-specific manner.</p></td>
</tr>
<tr class="even">
<td align="left"><p>HBA_CAN_BIND_TO_LUID</p></td>
<td align="left"><p>Indicates the ability of an HBA and its miniport driver to accept a persistent binding that identifies a Fibre Channel logical unit by the identification descriptor derived from SCSI inquiry data for the logical unit.</p></td>
</tr>
<tr class="odd">
<td align="left"><p>HBA_CAN_BIND_ANY_LUNS</p></td>
<td align="left"><p>Indicates the ability of an HBA and its miniport driver to accept persistent binding settings that specify both the operating system and Fibre Channel logical unit number.</p></td>
</tr>
<tr class="even">
<td align="left"><p>HBA_CAN_BIND_TARGETS</p></td>
<td align="left"><p>Indicates the ability of an HBA and its miniport driver to generate persistent bindings between Fibre Channel protocol (FCP) identifiers for logical units and the information that the operating system uses to identify logical units, such as the bus and target numbers that are stored in the <a href="https://msdn.microsoft.com/library/windows/hardware/ff556042" data-raw-source="[&lt;strong&gt;HBAScsiID&lt;/strong&gt;](https://msdn.microsoft.com/library/windows/hardware/ff556042)"><strong>HBAScsiID</strong></a>.</p></td>
</tr>
<tr class="odd">
<td align="left"><p>HBA_CAN_BIND_AUTOMAP</p></td>
<td align="left"><p>Indicates the ability of an HBA and its miniport driver to automatically generate target mappings and persistent bindings for all discovered storage resources. If this capability is not indicated or is disabled, the only bindings allowed are those that are explicitly configured in the operating system. Explicit configuration of bindings facilitates logical unit number (LUN) masking.</p></td>
</tr>
<tr class="even">
<td align="left"><p>HBA_CAN_BIND_CONFIGURED</p></td>
<td align="left"><p>Indicates the ability of an HBA and its miniport driver to accept dynamic configuration of persistent bindings.</p></td>
</tr>
</tbody>
</table>

 

By including *Hbaapi.h* your software will have access to a series of symbolic constants that correspond to the type names in the previous table. The definitions for these symbolic constants is not included in *Hbapiwmi.h* (the file that the WMI tool suite generates when it compiles).

 

 





