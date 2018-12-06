---
title: Select Firmware Image Slot (Function Index 25)
description: This function selects which firmware image is active.
ms.assetid: 65B8BF11-4377-455A-9A08-0C15FADC0BBC
ms.localizationpriority: medium
ms.date: 10/17/2018
---

# Select Firmware Image Slot (Function Index 25)


This function selects which firmware image is active. The selected image shall be loaded when the device resets.

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
<td align="left"><p>The firmware image slot that shall be selected as active when the device resets.</p></td>
</tr>
</tbody>
</table>

 

&gt; \[!Note\]   
&gt;The firmware shall write the **Firmware Slot** value to the lower 4 bits of the \**FW\_SLOT\_INFO* (3, 0x42) register.

 

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
<p>1: Invalid slot number.</p>
<p>2: There is no image in this slot.</p>
<p>Go to <a href="-dsm-interface-for-byte-addressable-energy-backed-function-class--function-interface-1-.md" data-raw-source="[_DSM Method Output](-dsm-interface-for-byte-addressable-energy-backed-function-class--function-interface-1-.md)">_DSM Method Output</a> for more information.</p></td>
</tr>
</tbody>
</table>

 

## <span id="related_topics"></span>Related topics


[Start Firmware Update (Function Index 22)](start-firmware-update--function-index-22-.md)

[Send Firmware Update Data (Function Index 23)](send-firmware-update-data--function-index-23-.md)

[Finish Firmware Update (Function Index 24)](finish-firmware-update--function-index-24-.md)

[Get Firmware Info (Function Index 26)](get-firmware-info--function-index-26-.md)

[\_DSM Interface for Byte Addressable Energy Backed Function Class (Function Interface 1)](-dsm-interface-for-byte-addressable-energy-backed-function-class--function-interface-1-.md)

 

 






