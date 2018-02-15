---
title: Get Operational Statistics (Function Index 13)
description: This function returns counters that track operations performed by the NVDIMM-N.
ms.assetid: D396F42E-9B11-46D7-8D9C-FE00B4998DEC
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
<td align="left"><p>Go to [_DSM Method Output](-dsm-interface-for-byte-addressable-energy-backed-function-class--function-interface-1-.md#dsm-method-output) for information.</p></td>
</tr>
<tr class="even">
<td align="left"><strong>Duration of Last Save Operation</strong></td>
<td align="left">4</td>
<td align="left">4</td>
<td align="left"><p>The last save operation duration (in milliseconds or seconds).</p>
<p>*Byte 0 – <em>LAST_SAVE_DURATION0</em> (2, 0x04)</p>
<p>*Byte 1 – <em>LAST_SAVE_DURATION1</em> (2, 0x05)</p>
<p>Byte 2 – Reserved.</p>
<p>Byte 3 – Reserved.</p></td>
</tr>
<tr class="odd">
<td align="left"><strong>Duration of Last Restore Operation</strong></td>
<td align="left">4</td>
<td align="left">8</td>
<td align="left"><p>The last restore operation duration (in milliseconds or seconds).</p>
<p>*Byte 0 – <em>LAST_RESTORE_DURATION0</em> (2, 0x06)</p>
<p>*Byte 1 – <em>LAST_RESTORE_DURATION1</em> (2, 0x07)</p>
<p>Byte 2 – Reserved.</p>
<p>Byte 3 – Reserved.</p></td>
</tr>
<tr class="even">
<td align="left"><strong>Duration of Last Erase Operation</strong></td>
<td align="left">4</td>
<td align="left">12</td>
<td align="left"><p>The last erase operation duration in milliseconds or seconds.</p>
<p>*Byte 0 – <em>LAST ERASE DURATION_TIME0</em> (2, 0x08)</p>
<p>*Byte 1 – <em>LAST_ERASE DURATION_TIME1</em> (2, 0x09)</p>
<p>Byte 2 – Reserved</p>
<p>Byte 3 – Reserved</p></td>
</tr>
<tr class="odd">
<td align="left"><strong>Number of Save Operations Completed</strong></td>
<td align="left">4</td>
<td align="left">16</td>
<td align="left"><p>The number of completed save operations over the NVDIMM-N module's lifetime.</p>
<p>*Byte 0 – <em>NUM_SAVE_OPS_COUNT0</em> (2, 0x0A)</p>
<p>*Byte 1 – <em>NUM_SAVE_OPS_COUNT1</em> (2, 0x0B)</p>
<p>Byte 2 – Reserved.</p>
<p>Byte 3 – Reserved.</p></td>
</tr>
<tr class="even">
<td align="left"><strong>Number of Restore Operations Completed</strong></td>
<td align="left">4</td>
<td align="left">20</td>
<td align="left"><p>The number of completed restore operations over the NVDIMM-N module's lifetime.</p>
<p>*Byte 0 – <em>NUM_RESTORE_OPS_COUNT0 0</em> (2, 0x0C)</p>
<p>*Byte 1 – <em>NUM_RESTORE_OPS_COUNT1</em> (2, 0x0D)</p>
<p>Byte 2 – Reserved.</p>
<p>Byte 3 – Reserved.</p></td>
</tr>
<tr class="odd">
<td align="left"><strong>Number of Erase Operations Completed</strong></td>
<td align="left">4</td>
<td align="left">24</td>
<td align="left"><p>The number of completed erase operations over the NVDIMM-N module's lifetime.</p>
<p>*Byte 0 – <em>NUM_ERASE_COUNTS0</em> (2, 0x0E)</p>
<p>*Byte 1 – <em>NUM_ERASE_COUNTS1</em> (2, 0x0F)</p>
<p>Byte 2 – Reserved.</p>
<p>Byte 3 – Reserved.</p></td>
</tr>
<tr class="even">
<td align="left"><strong>Number of Module Power Cycles</strong></td>
<td align="left">4</td>
<td align="left">28</td>
<td align="left"><p>The number of power cycles over the NVDIMM-N module's lifetime.</p>
<p>*Byte 0 – <em>NUM_MODULE_POWER_CYCLES0</em> (2, 0x10)</p>
<p>*Byte 1 – <em>NUM_MODULE_POWER_CYCLES1</em> (2, 0x11)</p>
<p>Byte 2 – Reserved.</p>
<p>Byte 3 – Reserved.</p></td>
</tr>
</tbody>
</table>

 

## <span id="related_topics"></span>Related topics


[\_DSM Interface for Byte Addressable Energy Backed Function Class (Function Interface 1)](-dsm-interface-for-byte-addressable-energy-backed-function-class--function-interface-1-.md)

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20[storage\storage]:%20Get%20Operational%20Statistics%20%28Function%20Index%2013%29%20%20RELEASE:%20%281/11/2018%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")





