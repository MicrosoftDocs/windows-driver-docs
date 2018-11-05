---
title: Arm NVDIMM-N (Function Index 20)
description: This function arms the NVDIMM-N for save operations in the event of a power loss.
ms.assetid: 15D21B5A-2320-4C22-9957-ECC0EB46B02E
ms.localizationpriority: medium
ms.date: 10/17/2018
---

# <span id="storage.arm_nvdimm-n__function_index_20_"></span>Arm NVDIMM-N (Function Index 20)


This function arms the NVDIMM-N for save operations in the event of a power loss. The platform is responsible for choosing the appropriate save trigger.

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
<p>1: The operation timed out.</p>
<p>Go to <a href="-dsm-interface-for-byte-addressable-energy-backed-function-class--function-interface-1-.md" data-raw-source="[_DSM Interface for Byte Addressable Energy Backed Function Class (Function Interface 1)](-dsm-interface-for-byte-addressable-energy-backed-function-class--function-interface-1-.md)">_DSM Interface for Byte Addressable Energy Backed Function Class (Function Interface 1)</a> for information.</p></td>
</tr>
</tbody>
</table>

 

&gt; \[!Note\]   
&gt;This is a synchronous function. It returns only when the arm operation has finished or timed out. If the operation takes longer than the timeout defined in \**ARM\_TIMEOUT0* (0, 0x20) and \**ARM\_TIMEOUT1* (0, 0x21), the platform shall abort this function before it returns.

 

## <span id="related_topics"></span>Related topics


[\_DSM Interface for Byte Addressable Energy Backed Function Class (Function Interface 1)](-dsm-interface-for-byte-addressable-energy-backed-function-class--function-interface-1-.md)

 

 






