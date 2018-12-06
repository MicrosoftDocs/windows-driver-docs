---
title: Texture Stage Arguments
description: Texture Stage Arguments
ms.assetid: 434a0b88-2fb6-43e3-8a54-48f134a0dbff
keywords:
- multiple textures WDK Direct3D , texture stages
- texture stages WDK Direct3D
- texture management WDK Direct3D , stages
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# Texture Stage Arguments


## <span id="ddk_texture_stage_arguments_gg"></span><span id="DDK_TEXTURE_STAGE_ARGUMENTS_GG"></span>


Each of the multiple texture blending operations combines two inputs. These can be selected by calling the **IDirect3DDevice7::SetTextureStageState** method and specifying one of the following members of the D3DTEXTURESTAGESTATETYPE enumerated type.

<table>
<colgroup>
<col width="50%" />
<col width="50%" />
</colgroup>
<thead>
<tr class="header">
<th align="left">Enumerator</th>
<th align="left">Meaning</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td align="left"><p>D3DTSS_ALPHAARG1</p></td>
<td align="left"><p>Controls first input to alpha operation.</p></td>
</tr>
<tr class="even">
<td align="left"><p>D3DTSS_ALPHAARG2</p></td>
<td align="left"><p>Controls second input to alpha operation.</p></td>
</tr>
<tr class="odd">
<td align="left"><p>D3DTSS_COLORARG1</p></td>
<td align="left"><p>Controls first input to color operation.</p></td>
</tr>
<tr class="even">
<td align="left"><p>D3DTSS_COLORARG2</p></td>
<td align="left"><p>Controls second input to color operation.</p></td>
</tr>
</tbody>
</table>

 

For a description of **IDirect3DDevice7::SetTextureStageState**, see the Direct3D SDK documentation.

### <span id="texture_argument_flags"></span><span id="TEXTURE_ARGUMENT_FLAGS"></span>Texture Argument Flags

At each texture stage, any of the preceding four parameters can be set using the texture argument flags listed in the following table.

<table>
<colgroup>
<col width="50%" />
<col width="50%" />
</colgroup>
<thead>
<tr class="header">
<th align="left">Flag</th>
<th align="left">Meaning</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td align="left"><p>D3DTA_CURRENT</p></td>
<td align="left"><p>The texture argument is the result of the previous blending stage. In the first texture stage (stage zero), this argument is equivalent to D3DTA_DIFFUSE. This can be thought of as the current color of the polygon as each texture is blended onto it. If the previous blending stage uses a bump-map texture (the D3DTOP_BUMPENVMAP operation), the system chooses the texture from the stage before the bump-map texture. (If <em>s</em> represents the current texture stage, and <em>s - 1</em> contains a bump-map texture, this argument becomes the result output by texture stage <em>s - 2</em>.)</p></td>
</tr>
<tr class="even">
<td align="left"><p>D3DTA_DIFFUSE</p></td>
<td align="left"><p>The iterated color data obtained from the Gouraud interpolators. This is often used as the ARG2 on the first texture, because there is no D3DTA_CURRENT texture color at that point.</p></td>
</tr>
<tr class="odd">
<td align="left"><p>D3DTA_TEXTURE</p></td>
<td align="left"><p>The texture bound to this texture stage using the <strong>IDirect3DDevice7::SetTexture</strong>(n, lpTex3) method (described in the Direct3D SDK documentation), where <em>n</em> is the stage number. <strong>IDirect3DDevice7::SetTexture</strong> defines which texture object to use for the texture in this stage when D3DTA_TEXTURE is one of the arguments. D3DTA_TEXTURE can only be present in D3DTSS_ALPHAARG1 and D3DTSS_COLORARG1, but not in D3DTSS_ALPHAARG1 and D3DTSS_COLORARG2.</p></td>
</tr>
<tr class="even">
<td align="left"><p>D3DTA_TFACTOR</p></td>
<td align="left"><p>A value set in Direct3D with D3DRENDERSTATE_TEXTUREFACTOR.</p></td>
</tr>
</tbody>
</table>

 

**Note**   Some implementations may not be able to simultaneously use both D3DTA\_TFACTOR and a D3DTA\_DIFFUSE color.

 

### <span id="modifier_flags"></span><span id="MODIFIER_FLAGS"></span>Modifier Flags

The two values listed in the following table should be combined with one of the preceding flags using the bitwise OR operator.

<table>
<colgroup>
<col width="50%" />
<col width="50%" />
</colgroup>
<thead>
<tr class="header">
<th align="left">Value</th>
<th align="left">Meaning</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td align="left"><p>D3DTA_ALPHAREPLICATE</p></td>
<td align="left"><p>Indicates that this argument should have its alpha channel replicated to all color channels before use in this operation. If this is a texture with only one component, it is automatically replicated to all color channels for these operations. This flag need not be specified for the ALPHA_ARGs, but using it does not produce an error.</p></td>
</tr>
<tr class="even">
<td align="left"><p>D3DTA_COMPLEMENT</p></td>
<td align="left"><p>Indicates that this argument should be inverted for the operation.</p></td>
</tr>
</tbody>
</table>

 

### <span id="defaults"></span><span id="DEFAULTS"></span>Defaults

The following default values are used if a state is not filled in by the application. While these default values have been defined to make multiple texture operations more convenient, robust code always fully specifies the desired state.

D3DTSS\_COLORARG1 and D3DTSS\_ALPHAARG1 both default to D3DTA\_TEXTURE, if the corresponding texture has been set. If no texture has been set for this stage, then these both default to D3DTA\_DIFFUSE.

D3DTSS\_COLORARG2 and D3DTSS\_ALPHAARG2 default to D3DTA\_CURRENT. Note that D3DTA\_CURRENT defaults to D3DTA\_DIFFUSE on the first stage (except as noted in the description of D3DTA\_CURRENT).

ARG2 defaults to D3DTA\_DIFFUSE, but is ignored because the operation defaults to D3DTOP\_SELECTARG1.

D3DTA\_DIFFUSE defaults to 0xFFFFFFF if no diffuse color is specified in the flexible vertex format (FVF) data.

D3DTA\_SPECULAR defaults to 0x00000000 if no specular color is specified in the FVF data.

D3DTA\_CURRENT defaults to D3DTA\_DIFFUSE if this is the first stage except when the previous blending stage is a D3DTOP\_BUMPENVMAP or D3DTOP\_BUMPENVMAPLUMINANCE color operation. In this case, the following occurs:

-   If the previous stage is D3DTOP\_BUMPENVMAP or D3DTOP\_BUMPENVMAPLUMINANCE, then this argument is the result of the stage before the previous stage.

-   In the second texture stage (stage one), this argument defaults to D3DTA\_DIFFUSE.

D3DTA\_TEXTURE is a value for a D3DTSS\_COLORARG1 or D3DTSS\_ALPHAARG1 state of any stage, or defaults to 0x0 if no texture is bound to this stage.

 

 





