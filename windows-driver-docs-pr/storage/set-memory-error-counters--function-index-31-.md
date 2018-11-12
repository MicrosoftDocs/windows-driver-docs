---
title: Set Memory Error Counters (Function Index 31)
description: This function sets the counters that track correctable and uncorrectable memory error events to a caller-specified value. The purpose of this function is to enable software validation.
ms.assetid: 0EC4B442-902B-4589-A831-9637F4D60F86
ms.localizationpriority: medium
ms.date: 10/17/2018
---

# Set Memory Error Counters (Function Index 31)


This function sets the counters that track correctable and uncorrectable memory error events to a caller-specified value. The purpose of this function is to enable software validation.

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
<td align="left"><strong>Count of DRAM Uncorrectable ECC Errors</strong></td>
<td align="left">1</td>
<td align="left">0</td>
<td align="left"><p>The number of uncorrectable ECC errors detected by the platform from the NVDIMM-N module.</p>
<p>The platform shall write this value to the <em><em>DRAM_ECC_ERROR_COUNT</em> (2, 0x80) register.</p></td>
</tr>
<tr class="even">
<td align="left"><strong>Count of DRAM Correctable ECC Error Above Threshold Events</strong></td>
<td align="left">1</td>
<td align="left">1</td>
<td align="left"><p>The number of correctable ECC threshold-exceeded events detected by the platform from the NVDIMM-N module.</p>
<p>The platform shall write this value to the <em></em>DRAM_THRESHOLD_ECC_COUNT</em> (2, 0x81) register.</p></td>
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
<td align="left"><p>Go to <a href="-dsm-interface-for-byte-addressable-energy-backed-function-class--function-interface-1-.md" data-raw-source="[_DSM Method Output](-dsm-interface-for-byte-addressable-energy-backed-function-class--function-interface-1-.md)">_DSM Method Output</a> for more information.</p></td>
</tr>
</tbody>
</table>

 

## <span id="related_topics"></span>Related topics


[Get NVDIMM-N Health Info (Function Index 11)](get-nvdimm-n-health-info--function-index-11-.md)

[\_DSM Interface for Byte Addressable Energy Backed Function Class (Function Interface 1)](-dsm-interface-for-byte-addressable-energy-backed-function-class--function-interface-1-.md)

 

 






