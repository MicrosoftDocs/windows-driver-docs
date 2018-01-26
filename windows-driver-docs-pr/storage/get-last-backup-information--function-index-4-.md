---
title: Get Last Backup Information (Function Index 4)
description: This function returns information about the saved image.
ms.assetid: F73A763B-4A4A-4CAB-AA62-AFA79849884B
---

# Get Last Backup Information (Function Index 4)


This function returns information about the saved image.

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
<td align="left"><p>Go to [_DSM Method Output](-dsm-interface-for-byte-addressable-energy-backed-function-class--function-interface-1-.md#dsm-method-output) for information.</p></td>
</tr>
<tr class="even">
<td align="left"><strong>Trigger Information</strong></td>
<td align="left">4</td>
<td align="left">4</td>
<td align="left"><p>Information on whether or not there is a valid DRAM image saved in the non-volatile memory subsystem and the trigger source of the save operation.</p>
<p>*Byte 0 – <em>CSAVE_INFO0</em> (0, 0x80)</p>
<p>Byte 1 – Reserved.</p>
<p>Byte 2 – Reserved.</p>
<p>Byte 3 – Reserved.</p></td>
</tr>
<tr class="odd">
<td align="left"><strong>Save Failure Information</strong></td>
<td align="left">4</td>
<td align="left">8</td>
<td align="left"><p>Failure information of the save operation.</p>
<p>*Byte 0 – <em>CSAVE_FAIL_INFO0</em> (0, 0x84)</p>
<p>*Byte 1 – <em>CSAVE_FAIL_INFO1</em> (0, 0x85)</p>
<p>Byte 2 – Reserved.</p>
<p>Byte 3 – Reserved.</p></td>
</tr>
</tbody>
</table>

 

## <span id="related_topics"></span>Related topics


[\_DSM Interface for Byte Addressable Energy Backed Function Class (Function Interface 1)](-dsm-interface-for-byte-addressable-energy-backed-function-class--function-interface-1-.md)

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20[storage\storage]:%20Get%20Last%20Backup%20Information%20%28Function%20Index%204%29%20%20RELEASE:%20%281/11/2018%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")





