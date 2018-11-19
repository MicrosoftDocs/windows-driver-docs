---
title: Get Save Operation Requirements (Function Index 2)
description: This function returns information about hardware requirements for a save operation.
ms.assetid: 502DAF89-F390-40A4-846C-C3B4DF3E505D
ms.localizationpriority: medium
ms.date: 10/17/2018
---

# Get Save Operation Requirements (Function Index 2)


This function returns information about hardware requirements for a save operation. This function shall succeed for all NVDIMM-Ns that support a host-managed Energy Source (ES) policy, but may return a failure status if the device supports device-managed ES policy and save operation requirements are not available.

&gt; \[!Note\]   
&gt;All registers marked with a star (\*) are registers defined in the Byte Addressable Energy Backed Interface specification.

 

## <span id="Input"></span><span id="input"></span><span id="INPUT"></span>Input


### <span id="Arg3"></span><span id="arg3"></span><span id="ARG3"></span>Arg3

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
<td align="left"><p>This function can return the following Function-Specific Error Codes:</p>
<p>1: The NVDIMM-N does not report save operation requirements.</p>
<p>Go to <a href="-dsm-interface-for-byte-addressable-energy-backed-function-class--function-interface-1-.md" data-raw-source="[_DSM Method Output](-dsm-interface-for-byte-addressable-energy-backed-function-class--function-interface-1-.md)">_DSM Method Output</a> for more information.</p></td>
</tr>
<tr class="even">
<td align="left"><strong>Average Power Requirement</strong></td>
<td align="left">2</td>
<td align="left">4</td>
<td align="left"><p>The average power (in milliwatts) required for the save operation.</p>
<p><em>Byte 0 – <em>CSAVE_POWER_REQ0</em> (0, 0x29)</p>
<p></em>Byte 1 – <em>CSAVE_POWER_REQ1</em> (0, 0x2A)</p></td>
</tr>
<tr class="odd">
<td align="left"><strong>Idle Power Requirement</strong></td>
<td align="left">2</td>
<td align="left">6</td>
<td align="left"><p>The average power (in milliwatts) the module requires after the save operation completes.</p>
<p><em>Byte 0 – <em>CSAVE_IDLE_POWER_REQ0</em> (0, 0x2B)</p>
<p></em>Byte 1 – <em>CSAVE_IDLE_POWER_REQ1</em> (0, 0x2C)</p></td>
</tr>
<tr class="even">
<td align="left"><strong>Minimum Voltage Requirement</strong></td>
<td align="left">2</td>
<td align="left">8</td>
<td align="left"><p>The minimum voltage (in millivolts) the ES has to service during a save operation</p>
<p><em>Byte 0 – <em>CSAVE_MIN_VOLT_REQ0</em> (0, 0x2D)</p>
<p></em>Byte 1 – <em>CSAVE_MIN_VOLT_REQ1</em> (0, 0x2E)</p></td>
</tr>
<tr class="odd">
<td align="left"><strong>Maximum Voltage Requirement</strong></td>
<td align="left">2</td>
<td align="left">10</td>
<td align="left"><p>The maximum voltage (in millivolts) the ES has to service during a save operation</p>
<p><em>Byte 0 – <em>CSAVE_MAX_VOLT_REQ0</em> (0, 0x2F)</p>
<p></em>Byte 1 – <em>CSAVE_MAX_VOLT_REQ1</em> (0, 0x30)</p></td>
</tr>
</tbody>
</table>

 

## <span id="related_topics"></span>Related topics


[\_DSM Interface for Byte Addressable Energy Backed Function Class (Function Interface 1)](-dsm-interface-for-byte-addressable-energy-backed-function-class--function-interface-1-.md)

 

 






