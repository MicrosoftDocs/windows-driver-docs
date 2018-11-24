---
title: Direct3D Version 10 Kernel Handles
description: Direct3D Version 10 Kernel Handles
ms.assetid: 48378f27-4c08-4931-9592-878a1a2b2556
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# Direct3D Version 10 Kernel Handles


The Direct3D version 10 kernel handle life spans are typically controlled by the user-mode display driver explicitly. Such handles allow the user-mode display driver to manipulate allocations. Such handles can also allow the user-mode display driver to perform other interactions with the kernel (including interactions with the display miniport driver).

The following shows an example of a kernel handle for a resource:

```cpp
// Strongly typed handle to identify a resource object to the driver: 
typedef struct D3D10DDI_HKMRESOURCE
{
    D3DKMT_HANDLE handle;
} D3D10DDI_HKMRESOURCE;
```

 

 





