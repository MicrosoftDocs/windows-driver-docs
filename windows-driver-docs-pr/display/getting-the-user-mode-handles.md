---
title: Getting the User-Mode Handles
description: Getting the User-Mode Handles
ms.assetid: b241bf00-1adb-4ab0-a00e-e922bdc9eee5
keywords:
- drawing kernel-mode video transport WDK DirectDraw , user-mode handles
- DirectDraw kernel-mode video transport WDK Windows 2000 display , user-mode handles
- kernel-mode video transport WDK DirectDraw , user-mode handles
- video transport kernel-mode WDK DirectDraw , user-mode handles
- user-mode handles WDK DirectDraw
ms.author: windows-driver-content
ms.date: 04/20/2017
ms.topic: article
ms.prod: windows-hardware
ms.technology: windows-devices
---

# Getting the User-Mode Handles


## <span id="ddk_getting_the_user_mode_handles_gg"></span><span id="DDK_GETTING_THE_USER_MODE_HANDLES_GG"></span>


The following procedures show how to obtain the user-mode (ring 3) handles.

To get the DirectDraw handle for a DirectDraw object:

1.  Call **QueryInterface(***lpDD*, &*IID\_IDirectDrawKernel*, &*pNewInterface***)** on the DirectDraw interface.

2.  Call the [**IDirectDrawKernel::GetKernelHandle**](https://msdn.microsoft.com/library/windows/hardware/ff567404) method on the new interface.

The **IDirectDrawKernel::GetKernelHandle** method returns a kernel-mode handle for the DirectDraw object. To release the handle, use the [**IDirectDrawKernel::ReleaseKernelHandle**](https://msdn.microsoft.com/library/windows/hardware/ff567407) method.

A user-mode component can also call the [**IDirectDrawKernel::GetCaps**](https://msdn.microsoft.com/library/windows/hardware/ff567401) method to retrieve the kernel-mode capabilities of the DirectDraw object.

### <span id="code_sample"></span><span id="CODE_SAMPLE"></span>Code Sample

```
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

1.  Call **QueryInterface(***lpSurface*, &*IID\_IDirectDrawSurfaceKernel*, &*pDDSK***)** on the DirectDrawSurface interface.

2.  Call the [**IDirectDrawSurfaceKernel::GetKernelHandle**](https://msdn.microsoft.com/library/windows/hardware/ff567411) method on the new interface.

The **IDirectDrawSurfaceKernel::GetKernelHandle** method returns a kernel-mode handle for the DirectDrawSurface driver. To release the handle, use the [**IDirectDrawSurfaceKernel::ReleaseKernelHandle**](https://msdn.microsoft.com/library/windows/hardware/ff567413) method.

### <span id="code_sample2"></span><span id="CODE_SAMPLE2"></span>Code Sample

```
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

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20[display\display]:%20Getting%20the%20User-Mode%20Handles%20%20RELEASE:%20%282/10/2017%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")




