---
title: Direct3D software requirements in Windows 8
description: This topic describes software requirements to support Microsoft Direct3D in Windows 8.
ms.assetid: EB9AB15A-4E47-48AE-AE39-6051F8FC39A8
ms.author: windows-driver-content
ms.date: 04/20/2017
ms.topic: article
ms.prod: windows-hardware
ms.technology: windows-devices
---

# Direct3D software requirements in Windows 8


This topic describes software requirements to support Microsoft Direct3D in Windows 8.

For Windows 8, independent hardware vendors must write a Windows Display Driver Model (WDDM) 1.2 driver that can support the relevant Direct3D feature level user-mode driver (UMD) device driver interfaces (DDIs).

For example, Microsoft Direct3D 9â€“capable hardware must, at minimum, support the Direct3D version 9 DDI. These software requirements vary based on the Microsoft DirectX hardware level as specified in this table:

**DirectX software requirements**

<table>
<colgroup>
<col width="50%" />
<col width="50%" />
</colgroup>
<thead>
<tr class="header">
<th align="left">DirectX hardware</th>
<th align="left">Software requirements</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td align="left">D3D9</td>
<td align="left"><p>Required: WDDM 1.2</p>
<p>Required: D3D9 - UMD DDI</p></td>
</tr>
<tr class="even">
<td align="left">D3D10</td>
<td align="left"><p>Required: WDDM 1.2</p>
<p>Required: D3D9 - UMD DDI</p>
<p>Required: D3D10- UMD DDI</p>
<p>Required: D3D11.1 - UMD DDI</p></td>
</tr>
<tr class="odd">
<td align="left">D3D10.1</td>
<td align="left"><p>Required: WDDM 1.2</p>
<p>Required: D3D9 - UMD DDI</p>
<p>Required: D3D10- UMD DDI</p>
<p>Required: D3D10.1- UMD DDI</p>
<p>Required: D3D11.1 - UMD DDI</p></td>
</tr>
<tr class="even">
<td align="left">D3D11</td>
<td align="left"><p>Required: WDDM 1.2</p>
<p>Required: D3D9 - UMD DDI</p>
<p>Required: D3D10- UMD DDI</p>
<p>Required: D3D10.1- UMD DDI</p>
<p>Required: D3D11 - UMD DDI</p>
<p>Required: D3D11.1 - UMD DDI</p></td>
</tr>
<tr class="odd">
<td align="left">D3D11.1</td>
<td align="left"><p>Required: WDDM 1.2</p>
<p>Required: D3D9 - UMD DDI</p>
<p>Required: D3D10- UMD DDI</p>
<p>Required: D3D10.1- UMD DDI</p>
<p>Required: D3D11 - UMD DDI</p>
<p>Required: D3D11.1 - UMD DDI</p></td>
</tr>
</tbody>
</table>

 

The following tables describe the functionality that's exposed by using user-mode driver (UMD) DDI changes in Windows 8.

**D3D9 - UMD DDI exposes the following new features in Windows 8**

| Required? | Feature                  |
|-----------|--------------------------|
| Required  | No overwrite and discard |
| Required  | Tileable copy flag       |

 

**D3D11.1 - UMD DDI exposes the following new features in Windows 8 across feature levels 10, 10.1, 11, and 11.1**

| Required?      | Feature                                                                            |
|----------------|------------------------------------------------------------------------------------|
| Required       | No overwrite and discard                                                           |
| Required       | Support for cross-process sharing of texture arrays (including Stereoscopic 3D)    |
| Required       | Tileable copy flag                                                                 |
| Required       | ClearView                                                                          |
| If Implemented | Logic ops                                                                          |
| Required       | Pixel formats (5551, 565, 4444) - exact support varies across feature level        |
| Required       | Same-surface blits                                                                 |
| Required       | Partial constant buffer updates                                                    |
| Required       | Offset constant buffer bind                                                        |
| Required       | Improved resource sharing                                                          |
| Required       | SampleCount=1 (limited Target-independent rasterization (TIR) on 10, 10.1, and 11) |

 

**D3D11.1 - UMD DDI exposes the following new features for feature level 11 & 11.1**

| Required?      | Feature                                   |
|----------------|-------------------------------------------|
| Required       | UAV-MSAA                                  |
| If Implemented | Double-precision shader functionality     |
| Required       | Masked sum of absolute differences (MSAD) |

 

**D3D11.1 - UMD DDI exposes the following new features for feature level 11.1**

| Required? | Feature                  |
|-----------|--------------------------|
| Required  | UAVs at every stage      |
| Required  | UAV-MSAA (at 16 samples) |
| Required  | TIR                      |

 

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20[display\display]:%20Direct3D%20software%20requirements%20in%20Windows%208%20%20RELEASE:%20%282/10/2017%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")




