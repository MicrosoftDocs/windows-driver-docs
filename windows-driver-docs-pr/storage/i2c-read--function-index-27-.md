---
title: I2C Read (Function Index 27)
description: This function reads an Inter-Integrated Circuit (I2C) register.
ms.assetid: 64D8999D-2E10-4836-9C17-7D809D9527BD
---

# I2C Read (Function Index 27)


This function reads an Inter-Integrated Circuit (I2C) register. This functionality enables scenarios that require the use of vendor-specific registers. It is also used for debugging.

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
<td align="left"><strong>Page</strong></td>
<td align="left">1</td>
<td align="left">0</td>
<td align="left"><p>The page in which the I2C register is located.</p></td>
</tr>
<tr class="even">
<td align="left"><strong>Offset</strong></td>
<td align="left">1</td>
<td align="left">1</td>
<td align="left"><p>The register’s offset inside the page.</p></td>
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
<p>1: Invalid page.</p>
<p>Go to [_DSM Method Output](-dsm-interface-for-byte-addressable-energy-backed-function-class--function-interface-1-.md#dsm-method-output) for more information.</p></td>
</tr>
<tr class="even">
<td align="left"><strong>Data</strong></td>
<td align="left">1</td>
<td align="left">4</td>
<td align="left"><p>The data in the specified register.</p></td>
</tr>
</tbody>
</table>

 

## <span id="related_topics"></span>Related topics


[I2C Write (Function Index 28)](i2c-write--function-index-28-.md)

[\_DSM Interface for Byte Addressable Energy Backed Function Class (Function Interface 1)](-dsm-interface-for-byte-addressable-energy-backed-function-class--function-interface-1-.md)

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20[storage\storage]:%20I2C%20Read%20%28Function%20Index%2027%29%20%20RELEASE:%20%281/11/2018%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")





