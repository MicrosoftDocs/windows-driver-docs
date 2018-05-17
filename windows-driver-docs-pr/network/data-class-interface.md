---
title: Data Class Interface
description: Data Class Interface
ms.assetid: d7bf9ec3-8bf3-45a9-84a2-c507953d1ad4
ms.author: windowsdriverdev
ms.date: 04/20/2017
ms.topic: article
ms.prod: windows-hardware
ms.technology: windows-devices
---

# Data Class Interface


## <a href="" id="ddk-data-class-interface-ng"></a>


The Data Class interface is described by a standard USB Interface Descriptor followed by two endpoint descriptors. The two endpoint descriptors in the Data Class interface define standard USB Bulk-type endpoints: one Bulk-IN and one Bulk-OUT. The following table defines the prominent fields of the Data Class Interface Descriptor.

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
<th align="left">Offset (bytes)</th>
<th align="left">Field</th>
<th align="left">Size (bytes)</th>
<th align="left">Value</th>
<th align="left">Description</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td align="left"><p>5</p></td>
<td align="left"><p>bInterfaceClass</p></td>
<td align="left"><p>1</p></td>
<td align="left"><p>0Ah</p></td>
<td align="left"><p>Data Interface Class code.</p></td>
</tr>
<tr class="even">
<td align="left"><p>6</p></td>
<td align="left"><p>bInterfaceSubClass</p></td>
<td align="left"><p>1</p></td>
<td align="left"><p>00h</p></td>
<td align="left"><p>Data Class SubClass code.</p></td>
</tr>
<tr class="odd">
<td align="left"><p>7</p></td>
<td align="left"><p>bInterfaceProtocol</p></td>
<td align="left"><p>1</p></td>
<td align="left"><p>00h</p></td>
<td align="left"><p>Data Class Protocol code.</p></td>
</tr>
</tbody>
</table>

 

 

 





