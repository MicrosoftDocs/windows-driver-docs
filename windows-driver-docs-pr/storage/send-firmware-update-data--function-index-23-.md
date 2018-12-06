---
title: Send Firmware Update Data (Function Index 23)
description: This function sends firmware data to the device.
ms.assetid: 3F28C89B-040A-407B-B780-96D6767DC5C7
ms.localizationpriority: medium
ms.date: 10/17/2018
---

# Send Firmware Update Data (Function Index 23)


This function sends firmware data to the device.

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
<td align="left"><strong>Region Length</strong></td>
<td align="left">4</td>
<td align="left">0</td>
<td align="left"><p>The number of bytes being sent in this function.</p></td>
</tr>
<tr class="even">
<td align="left"><strong>Region ID</strong></td>
<td align="left">2</td>
<td align="left">4</td>
<td align="left"><p>The identification of the region that is being written.</p></td>
</tr>
<tr class="odd">
<td align="left"><strong>Block ID</strong></td>
<td align="left">1</td>
<td align="left">6</td>
<td align="left"><p>The identification of the block being written inside the region.</p></td>
</tr>
<tr class="even">
<td align="left"><strong>Firmware Data</strong></td>
<td align="left">The number specified by <em>Region Length</em>.</td>
<td align="left">7</td>
<td align="left"><p>A region-sized packet of firmware image data.</p></td>
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
<td align="left"><p>This function can return the following Function-Specific Error Codes:</p>
<p>1: There is no firmware update operation in progress.</p>
<p>2: Invalid region size.</p>
<p>3: Transfer failed due to data corruption.</p>
<p>4: Operation timed out.</p>
<p>5: The firmware commit operation failed.</p>
<p>Go to <a href="-dsm-interface-for-byte-addressable-energy-backed-function-class--function-interface-1-.md" data-raw-source="[_DSM Method Output](-dsm-interface-for-byte-addressable-energy-backed-function-class--function-interface-1-.md)">_DSM Method Output</a> for more information.</p></td>
</tr>
</tbody>
</table>

 

&gt; \[!Note\]   
&gt;This function shall compute the CRC of the Firmware Data and compare it with \**FW\_REGION\_CRC0* (3, 0x40) and \**FW\_REGION\_CRC1* (3, 0x41). If the values don’t match, the function shall fail with Function-Specific Error Code 3. Please refer to the Byte Addressable Energy Backed Interface JEDEC standard for the CRC algorithm specification.

 

## <span id="related_topics"></span>Related topics


[Start Firmware Update (Function Index 22)](start-firmware-update--function-index-22-.md)

[Finish Firmware Update (Function Index 24)](finish-firmware-update--function-index-24-.md)

[Select Firmware Image Slot (Function Index 25)](select-firmware-image-slot--function-index-25-.md)

[Get Firmware Info (Function Index 26)](get-firmware-info--function-index-26-.md)

[\_DSM Interface for Byte Addressable Energy Backed Function Class (Function Interface 1)](-dsm-interface-for-byte-addressable-energy-backed-function-class--function-interface-1-.md)

 

 






