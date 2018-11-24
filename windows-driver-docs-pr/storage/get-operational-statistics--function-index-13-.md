---
title: Get Operational Statistics (Function Index 13)
description: This function returns counters that track operations performed by the NVDIMM-N.
ms.assetid: D396F42E-9B11-46D7-8D9C-FE00B4998DEC
ms.localizationpriority: medium
ms.date: 10/17/2018
---

# Get Operational Statistics (Function Index 13)


This function returns counters that track operations performed by the NVDIMM-N.

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
<td align="left"><strong>Duration of Last Save Operation</strong></td>
<td align="left">4</td>
<td align="left">4</td>
<td align="left"><p>The last save operation duration (in milliseconds or seconds).</p>
<p><em>Byte 0 – <em>LAST_SAVE_DURATION0</em> (2, 0x04)</p>
<p></em>Byte 1 – <em>LAST_SAVE_DURATION1</em> (2, 0x05)</p>
<p>Byte 2 – Reserved.</p>
<p>Byte 3 – Reserved.</p></td>
</tr>
<tr class="odd">
<td align="left"><strong>Duration of Last Restore Operation</strong></td>
<td align="left">4</td>
<td align="left">8</td>
<td align="left"><p>The last restore operation duration (in milliseconds or seconds).</p>
<p><em>Byte 0 – <em>LAST_RESTORE_DURATION0</em> (2, 0x06)</p>
<p></em>Byte 1 – <em>LAST_RESTORE_DURATION1</em> (2, 0x07)</p>
<p>Byte 2 – Reserved.</p>
<p>Byte 3 – Reserved.</p></td>
</tr>
<tr class="even">
<td align="left"><strong>Duration of Last Erase Operation</strong></td>
<td align="left">4</td>
<td align="left">12</td>
<td align="left"><p>The last erase operation duration in milliseconds or seconds.</p>
<p><em>Byte 0 – <em>LAST ERASE DURATION_TIME0</em> (2, 0x08)</p>
<p></em>Byte 1 – <em>LAST_ERASE DURATION_TIME1</em> (2, 0x09)</p>
<p>Byte 2 – Reserved</p>
<p>Byte 3 – Reserved</p></td>
</tr>
<tr class="odd">
<td align="left"><strong>Number of Save Operations Completed</strong></td>
<td align="left">4</td>
<td align="left">16</td>
<td align="left"><p>The number of completed save operations over the NVDIMM-N module&#39;s lifetime.</p>
<p><em>Byte 0 – <em>NUM_SAVE_OPS_COUNT0</em> (2, 0x0A)</p>
<p></em>Byte 1 – <em>NUM_SAVE_OPS_COUNT1</em> (2, 0x0B)</p>
<p>Byte 2 – Reserved.</p>
<p>Byte 3 – Reserved.</p></td>
</tr>
<tr class="even">
<td align="left"><strong>Number of Restore Operations Completed</strong></td>
<td align="left">4</td>
<td align="left">20</td>
<td align="left"><p>The number of completed restore operations over the NVDIMM-N module&#39;s lifetime.</p>
<p><em>Byte 0 – <em>NUM_RESTORE_OPS_COUNT0 0</em> (2, 0x0C)</p>
<p></em>Byte 1 – <em>NUM_RESTORE_OPS_COUNT1</em> (2, 0x0D)</p>
<p>Byte 2 – Reserved.</p>
<p>Byte 3 – Reserved.</p></td>
</tr>
<tr class="odd">
<td align="left"><strong>Number of Erase Operations Completed</strong></td>
<td align="left">4</td>
<td align="left">24</td>
<td align="left"><p>The number of completed erase operations over the NVDIMM-N module&#39;s lifetime.</p>
<p><em>Byte 0 – <em>NUM_ERASE_COUNTS0</em> (2, 0x0E)</p>
<p></em>Byte 1 – <em>NUM_ERASE_COUNTS1</em> (2, 0x0F)</p>
<p>Byte 2 – Reserved.</p>
<p>Byte 3 – Reserved.</p></td>
</tr>
<tr class="even">
<td align="left"><strong>Number of Module Power Cycles</strong></td>
<td align="left">4</td>
<td align="left">28</td>
<td align="left"><p>The number of power cycles over the NVDIMM-N module&#39;s lifetime.</p>
<p><em>Byte 0 – <em>NUM_MODULE_POWER_CYCLES0</em> (2, 0x10)</p>
<p></em>Byte 1 – <em>NUM_MODULE_POWER_CYCLES1</em> (2, 0x11)</p>
<p>Byte 2 – Reserved.</p>
<p>Byte 3 – Reserved.</p></td>
</tr>
</tbody>
</table>

 

## <span id="related_topics"></span>Related topics


[\_DSM Interface for Byte Addressable Energy Backed Function Class (Function Interface 1)](-dsm-interface-for-byte-addressable-energy-backed-function-class--function-interface-1-.md)

 

 






