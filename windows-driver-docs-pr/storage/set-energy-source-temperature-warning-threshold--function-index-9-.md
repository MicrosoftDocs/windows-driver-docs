---
title: Set Energy Source Temperature Warning Threshold (Function Index 9)
description: This function sets the warning threshold for operating Energy Source (ES) temperature.
ms.assetid: AE624191-87F2-4673-A31B-CABE94623535
ms.localizationpriority: medium
ms.date: 10/17/2018
---

# Set Energy Source Temperature Warning Threshold (Function Index 9)


This function sets the warning threshold for operating Energy Source (ES) temperature. This function may return a failure status if the ES is host-managed and thresholds are not supported by the platform.

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
<td align="left"><strong>ES Lifetime Temperature Warning Threshold</strong></td>
<td align="left">1</td>
<td align="left">0</td>
<td align="left"><p>The new value (in degrees Celsius) of the warning threshold.</p>
<p>The platform shall write this value to the *<em>ES_TEMP_WARNING_THRESHOLD</em> (0, 0x99) register.</p></td>
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


[Set Energy Source Lifetime Warning Threshold (Function Index 8)](set-energy-source-lifetime-warning-threshold--function-index-8-.md)

[Get Energy Source Thresholds (Function Index 7)](get-energy-source-thresholds--function-index-7-.md)

[\_DSM Interface for Byte Addressable Energy Backed Function Class (Function Interface 1)](-dsm-interface-for-byte-addressable-energy-backed-function-class--function-interface-1-.md)

 

 






