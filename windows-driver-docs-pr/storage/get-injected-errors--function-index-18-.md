---
title: Get Injected Errors (Function Index 18)
description: This function returns information about errors currently being injected.
ms.assetid: 60D4E64C-ABB6-4B24-971F-594306D8C07C
---

# Get Injected Errors (Function Index 18)


This function returns information about errors currently being injected.

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
<td align="left"><strong>Operation Failures Injected</strong></td>
<td align="left">2</td>
<td align="left">4</td>
<td align="left"><p>Information about which operation or non-volatile memory errors are currently injected.</p>
<p>*Byte 0 – <em>INJECT_OPS_FAILURES</em> (2, 0x60)</p>
<p>*Byte 1 – If <em>INJECT_BAD_BLOCKS</em> is ‘1’ (bit 7 of Byte 0), this is *<em>INJECT_BAD_BLOCK_CAP</em> (2, 0x67). Otherwise, this shall be 0.</p></td>
</tr>
<tr class="odd">
<td align="left"><strong>Energy Source Failures Injected</strong></td>
<td align="left">1</td>
<td align="left">6</td>
<td align="left"><p>Information about which Energy Source (ES) errors are currently injected.</p>
<p>*Byte 0 – <em>INJECT_ES_FAILURES</em> (2, 0x64)</p></td>
</tr>
<tr class="even">
<td align="left"><strong>Firmware Update Failures Injected</strong></td>
<td align="left">1</td>
<td align="left">7</td>
<td align="left"><p>Information about which firmware operation errors are currently injected.</p>
<p>*Byte 0 – <em>INJECT_FW_FAILURES</em> (2, 0x65)</p></td>
</tr>
</tbody>
</table>

 

## <span id="Remarks"></span><span id="remarks"></span><span id="REMARKS"></span>Remarks


If the platform disabled error injections, this function shall succeed and return the same information as if there were no errors currently injected.

## <span id="related_topics"></span>Related topics


[Inject Error (Function Index 17)](inject-error--function-index-17-.md)

[Query Error Injection Status (Function Index 16)](query-error-injection-status--function-index-16-.md)

[\_DSM Interface for Byte Addressable Energy Backed Function Class (Function Interface 1)](-dsm-interface-for-byte-addressable-energy-backed-function-class--function-interface-1-.md)

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20[storage\storage]:%20Get%20Injected%20Errors%20%28Function%20Index%2018%29%20%20RELEASE:%20%281/11/2018%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")





