---
title: Retrieving Graphics Memory Numbers
description: Retrieving Graphics Memory Numbers
ms.assetid: ec704093-ad9a-4717-8e9e-537a2848b1c7
ms.author: windowsdriverdev
ms.date: 04/20/2017
ms.topic: article
ms.prod: windows-hardware
ms.technology: windows-devices
---

# Retrieving Graphics Memory Numbers


Software developers who create graphics applications can use the Microsoft DirectX version 10 APIs starting in Windows Vista to retrieve the accurate set of graphics memory numbers on computers running [Windows Display Driver Model (WDDM)](windows-vista-display-driver-model-design-guide.md) display drivers. The following steps show how to retrieve the graphics memory numbers:

1.  Because the new graphics memory reporting is available only on computers running Windows Display Driver Model (WDDM) display drivers, an application must first call the following function to confirm the driver model:
    ```
    HasWDDMDriver()
    {
        LPDIRECT3DCREATE9EX pD3D9Create9Ex = NULL;
        HMODULE             hD3D9          = NULL;

        hD3D9 = LoadLibrary( L"d3d9.dll" );

        if ( NULL == hD3D9 ) {
            return false;
        }

        //
        //  Try to create a IDirect3D9Ex interface (also known as a DX9L 
        //  interface).
        //  This interface can only be created if the driver is written 
        //  according to the Windows Display Driver Model (WDDM).
        //
        pD3D9Create9Ex = (LPDIRECT3DCREATE9EX) GetProcAddress (
            hD3D9, "Direct3DCreate9Ex" );

        return pD3D9Create9Ex != NULL;
    }
    ```

2.  After the application determines that the display driver model is the WDDM, the application can use the new DirectX version 10 APIs to get the graphics memory numbers. The application gets the graphics memory numbers from the following [**DXGI\_ADAPTER\_DESC**](https://msdn.microsoft.com/library/windows/desktop/bb173058) data structure, which is present in Dxgi.h and is included in the DirectX Software Development Kit (SDK).
    ```
    typedef struct DXGI_ADAPTER_DESC {
        WCHAR Description[ 128 ];
        UINT VendorId;
        UINT DeviceId;
        UINT SubSysId;
        UINT Revision;
        SIZE_T DedicatedVideoMemory;
        SIZE_T DedicatedSystemMemory;
        SIZE_T SharedSystemMemory;
        LUID AdapterLuid;
        } DXGI_ADAPTER_DESC;
    ```

Because of the extensive use of graphics in the Windows Vista and later desktop and DirectX games, software that runs on Windows Vista and later should be able to accurately determine the amount of available graphics memory. WDDM manages the virtualization of graphics memory in itself and also ensures accurate reporting of various aspects of graphics memory. Application developers and software vendors should take advantage of the DirectX version 10 APIs for retrieving the accurate set of graphics memory values on computers that have Windows Vista display drivers.

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20[display\display]:%20Retrieving%20Graphics%20Memory%20Numbers%20%20RELEASE:%20%282/10/2017%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")




