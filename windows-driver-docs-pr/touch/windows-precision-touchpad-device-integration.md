---
title: Device Integration
description: Windows Precision Touchpads define an experience. Integration of the module has a significant impact on how well that experience is realized. This topic describes Windows Precision Touchpads integration.
ms.assetid: 418FB0E0-AF18-42F8-8011-5032B18A99E5
---

# Device Integration


Windows Precision Touchpads define an experience. Integration of the module has a significant impact on how well that experience is realized. This topic describes Windows Precision Touchpads integration.

## <span id="Size"></span><span id="size"></span><span id="SIZE"></span>Size


A Windows Precision Touchpad shall have a sensor with minimum dimensions of 32mm x 64mm as shown in *Figure 1 Windows Precision Touchpad Minimum Size*. This shall be the minimum permissible size reported by using the physical maximum for X and Y in the report descriptor.

![windows precision touchpad minimum size](images/implementationfig8minsize.jpg)

**Figure 1 Windows Precision Touchpad Minimum Size**

The best Windows Precision Touchpads shall have recommended dimensions of approximately 65mm x 105mm as shown in *Figure 2 Windows Precision Touchpad Optimal Size*, to allow for more comfortable interactions.

![windows precision touchpad optimal size](images/implementationfig9optimalsize.png)

**Figure 2 Windows Precision Touchpad Optimal Size**

## <span id="Placement"></span><span id="placement"></span><span id="PLACEMENT"></span>Placement


Windows Precision Touchpad placement is defined by three measurements: horizontal offset, vertical offset and depth offset.

### <span id="Horizontal_offset"></span><span id="horizontal_offset"></span><span id="HORIZONTAL_OFFSET"></span>Horizontal offset

The optimal placement for a Windows Precision Touchpad is to center the device with the line that bisects the F and J keys of the integrated keyboard, as shown in *Figure 3 Optimal Horizontal Placement (Zero-Offset)*.

![optimal horizontal placement (zero-offset)](images/implementationfig10optimalhorizontalplacementzerooffset.jpg)

**Figure 3 Optimal Horizontal Placement (Zero-Offset)**

If a Windows Precision Touchpad cannot be integrated with the optimal zero offset, the integrator shall store the positive or negative offset (in himetric) in the registry to allow the host to compensate.

With reference to *Figure 4 Horizontal Placement (Right-Offset)*, if a device has an offset, the value to store is computed by taking the length of the touchpad to the right of the bisecting line and subtracting the length of the touchpad to the left of the bisecting line such that (Y – X) = Offset value. If a device has a right offset, this value will be positive, whereas a device with a left offset will result in a negative value.

![horizontal placement (right-offset)](images/implementationfig11horizontalplacementrightoffset.jpg)

**Figure 4 Horizontal Placement (Right-Offset)**

**HKEY\_LOCAL\_MACHINE\\Software\\Microsoft\\Windows\\CurrentVersion\\PrecisionTouchPad**

<table>
<colgroup>
<col width="20%" />
<col width="20%" />
<col width="20%" />
<col width="20%" />
<col width="20%" />
</colgroup>
<thead>
<tr class="header">
<th align="left">Setting</th>
<th align="left">Name</th>
<th align="left">Type</th>
<th align="left">Default Value</th>
<th align="left">Value</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td align="left">Horizontal Offset</td>
<td align="left">HorizontalOffset</td>
<td align="left">DWORD</td>
<td align="left">0</td>
<td align="left">Absolute offset distance in himetric</td>
</tr>
<tr class="even">
<td align="left">Indicate Negative</td>
<td align="left">HorizontalOffsetIsNeg</td>
<td align="left">DWORD</td>
<td align="left">0</td>
<td align="left"><p>0 = Positive Offset</p>
<p>1 = Negative Offset</p></td>
</tr>
</tbody>
</table>

 

### <span id="Vertical_offset"></span><span id="vertical_offset"></span><span id="VERTICAL_OFFSET"></span>Vertical offset

Windows Precision Touchpads shall be integrated at different vertical offsets from the keyboard spacebar due as shown in *Figure 4 Vertical Offset*. The integrator shall store the positive offset (in himetric) in the registry to allow the host to compensate. If a value is not provided, the host shall assume a default offset of 10mm.

![vertical offset](images/implementationfig12verticaloffset.jpg)

**Figure 4 Vertical Offset**

**HKEY\_LOCAL\_MACHINE\\Software\\Microsoft\\Windows\\CurrentVersion\\PrecisionTouchPad**

| Setting         | Name           | Type  | Default Value | Value                       |
|-----------------|----------------|-------|---------------|-----------------------------|
| Vertical Offset | SpaceBarOffset | DWORD | 1000          | Offset distance in himetric |

 

**Note**  
If the touchpad is not below the space bar, but is located above the keyboard, leave the vertical offset at the default value.

 

### <span id="Depth_offset"></span><span id="depth_offset"></span><span id="DEPTH_OFFSET"></span>Depth offset

Windows Precision Touchpads shall be integrated such that the digitizer surface is flush with the palm deck as shown in *Figure 5 Depth Offset*. Up to 1.5mm of depth offset is permitted due to manufacturing and integration tolerances; however the highest quality implementations will seek to eliminate this offset.

![depth offset](images/implementationfig13depthoffset.jpg)

**Figure 5 Depth Offset**

 

 




