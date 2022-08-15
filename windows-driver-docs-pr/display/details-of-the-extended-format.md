---
title: Details of the Extended Format
description: Details of the Extended Format
keywords:
- Direct3D version 10.1 WDK Windows 7 display , extended format
- extended format WDK Windows 7 display
ms.date: 09/10/2019
---

# Details of the Extended Format

This section applies only to Windows 7 and later operating systems.

In the following table, the XR part of a format name can be considered a new shader interpretation of the bits akin to UNORM or SINT. The XR\_BIAS part of a format name is a special case that overloads this interpretation semantic with additional metadata. This metadata indicates that the format must be explicitly offset and biased in shader code on transitions into and out of the shader. The driver is not required to perform any of this biasing work; it is left entirely to the application.

## Table of extended formats

The following table shows resources with particular attributes that use the extended formats (DXGI_FORMAT_*) if the hardware supports these extended formats for the resource with those attributes or if extended formats for those resources are optional. See [DXGI_FORMAT](/windows/win32/api/dxgiformat/ne-dxgiformat-dxgi_format) for a description of each format.

Column key for the below table:

- **A**: DXGI_FORMAT_B8G8R8A8_TYPELESS
- **B**: DXGI_FORMAT_B8G8R8A8_UNORM (existing)
- **C**: DXGI_FORMAT_B8G8R8A8_UNORM_SRGB
- **D**: DXGI_FORMAT_B8G8R8X8_TYPELESS
- **E**: DXGI_FORMAT_B8G8R8X8_UNORM (existing)
- **F**: DXGI_FORMAT_B8G8R8X8_UNORM_SRGB
- **G**: DXGI_FORMAT_R10G10B10A2_TYPELESS
- **H**: DXGI_FORMAT_R10G10B10_XR_BIAS_A2_UNORM

<table>
<head>
    <tr>
        <th>Resource Attribute</th>
        <th>A</th>
        <th>B</th>
        <th>C</th>
        <th>D</th>
        <th>E</th>
        <th>F</th>
        <th>G</th>
        <th>H</th>
    </tr>
</head>
    <tr>
        <td>Buffer</td>
        <td>N/A</td>
        <td>R (changed)</td>
        <td>N/A</td>
        <td>N/A</td>
        <td>R (changed)</td>
        <td>N/A</td>
        <td>N/A</td>
        <td>N/A</td>
    </tr>
    <tr>
        <td>Input Assembler Vertex Buffer</td>
        <td>N/A</td>
        <td>R (changed)</td>
        <td>N/A</td>
        <td>N/A</td>
        <td>R (changed)</td>
        <td>N/A</td>
        <td>N/A</td>
        <td>N/A</td>
    </tr>
    <tr>
        <td>Texture1D</td>
        <td>R</td>
        <td>R (changed)</td>
        <td>R</td>
        <td>R</td>
        <td>R (changed)</td>
        <td>R</td>
        <td>R</td>
        <td>N/A</td>
    </tr>
    <tr>
        <td>Texture2D</td>
        <td>R</td>
        <td>R (changed)</td>
        <td>R</td>
        <td>R</td>
        <td>R</td>
        <td>R</td>
        <td>R</td>
        <td>R</td>
    </tr>    <tr>
        <td>Texture3D</td>
        <td>R</td>
        <td>R (changed)</td>
        <td>R</td>
        <td>R</td>
        <td>R (changed)</td>
        <td>R</td>
        <td>R</td>
        <td>N/A</td>
    </tr>
    <tr>
        <td>Texture Cube</td>
        <td>R</td>
        <td>R (changed)</td>
        <td>R</td>
        <td>R</td>
        <td>R (changed)</td>
        <td>R</td>
        <td>R</td>
        <td>N/A</td>
    </tr>
    <tr>
        <td>Shader ID</td>
        <td>N/A</td>
        <td>R</td>
        <td>R</td>
        <td>N/A</td>
        <td>R</td>
        <td>R</td>
        <td>N/A</td>
        <td>N/A</td>
    </tr>
    <tr>
        <td>Shader Sample (any filter)</td>
        <td>N/A</td>
        <td>R</td>
        <td>R</td>
        <td>N/A</td>
        <td>R</td>
        <td>R</td>
        <td>N/A</td>
        <td>N/A</td>
    </tr>
    <tr>
        <td>MIP-map textures</td>
        <td>R</td>
        <td>R (changed)</td>
        <td>R</td>
        <td>R</td>
        <td>R (changed)</td>
        <td>R</td>
        <td>R</td>
        <td>N/A</td>
    </tr>
    <tr>
        <td>MIP-map Auto-Generation</td>
        <td>N/A</td>
        <td>R (changed)</td>
        <td>R</td>
        <td>N/A</td>
        <td>R (changed)</td>
        <td>R</td>
        <td>N/A</td>
        <td>N/A</td>
    </tr>
    <tr>
        <td>Render Target</td>
        <td>N/A</td>
        <td>R</td>
        <td>R</td>
        <td>N/A</td>
        <td>R</td>
        <td>R</td>
        <td>N/A</td>
        <td>N/A</td>
    </tr>
    <tr>
        <td>Blendable Render Target</td>
        <td>N/A</td>
        <td>R</td>
        <td>R</td>
        <td>N/A</td>
        <td>R</td>
        <td>R</td>
        <td>N/A</td>
        <td>N/A</td>
    </tr>
    <tr>
        <td>CPU Lockable</td>
        <td>R</td>
        <td>R</td>
        <td>R</td>
        <td>R</td>
        <td>R</td>
        <td>R</td>
        <td>R</td>
        <td>R</td>
    </tr>
    <tr>
        <td>Multi-Sample Render Target</td>
        <td>N/A</td>
        <td>O</td>
        <td>O</td>
        <td>N/A</td>
        <td>O</td>
        <td>O</td>
        <td>N/A</td>
        <td>N/A</td>
    </tr>
    <tr>
        <td>Multi-Sample Resolve</td>
        <td>N/A</td>
        <td>R (changed)</td>
        <td>R</td>
        <td>N/A</td>
        <td>R (changed)</td>
        <td>R</td>
        <td>N/A</td>
        <td>N/A</td>
    </tr>
    <tr>
        <td>Multi-Sample Load</td>
        <td>N/A</td>
        <td>R</td>
        <td>R</td>
        <td>N/A</td>
        <td>R</td>
        <td>R</td>
        <td>N/A</td>
        <td>N/A</td>
    </tr>
    <tr>
        <td>Display Scan Out</td>
        <td>N/A</td>
        <td>R (changed)</td>
        <td>R</td>
        <td>N/A</td>
        <td>N/A</td>
        <td>N/A</td>
        <td>N/A</td>
        <td>R</td>
    </tr>
    <tr>
        <td>Cast Within Bit Layout</td>
        <td>R</td>
        <td>R (changed)</td>
        <td>R</td>
        <td>R</td>
        <td>R</td>
        <td>R</td>
        <td>R</td>
        <td>R</td>
    </tr>
</table>

>[!NOTE]
>In the preceding table, cell entries have the following meaning:
>
>- "R" indicates that hardware support is required
>- "o" indicates that hardware support is optional
>- N/A indicates that the resource attribute either is not applicable to the extended format or does not allow the extended format

>[!NOTE]
>The DXGI\_FORMAT\_B8G8R8A8\_UNORM and DXGI\_FORMAT\_B8G8R8X8\_UNORM formats already existed in the DXGI\_FORMAT enumeration. However, they are now considered members of the appropriate new family. Their requirements have changed compared to their original definitions.

>[!NOTE]
>Rows for the "Input Assembler Index Buffer", "Shader sample\_c (comparison filter)", "Shader sample (mono 1-bit filter)", "Shader gather4", and "Depth-Stencil Target" resource attributes are not included in the preceding table for readability. All meaning for these resource attributes is N/A.

The following sections describe the details of the new extended formats:

[XR Layout](xr-layout.md)

[XR Format Alpha Content](xr-format-alpha-content.md)

[DXGI\_FORMAT\_R10G10B10\_XR\_BIAS\_A2\_UNORM](dxgi-format-r10g10b10-xr-bias-a2-unorm.md)

[Casting Ability of XR Formats](casting-ability-of-xr-formats.md)

[XR\_BIAS Color Channel Conversion Rules](xr-bias-color-channel-conversion-rules.md)

[Interpretation of X Channel](interpretation-of-x-channel.md)
