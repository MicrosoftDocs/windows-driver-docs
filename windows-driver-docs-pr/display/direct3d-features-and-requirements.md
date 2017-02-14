---
title: Direct3D features and requirements in WDDM 1.2
description: Microsoft Direct3D offers a rich collection of 3-D graphics APIs, which are widely used by software applications for complex visualization and game development.
ms.assetid: 8A40276D-FAE3-4433-A3E5-573700331B07
---

# Direct3D features and requirements in WDDM 1.2


Microsoft Direct3D offers a rich collection of 3-D graphics APIs, which are widely used by software applications for complex visualization and game development. This section describes feature improvements and Windows 8 Direct3D software and hardware requirements.

## <span id="in_this_section"></span>In this section


<table>
<colgroup>
<col width="50%" />
<col width="50%" />
</colgroup>
<thead>
<tr class="header">
<th align="left">Topic</th>
<th align="left">Description</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td align="left"><p>[DirectX feature improvements in Windows 8](directx-feature-improvements-in-windows-8.md)</p></td>
<td align="left"><p>Windows 8 includes Microsoft DirectX feature improvements that benefit developers, end users and system manufacturers.</p></td>
</tr>
<tr class="even">
<td align="left"><p>[Direct3D software requirements in Windows 8](software-requirements.md)</p></td>
<td align="left"><p>This topic describes software requirements to support Direct3D in Windows 8.</p></td>
</tr>
<tr class="odd">
<td align="left"><p>[Hardware requirements](hardware-requirements.md)</p></td>
<td align="left"><p>This topic describes hardware requirements to support Direct3D in Windows 8.</p></td>
</tr>
</tbody>
</table>

 

Depending on the capability of the graphics adapter, Direct3D allows applications to utilize hardware acceleration for the entire 3-D rendering pipeline or for partial acceleration. Newer versions of the Direct3D APIs such as Direct3D 9Ex and Microsoft Direct3D 10 are available only starting with Windows Vista because the Windows Display Driver Model (WDDM) provides the display driver interfaces needed for the functionality. This figure shows the incremental versions of Direct3D APIs that are supported on the various versions of WDDM:

![direct3d apis supported on the various versions of wddm](images/direct3dapissupportedwddm.jpg)

**Direct3D APIs supported on various versions of WDDM**

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20[display\display]:%20Direct3D%20features%20and%20requirements%20in%20WDDM%201.2%20%20RELEASE:%20%282/10/2017%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")




