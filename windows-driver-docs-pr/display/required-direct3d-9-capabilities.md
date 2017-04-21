---
title: Required Direct3D 9 capabilities
ms.assetid: AE8ED273-2329-4E53-9FCD-5A8E863AED83
description: Capabilities required for the user-mode driver to access Direct3D 9 features.
ms.author: windows-driver-content
ms.date: 04/20/2017
ms.topic: article
ms.prod: windows-hardware
ms.technology: windows-devices
---

# Required Direct3D 9 capabilities


For applications to fully access the features of Microsoft Direct3D versions 9\_1, 9\_2, and 9\_3, the user-mode driver must expose certain hardware capabilities. These capabilities are expressed in terms of the [**D3DCAPS9**](https://msdn.microsoft.com/library/windows/desktop/bb172513) structure that is returned by the user-mode driver's [*GetCaps*](https://msdn.microsoft.com/library/windows/hardware/ff566762) function. To indicate support of the capabilities, the driver must set these members of **D3DCAPS9** to a bitwise-OR of all of the respective flag values:

## <span id="Minimum_capabilities_for_Direct3D_level_9_1"></span><span id="minimum_capabilities_for_direct3d_level_9_1"></span><span id="MINIMUM_CAPABILITIES_FOR_DIRECT3D_LEVEL_9_1"></span>Minimum capabilities for Direct3D level 9\_1


<table>
<colgroup>
<col width="50%" />
<col width="50%" />
</colgroup>
<thead>
<tr class="header">
<th align="left">[<strong>D3DCAPS9</strong>](https://msdn.microsoft.com/library/windows/desktop/bb172513) member</th>
<th align="left">Flag value</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td align="left"><strong>Caps2</strong></td>
<td align="left"><p>D3DCAPS2_DYNAMICTEXTURES</p>
<p>D3DCAPS2_FULLSCREENGAMMA</p></td>
</tr>
<tr class="even">
<td align="left"><strong>PresentationIntervals</strong></td>
<td align="left"><p>D3DPRESENT_INTERVAL_IMMEDIATE</p>
<p>D3DPRESENT_INTERVAL_ONE</p></td>
</tr>
<tr class="odd">
<td align="left"><strong>PrimitiveMiscCaps</strong></td>
<td align="left"><p>D3DPMISCCAPS_COLORWRITEENABLE</p></td>
</tr>
<tr class="even">
<td align="left"><strong>ShadeCaps</strong></td>
<td align="left"><p>D3DPSHADECAPS_ALPHAGOURAUDBLEND</p>
<p>D3DPSHADECAPS_COLORGOURAUDRGB</p>
<p>D3DPSHADECAPS_FOGGOURAUD</p>
<p>D3DPSHADECAPS_SPECULARGOURAUDRGB</p></td>
</tr>
<tr class="odd">
<td align="left"><strong>TextureFilterCaps</strong></td>
<td align="left"><p>D3DPTFILTERCAPS_MINFLINEAR</p>
<p>D3DPTFILTERCAPS_MINFPOINT</p>
<p>D3DPTFILTERCAPS_MAGFLINEAR</p>
<p>D3DPTFILTERCAPS_MAGFPOINT</p></td>
</tr>
<tr class="even">
<td align="left"><strong>TextureCaps</strong>
<p>(See Note.)</p></td>
<td align="left"><p>D3DPTEXTURECAPS_ALPHA</p>
<p>D3DPTEXTURECAPS_CUBEMAP</p>
<p>D3DPTEXTURECAPS_MIPMAP</p>
<p>D3DPTEXTURECAPS_PERSPECTIVE</p></td>
</tr>
<tr class="odd">
<td align="left"><strong>TextureAddressCaps</strong></td>
<td align="left"><p>D3DPTADDRESSCAPS_CLAMP</p>
<p>D3DPTADDRESSCAPS_INDEPENDENTUV</p>
<p>D3DPTADDRESSCAPS_MIRROR</p>
<p>D3DPTADDRESSCAPS_WRAP</p></td>
</tr>
<tr class="even">
<td align="left"><strong>TextureOpCaps</strong></td>
<td align="left"><p>D3DTEXOPCAPS_DISABLE</p>
<p>D3DTEXOPCAPS_MODULATE</p>
<p>D3DTEXOPCAPS_SELECTARG1</p>
<p>D3DTEXOPCAPS_SELECTARG2</p></td>
</tr>
<tr class="odd">
<td align="left"><strong>SrcBlendCaps</strong></td>
<td align="left"><p>D3DPBLENDCAPS_INVDESTALPHA</p>
<p>D3DPBLENDCAPS_INVDESTCOLOR</p>
<p>D3DPBLENDCAPS_INVSRCALPHA</p>
<p>D3DPBLENDCAPS_ONE</p>
<p>D3DPBLENDCAPS_SRCALPHA</p>
<p>D3DPBLENDCAPS_ZERO</p></td>
</tr>
<tr class="even">
<td align="left"><strong>DestBlendCaps</strong></td>
<td align="left"><p>D3DPBLENDCAPS_ONE</p>
<p>D3DPBLENDCAPS_INVSRCALPHA</p>
<p>D3DPBLENDCAPS_INVSRCCOLOR</p>
<p>D3DPBLENDCAPS_SRCALPHA</p>
<p>D3DPBLENDCAPS_ZERO</p></td>
</tr>
<tr class="odd">
<td align="left"><strong>StretchRectFilterCaps</strong></td>
<td align="left"><p>D3DPTFILTERCAPS_MAGFLINEAR</p>
<p>D3DPTFILTERCAPS_MAGFPOINT</p>
<p>D3DPTFILTERCAPS_MINFLINEAR</p>
<p>D3DPTFILTERCAPS_MINFPOINT</p></td>
</tr>
<tr class="even">
<td align="left"><strong>ZCmpCaps</strong></td>
<td align="left"><p>D3DPCMPCAPS_ALWAYS</p>
<p>D3DPCMPCAPS_LESSEQUAL</p></td>
</tr>
<tr class="odd">
<td align="left"><strong>RasterCaps</strong></td>
<td align="left"><p>D3DPRASTERCAPS_DEPTHBIAS</p>
<p>D3DPRASTERCAPS_SLOPESCALEDEPTHBIAS</p></td>
</tr>
<tr class="even">
<td align="left"><strong>StencilCaps</strong></td>
<td align="left"><p>D3DSTENCILCAPS_TWOSIDED</p></td>
</tr>
<tr class="odd">
<td align="left"><strong>MaxTextureWidth</strong></td>
<td align="left"><p>2048</p></td>
</tr>
<tr class="even">
<td align="left"><strong>MaxTextureHeight</strong></td>
<td align="left"><p>2048</p></td>
</tr>
<tr class="odd">
<td align="left"><strong>NumSimultaneousRTs</strong></td>
<td align="left"><p>1</p></td>
</tr>
<tr class="even">
<td align="left"><strong>MaxSimultaneousTextures</strong></td>
<td align="left"><p>8</p></td>
</tr>
<tr class="odd">
<td align="left"><strong>MaxTextureBlendStages</strong></td>
<td align="left"><p>8</p></td>
</tr>
<tr class="even">
<td align="left"><strong>PixelShaderVersion</strong></td>
<td align="left"><p>D3DPS_VERSION(2,0)</p></td>
</tr>
<tr class="odd">
<td align="left"><strong>MaxPrimitiveCount</strong></td>
<td align="left"><p>65535</p></td>
</tr>
<tr class="even">
<td align="left"><strong>MaxVertexIndex</strong></td>
<td align="left"><p>65534</p></td>
</tr>
<tr class="odd">
<td align="left"><strong>MaxVolumeExtent</strong></td>
<td align="left"><p>256</p></td>
</tr>
<tr class="even">
<td align="left"><strong>MaxTextureRepeat</strong></td>
<td align="left"><p>Must be zero, or 128, or greater.</p></td>
</tr>
<tr class="odd">
<td align="left"><strong>MaxAnisotropy</strong></td>
<td align="left"><p>2</p></td>
</tr>
<tr class="even">
<td align="left"><strong>MaxVertexW</strong></td>
<td align="left"><p>0.f</p></td>
</tr>
</tbody>
</table>

 

**Note**  These requirements also apply:
-   The driver must also set the **TextureCaps** member to a value of D3DPTEXTURECAPS\_NONPOW2CONDITIONAL and D3DPTEXTURECAPS\_POW2, or to neither.
-   When the driver responds to an event, where [**D3DDDIARG\_CREATEQUERY**](https://msdn.microsoft.com/library/windows/hardware/ff542958).**QueryType** is D3DDDIQUERYTYPE\_EVENT, it must always set the event's **BOOL** value to **TRUE** when responding. See [*CreateQuery*](https://msdn.microsoft.com/library/windows/hardware/ff540673) and **D3DDDIARG\_CREATEQUERY**.

 

## <span id="Minimum_capabilities_for_Direct3D_level_9_2"></span><span id="minimum_capabilities_for_direct3d_level_9_2"></span><span id="MINIMUM_CAPABILITIES_FOR_DIRECT3D_LEVEL_9_2"></span>Minimum capabilities for Direct3D level 9\_2


These capabilities must be set in addition to those listed for Direct3D level 9\_1.

<table>
<colgroup>
<col width="50%" />
<col width="50%" />
</colgroup>
<thead>
<tr class="header">
<th align="left">[<strong>D3DCAPS9</strong>](https://msdn.microsoft.com/library/windows/desktop/bb172513) member</th>
<th align="left">Flag value</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td align="left"><strong>PrimitiveMiscCaps</strong></td>
<td align="left"><p>D3DPMISCCAPS_SEPARATEALPHABLEND</p></td>
</tr>
<tr class="even">
<td align="left"><strong>DevCaps2</strong></td>
<td align="left"><p>D3DDEVCAPS2_VERTEXELEMENTSCANSHARESTREAMOFFSET</p></td>
</tr>
<tr class="odd">
<td align="left"><strong>TextureAddressCaps</strong></td>
<td align="left"><p>D3DPTADDRESSCAPS_MIRRORONCE</p></td>
</tr>
<tr class="even">
<td align="left"><strong>VolumeTextureAddressCaps</strong></td>
<td align="left"><p>D3DPTADDRESSCAPS_MIRRORONCE</p></td>
</tr>
<tr class="odd">
<td align="left"><strong>MaxTextureWidth</strong></td>
<td align="left"><p>2048</p></td>
</tr>
<tr class="even">
<td align="left"><strong>MaxTextureHeight</strong></td>
<td align="left"><p>2048</p></td>
</tr>
<tr class="odd">
<td align="left"><strong>MaxTextureRepeat</strong></td>
<td align="left"><p>Must be zero, or 2048, or greater.</p></td>
</tr>
<tr class="even">
<td align="left"><strong>VertexShaderVersion</strong></td>
<td align="left"><p>D3DVS_VERSION(2,0)</p></td>
</tr>
<tr class="odd">
<td align="left"><strong>MaxAnisotropy</strong></td>
<td align="left"><p>16</p></td>
</tr>
<tr class="even">
<td align="left"><strong>MaxPrimitiveCount</strong></td>
<td align="left"><p>1048575</p></td>
</tr>
<tr class="odd">
<td align="left"><strong>MaxVertexIndex</strong></td>
<td align="left"><p>1048575</p></td>
</tr>
<tr class="even">
<td align="left"><strong>MaxVertexW</strong></td>
<td align="left"><p>10000000000.f</p></td>
</tr>
</tbody>
</table>

 

**Note**  This requirement also applies:
-   When the driver responds to a *z*-testing query, where [**D3DDDIARG\_CREATEQUERY**](https://msdn.microsoft.com/library/windows/hardware/ff542958).**QueryType** is D3DDDIQUERYTYPE\_OCCLUSION, it must always set the query's **UINT** value to a non-zero value when responding. See [*CreateQuery*](https://msdn.microsoft.com/library/windows/hardware/ff540673) and **D3DDDIARG\_CREATEQUERY**.

 

## <span id="Minimum_capabilities_for_Direct3D_level_9_3"></span><span id="minimum_capabilities_for_direct3d_level_9_3"></span><span id="MINIMUM_CAPABILITIES_FOR_DIRECT3D_LEVEL_9_3"></span>Minimum capabilities for Direct3D level 9\_3


These capabilities must be set in addition to those listed for Direct3D levels 9\_1 and 9\_2.

<table>
<colgroup>
<col width="50%" />
<col width="50%" />
</colgroup>
<thead>
<tr class="header">
<th align="left">[<strong>D3DCAPS9</strong>](https://msdn.microsoft.com/library/windows/desktop/bb172513) member</th>
<th align="left">Flag value</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td align="left"><strong>PS20Caps</strong>-&gt;<strong>Caps</strong></td>
<td align="left"><p>D3DPS20CAPS_GRADIENTINSTRUCTIONS</p></td>
</tr>
<tr class="even">
<td align="left"><strong>PrimitiveMiscCaps</strong></td>
<td align="left"><p>D3DPMISCCAPS_INDEPENDENTWRITEMASKS</p>
<p>D3DPMISCCAPS_MRTPOSTPIXELSHADERBLENDING</p></td>
</tr>
<tr class="odd">
<td align="left"><strong>TextureAddressCaps</strong></td>
<td align="left"><p>D3DPTADDRESSCAPS_BORDER</p></td>
</tr>
<tr class="even">
<td align="left"><strong>MaxTextureWidth</strong></td>
<td align="left"><p>4096</p></td>
</tr>
<tr class="odd">
<td align="left"><strong>MaxTextureHeight</strong></td>
<td align="left"><p>4096</p></td>
</tr>
<tr class="even">
<td align="left"><strong>MaxTextureRepeat</strong></td>
<td align="left"><p>Must be zero, or 8192, or greater.</p></td>
</tr>
<tr class="odd">
<td align="left"><strong>NumSimultaneousRTs</strong></td>
<td align="left"><p>4</p></td>
</tr>
<tr class="even">
<td align="left"><strong>PS20Caps</strong>-&gt;<strong>NumInstructionSlots</strong></td>
<td align="left"><p>512 (Pixel Shader Version 2b)</p></td>
</tr>
<tr class="odd">
<td align="left"><strong>PS20Caps</strong>-&gt;<strong>NumTemps</strong></td>
<td align="left"><p>32 (Pixel Shader Version 2b)</p></td>
</tr>
<tr class="even">
<td align="left"><strong>VS20Caps</strong>-&gt;<strong>NumTemps</strong></td>
<td align="left"><p>32 (Vertex Shader Version 2a)</p></td>
</tr>
<tr class="odd">
<td align="left"><strong>MaxVertexShaderConst</strong></td>
<td align="left"><p>256 (Vertex Shader Version 2a)</p></td>
</tr>
<tr class="even">
<td align="left"><strong>VertexShaderVersion</strong></td>
<td align="left"><p>D3DVS_VERSION(3,0) (See Note.)</p></td>
</tr>
</tbody>
</table>

 

**Note**  The **VertexShaderVersion** value of D3DVS\_VERSION(3,0) guarantees instancing support. Direct3D 10Level 9 does not expose Shader Model 3.0.

 

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20[display\display]:%20Required%20Direct3D%209%20capabilities%20%20RELEASE:%20%282/10/2017%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")




