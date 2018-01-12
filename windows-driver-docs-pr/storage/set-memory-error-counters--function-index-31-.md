---
title: Set Memory Error Counters (Function Index 31)
description: This function sets the counters that track correctable and uncorrectable memory error events to a caller-specified value. The purpose of this function is to enable software validation.
ms.assetid: 0EC4B442-902B-4589-A831-9637F4D60F86
---

# Set Memory Error Counters (Function Index 31)


This function sets the counters that track correctable and uncorrectable memory error events to a caller-specified value. The purpose of this function is to enable software validation.

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
<td align="left"><strong>Count of DRAM Uncorrectable ECC Errors</strong></td>
<td align="left">1</td>
<td align="left">0</td>
<td align="left"><p>The number of uncorrectable ECC errors detected by the platform from the NVDIMM-N module.</p>
<p>The platform shall write this value to the <em>*DRAM_ECC_ERROR_COUNT</em> (2, 0x80) register.</p></td>
</tr>
<tr class="even">
<td align="left"><strong>Count of DRAM Correctable ECC Error Above Threshold Events</strong></td>
<td align="left">1</td>
<td align="left">1</td>
<td align="left"><p>The number of correctable ECC threshold-exceeded events detected by the platform from the NVDIMM-N module.</p>
<p>The platform shall write this value to the <em>*DRAM_THRESHOLD_ECC_COUNT</em> (2, 0x81) register.</p></td>
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
<td align="left"><p>Go to [_DSM Method Output](-dsm-interface-for-byte-addressable-energy-backed-function-class--function-interface-1-.md#dsm-method-output) for more information.</p></td>
</tr>
</tbody>
</table>

 

## <span id="related_topics"></span>Related topics


[Get NVDIMM-N Health Info (Function Index 11)](get-nvdimm-n-health-info--function-index-11-.md)

[\_DSM Interface for Byte Addressable Energy Backed Function Class (Function Interface 1)](-dsm-interface-for-byte-addressable-energy-backed-function-class--function-interface-1-.md)

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20[storage\storage]:%20Set%20Memory%20Error%20Counters%20%28Function%20Index%2031%29%20%20RELEASE:%20%281/11/2018%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")





