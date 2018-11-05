---
title: Set Energy Source Lifetime Warning Threshold (Function Index 8)
description: This function sets the warning threshold for remaining Energy Source (ES) lifetime percentage.
ms.assetid: 18D80829-8B54-48CE-A4A1-C3D57D0F60DC
ms.localizationpriority: medium
ms.date: 10/17/2018
---

# Set Energy Source Lifetime Warning Threshold (Function Index 8)


This function sets the warning threshold for remaining Energy Source (ES) lifetime percentage. This function may return a failure status if the ES is host-managed and the platform does not support thresholds.

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
<td align="left"><strong>ES Lifetime Percentage Warning Threshold</strong></td>
<td align="left">1</td>
<td align="left">0</td>
<td align="left"><p>The percentage value of the warning threshold, which must be between 0 and 100.</p>
<p>The platform shall write this value to the *<em>ES_LIFETIME_WARNING_THRESHOLD</em> (0, 0x99) register.</p></td>
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
<p>1: The platform does not support ES thresholds.</p>
<p>Go to <a href="-dsm-interface-for-byte-addressable-energy-backed-function-class--function-interface-1-.md" data-raw-source="[_DSM Method Output](-dsm-interface-for-byte-addressable-energy-backed-function-class--function-interface-1-.md)">_DSM Method Output</a> for more information.</p></td>
</tr>
</tbody>
</table>

 

## <span id="related_topics"></span>Related topics


[Set Energy Source Temperature Warning Threshold (Function Index 9)](set-energy-source-temperature-warning-threshold--function-index-9-.md)

[Get Energy Source Thresholds (Function Index 7)](get-energy-source-thresholds--function-index-7-.md)

[\_DSM Interface for Byte Addressable Energy Backed Function Class (Function Interface 1)](-dsm-interface-for-byte-addressable-energy-backed-function-class--function-interface-1-.md)

 

 






