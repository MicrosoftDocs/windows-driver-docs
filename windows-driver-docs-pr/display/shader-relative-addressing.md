---
title: Shader Relative Addressing
description: Shader Relative Addressing
ms.date: 01/05/2018
ms.localizationpriority: medium
---

# Shader Relative Addressing

Pixel and vertex shader versions that support relative addressing can specify that relative addressing is used in bit 13 of [destination](destination-parameter-token.md) and [source parameter tokens](source-parameter-token.md). When relative addressing is specified, an additional DWORD token follows the destination or source parameter token.

Note that this relative-addressing token is present only for vertex shader version 2\_0 and later and for pixel shader version 3\_0 and later. Relative addressing is not used for pixel shader versions earlier than 3\_0.

This relative-addressing token is formatted the same as the destination or source parameter token and the following rules apply:

-   Only D3DSPR\_ADDR or D3DSPR\_LOOP can be used as [register types](/windows-hardware/drivers/ddi/d3d9types/ne-d3d9types-_d3dshader_param_register_type).

-   Swizzle bits in source parameter tokens are used to determine a register component.

-   Bit 31 is 0x1.

-   Register offset is used.

-   All other bits are not used.

Address registers and the aL register are used for relative addressing of constant registers.

## Requirements

Available in Windows Vista and later versions of the Windows operating systems.
