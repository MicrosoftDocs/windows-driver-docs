---
title: I2C Read (Function Index 27)
description: This function reads an Inter-Integrated Circuit (I2C) register.
ms.assetid: 64D8999D-2E10-4836-9C17-7D809D9527BD
ms.localizationpriority: medium
ms.date: 10/17/2018
---

# I2C Read (Function Index 27)


This function reads an Inter-Integrated Circuit (I2C) register. This functionality enables scenarios that require the use of vendor-specific registers. It is also used for debugging.

## <span id="Input"></span><span id="input"></span><span id="INPUT"></span>Input


### <span id="Args3"></span><span id="args3"></span><span id="ARGS3"></span>Args3

<table>
<colgroup>
<col width="25%" />
<col width="25%" />
<col width="25%" />
<col width="25%" />
</colgroup>
<thead>
<tr class="header">
<th align="left">Field</th>
<th align="left">Byte Length</th>
<th align="left">Byte Offset</th>
<th align="left">Description</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td align="left"><strong>Page</strong></td>
<td align="left">1</td>
<td align="left">0</td>
<td align="left"><p>The page in which the I2C register is located.</p></td>
</tr>
<tr class="even">
<td align="left"><strong>Offset</strong></td>
<td align="left">1</td>
<td align="left">1</td>
<td align="left"><p>The register’s offset inside the page.</p></td>
</tr>
</tbody>
</table>

 

## <span id="Output"></span><span id="output"></span><span id="OUTPUT"></span>Output


<table>
<colgroup>
<col width="25%" />
<col width="25%" />
<col width="25%" />
<col width="25%" />
</colgroup>
<thead>
<tr class="header">
<th align="left">Field</th>
<th align="left">Byte Length</th>
<th align="left">Byte Offset</th>
<th align="left">Description</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td align="left"><strong>Status</strong></td>
<td align="left">4</td>
<td align="left">0</td>
<td align="left"><p>This function can return the following Function-Specific Error Code:</p>
<p>1: Invalid page.</p>
<p>Go to <a href="-dsm-interface-for-byte-addressable-energy-backed-function-class--function-interface-1-.md" data-raw-source="[_DSM Method Output](-dsm-interface-for-byte-addressable-energy-backed-function-class--function-interface-1-.md)">_DSM Method Output</a> for more information.</p></td>
</tr>
<tr class="even">
<td align="left"><strong>Data</strong></td>
<td align="left">1</td>
<td align="left">4</td>
<td align="left"><p>The data in the specified register.</p></td>
</tr>
</tbody>
</table>

 

## <span id="related_topics"></span>Related topics


[I2C Write (Function Index 28)](i2c-write--function-index-28-.md)

[\_DSM Interface for Byte Addressable Energy Backed Function Class (Function Interface 1)](-dsm-interface-for-byte-addressable-energy-backed-function-class--function-interface-1-.md)

 

 






