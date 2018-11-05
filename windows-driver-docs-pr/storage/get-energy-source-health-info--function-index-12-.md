---
title: Get Energy Source Health Info (Function Index 12)
description: This function returns information about the health of the Energy Source (ES) module.
ms.assetid: A2044F2A-79DA-4D3A-93B7-BE9D389DA399
ms.localizationpriority: medium
ms.date: 10/17/2018
---

# Get Energy Source Health Info (Function Index 12)


This function returns information about the health of the Energy Source (ES) module. This function may return a failure status if the ES is host-managed and health information is not available.

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
<td align="left"><p>This function can return the following Function-Specific Error Code:</p>
<p>1: The platform does not support ES health information.</p>
<p>Go to <a href="-dsm-interface-for-byte-addressable-energy-backed-function-class--function-interface-1-.md" data-raw-source="[_DSM Method Output](-dsm-interface-for-byte-addressable-energy-backed-function-class--function-interface-1-.md)">_DSM Method Output</a> for more information.</p></td>
</tr>
<tr class="even">
<td align="left"><strong>ES Lifetime Percentage</strong></td>
<td align="left">1</td>
<td align="left">4</td>
<td align="left"><p>The last known ES lifetime percentage.</p>
<p><em>Byte 0 – <em>ES_LIFETIME</em> (1, 0x70)</p></td>
</tr>
<tr class="odd">
<td align="left"><strong>ES Current Temperature</strong></td>
<td align="left">2</td>
<td align="left">5</td>
<td align="left"><p>The ES temperature in degrees Celsius. The minimum value is 0.</p>
<p></em>Byte 0 – <em>ES_TEMP0</em> (1, 0x71)</p>
<p><em>Byte 1 – <em>ES_TEMP1</em> (1, 0x72)</p></td>
</tr>
<tr class="even">
<td align="left"><strong>Total Runtime</strong></td>
<td align="left">4</td>
<td align="left">7</td>
<td align="left"><p>The time (in hours) the ES has been operational since it was manufactured.</p>
<p></em>Byte 0 – <em>ES_RUNTIME0</em> (1, 0x73)</p>
<p>*Byte 1 – <em>ES_RUNTIME1</em> (1, 0x74)</p>
<p>Byte 2 – Reserved</p>
<p>Byte 3 – Reserved</p></td>
</tr>
</tbody>
</table>

 

## <span id="related_topics"></span>Related topics


[Get NVDIMM-N Health Info (Function Index 11)](get-nvdimm-n-health-info--function-index-11-.md)

[Get Energy Source Health Info (Function Index 12)](get-energy-source-health-info--function-index-12-.md)

[\_DSM Interface for Byte Addressable Energy Backed Function Class (Function Interface 1)](-dsm-interface-for-byte-addressable-energy-backed-function-class--function-interface-1-.md)

 

 






