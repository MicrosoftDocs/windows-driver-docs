---
title: Get Last Backup Information (Function Index 4)
description: This function returns information about the saved image.
ms.assetid: F73A763B-4A4A-4CAB-AA62-AFA79849884B
ms.localizationpriority: medium
ms.date: 10/17/2018
---

# Get Last Backup Information (Function Index 4)


This function returns information about the saved image.

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
<td align="left"><strong>Trigger Information</strong></td>
<td align="left">4</td>
<td align="left">4</td>
<td align="left"><p>Information on whether or not there is a valid DRAM image saved in the non-volatile memory subsystem and the trigger source of the save operation.</p>
<p><em>Byte 0 – <em>CSAVE_INFO0</em> (0, 0x80)</p>
<p>Byte 1 – Reserved.</p>
<p>Byte 2 – Reserved.</p>
<p>Byte 3 – Reserved.</p></td>
</tr>
<tr class="odd">
<td align="left"><strong>Save Failure Information</strong></td>
<td align="left">4</td>
<td align="left">8</td>
<td align="left"><p>Failure information of the save operation.</p>
<p></em>Byte 0 – <em>CSAVE_FAIL_INFO0</em> (0, 0x84)</p>
<p>*Byte 1 – <em>CSAVE_FAIL_INFO1</em> (0, 0x85)</p>
<p>Byte 2 – Reserved.</p>
<p>Byte 3 – Reserved.</p></td>
</tr>
</tbody>
</table>

 

## <span id="related_topics"></span>Related topics


[\_DSM Interface for Byte Addressable Energy Backed Function Class (Function Interface 1)](-dsm-interface-for-byte-addressable-energy-backed-function-class--function-interface-1-.md)

 

 






