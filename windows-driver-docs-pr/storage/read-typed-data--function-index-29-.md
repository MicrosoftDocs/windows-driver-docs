---
title: Read Typed Data (Function Index 29)
description: This function reads a 32-byte block inside a typed block data region.
ms.assetid: 67B13EBA-F751-4E85-9143-1C331C405B85
ms.localizationpriority: medium
ms.date: 10/17/2018
---

# Read Typed Data (Function Index 29)


This function reads a 32-byte block inside a typed block data region. This functionality enables scenarios that require the use of vendor-specific registers. It is also used for debugging.

&gt; \[!Note\]   
&gt;All registers marked with a star (\*) are registers defined in the Byte Addressable Energy Backed Interface specification.

 

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
<td align="left"><strong>Data Type</strong></td>
<td align="left">1</td>
<td align="left">0</td>
<td align="left"><p>The type of the data. This must be one of the values specified in *<em>TYPED_BLOCK_DATA</em> (3, 0x04).</p></td>
</tr>
<tr class="even">
<td align="left"><strong>Region ID</strong></td>
<td align="left">2</td>
<td align="left">1</td>
<td align="left"><p>The identification of the region that is being read.</p></td>
</tr>
<tr class="odd">
<td align="left"><strong>Block ID</strong></td>
<td align="left">1</td>
<td align="left">3</td>
<td align="left"><p>The identification of the block being read inside the region.</p></td>
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
<p>1: Invalid data type.</p>
<p>Go to <a href="-dsm-interface-for-byte-addressable-energy-backed-function-class--function-interface-1-.md" data-raw-source="[_DSM Method Output](-dsm-interface-for-byte-addressable-energy-backed-function-class--function-interface-1-.md)">_DSM Method Output</a> for more information.</p></td>
</tr>
<tr class="even">
<td align="left"><strong>Data</strong></td>
<td align="left">32</td>
<td align="left">4</td>
<td align="left"><p>The data from the specified block.</p></td>
</tr>
</tbody>
</table>

 

## <span id="Remarks"></span><span id="remarks"></span><span id="REMARKS"></span>Remarks


The platform shall use Typed Block Data registers to implement this function.

## <span id="related_topics"></span>Related topics


[Write Typed Data (Function Index 30)](write-typed-data--function-index-30-.md)

[\_DSM Interface for Byte Addressable Energy Backed Function Class (Function Interface 1)](-dsm-interface-for-byte-addressable-energy-backed-function-class--function-interface-1-.md)

 

 






