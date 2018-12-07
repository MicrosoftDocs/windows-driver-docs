---
title: Start Firmware Update (Function Index 22)
description: This function initiates a firmware update to a particular firmware slot.
ms.assetid: 34950124-6DBF-43CE-862A-E6DEF7A5FADE
ms.localizationpriority: medium
ms.date: 10/17/2018
---

# Start Firmware Update (Function Index 22)


This function initiates a firmware update to a particular firmware slot. There can only be one firmware update operation at any given time.

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
<td align="left"><p>The firmware slot that is being updated.</p></td>
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
<td align="left"><p>This function can return the following Function-Specific Error Code:</p>
<p>1: There is a firmware update operation currently in progress.</p>
<p>Go to <a href="-dsm-interface-for-byte-addressable-energy-backed-function-class--function-interface-1-.md" data-raw-source="[_DSM Method Output](-dsm-interface-for-byte-addressable-energy-backed-function-class--function-interface-1-.md)">_DSM Method Output</a> for more information.</p></td>
</tr>
</tbody>
</table>

 

## <span id="Remarks"></span><span id="remarks"></span><span id="REMARKS"></span>Remarks


The host calls the following firmware functions in order to update & activate the firmware:

1.  The host calls Start Firmware Update (Function Index 22) to start the firmware update operation. In this step, the host chooses which firmware slot it is updating.

2.  The host repeatedly calls [Send Firmware Update Data (Function Index 23)](send-firmware-update-data--function-index-23-.md) to transfer the data to the device. Each call transmits a region-sized chunk of data; the host is responsible for padding if the last transfer is not region-sized.

3.  The host calls [Finish Firmware Update (Function Index 24)](finish-firmware-update--function-index-24-.md) to signal to the platform that the firmware update operation is over.

4.  The host calls [Select Firmware Image Slot (Function Index 25)](select-firmware-image-slot--function-index-25-.md) in order to activate the new firmware image. The update will take effect on the next system reboot.

## <span id="related_topics"></span>Related topics


[Send Firmware Update Data (Function Index 23)](send-firmware-update-data--function-index-23-.md)

[Finish Firmware Update (Function Index 24)](finish-firmware-update--function-index-24-.md)

[Select Firmware Image Slot (Function Index 25)](select-firmware-image-slot--function-index-25-.md)

[Get Firmware Info (Function Index 26)](get-firmware-info--function-index-26-.md)

[\_DSM Interface for Byte Addressable Energy Backed Function Class (Function Interface 1)](-dsm-interface-for-byte-addressable-energy-backed-function-class--function-interface-1-.md)

 

 






