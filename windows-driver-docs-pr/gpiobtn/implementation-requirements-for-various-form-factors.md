---
title: Implementation requirements for various form factors
author: windows-driver-content
description: This topic describes implementation requirements for various form factors.
ms.assetid: F14E9811-B432-409B-B7AD-262C2DD76C25
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

 

 

 


--------------------
[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20[gpiobtn\gpiobtn]:%20Implementation%20requirements%20for%20various%20form%20factors%20%20RELEASE:%20%289/25/2017%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")


