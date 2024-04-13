---
title: Getting the User-Mode Handles
description: Getting the User-Mode Handles
keywords:
- drawing kernel-mode video transport WDK DirectDraw , user-mode handles
- DirectDraw kernel-mode video transport WDK Windows 2000 display , user-mode handles
- kernel-mode video transport WDK DirectDraw , user-mode handles
- video transport kernel-mode WDK DirectDraw , user-mode handles
- user-mode handles WDK DirectDraw
ms.date: 04/20/2017
---

# Getting the User-Mode Handles


## <span id="ddk_getting_the_user_mode_handles_gg"></span><span id="DDK_GETTING_THE_USER_MODE_HANDLES_GG"></span>


The following procedures show how to obtain the user-mode (ring 3) handles.

To get the DirectDraw handle for a DirectDraw object:

1. Call **QueryInterface(**<em>lpDD</em>, &*IID\_IDirectDrawKernel*, &<em>pNewInterface</em>**)** on the DirectDraw interface.

2. Call the [**IDirectDrawKernel::GetKernelHandle**](/windows/win32/api/ddkernel/nf-ddkernel-idirectdrawkernel-getkernelhandle) method on the new interface.

The **IDirectDrawKernel::GetKernelHandle** method returns a kernel-mode handle for the DirectDraw object. To release the handle, use the [**IDirectDrawKernel::ReleaseKernelHandle**](/windows/win32/api/ddkernel/nf-ddkernel-idirectdrawkernel-releasekernelhandle) method.

A user-mode component can also call the [**IDirectDrawKernel::GetCaps**](/windows/win32/api/ddkernel/nf-ddkernel-idirectdrawkernel-getcaps) method to retrieve the kernel-mode capabilities of the DirectDraw object.

### <span id="code_sample"></span><span id="CODE_SAMPLE"></span>Code Sample

```cpp
ddRVal = IDirectDraw_QueryInterface( lpDD, &IID_IDirectDrawKernel, &pDDK );
if( ( ddRVal == DD_OK ) && ( pDDK != NULL ) )
{
    dwDirectDrawHandle = 0;
    IDirectDrawKernel_GetKernelHandle( pDDK, dwDirectDrawHandle );
    if( dwDirectDrawHandle == 0 )
    {
        // error
    }
}
```

To get the DirectDrawSurface handle:

1. Call **QueryInterface(**<em>lpSurface</em>, &*IID\_IDirectDrawSurfaceKernel*, &<em>pDDSK</em>**)** on the DirectDrawSurface interface.

2. Call the [**IDirectDrawSurfaceKernel::GetKernelHandle**](/windows/win32/api/ddkernel/nf-ddkernel-idirectdrawsurfacekernel-getkernelhandle) method on the new interface.

The **IDirectDrawSurfaceKernel::GetKernelHandle** method returns a kernel-mode handle for the DirectDrawSurface driver. To release the handle, use the [**IDirectDrawSurfaceKernel::ReleaseKernelHandle**](/windows/win32/api/ddkernel/nf-ddkernel-idirectdrawsurfacekernel-releasekernelhandle) method.

### <span id="code_sample2"></span><span id="CODE_SAMPLE2"></span>Code Sample

```cpp
ddRVal = IDirectDraw_QueryInterface( lpSurface,
             &IID_IDirectDrawSurfaceKernel, &pDDSK );
if( ( ddRVal == DD_OK ) && ( pDDK != NULL ) )
{
    dwSurfaceHandle = 0;
    IDirectDrawSurfaceKernel_GetKernelHandle( pDDSK, dwSurfaceHandle );
    if( dwSurfaceHandle == 0 )
    {
        // error
    }
}
```

 

