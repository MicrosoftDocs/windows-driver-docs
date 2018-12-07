---
title: Get Critical Health Info (Function Index 10)
description: This function returns critical health-related information.
ms.assetid: 2083628D-FB46-4104-9F70-F7124B35DD04
ms.localizationpriority: medium
ms.date: 10/17/2018
---

# Get Critical Health Info (Function Index 10)


This function returns critical health-related information. Call [Get NVDIMM-N Health Info (Function Index 11)](get-nvdimm-n-health-info--function-index-11-.md) and [Get Energy Source Health Info (Function Index 12)](get-energy-source-health-info--function-index-12-.md) to obtain further health-related information.

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
<td align="left"><strong>Critical Health Info</strong></td>
<td align="left">1</td>
<td align="left">4</td>
<td align="left"><p>A high level status report of any issues with the NVDIMM-N module.</p>
<p>*Byte 0 – <em>MODULE_HEALTH</em> (0, 0xA0)</p></td>
</tr>
</tbody>
</table>

 

## <span id="related_topics"></span>Related topics


[Get NVDIMM-N Health Info (Function Index 11)](get-nvdimm-n-health-info--function-index-11-.md)

[Get Energy Source Health Info (Function Index 12)](get-energy-source-health-info--function-index-12-.md)

[\_DSM Interface for Byte Addressable Energy Backed Function Class (Function Interface 1)](-dsm-interface-for-byte-addressable-energy-backed-function-class--function-interface-1-.md)

 

 






