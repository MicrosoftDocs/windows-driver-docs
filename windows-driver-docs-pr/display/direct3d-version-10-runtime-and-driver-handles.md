---
title: Direct3D Version 10 Runtime and Driver Handles
description: Direct3D Version 10 Runtime and Driver Handles
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# Direct3D Version 10 Runtime and Driver Handles


The Direct3D version 10 runtime and driver handles share the same life span. The Direct3D runtime specifies the lifetime of an object between calls to create-type functions (for example, [**CreateResource(D3D10)**](/windows-hardware/drivers/ddi/d3d10umddi/nc-d3d10umddi-pfnd3d10ddi_createresource)) and calls to destroy-type functions (for example, [**DestroyResource(D3D10)**](/windows-hardware/drivers/ddi/d3d10umddi/nc-d3d10umddi-pfnd3d10ddi_destroyresource)). The runtime provides driver-handle values as well as runtime-handle values. These handles are essentially pointers that are wrapped with a strong type to identify the object that is being operated on. The following are examples of runtime and driver handles for resources:

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

1.  To determine the value of the driver handle pointer, the runtime first calls a _CalcPrivate_**ObjType**_Size_ function (for example, the [**CalcPrivateResourceSize**](/windows-hardware/drivers/ddi/d3d10umddi/nc-d3d10umddi-pfnd3d10ddi_calcprivateresourcesize) function). In this call, the runtime passes in the creation parameters (for example, a pointer to the [**D3D10DDIARG\_CREATERESOURCE**](/windows-hardware/drivers/ddi/d3d10umddi/ns-d3d10umddi-d3d10ddiarg_createresource) structure). The runtime also passes in the creation parameters in the call to a _Create_**ObjType** function.

    The user-mode display driver is generally not required to allocate anything during a call to _CalcPrivate_**ObjType**_Size_. However, if the driver does and fails or must indicate any other type of failure condition, the driver can return SIZE\_T( -1 ) to prevent handle creation. The runtime then returns an E\_OUTOFMEMORY error condition to the calling application.

    Minimally, the driver should return **sizeof(** void\* **)** from a call to _CalcPrivate_**ObjType**_Size_.

2.  If the runtime can allocate enough space to satisfy the size required by the user-mode display driver, the runtime will then call a _Create_**ObjType** function (for example, [**CreateResource(D3D10)**](/windows-hardware/drivers/ddi/d3d10umddi/nc-d3d10umddi-pfnd3d10ddi_createresource)) with the same creation parameters, along with the new unique value for the driver handle. The pointer value of the driver handle will be unique and constant for the life span of the handle, as it points to a region of memory the size of which was returned by _CalcPrivate_**ObjType**_Size_. The user-mode display driver can use this region of memory as required. The driver should gain an increase in efficiency by locating any frequently accessed data into the region of memory provided by the runtime.

 

