---
title: Get Firmware Info (Function Index 26)
description: This function retrieves information about a firmware image slot.
ms.assetid: ABE67651-6351-4D8E-BCFF-0488D2A34DC5
ms.localizationpriority: medium
ms.date: 10/17/2018
---

# Get Firmware Info (Function Index 26)


This function retrieves information about a firmware image slot. Call [Get NVDIMM-N Identification (Function Index 1)](get-nvdimm-n-identification--function-index-1-.md) to retrieve the current slot number .

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
<td align="left"><strong>Firmware Slot</strong></td>
<td align="left">1</td>
<td align="left">0</td>
<td align="left"><p>The firmware image slot to report information for.</p></td>
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
<td align="left"><p>Go to <a href="-dsm-interface-for-byte-addressable-energy-backed-function-class--function-interface-1-.md" data-raw-source="[_DSM Method Output](-dsm-interface-for-byte-addressable-energy-backed-function-class--function-interface-1-.md)">_DSM Method Output</a> for information.</p></td>
</tr>
<tr class="even">
<td align="left"><strong>Version</strong></td>
<td align="left">2</td>
<td align="left">4</td>
<td align="left"><p>Firmware version of the firmware image in the specified slot.</p>
<p><em>Byte 0 – <em>SLOTX_FWVER0</em> (0, 0x07/0x09)</p>
<p></em>Byte 1 – <em>SLOTX_FWVER1</em> (0, 0x08/0x0A)</p></td>
</tr>
</tbody>
</table>

 

## <span id="related_topics"></span>Related topics


[Start Firmware Update (Function Index 22)](start-firmware-update--function-index-22-.md)

[Send Firmware Update Data (Function Index 23)](send-firmware-update-data--function-index-23-.md)

[Finish Firmware Update (Function Index 24)](finish-firmware-update--function-index-24-.md)

[Select Firmware Image Slot (Function Index 25)](select-firmware-image-slot--function-index-25-.md)

[\_DSM Interface for Byte Addressable Energy Backed Function Class (Function Interface 1)](-dsm-interface-for-byte-addressable-energy-backed-function-class--function-interface-1-.md)

 

 






