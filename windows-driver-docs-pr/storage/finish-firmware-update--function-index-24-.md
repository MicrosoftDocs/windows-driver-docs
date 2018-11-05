---
title: Finish Firmware Update (Function Index 24)
description: This function finishes the firmware update operation that a call to Start Firmware Update (Function Index 22) initiated.
ms.assetid: 1A9446D7-67F7-4AC2-8784-BFC05A0EA608
ms.localizationpriority: medium
ms.date: 10/17/2018
---

# Finish Firmware Update (Function Index 24)


This function finishes the firmware update operation that a call to [Start Firmware Update (Function Index 22)](start-firmware-update--function-index-22-.md) initiated.

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
<td align="left"><p>This function can return the following Function-Specific Error Codes:</p>
<p>1: There is no firmware update operation in progress.</p>
<p>2: Invalid firmware image.</p>
<p>Go to <a href="-dsm-interface-for-byte-addressable-energy-backed-function-class--function-interface-1-.md" data-raw-source="[_DSM Method Output](-dsm-interface-for-byte-addressable-energy-backed-function-class--function-interface-1-.md)">_DSM Method Output</a> for more information.</p></td>
</tr>
</tbody>
</table>

 

## <span id="related_topics"></span>Related topics


[Start Firmware Update (Function Index 22)](start-firmware-update--function-index-22-.md)

[Send Firmware Update Data (Function Index 23)](send-firmware-update-data--function-index-23-.md)

[Select Firmware Image Slot (Function Index 25)](select-firmware-image-slot--function-index-25-.md)

[Get Firmware Info (Function Index 26)](get-firmware-info--function-index-26-.md)

[\_DSM Interface for Byte Addressable Energy Backed Function Class (Function Interface 1)](-dsm-interface-for-byte-addressable-energy-backed-function-class--function-interface-1-.md)

 

 






