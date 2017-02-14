---
title: Accessing a Multisampled Primary Surface
description: Accessing a Multisampled Primary Surface
ms.assetid: 5d83699c-45ae-46d1-8804-1a18bfbc203f
keywords: ["DirectX 8.0 release notes WDK Windows 2000 display , multisample rendering, accessing a primary surface", "multisample rendering WDK DirectX 8.0 , accessing a primary surface", "rendering multisamples WDK DirectX 8.0 , accessing a primary surface"]
---

# Accessing a Multisampled Primary Surface


## <span id="ddk_accessing_a_multisampled_primary_surface_gg"></span><span id="DDK_ACCESSING_A_MULTISAMPLED_PRIMARY_SURFACE_GG"></span>


The Direct3D runtime prevents high-performance CPU access to multisampled buffers. However, the runtime might call a driver's [*DdLock*](https://msdn.microsoft.com/library/windows/hardware/ff549599) function for low-performance access to multisampled buffers, such as for screen-shots and for image verification in test scenarios.

Because the runtime cannot process the sample layout of multisampled buffers, the driver must convert the format, and the driver's [*DdLock*](https://msdn.microsoft.com/library/windows/hardware/ff549599) function must return a buffer of data that contains the contents of the primary surface in a single sample-per-pixel format. If an application calls IDirect3DDevice8::GetFrontBuffer to obtain a copy of the front buffer of a multisampled flipping chain, the Direct3D runtime calls the driver's *DdLock* function to lock the front buffer. This buffer contains a version of the current front buffer that is resolved to the nominal width, height and pixel format of the primary surface.

If such a buffer is available in device memory, then the driver can return a pointer to that buffer. If such a buffer is not available in device memory (as is the case for devices that resolve multisample buffers at scan-out time), then the driver should allocate a buffer in system memory and resolve the multisampled front buffer into this system buffer. The runtime lets the driver take as much time as required to resolve the multisampled front buffer into this system buffer.

Regardless of whether the runtime sets the DDLOCK\_READONLY flag when it calls the driver's [*DdLock*](https://msdn.microsoft.com/library/windows/hardware/ff549599) function, the runtime treats these buffers as read only. Therefore, the driver is not required to copy any data from the system memory surface back into device memory. In addition, the driver's [*DdUnlock*](https://msdn.microsoft.com/library/windows/hardware/ff550365) function is not required to convert the single sample-per-pixel format back to the primary surface's multisampled format.

Calls by applications to the cursor methods of the **IDirect3DDevice8** interface can also result in [*DdBlt*](https://msdn.microsoft.com/library/windows/hardware/ff549205) calls targeting a multisampled primary. These *DdBlt* calls must handle the conversion from the single sample-per-pixel cursor data to the multisampled primary.

For more information about **IDirect3DDevice8**, see the DirectX 8.0 SDK documentation.

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20[display\display]:%20Accessing%20a%20Multisampled%20Primary%20Surface%20%20RELEASE:%20%282/10/2017%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")




