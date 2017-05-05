---
title: Specifying GDI Hardware-Accelerated Rendering Operations
description: Specifying GDI Hardware-Accelerated Rendering Operations
ms.assetid: 71eb9cdf-0448-48d1-835a-84bbbba13670
keywords:
- rendering operations with GDI hardware acceleration WDK display
ms.author: windowsdriverdev
ms.date: 04/20/2017
ms.topic: article
ms.prod: windows-hardware
ms.technology: windows-devices
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
<td align="left"><p>[<strong>DXGK_GDIARG_ALPHABLEND</strong>](https://msdn.microsoft.com/library/windows/hardware/ff561074)</p></td>
<td align="left"><p>DXGK_GDIOP_ALPHABLEND = 3</p></td>
</tr>
<tr class="even">
<td align="left"><p>bit-block transfer with no stretching</p></td>
<td align="left"><p>BitBlt</p></td>
<td align="left"><p>[<strong>DXGK_GDIARG_BITBLT</strong>](https://msdn.microsoft.com/library/windows/hardware/ff561079)</p></td>
<td align="left"><p>DXGK_GDIOP_BITBLT = 1</p></td>
</tr>
<tr class="odd">
<td align="left"><p>ClearType and antialiased text pixel blend</p></td>
<td align="left"><p>ClearTypeBlend</p></td>
<td align="left"><p>[<strong>DXGK_GDIARG_CLEARTYPEBLEND</strong>](https://msdn.microsoft.com/library/windows/hardware/ff561082)</p></td>
<td align="left"><p>DXGK_GDIOP_CLEARTYPEBLEND = 7</p></td>
</tr>
<tr class="even">
<td align="left"><p>color fill</p></td>
<td align="left"><p>ColorFill</p></td>
<td align="left"><p>[<strong>DXGK_GDIARG_COLORFILL</strong>](https://msdn.microsoft.com/library/windows/hardware/ff561083)</p></td>
<td align="left"><p>DXGK_GDIOP_COLORFILL = 2</p></td>
</tr>
<tr class="odd">
<td align="left"><p>stretched bit-block transfer</p></td>
<td align="left"><p>StretchBlt</p></td>
<td align="left"><p>[<strong>DXGK_GDIARG_STRETCHBLT</strong>](https://msdn.microsoft.com/library/windows/hardware/ff561089)</p></td>
<td align="left"><p>DXGK_GDIOP_STRETCHBLT = 4</p></td>
</tr>
<tr class="even">
<td align="left"><p>bit-block transfer with transparency</p></td>
<td align="left"><p>TransparentBlt</p></td>
<td align="left"><p>[<strong>DXGK_GDIARG_TRANSPARENTBLT</strong>](https://msdn.microsoft.com/library/windows/hardware/ff561091)</p></td>
<td align="left"><p>DXGK_GDIOP_TRANSPARENTBLT = 6</p></td>
</tr>
</tbody>
</table>

 

The operating system uses the **OpCode** member of DXGK\_RENDERKM\_COMMAND to indicate the specific GDI hardware-accelerated rendering operation that the display miniport driver must process. The **OpCode** member is of type [**DXGK\_RENDERKM\_OPERATION**](https://msdn.microsoft.com/library/windows/hardware/ff562029), with values shown in the table.

The operating system will also supply the appropriate value of the DXGK\_RENDERKM\_COMMAND **CommandSize** member, which specifies the size of the current rendering command, in bytes, including the value of **OpCode** and the number of sub-rectangles in the command.

Further information about the capability of the display adapter to perform a bit-block transfer with transparency is provided in the [**D3DKM\_TRANSPARENTBLTFLAGS**](https://msdn.microsoft.com/library/windows/hardware/ff548468) structure contained in the DXGK\_GDIARG\_TRANSPARENTBLT-&gt;**Flags** member.

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20[display\display]:%20Specifying%20GDI%20Hardware-Accelerated%20Rendering%20Operations%20%20RELEASE:%20%282/10/2017%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")




