---
title: Write Typed Data (Function Index 30)
description: This function writes a 32-byte block inside a typed block data region.
ms.assetid: 0162E7C3-CF1E-452C-908E-D65C090CD365
---

# Write Typed Data (Function Index 30)


This function writes a 32-byte block inside a typed block data region. This functionality enables scenarios that require the use of vendor-specific registers. It is also used for debugging.

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
<td align="left"><strong>Data Type</strong></td>
<td align="left">1</td>
<td align="left">0</td>
<td align="left"><p>The type of the data. This must be one of the values specified in *<em>TYPED_BLOCK_DATA</em> (3, 0x04).</p></td>
</tr>
<tr class="even">
<td align="left"><strong>Region ID</strong></td>
<td align="left">2</td>
<td align="left">1</td>
<td align="left"><p>The identification of the region that is being written</p></td>
</tr>
<tr class="odd">
<td align="left"><strong>Block ID</strong></td>
<td align="left">1</td>
<td align="left">3</td>
<td align="left"><p>The identification of the block being written inside the region.</p></td>
</tr>
<tr class="even">
<td align="left"><strong>Data</strong></td>
<td align="left">32</td>
<td align="left">4</td>
<td align="left"><p>The data to be written.</p></td>
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
<p>1: Invalid data type.</p>
<p>Go to [_DSM Method Output](-dsm-interface-for-byte-addressable-energy-backed-function-class--function-interface-1-.md#dsm-method-output) for more information.</p></td>
</tr>
</tbody>
</table>

 

## <span id="Remarks"></span><span id="remarks"></span><span id="REMARKS"></span>Remarks


The platform shall use Typed Block Data registers to implement this function.

## <span id="related_topics"></span>Related topics


[Read Typed Data (Function Index 29)](read-typed-data--function-index-29-.md)

[\_DSM Interface for Byte Addressable Energy Backed Function Class (Function Interface 1)](-dsm-interface-for-byte-addressable-energy-backed-function-class--function-interface-1-.md)

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20[storage\storage]:%20Write%20Typed%20Data%20%28Function%20Index%2030%29%20%20RELEASE:%20%281/11/2018%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")





