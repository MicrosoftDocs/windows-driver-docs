---
title: Direct3D hardware requirements in Windows 8
description: This topic describes hardware requirements to support Microsoft Direct3D in Windows 8.
ms.assetid: 7297C938-D2DD-4A06-B9AD-18DDAA73A1E4
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# Direct3D hardware requirements in Windows 8


This topic describes hardware requirements to support Microsoft Direct3D in Windows 8.

Independent hardware vendors must follow the Windows 8 Direct3D rendering requirements for hardware, as specified in this table. See also [DirectX feature improvements in Windows 8](directx-feature-improvements-in-windows-8.md) for specifics.

**Direct3D rendering requirements for hardware**

| Microsoft DirectX hardware version | Required/Optional | Windows 8 rendering requirements |
|------------------------------------|-------------------|----------------------------------|
| D3D9                               | Required          | D3D9 HW Spec                     |
| D3D10                              | Required          | D3D9 HW Spec                     |
| D3D10                              | Required          | D3D10 HW Spec                    |
| D3D10.1                            | Required          | D3D9 HW Spec                     |
| D3D10.1                            | Required          | D3D10 HW Spec                    |
| D3D10.1                            | Required          | D3D10.1 HW Spec                  |
| D3D11                              | Required          | D3D9 HW Spec                     |
| D3D11                              | Required          | D3D10 HW Spec                    |
| D3D11                              | Required          | D3D10.1 HW Spec                  |
| D3D11                              | Required          | D3D11 HW Spec                    |
| D3D11.1                            | Required          | D3D9 HW Spec                     |
| D3D11.1                            | Required          | D3D10 HW Spec                    |
| D3D11.1                            | Required          | D3D10.1 HW Spec                  |
| D3D11.1                            | Required          | D3D11 HW Spec                    |
| D3D11.1                            | Required          | D3D11.1 HW Spec                  |

 

The following tables describe the Direct3D hardware specification updates for Windows 8.

**Microsoft Direct3D 10 hardware specification changes for Windows 8**

| Required?      | Feature                            |
|----------------|------------------------------------|
| Required       | Pixel formats (5551, 565, 4444) \* |
| Required       | Same-surface blits \*              |
| If implemented | Logic ops                          |

 

**Direct3D 10.1 hardware specification changes for Windows 8**

| Required?      | Feature                            |
|----------------|------------------------------------|
| Required       | Pixel formats (5551, 565, 4444) \* |
| Required       | Same-surface blits \*              |
| If implemented | Logic ops                          |

 

**Microsoft Direct3D 11 hardware specification changes for Windows 8**

| Required?      | Feature                            |
|----------------|------------------------------------|
| Required       | Pixel formats (5551, 565, 4444) \* |
| Required       | Same-surface blits \*              |
| If implemented | UAV-MSAA                           |
| If implemented | Threading concurrent creates       |
| If implemented | Threading command lists            |
| If implemented | Double-precision support           |
| If implemented | Logic ops                          |

 

**Direct3D 11.1 hardware specification for Windows 8**

| Required?      | Feature                                |
|----------------|----------------------------------------|
| Required       | Logic ops                              |
| Required       | Pixel formats (5551, 565, 4444) \*     |
| Required       | Same-surface blits \*                  |
| Required       | UAVs at every stage                    |
| Required       | UAV-MSAA                               |
| Required       | Target-independent rasterization (TIR) |
| If implemented | Threading concurrent creates           |
| If implemented | Threading Command Lists                |
| If implemented | Double-precision support               |

 

**\\*** Already exists in the Microsoft Direct3D 9 hardware specification, but is not previously exposed in Direct3D 10.

 

 





