---
title: Implementation requirements for various form factors
description: This topic describes implementation requirements for various form factors.
ms.assetid: F14E9811-B432-409B-B7AD-262C2DD76C25
ms.localizationpriority: medium
ms.date: 10/17/2018
---

# Implementation requirements for various form factors


This topic describes implementation requirements for various form factors.

<table>
<colgroup>
<col width="25%" />
<col width="25%" />
<col width="25%" />
<col width="25%" />
</colgroup>
<thead>
<tr class="header">
<th align="left"></th>
<th align="left">Form factor</th>
<th align="left">Definition</th>
<th align="left">GPIO indicator implementation requirements</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td align="left"><p><img src="images/slate.jpg" alt="Slate" /></p></td>
<td align="left">Slate</td>
<td align="left">Tablet form factor with no attachable keyboard</td>
<td align="left">When a stationary docking accessory is available, the docking indicator must be implemented.</td>
</tr>
<tr class="even">
<td align="left"><p><img src="images/laptop.jpg" alt="Laptop" /></p></td>
<td align="left">Laptop</td>
<td align="left">Permanently attached keyboard that is always available for typing.</td>
<td align="left">Statically set the mode to laptop.</td>
</tr>
<tr class="odd">
<td align="left"><p><img src="images/convertible.jpg" alt="Convertible" /></p></td>
<td align="left">Convertible</td>
<td align="left">System that can be used as either a slate or a tablet. The keyboard can be detached, flipped, or swivelled.</td>
<td align="left"><p>Implement the laptop/slate indicator.</p>
<p>If a stationary docking accessory is available, the docking indicator must also be implemented.</p></td>
</tr>
<tr class="even">
<td align="left"><p><img src="images/allinone.jpg" alt="All-in-One" /></p></td>
<td align="left">All-in-One</td>
<td align="left">Medium size desktop/semi-portable systems that have a keyboard that is attached as an accessory.</td>
<td align="left">No implementation required because the keyboard is an optional accessory.</td>
</tr>
</tbody>
</table>

 

 

 




