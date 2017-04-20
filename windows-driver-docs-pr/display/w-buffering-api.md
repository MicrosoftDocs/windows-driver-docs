---
title: W-Buffering API
description: W-Buffering API
ms.assetid: 7244d697-5200-4d37-9a75-270788c1c7f7
keywords:
- Direct3D WDK Windows 2000 display , w-buffering
- w-buffering WDK Direct3D
ms.author: windows-driver-content
ms.date: 04/20/2017
ms.topic: article
ms.prod: windows-hardware
ms.technology: windows-devices
---

# W-Buffering API


## <span id="ddk_w_buffering_api_gg"></span><span id="DDK_W_BUFFERING_API_GG"></span>


The D3DRENDERSTATE\_ZENABLE render state supports three settings from the D3DZBUFFERTYPE enumerated type.

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
<td align="left"><p>D3DZB_FALSE</p></td>
<td align="left"><p>Disables all depth buffering.</p></td>
</tr>
<tr class="even">
<td align="left"><p>D3DZB_TRUE</p></td>
<td align="left"><p>Enables z-buffer using perspective correct <em>z</em>.</p></td>
</tr>
<tr class="odd">
<td align="left"><p>D3DZB_USEW</p></td>
<td align="left"><p>Disables z-buffering but enables w-buffering, which is eye-relative <em>z</em>.</p></td>
</tr>
</tbody>
</table>

 

Because the exact format used for storing *w* varies widely, it should be assumed to be opaque.

Surface allocations and depth-fill operations work identically when using w-buffering. All z-buffer compare modes work identically in either case.

For more information, see the DirectX SDK documentation.

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20[display\display]:%20W-Buffering%20API%20%20RELEASE:%20%282/10/2017%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")




