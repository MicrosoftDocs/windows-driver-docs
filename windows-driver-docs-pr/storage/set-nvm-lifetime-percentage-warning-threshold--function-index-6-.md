---
title: Set NVM Lifetime Percentage Warning Threshold (Function Index 6)
description: This function sets the warning threshold for remaining non-volatile memory lifetime percentage.
ms.assetid: B5568876-D9E1-4086-8819-FC5FF6BC2C15
ms.localizationpriority: medium
ms.date: 10/17/2018
---

# Set NVM Lifetime Percentage Warning Threshold (Function Index 6)


This function sets the warning threshold for remaining non-volatile memory lifetime percentage.

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
<td align="left"><strong>NVM Lifetime Percentage Warning Threshold</strong></td>
<td align="left">1</td>
<td align="left">0</td>
<td align="left"><p>The percentage value of the warning threshold, which must be between 0 and 100.</p>
<p>The platform shall write this value to the *<em>NVM_LIFETIME_WARNING_THRESHOLD (0, 0x98)</em> register.</p></td>
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
<td align="left"><p>Go to <a href="-dsm-interface-for-byte-addressable-energy-backed-function-class--function-interface-1-.md" data-raw-source="[_DSM Method Output](-dsm-interface-for-byte-addressable-energy-backed-function-class--function-interface-1-.md)">_DSM Method Output</a> for information.</p></td>
</tr>
</tbody>
</table>

 

## <span id="related_topics"></span>Related topics


[Get NVM Thresholds (Function Index 5)](get-nvm-thresholds--function-index-5-.md)

[\_DSM Interface for Byte Addressable Energy Backed Function Class (Function Interface 1)](-dsm-interface-for-byte-addressable-energy-backed-function-class--function-interface-1-.md)

 

 






