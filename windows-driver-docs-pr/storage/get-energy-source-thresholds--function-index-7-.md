---
title: Get Energy Source Thresholds (Function Index 7)
description: This function returns warning and error thresholds which, if hit or surpassed, indicate a problem with the Energy Source (ES).
ms.assetid: 12B7D7CF-DB65-42A5-9831-F0D85BED2574
---

# Get Energy Source Thresholds (Function Index 7)


This function returns warning and error thresholds which, if hit or surpassed, indicate a problem with the Energy Source (ES). This function may return a failure status if the ES is host-managed and the platform does not support thresholds.

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
<td align="left"><strong>ES Lifetime Percentage Warning Threshold</strong></td>
<td align="left">1</td>
<td align="left">4</td>
<td align="left"><p>The percentage value of the warning threshold for the ES lifetime.</p>
<p>*Byte 0 – <em>ES_LIFETIME_WARNING_THRESHOLD</em> (0, 0x99)</p></td>
</tr>
<tr class="odd">
<td align="left"><strong>ES Lifetime Percentage Error Threshold</strong></td>
<td align="left">1</td>
<td align="left">5</td>
<td align="left"><p>The percentage value of the error threshold for the ES lifetime.</p>
<p>*Byte 0 – <em>ES_LIFETIME_ERROR_THRESHOLD</em> (0, 0x91)</p></td>
</tr>
<tr class="even">
<td align="left"><strong>ES Temperature Warning Threshold</strong></td>
<td align="left">1</td>
<td align="left">6</td>
<td align="left"><p>The percentage value of the warning threshold for the ES temperature.</p>
<p>*Byte 0 – <em>ES_TEMP_WARNING_THRESHOLD</em> (0, 0x9A)</p></td>
</tr>
<tr class="odd">
<td align="left"><strong>ES Temperature Error Threshold</strong></td>
<td align="left">1</td>
<td align="left">7</td>
<td align="left"><p>The percentage value of the error threshold for the ES temperature.</p>
<p>*Byte 0 – <em>ES_TEMP_ERROR_THRESHOLD</em> (0, 0x92)</p></td>
</tr>
</tbody>
</table>

 

## <span id="related_topics"></span>Related topics


[Set Energy Source Lifetime Warning Threshold (Function Index 8)](set-energy-source-lifetime-warning-threshold--function-index-8-.md)

[Set Energy Source Temperature Warning Threshold (Function Index 9)](set-energy-source-temperature-warning-threshold--function-index-9-.md)

[\_DSM Interface for Byte Addressable Energy Backed Function Class (Function Interface 1)](-dsm-interface-for-byte-addressable-energy-backed-function-class--function-interface-1-.md)

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20[storage\storage]:%20Get%20Energy%20Source%20Thresholds%20%28Function%20Index%207%29%20%20RELEASE:%20%281/11/2018%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")





