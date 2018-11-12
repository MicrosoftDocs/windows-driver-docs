---
title: Direct3D Version 10 Runtime and Driver Handles
description: Direct3D Version 10 Runtime and Driver Handles
ms.assetid: 1e50afe1-7103-45c4-8f58-a08d51423b22
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# Direct3D Version 10 Runtime and Driver Handles


The Direct3D version 10 runtime and driver handles share the same life span. The Direct3D runtime specifies the lifetime of an object between calls to create-type functions (for example, [**CreateResource(D3D10)**](https://msdn.microsoft.com/library/windows/hardware/ff540691)) and calls to destroy-type functions (for example, [**DestroyResource(D3D10)**](https://msdn.microsoft.com/library/windows/hardware/ff552797)). The runtime provides driver-handle values as well as runtime-handle values. These handles are essentially pointers that are wrapped with a strong type to identify the object that is being operated on. The following are examples of runtime and driver handles for resources:

```cpp
// Strongly typed handle to identify a resource object to the driver: 
typedef struct D3D10DDI_HRESOURCE
{
    void* pDrvPrivate; // Pointer to memory location as large as the driver requested.
} D3D10DDI_HRESOURCE;

// Strongly typed handle to identify a resource object to the runtime:
typedef struct D3D10DDI_HRTRESOURCE
{
    void* handle;
} D3D10DDI_HRTRESOURCE;
```

All driver handles for a rendering device object and its children objects undergo the following two-pass creation mechanism:

1.  To determine the value of the driver handle pointer, the runtime first calls a *CalcPrivate***ObjType***Size* function (for example, the [**CalcPrivateResourceSize**](https://msdn.microsoft.com/library/windows/hardware/ff538302) function). In this call, the runtime passes in the creation parameters (for example, a pointer to the [**D3D10DDIARG\_CREATERESOURCE**](https://msdn.microsoft.com/library/windows/hardware/ff541697) structure). The runtime also passes in the creation parameters in the call to a *Create***ObjType** function.

    The user-mode display driver is generally not required to allocate anything during a call to *CalcPrivate***ObjType***Size*. However, if the driver does and fails or must indicate any other type of failure condition, the driver can return SIZE\_T( -1 ) to prevent handle creation. The runtime then returns an E\_OUTOFMEMORY error condition to the calling application.

    Minimally, the driver should return **sizeof(** void\* **)** from a call to *CalcPrivate***ObjType***Size*.

2.  If the runtime can allocate enough space to satisfy the size required by the user-mode display driver, the runtime will then call a *Create***ObjType** function (for example, [**CreateResource(D3D10)**](https://msdn.microsoft.com/library/windows/hardware/ff540691)) with the same creation parameters, along with the new unique value for the driver handle. The pointer value of the driver handle will be unique and constant for the life span of the handle, as it points to a region of memory the size of which was returned by *CalcPrivate***ObjType***Size*. The user-mode display driver can use this region of memory as required. The driver should gain an increase in efficiency by locating any frequently accessed data into the region of memory provided by the runtime.

 

 





