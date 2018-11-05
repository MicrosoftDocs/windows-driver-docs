---
title: Get NVM Thresholds (Function Index 5)
description: This function returns the lifetime percentage warning and error thresholds, which if hit or surpassed, indicate a problem with the NVDIMM-N.
ms.assetid: E243AF8B-D70A-4FEF-BB88-ED78C4883D42
ms.localizationpriority: medium
ms.date: 10/17/2018
---

# Get NVM Thresholds (Function Index 5)


This function returns the lifetime percentage warning and error thresholds, which if hit or surpassed, indicate a problem with the NVDIMM-N.

&gt; \[!Note\]   
&gt;All registers marked with a star (\*) are registers defined in the Byte Addressable Energy Backed Interface specification.

 

## <span id="Input"></span><span id="input"></span><span id="INPUT"></span>Input


### <span id="Args3"></span><span id="args3"></span><span id="ARGS3"></span>Args3

None.

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
<tr class="even">
<td align="left"><strong>NVM Lifetime Percentage Warning Threshold</strong></td>
<td align="left">1</td>
<td align="left">4</td>
<td align="left"><p>The percentage value of the warning threshold for the non-volatile memory lifetime.</p>
<p><em>Byte 0 – <em>NVM_LIFETIME_WARNING_THRESHOLD</em> (0, 0x98)</p></td>
</tr>
<tr class="odd">
<td align="left"><strong>NVM Lifetime Percentage Error Threshold</strong></td>
<td align="left">1</td>
<td align="left">5</td>
<td align="left"><p>The percentage value of the error threshold for the non-volatile memory lifetime.</p>
<p></em>Byte 0 – <em>NVM_LIFETIME_ERROR_THRESHOLD</em> (0, 0x90)</p></td>
</tr>
</tbody>
</table>

 

## <span id="related_topics"></span>Related topics


[Set NVM Lifetime Percentage Warning Threshold (Function Index 6)](set-nvm-lifetime-percentage-warning-threshold--function-index-6-.md)

[\_DSM Interface for Byte Addressable Energy Backed Function Class (Function Interface 1)](-dsm-interface-for-byte-addressable-energy-backed-function-class--function-interface-1-.md)

 

 






