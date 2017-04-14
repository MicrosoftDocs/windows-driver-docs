---
title: Multiple Texture Validation
description: Multiple Texture Validation
ms.assetid: 3f56f7c1-89d6-40d0-9540-b6280379ddc5
keywords: ["multiple textures WDK Direct3D , validation", "texture management WDK Direct3D , validation"]
---

# Multiple Texture Validation


## <span id="ddk_multiple_texture_validation_gg"></span><span id="DDK_MULTIPLE_TEXTURE_VALIDATION_GG"></span>


Current hardware does not necessarily implement everything that Direct3D can express. The application determines whether a particular blending operation can be performed by first setting up the desired blending mode, and then calling the **IDirect3DDevice7::ValidateDevice** method. The driver must accurately report its capabilities at initialization time and support [**D3dValidateTextureStageState**](https://msdn.microsoft.com/library/windows/hardware/ff549064) to allow its capabilities to be validated. Validation also covers operations specified at the TBLEND level. For information about **IDirect3DDevice7::ValidateDevice**, see the Direct3D SDK documentation.

The following table lists the return codes for **IDirect3DDevice7::ValidateDevice**.

<table>
<colgroup>
<col width="50%" />
<col width="50%" />
</colgroup>
<thead>
<tr class="header">
<th align="left">Return Code</th>
<th align="left">Meaning</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td align="left"><p>CONFLICTINGTEXTUREFILTER</p></td>
<td align="left"><p>The hardware cannot do trilinear filtering and multiple texturing at the same time.</p></td>
</tr>
<tr class="even">
<td align="left"><p>TOOMANYOPERATIONS</p></td>
<td align="left"><p>The hardware cannot handle the specified number of options.</p></td>
</tr>
<tr class="odd">
<td align="left"><p>UNSUPPORTEDALPHAARG</p></td>
<td align="left"><p>The specified alpha argument is unsupported.</p></td>
</tr>
<tr class="even">
<td align="left"><p>UNSUPPORTEDALPHAOPERATION</p></td>
<td align="left"><p>The specified alpha operation is unsupported.</p></td>
</tr>
<tr class="odd">
<td align="left"><p>UNSUPPORTEDCOLORARG</p></td>
<td align="left"><p>The specified color argument is unsupported.</p></td>
</tr>
<tr class="even">
<td align="left"><p>UNSUPPORTEDCOLOROPERATION</p></td>
<td align="left"><p>The specified color operation is unsupported.</p></td>
</tr>
<tr class="odd">
<td align="left"><p>UNSUPPORTEDFACTORVALUE</p></td>
<td align="left"><p>The hardware cannot support D3DTA_TFACTOR greater than 1.0.</p></td>
</tr>
<tr class="even">
<td align="left"><p>WRONGTEXTUREFORMAT</p></td>
<td align="left"><p>The hardware cannot support the current state in the selected texture format.</p></td>
</tr>
</tbody>
</table>

 

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20[display\display]:%20Multiple%20Texture%20Validation%20%20RELEASE:%20%282/10/2017%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")




