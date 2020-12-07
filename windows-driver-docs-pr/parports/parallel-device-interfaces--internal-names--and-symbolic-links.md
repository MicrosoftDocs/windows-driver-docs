---
title: Parallel Device Interfaces, Internal Names, and Symbolic Links
description: Parallel Device Interfaces, Internal Names, and Symbolic Links
keywords:
- system-supplied parallel drivers WDK , device interfaces
- system-supplied parallel drivers WDK , internal names
- system-supplied parallel drivers WDK , symbolic links
- device interfaces WDK parallel drivers
- symbolic links WDK parallel drivers
- internal names WDK parallel drivers
- names WDK parallel drivers
- unprotected symbolic links WDK
- parallel devices WDK , device interfaces
- device objects WDK parallel drivers
- parallel devices WDK , internal names
- parallel devices WDK , symbolic links
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# Parallel Device Interfaces, Internal Names, and Symbolic Links





This section describes the device interfaces, internal names, and symbolic links that are created by the system-supplied parallel drivers for parallel ports and devices attached to parallel ports.

For each parallel port enumerated in the system and for each parallel device enumerated on a parallel port, the parallel drivers create device objects, interfaces, internal names, and unprotected symbolic links as follows.

<table>
<colgroup>
<col width="20%" />
<col width="20%" />
<col width="20%" />
<col width="20%" />
<col width="20%" />
</colgroup>
<thead>
<tr class="header">
<th>Device type</th>
<th>Device object</th>
<th>Device interface</th>
<th>Internal name</th>
<th>Symbolic link</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><p>Parallel port</p></td>
<td><p>FDO</p></td>
<td><p>GUID_PARALLEL_DEVICE</p></td>
<td><p>"\Device\ParallelPort<em>m",</em></p>
<p><em>m &gt;=</em> 0</p></td>
<td><p>None</p></td>
</tr>
<tr class="even">
<td><p>Raw parallel device</p></td>
<td><p>PDO</p></td>
<td><p>GUID_PARCLASS_DEVICE</p></td>
<td><p>"\Device\Parallel<em>m</em>",</p>
<p><em>m &gt;=</em> 0</p></td>
<td><p>"LPT<em>n</em>",</p>
<p><em>n = m +</em> 1</p></td>
</tr>
<tr class="odd">
<td><p>IEEE 1284.3 device</p></td>
<td><p>PDO</p></td>
<td><p>None</p></td>
<td><p>"\Device\Parallel<em>m.x</em>",</p>
<p><em>m &gt;=</em> 0<em>,</em></p>
<p>Windows 2000: <em>x =</em> 0 <em>to</em> 3</p>
<p>Windows XP and later: <em>x =</em> 0 <em>or</em> 1</p></td>
<td><p>"LPT<em>n.x</em>",</p>
<p><em>n = m +</em>1</p></td>
</tr>
<tr class="even">
<td><p>IEEE 1284 end-of-chain device</p></td>
<td><p>PDO</p></td>
<td><p>None</p></td>
<td><p>"\Device\Parallel<em>m.</em>4"</p>
<p><em>m</em> &gt;= 0</p></td>
<td><p>"LPT<em>n.</em>4"</p>
<p><em>n = m +</em>1</p></td>
</tr>
</tbody>
</table>

 

For example, the following device names and symbolic links are assigned to "\\Device\\ParallelPort0", which has two IEEE 1284.3 daisy chain devices and an IEEE 1284 end-of-chain device attached to it.

<table>
<colgroup>
<col width="25%" />
<col width="25%" />
<col width="25%" />
<col width="25%" />
</colgroup>
<thead>
<tr class="header">
<th>Device type</th>
<th>Device object</th>
<th>Internal name</th>
<th>Symbolic link</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><p>Parallel Port</p></td>
<td><p>FDO</p></td>
<td><p>"\Device\ParallelPort0"</p></td>
<td><p>None</p></td>
</tr>
<tr class="even">
<td><p>IEEE 1284.3 device</p></td>
<td><p>PDO</p></td>
<td><p>"\Device\Parallel0.0"</p></td>
<td><p>"LPT1.0"</p></td>
</tr>
<tr class="odd">
<td><p>IEEE 1284.3 device</p></td>
<td><p>PDO</p></td>
<td><p>"\Device\Parallel0.1"</p></td>
<td><p>"LPT1.1"</p></td>
</tr>
<tr class="even">
<td><p>IEEE 1284 end-of-chain device</p></td>
<td><p>PDO</p></td>
<td><p>"\Device\Parallel0.4"</p></td>
<td><p>"LPT1.4"</p></td>
</tr>
</tbody>
</table>

 

 

 




