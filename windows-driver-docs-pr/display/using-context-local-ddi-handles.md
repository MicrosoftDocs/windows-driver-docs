---
title: Using Context-Local DDI Handles
description: Using Context-Local DDI Handles
ms.assetid: 1b3e5c29-9b9e-4c10-8fe0-706255c8fd91
keywords:
- Direct3D version 11 WDK Windows 7 display , deferred contexts, using context-local DDI handles
- Direct3D version 11 WDK Windows Server 2008 R2 display , deferred contexts, using context-local DDI handles
- deferred contexts WDK Windows 7 display , using context-local DDI handles
- deferred contexts WDK Windows Server 2008 R2 display , using context-local DDI handles
- context-local DDI handles WDK Windows 7 display
- context-local DDI handles WDK Windows Server 2008 R2 display
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# Using Context-Local DDI Handles


This section applies only to Windows 7 and later, and Windows Server 2008 R2 and later versions of Windows operating system.

Each object (for example, resource, shader, and so on) has context-local DDI handles.

Suppose an object is used with three deferred contexts. In this situation, four handles refer to the same object (one handle for each deferred context and another handle for the immediate context). Because each context can be manipulated by a thread concurrently, a context-local handle ensures that multiple CPU threads do not contend over similar memory (either intentionally or unintentionally). Context-local handles are also intuitive because the driver probably must modify much of this data that is logically associated per context anyway (for example, the object might be bound by the context, and so on).

There is still the distinction of an immediate context handle versus a deferred context handle. In particular, the immediate context handle is guaranteed to be the first handle that is allocated and the last handle that is destroyed. The corresponding immediate context handle is provided during "opening" of each deferred context handle to link them together. There is currently no concept of an object having a per-device DDI handle (that is, a handle that is created before and destroyed after the immediate context handle, and would only be referenced in order by context handle creation).

Some handles have dependency relationships with other handles (for example, views have a dependency on their corresponding resource). The creation and destruction ordering guarantee that exists for the immediate context is extended to deferred context handles as well (that is, the runtime creates a context-local resource handle before the runtime creates any context-local view handles to that resource, and the runtime destroys a context-local resource handle after the runtime destroys all context-local view handles to that resource). When the runtime creates a context-local handle, the runtime provides the corresponding context-local dependency handles as well.

### <span id="driver_data_organization"></span><span id="DRIVER_DATA_ORGANIZATION"></span>Driver Data Organization

There are a few concerns about driver data organization that need attention. Like Direct3D version 10, the proper locality of data can reduce cache misses between the API and driver. The proper locality of data can also prevent the cache thrashing, which occurs when multiple pieces of frequently accessed data all resolve to the same cache index and exhaust the associatively of the cache. The DDI has been designed since Direct3D version 10 to help avoid such issues from manifesting by the driver informing the API how much memory the driver requires to satisfy a handle and the API assigning the value of the handle. However, new thread-related concerns impact the DDI design in the Direct3D version 11 timeframe.

Naturally, context-local handles provide a way to associate object data per-context, which avoids contention issues between threads. However, since such data is replicated for each deferred context, the size of such data is a major concern. That provides the natural rationalization to share read-only data between the immediate context handle and the deferred context handles. During creation of deferred context handles, the immediate context handle is provided to establish the connection between handles. However, any data that is located off of the deferred context handles gain locality benefits with API data, and the additional level of indirection to read-only data prevents locality benefits from extending to the read-only data. Some read-only data can be replicated into each context handle region if the locality benefits justify the data duplication. However, the memory that backs each deferred context handle should be considered at such a premium that it might be worthwhile to relocate data that is nonadjacent from the handle if that data is relatively large and not accessed as frequently as other data. Ideally, the type of data that is associated with each deferred context handle would be all high-frequency data anyway; therefore, the data would not be large enough to consider relocation necessary. Naturally, the driver must balance these conflicting motivations.

In order to make the driver data design efficiently compatible with Direct3D version 10, yet not divergent in implementation, the read-only data should be located contiguous (but still segregated from and after) the immediate context handle data. If the driver uses this design, the driver must be aware that cache-line padding is required between the immediate context handle data and the read-only data. Because a thread might manipulate each context handle data frequently (if not concurrently), false-sharing penalties occur between the immediate context handle data and deferred context handle data if cache-line padding is not used. The driver design must be cognizant of false-sharing penalties that manifest if pointers are established and traversed regularly between context handle memory regions.

The Direct3D runtime uses the following Direct3D 11 DDI for deferred context local handles:

-   The [**CheckDeferredContextHandleSizes**](https://msdn.microsoft.com/library/windows/hardware/ff539388) function verifies the sizes of the driver-private memory spaces that hold the handle data of deferred context handles.

-   The [**CalcDeferredContextHandleSize**](https://msdn.microsoft.com/library/windows/hardware/ff538272) function determines the size of the region of memory for a deferred context.

For the Direct3D runtime to retrieve the deferred context handle size that is required by the driver, the preceding DDI functions must be used. Immediately after creation of an object for the immediate context, the runtime calls [**CalcDeferredContextHandleSize**](https://msdn.microsoft.com/library/windows/hardware/ff538272) to query the driver for the amount of storage space that the driver requires to satisfy deferred context handles to this object. However, the Direct3D API must tune its CLS memory allocator by determining how many unique handle sizes and their values are accessed; the runtime calls the driver's [**CheckDeferredContextHandleSizes**](https://msdn.microsoft.com/library/windows/hardware/ff539388) function to obtain this information. Therefore, during device instantiation, the API requests an array of deferred context handle sizes by double polling. The first poll is to request how many sizes are returned, while the second poll passes in an array to retrieve the value of each size. The driver must indicate how much memory it requires to satisfy a handle along with which handle type. The driver can return multiple sizes that are associated with a particular handle type. However, it is undefined for the driver to ever return a value from **CalcDeferredContextHandleSize** that was not also correspondingly returned in the **CheckDeferredContextHandleSizes** array.

As for creating the DDI handles, the create methods on the deferred context are used. For example, examine the [**CreateBlendState(D3D10\_1)**](https://msdn.microsoft.com/library/windows/hardware/ff540597) and [**DestroyBlendState**](https://msdn.microsoft.com/library/windows/hardware/ff552745) functions. The HDEVICE naturally points to the appropriate deferred context (versus the immediate context); other CONST structure pointers are **NULL** (assuming the object has no dependencies); and, the D3D10DDI\_HRT\* handle is a D3D10DDI\_H\* handle to the corresponding immediate context object.

For objects that have dependencies (for example, views have a dependency relationship on their corresponding resource), the structure pointer that provides the dependency handle is not **NULL**. However, the only valid member of the structure is the dependency handle; whereas, the rest of the members are filled with zero. As an example, the [**D3D11DDIARG\_CREATESHADERRESOURCEVIEW**](https://msdn.microsoft.com/library/windows/hardware/ff542073) pointer in a call to the driver's [**CreateShaderResourceView(D3D11)**](https://msdn.microsoft.com/library/windows/hardware/ff540708) function will not be **NULL** when the runtime calls this function on a deferred context. In this CreateShaderResourceView(D3D11) call, the runtime assigns the appropriate context-local handle for the resource to the **hDrvResource** member of D3D11DDIARG\_CREATESHADERRESOURCEVIEW. The rest of the members of D3D11DDIARG\_CREATESHADERRESOURCEVIEW, though, are filled with zero.

The following example code shows how the Direct3D runtime translates an application's create request and the first use of deferred context to calls to the user-mode display driver to create immediate versus deferred contexts. The application's call to **ID3D11Device::CreateTexture2D** initiates the runtime code in the following "Resource Create" section. The application's call to **ID3D11Device::CopyResource** initiates the runtime code in the following "Deferred Context Resource Usage" section.

```cpp
// Device Create
 IC::pfnCheckDeferredContextHandleSizes( hIC, &u, NULL );
pArray = malloc( u * ... );
IC::pfnCheckDeferredContextHandleSizes( hIC, &u, pArray );

// Resource Create
 s = IC::pfnCalcPrivateResourceSize( hIC, &Args );
pICRHandle = malloc( s );
 IC::pfnCreateResource( hIC, &Args, pICRHandle, hRTResource );
 s2 = IC::pfnCalcDeferredContextHandleSize( hIC, D3D10DDI_HT_RESOURCE, pICRHandle );

// Deferred Context Resource Usage
pDCRHandle = malloc( s2 );
 DC::pfnCreateResource( hDC, NULL, pDCRHandle, pICRHandle );
```

### <span id="issues_with_pfnseterrorcb"></span><span id="ISSUES_WITH_PFNSETERRORCB"></span>Issues with pfnSetErrorCb

None of the create functions return an error code, which would have been ideal for the Direct3D version 11 threading model. All of the create functions use [**pfnSetErrorCb**](https://msdn.microsoft.com/library/windows/hardware/ff568929) to retrieve error codes back from the driver. To maximize compatibility with the Direct3D version 10 driver model, new DDI create functions that return error codes were not introduced. Instead, the driver must continue to use the unified device/immediate context D3D10DDI\_HRTCORELAYER handle with **pfnSetErrorCb** during the creation functions. When the driver supports command lists, the driver should use the appropriate **pfnSetErrorCb** that is associated with the corresponding context. That is, deferred context errors should go to the particular deferred context call to **pfnSetErrorCb** with the corresponding handle, and so on.

Deferred contexts can return E\_OUTOFMEMORY through a call to [**pfnSetErrorCb**](https://msdn.microsoft.com/library/windows/hardware/ff568929) from DDI functions that previously only allowed D3DDDIERR\_DEVICEREMOVED (like [**Draw**](https://msdn.microsoft.com/library/windows/hardware/ff556120), [**SetBlendState**](https://msdn.microsoft.com/library/windows/hardware/ff569527), and so on), since deferred context memory demands perpetually grow with each call to a DDI function. The Direct3D API triggers a local context removal, to assist the driver with such a failure case, which effectively tosses out the partially built command list. The application continues to determine that it is recording a command list; however, when the application eventually calls the **FinishCommandList** function, **FinishCommandList** returns a failure code of E\_OUTOFMEMORY.

 

 





