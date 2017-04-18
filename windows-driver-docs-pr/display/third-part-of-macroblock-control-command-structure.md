---
title: Third Part of Macroblock Control Command Structure
description: Third Part of Macroblock Control Command Structure
ms.assetid: 4e378d2f-dbb2-42b6-984e-b231bb806a7c
keywords: ["macroblocks WDK DirectX VA , generic command structure"]
---

# Third Part of Macroblock Control Command Structure


## <span id="ddk_third_part_of_macroblock_control_command_structure_gg"></span><span id="DDK_THIRD_PART_OF_MACROBLOCK_CONTROL_COMMAND_STRUCTURE_GG"></span>


If the **bPicIntra** member of [**DXVA\_PictureParameters**](https://msdn.microsoft.com/library/windows/hardware/ff564012) is 1, the macroblock control command structure ends with the data described in the [Second Part of Macroblock Control Command Structure](second-part-of-macroblock-control-command-structure.md). If **bPicIntra** is zero, the following additional data elements are included in the macroblock control command to control the motion compensation process. The data that follows is an array of [**DXVA\_MVvalue**](https://msdn.microsoft.com/library/windows/hardware/ff564004) structures contained in the **MVector** member of the macroblock control command structure. The number of elements in **MVector** depends on the type of picture specified by the members of DXVA\_PictureParameters in the following table.

<table>
<colgroup>
<col width="25%" />
<col width="25%" />
<col width="25%" />
<col width="25%" />
</colgroup>
<thead>
<tr class="header">
<th align="left">bPicOBMC</th>
<th align="left">bPicBinPB</th>
<th align="left">bPic4MVallowed</th>
<th align="left">Number of Elements in MVector</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td align="left"><p>0</p></td>
<td align="left"><p>0</p></td>
<td align="left"><p>0</p></td>
<td align="left"><p>4</p></td>
</tr>
<tr class="even">
<td align="left"><p>0</p></td>
<td align="left"><p>0</p></td>
<td align="left"><p>1</p></td>
<td align="left"><p>4</p></td>
</tr>
<tr class="odd">
<td align="left"><p>0</p></td>
<td align="left"><p>1</p></td>
<td align="left"><p>0</p></td>
<td align="left"><p>4</p></td>
</tr>
<tr class="even">
<td align="left"><p>0</p></td>
<td align="left"><p>1</p></td>
<td align="left"><p>1</p></td>
<td align="left"><p>5</p></td>
</tr>
<tr class="odd">
<td align="left"><p>1</p></td>
<td align="left"><p>0</p></td>
<td align="left"><p>0</p></td>
<td align="left"><p>10</p></td>
</tr>
<tr class="even">
<td align="left"><p>1</p></td>
<td align="left"><p>0</p></td>
<td align="left"><p>1</p></td>
<td align="left"><p>10</p></td>
</tr>
<tr class="odd">
<td align="left"><p>1</p></td>
<td align="left"><p>1</p></td>
<td align="left"><p>0</p></td>
<td align="left"><p>11</p></td>
</tr>
<tr class="even">
<td align="left"><p>1</p></td>
<td align="left"><p>1</p></td>
<td align="left"><p>1</p></td>
<td align="left"><p>11</p></td>
</tr>
</tbody>
</table>

 

**Note**   The number of motion vectors specified in the **MVector** arrays for the macroblock control command structures defined in the *dxva.h* file is four, as this is the most commonly used form of the structure.

 

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20[display\display]:%20Third%20Part%20of%20Macroblock%20Control%20Command%20Structure%20%20RELEASE:%20%282/10/2017%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")




