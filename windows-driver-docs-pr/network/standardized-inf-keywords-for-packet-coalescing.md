---
title: Standardized INF Keywords for Packet Coalescing
description: Standardized INF Keywords for Packet Coalescing
ms.assetid: 423E9B50-6474-454A-97BB-91404DF9F729
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# Standardized INF Keywords for Packet Coalescing


A standardized INF keyword is defined to enable or disable support for packet coalescing on a miniport driver.

The INF file for the miniport driver of an adapter that supports packet coalescing must specify the **\*PacketCoalescing** standardized INF keyword. Once the driver is installed, administrators can update the **\*PacketCoalescing** keyword value in the **Advanced** property page for the adapter. For more information about advanced properties, see [Specifying Configuration Parameters for the Advanced Properties Page](specifying-configuration-parameters-for-the-advanced-properties-page.md).

**Note**   The miniport driver is automatically restarted after a change is made in the **Advanced** property page for the adapter.

 

The **\*PacketCoalescing** INF keyword is an enumeration keyword. The following table describes the possible INF entries for the **\*PacketCoalescing** INF keyword. The columns in this table describe the following attributes for an enumeration keyword:

<a href="" id="subkeyname"></a>SubkeyName  
The name of the keyword that you must specify in the INF file. This name also appears in the registry under the **NDI\\params\\** key for the network adapter.

<a href="" id="paramdesc"></a>ParamDesc  
The display text that is associated with SubkeyName.

**Note**  The independent hardware vendor (IHV) can define any descriptive text for the SubkeyName.

 

<a href="" id="value"></a>Value  
The enumeration integer value that is associated with each SubkeyName in the list.

<a href="" id="enumdesc"></a>EnumDesc  
The display text that is associated with each value that appears in the menu.

<table>
<colgroup>
<col width="25%" />
<col width="25%" />
<col width="25%" />
<col width="25%" />
</colgroup>
<thead>
<tr class="header">
<th align="left">SubkeyName</th>
<th align="left">ParamDesc</th>
<th align="left">Value</th>
<th align="left">EnumDesc</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td align="left"><p><strong>*PacketCoalescing</strong></p></td>
<td align="left"><p>Packet coalescing</p></td>
<td align="left"><p>0</p></td>
<td align="left"><p>Disabled</p></td>
</tr>
<tr class="even">
<td align="left"></td>
<td align="left"></td>
<td align="left"><p>1 (Default)</p></td>
<td align="left"><p>Enabled</p></td>
</tr>
</tbody>
</table>

 

The miniport driver must check the **\*PacketCoalescing** keyword value in the registry before it advertises its support for packet coalescing. If the **\*PacketCoalescing** keyword has a value of zero, the miniport must not advertise support for any packet coalescing capabilities. For more information, see [Reporting Packet Coalescing Capabilities](reporting-packet-coalescing-capabilities.md).

For more information about standardized INF keywords, see [Standardized INF Keywords for Network Devices](standardized-inf-keywords-for-network-devices.md).

 

 





