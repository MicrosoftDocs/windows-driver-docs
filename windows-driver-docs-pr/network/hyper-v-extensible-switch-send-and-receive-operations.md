---
title: Hyper-V Extensible Switch Send and Receive Operations
description: Hyper-V Extensible Switch Send and Receive Operations
ms.assetid: 3BC59344-CF8E-436F-A1C9-883707990C7D
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# Hyper-V Extensible Switch Send and Receive Operations


This section describes the send and receive operations for Hyper-V extensible switch extensions. The following table describes the operations that an extension can perform on packets that are sent or received over the extensible switch data path.

<table>
<colgroup>
<col width="25%" />
<col width="25%" />
<col width="25%" />
<col width="25%" />
</colgroup>
<thead>
<tr class="header">
<th align="left">Operation</th>
<th align="left"><a href="capturing-extensions.md" data-raw-source="[Capturing Extensions](capturing-extensions.md)">Capturing Extensions</a></th>
<th align="left"><a href="filtering-extensions.md" data-raw-source="[Filtering Extensions](filtering-extensions.md)">Filtering Extensions</a></th>
<th align="left"><a href="forwarding-extensions.md" data-raw-source="[Forwarding Extensions](forwarding-extensions.md)">Forwarding Extensions</a></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td align="left">Originating packets</td>
<td align="left">X</td>
<td align="left">X</td>
<td align="left">X</td>
</tr>
<tr class="even">
<td align="left">Cloning packets</td>
<td align="left"></td>
<td align="left">X</td>
<td align="left">X</td>
</tr>
<tr class="odd">
<td align="left">Forwarding packets</td>
<td align="left"></td>
<td align="left"></td>
<td align="left">X</td>
</tr>
</tbody>
</table>

 

This section includes the following topics:

[Originating Packet Traffic](originating-packet-traffic.md)

[Cloning Packet Traffic](cloning-or-duplicating-packet-traffic.md)

[Forwarding Packets to Hyper-V Extensible Switch Ports](forwarding-packets-to-hyper-v-extensible-switch-ports.md)

For more information about the extensible switch data path, see [Hyper-V Extensible Switch Data Path](hyper-v-extensible-switch-data-path.md).

 

 





