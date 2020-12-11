---
title: Retrieving Graphics Memory Numbers
description: Retrieving Graphics Memory Numbers
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# Retrieving Graphics Memory Numbers


Software developers who create graphics applications can use the Microsoft DirectX version 10 APIs starting in Windows Vista to retrieve the accurate set of graphics memory numbers on computers running [Windows Display Driver Model (WDDM)](windows-vista-display-driver-model-design-guide.md) display drivers. The following steps show how to retrieve the graphics memory numbers:

1.  Because the new graphics memory reporting is available only on computers running Windows Display Driver Model (WDDM) display drivers, an application must first call the following function to confirm the driver model:
    ```cpp
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

2.  After the application determines that the display driver model is the WDDM, the application can use the new DirectX version 10 APIs to get the graphics memory numbers. The application gets the graphics memory numbers from the following [**DXGI\_ADAPTER\_DESC**](/windows/win32/api/dxgi/ns-dxgi-dxgi_adapter_desc) data structure, which is present in Dxgi.h and is included in the DirectX Software Development Kit (SDK).
    ```cpp
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
