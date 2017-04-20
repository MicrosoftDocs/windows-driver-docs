---
title: Direct3D hardware requirements in Windows 8
description: This topic describes hardware requirements to support Microsoft Direct3D in Windows 8.
ms.assetid: 7297C938-D2DD-4A06-B9AD-18DDAA73A1E4
ms.author: windows-driver-content
ms.date: 04/20/2017
ms.topic: article
ms.prod: windows-hardware
ms.technology: windows-devices
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

 

**\*** Already exists in the Microsoft Direct3D 9 hardware specification, but is not previously exposed in Direct3D 10.

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20[display\display]:%20Direct3D%20hardware%20requirements%20in%20Windows%208%20%20RELEASE:%20%282/10/2017%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")




