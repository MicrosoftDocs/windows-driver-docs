---
title: Get NVDIMM-N Health Info (Function Index 11)
description: This function returns information about the health of the NVDIMM-N module.
ms.assetid: E0FCC4C6-31CB-4D46-ADCE-99EBA2BFF798
ms.localizationpriority: medium
ms.date: 10/17/2018
---

# <span id="storage.get_nvdimm-n_health_info__function_index_11_"></span>Get NVDIMM-N Health Info (Function Index 11)


This function returns information about the health of the NVDIMM-N module.

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
<td align="left"><strong>Module Health</strong></td>
<td align="left">2</td>
<td align="left">4</td>
<td align="left"><p>Detailed information regarding the NVDIMM-N module&#39;s health.</p>
<p><em>Byte 0 – <em>MODULE_HEALTH_STATUS0</em> (0, 0xA1)</p>
<p></em>Byte 1 – <em>MODULE_HEALTH_STATUS1</em> (0, 0xA2)</p></td>
</tr>
<tr class="odd">
<td align="left"><strong>Module Current Temperature</strong></td>
<td align="left">2</td>
<td align="left">6</td>
<td align="left"><p>The module temperature in degrees Celsius. The minimum value is 0</p>
.
<p>This information is retrieved from the temperature sensor on the NVDIMM-N’s Serial Presence Detect EEPROM.</p></td>
</tr>
<tr class="even">
<td align="left"><strong>Error Threshold Status</strong></td>
<td align="left">1</td>
<td align="left">8</td>
<td align="left"><p>Status regarding the error thresholds on the NVDIMM-N module.</p>
<p><em>Byte 0 – <em>ERROR_THRESHOLD_STATUS</em> (0, 0xA5)</p></td>
</tr>
<tr class="odd">
<td align="left"><strong>Warning Threshold Status</strong></td>
<td align="left">1</td>
<td align="left">9</td>
<td align="left"><p>Status regarding the warning thresholds on the NVDIMM-N module.</p>
<p></em>Byte 0 – <em>WARNING_THRESHOLD_STATUS</em> (0, 0xA7)</p></td>
</tr>
<tr class="even">
<td align="left"><strong>NVM Lifetime</strong></td>
<td align="left">1</td>
<td align="left">10</td>
<td align="left"><p>The last known non-volatile memory lifetime percentage value.</p>
<p><em>Byte 0 – <em>NVM_LIFETIME</em> (0, 0xC0)</p></td>
</tr>
<tr class="odd">
<td align="left"><strong>Count of DRAM Uncorrectable ECC Errors</strong></td>
<td align="left">1</td>
<td align="left">11</td>
<td align="left"><p>The number of uncorrectable ECC errors detected by the platform from the NVDIMM-N module.</p>
<p></em>Byte 0 – <em>DRAM_ECC_ERROR_COUNT</em> (2, 0x80)</p></td>
</tr>
<tr class="even">
<td align="left"><strong>Count of DRAM Correctable ECC Error Above Threshold Events</strong></td>
<td align="left">1</td>
<td align="left">12</td>
<td align="left"><p>The number of correctable ECC threshold-exceeded events detected by the platform from the NVDIMM-N module.</p>
<p>*Byte 0 – <em>DRAM_THRESHOLD_ECC_COUNT</em> (2, 0x81)</p></td>
</tr>
</tbody>
</table>

 

## <span id="related_topics"></span>Related topics


[Get Critical Health Info (Function Index 10)](get-critical-health-info--function-index-10-.md)

[Get Energy Source Health Info (Function Index 12)](get-energy-source-health-info--function-index-12-.md)

[\_DSM Interface for Byte Addressable Energy Backed Function Class (Function Interface 1)](-dsm-interface-for-byte-addressable-energy-backed-function-class--function-interface-1-.md)

 

 






