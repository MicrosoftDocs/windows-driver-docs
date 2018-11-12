---
title: Specifying GDI Hardware-Accelerated Rendering Operations
description: Specifying GDI Hardware-Accelerated Rendering Operations
ms.assetid: 71eb9cdf-0448-48d1-835a-84bbbba13670
keywords:
- rendering operations with GDI hardware acceleration WDK display
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# Specifying GDI Hardware-Accelerated Rendering Operations


## <span id="ddk_introduction_to_command_and_dma_buffers_gg"></span><span id="DDK_INTRODUCTION_TO_COMMAND_AND_DMA_BUFFERS_GG"></span>


When the [**DxgkDdiRenderKm**](https://msdn.microsoft.com/library/windows/hardware/ff559800) function is called, the operating system specifies the type of GDI hardware-accelerated rendering operation to perform through the *pRenderKmArgs* parameter. The display port driver of the DirectX graphics kernel subsystem (*Dxgkrnl.sys*) sets the *pRenderKmArgs*-&gt;**pCommand** member to point to a command buffer that contains an array of variable-size [**DXGK\_RENDERKM\_COMMAND**](https://msdn.microsoft.com/library/windows/hardware/ff562026) structures. It also sets the *pRenderKmArgs*-&gt;**pCommandLength** member to the size of the command buffer, in bytes.

The driver must translate the input DXGK\_RENDERKM\_COMMAND command buffer into DMA buffer commands and build the patch location list.

DXGK\_RENDERKM\_COMMAND contains members that specify characteristics of GDI hardware-accelerated rendering operations, as described in the following table.

<table>
<colgroup>
<col width="25%" />
<col width="25%" />
<col width="25%" />
<col width="25%" />
</colgroup>
<thead>
<tr class="header">
<th align="left">Rendering Operation</th>
<th align="left">DXGK_RENDERKM_COMMAND Member</th>
<th align="left">Corresponding DXGK_GDIARG_XXX Structure</th>
<th align="left">Corresponding DXGK_RENDERKM_OPERATION Value</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td align="left"><p>alpha blend</p></td>
<td align="left"><p>AlphaBlend</p></td>
<td align="left"><p><a href="https://msdn.microsoft.com/library/windows/hardware/ff561074" data-raw-source="[&lt;strong&gt;DXGK_GDIARG_ALPHABLEND&lt;/strong&gt;](https://msdn.microsoft.com/library/windows/hardware/ff561074)"><strong>DXGK_GDIARG_ALPHABLEND</strong></a></p></td>
<td align="left"><p>DXGK_GDIOP_ALPHABLEND = 3</p></td>
</tr>
<tr class="even">
<td align="left"><p>bit-block transfer with no stretching</p></td>
<td align="left"><p>BitBlt</p></td>
<td align="left"><p><a href="https://msdn.microsoft.com/library/windows/hardware/ff561079" data-raw-source="[&lt;strong&gt;DXGK_GDIARG_BITBLT&lt;/strong&gt;](https://msdn.microsoft.com/library/windows/hardware/ff561079)"><strong>DXGK_GDIARG_BITBLT</strong></a></p></td>
<td align="left"><p>DXGK_GDIOP_BITBLT = 1</p></td>
</tr>
<tr class="odd">
<td align="left"><p>ClearType and antialiased text pixel blend</p></td>
<td align="left"><p>ClearTypeBlend</p></td>
<td align="left"><p><a href="https://msdn.microsoft.com/library/windows/hardware/ff561082" data-raw-source="[&lt;strong&gt;DXGK_GDIARG_CLEARTYPEBLEND&lt;/strong&gt;](https://msdn.microsoft.com/library/windows/hardware/ff561082)"><strong>DXGK_GDIARG_CLEARTYPEBLEND</strong></a></p></td>
<td align="left"><p>DXGK_GDIOP_CLEARTYPEBLEND = 7</p></td>
</tr>
<tr class="even">
<td align="left"><p>color fill</p></td>
<td align="left"><p>ColorFill</p></td>
<td align="left"><p><a href="https://msdn.microsoft.com/library/windows/hardware/ff561083" data-raw-source="[&lt;strong&gt;DXGK_GDIARG_COLORFILL&lt;/strong&gt;](https://msdn.microsoft.com/library/windows/hardware/ff561083)"><strong>DXGK_GDIARG_COLORFILL</strong></a></p></td>
<td align="left"><p>DXGK_GDIOP_COLORFILL = 2</p></td>
</tr>
<tr class="odd">
<td align="left"><p>stretched bit-block transfer</p></td>
<td align="left"><p>StretchBlt</p></td>
<td align="left"><p><a href="https://msdn.microsoft.com/library/windows/hardware/ff561089" data-raw-source="[&lt;strong&gt;DXGK_GDIARG_STRETCHBLT&lt;/strong&gt;](https://msdn.microsoft.com/library/windows/hardware/ff561089)"><strong>DXGK_GDIARG_STRETCHBLT</strong></a></p></td>
<td align="left"><p>DXGK_GDIOP_STRETCHBLT = 4</p></td>
</tr>
<tr class="even">
<td align="left"><p>bit-block transfer with transparency</p></td>
<td align="left"><p>TransparentBlt</p></td>
<td align="left"><p><a href="https://msdn.microsoft.com/library/windows/hardware/ff561091" data-raw-source="[&lt;strong&gt;DXGK_GDIARG_TRANSPARENTBLT&lt;/strong&gt;](https://msdn.microsoft.com/library/windows/hardware/ff561091)"><strong>DXGK_GDIARG_TRANSPARENTBLT</strong></a></p></td>
<td align="left"><p>DXGK_GDIOP_TRANSPARENTBLT = 6</p></td>
</tr>
</tbody>
</table>

 

The operating system uses the **OpCode** member of DXGK\_RENDERKM\_COMMAND to indicate the specific GDI hardware-accelerated rendering operation that the display miniport driver must process. The **OpCode** member is of type [**DXGK\_RENDERKM\_OPERATION**](https://msdn.microsoft.com/library/windows/hardware/ff562029), with values shown in the table.

The operating system will also supply the appropriate value of the DXGK\_RENDERKM\_COMMAND **CommandSize** member, which specifies the size of the current rendering command, in bytes, including the value of **OpCode** and the number of sub-rectangles in the command.

Further information about the capability of the display adapter to perform a bit-block transfer with transparency is provided in the [**D3DKM\_TRANSPARENTBLTFLAGS**](https://msdn.microsoft.com/library/windows/hardware/ff548468) structure contained in the DXGK\_GDIARG\_TRANSPARENTBLT-&gt;**Flags** member.

 

 





