---
title: Querying for Information from the GPU
description: Querying for Information from the GPU
ms.assetid: 0d3942c2-3ae8-4eaa-9780-f146dd49699c
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# Querying for Information from the GPU


The Direct3D runtime might require information from the graphics processing unit (GPU) other than an output render target or output vertex buffer. Because the GPU executes in parallel with the CPU, the user-mode display driver should supply functions that expose the asynchronous nature of communication with the GPU efficiently.

The query object is the resource that the runtime and driver use for asynchronous notification. To create a query object, the runtime first calls the driver's [**CalcPrivateQuerySize**](https://msdn.microsoft.com/library/windows/hardware/ff538296) function so that the driver can supply the size of the memory region that the driver requires for the query object. The runtime then calls the driver's [**CreateQuery(D3D10)**](https://msdn.microsoft.com/library/windows/hardware/ff540675) function to create the query object. In the *CalcPrivateQuerySize* and *CreateQuery(D3D10)* calls, the runtime supplies a query-type value from the [**D3D10DDI\_QUERY**](https://msdn.microsoft.com/library/windows/hardware/ff541850) enumeration in the **Query** member of the [**D3D10DDIARG\_CREATEQUERY**](https://msdn.microsoft.com/library/windows/hardware/ff541685) structure that the *pCreateQuery* parameters point to.

Each query object instance exists in one of three states: *building*, *issued*, and *signaled*. The runtime calls the driver's [**QueryBegin**](https://msdn.microsoft.com/library/windows/hardware/ff569214) function to transition the query object to the building state.

**Note**   All query types support *QueryBegin* except for D3D10DDI\_QUERY\_EVENT and D3D10DDI\_QUERY\_TIMESTAMP. The building concept does not exist for D3D10DDI\_QUERY\_EVENT and D3D10DDI\_QUERY\_TIMESTAMP.

 

The runtime calls the driver's [**QueryEnd**](https://msdn.microsoft.com/library/windows/hardware/ff569217) function to transition the query object to the issued state. Transitions to the signaled state occur asynchronously some time later. The runtime calls the driver's [**QueryGetData**](https://msdn.microsoft.com/library/windows/hardware/ff569218) function to detect whether the query has transitioned to the signaled state. If the query is in the signaled state, *QueryGetData* can pass back data that applies to the query in the memory region that the *pData* parameter points to.

All query objects of the same type are FIFO (that is, first-in, first-out). For example, all query objects of type D3D10DDI\_QUERY\_EVENT complete in FIFO order based on their issued order. However, query objects of different types can complete or signal in an overlapping order. For example, a query of type D3D10DDI\_QUERY\_EVENT can complete before a query of type D3D10DDI\_QUERY\_OCCLUSION, even if the runtime issued the D3D10DDI\_QUERY\_EVENT query after the runtime issued the D3D10DDI\_QUERY\_OCCLUSION query.

When the runtime no longer requires the query object, the runtime frees the memory region that the runtime previously allocated for the object and calls the driver's [**DestroyQuery(D3D10)**](https://msdn.microsoft.com/library/windows/hardware/ff552785) function to notify the driver that the driver can no longer access this memory region.

 

 





