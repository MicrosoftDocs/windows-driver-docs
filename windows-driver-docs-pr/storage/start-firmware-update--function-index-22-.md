---
title: Start Firmware Update (Function Index 22)
description: This function initiates a firmware update to a particular firmware slot.
ms.assetid: 34950124-6DBF-43CE-862A-E6DEF7A5FADE
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
<p>Go to [_DSM Method Output](-dsm-interface-for-byte-addressable-energy-backed-function-class--function-interface-1-.md#dsm-method-output) for more information.</p></td>
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

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20[storage\storage]:%20Start%20Firmware%20Update%20%28Function%20Index%2022%29%20%20RELEASE:%20%281/11/2018%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")





