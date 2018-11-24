---
title: Third Part of Macroblock Control Command Structure
description: Third Part of Macroblock Control Command Structure
ms.assetid: 4e378d2f-dbb2-42b6-984e-b231bb806a7c
keywords:
- macroblocks WDK DirectX VA , generic command structure
ms.date: 04/20/2017
ms.localizationpriority: medium
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

 

 

 





