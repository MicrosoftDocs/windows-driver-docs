---
title: Direct3D software requirements in Windows 8
description: This topic describes software requirements to support Microsoft Direct3D in Windows 8.
ms.assetid: EB9AB15A-4E47-48AE-AE39-6051F8FC39A8
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# Direct3D software requirements in Windows 8


This topic describes software requirements to support Microsoft Direct3D in Windows 8.

For Windows 8, independent hardware vendors must write a Windows Display Driver Model (WDDM) 1.2 driver that can support the relevant Direct3D feature level user-mode driver (UMD) device driver interfaces (DDIs).

For example, Microsoft Direct3D 9-capable hardware must, at minimum, support the Direct3D version 9 DDI. These software requirements vary based on the Microsoft DirectX hardware level as specified in this table:

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

 

 

 





