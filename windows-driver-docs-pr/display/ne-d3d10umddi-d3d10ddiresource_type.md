---
UID: NE:d3d10umddi.D3D10DDIRESOURCE_TYPE
title: D3D10DDIRESOURCE_TYPE (d3d10umddi.h)
description: Learn more about the D3D10DDIRESOURCE_TYPE enumeration.
ms.date: 11/03/2022
keywords: ["D3D10DDIRESOURCE_TYPE enumeration"]
ms.keywords: 
req.header: d3d10umddi.h
req.include-header: D3d10umddi.h
req.target-type: Windows
req.target-min-winverclnt: Windows Vista
req.target-min-winversvr: 
req.kmdf-ver: 
req.umdf-ver: 
req.ddi-compliance: 
req.unicode-ansi: 
req.idl: 
req.max-support: 
req.namespace: 
req.assembly: 
req.type-library: 
req.lib: 
req.dll: 
req.irql: 
targetos: Windows
tech.root: display
req.typenames: D3D10DDIRESOURCE_TYPE
f1_keywords:
 - D3D10DDIRESOURCE_TYPE
 - d3d10umddi/D3D10DDIRESOURCE_TYPE
topic_type:
 - APIRef
 - kbSyntax
api_type:
 - HeaderDef
api_location:
 - d3d10umddi.h
api_name:
 - D3D10DDIRESOURCE_TYPE
---

# D3D10DDIRESOURCE_TYPE enumeration

## Description

**D3D10DDIRESOURCE_TYPE** contains values that identify a type of resource.

## Constants

### D3D10DDIRESOURCE_BUFFER:1

The resource is a buffer.

### D3D10DDIRESOURCE_TEXTURE1D:2

The resource is a one-dimensional (1-D) texture.

### D3D10DDIRESOURCE_TEXTURE2D:3

The resource is a two-dimensional (2-D) texture.

### D3D10DDIRESOURCE_TEXTURE3D:4

The resource is a three-dimensional (3-D) texture.

### D3D10DDIRESOURCE_TEXTURECUBE:5

The resource is a cube texture.

### D3D11DDIRESOURCE_BUFFEREX:6

The resource is an expanded buffer. Supported in Windows 7 and later versions.

## Requirements

| Minimum client version | Windows Vista                           |
|------------------------|-----------------------------------------|
| Header                 | *d3d10umddi.h* (include *d3d10umddi.h*) |

## See Also

[**CreateResource(D3D10)**](/windows-hardware/drivers/ddi/d3d10umddi/nc-d3d10umddi-pfnd3d10ddi_createresource)

[**CreateShaderResourceView(D3D11)**](/windows-hardware/drivers/ddi/d3d10umddi/nc-d3d10umddi-pfnd3d11ddi_createshaderresourceview)

[**D3D10DDIARG_CREATERESOURCE**](/windows-hardware/drivers/ddi/d3d10umddi/ns-d3d10umddi-d3d10ddiarg_createresource)

[**D3D10_DDI_RESOURCE_USAGE**](/windows-hardware/drivers/ddi/d3d10umddi/ne-d3d10umddi-d3d10_ddi_resource_usage)

[**D3D11DDIARG_CREATESHADERRESOURCEVIEW**](/windows-hardware/drivers/ddi/d3d10umddi/ns-d3d10umddi-d3d11ddiarg_createshaderresourceview)
