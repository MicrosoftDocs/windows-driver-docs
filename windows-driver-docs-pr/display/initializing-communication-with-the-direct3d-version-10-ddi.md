---
title: Initializing Communication with the Direct3D Version 10 DDI
description: Initializing Communication with the Direct3D Version 10 DDI
ms.assetid: dc3cc26f-7295-46d6-9bd7-aae7027ea92c
ms.author: windows-driver-content
ms.date: 04/20/2017
ms.topic: article
ms.prod: windows-hardware
ms.technology: windows-devices
---

# Initializing Communication with the Direct3D Version 10 DDI


To initialize communication with the user-mode display driver DLL's version 10 DDI, the Direct3D version 10 runtime first loads the DLL if the DLL is not yet loaded. The Direct3D runtime next calls the user-mode display driver's [**OpenAdapter10**](https://msdn.microsoft.com/library/windows/hardware/ff568602) function through the DLL's export table to open an instance of the graphics adapter. The *OpenAdapter10* function is the DLL's only exported Direct3D version 10 function.

In the call to the driver's *OpenAdapter10* function, the runtime supplies the [**pfnQueryAdapterInfoCb**](https://msdn.microsoft.com/library/windows/hardware/ff568920) adapter callback function in the **pAdapterCallbacks** member of the [**D3D10DDIARG\_OPENADAPTER**](https://msdn.microsoft.com/library/windows/hardware/ff541724) structure. The runtime also supplies its version in the **Interface** and **Version** members of D3D10DDIARG\_OPENADAPTER. The user-mode display driver must verify that it can use this version of the runtime. The user-mode display driver must not fail newer versions of the runtime because newer runtime versions can use previous DDI versions and therefore can correctly communicate with drivers that implement those previous DDI versions. The user-mode display driver returns a table of its adapter-specific functions in the **pAdapterFuncs** member of D3D10DDIARG\_OPENADAPTER.

The user-mode display driver should call the [**pfnQueryAdapterInfoCb**](https://msdn.microsoft.com/library/windows/hardware/ff568920) adapter callback function to query for the graphics hardware capabilities from the display miniport driver.

The runtime calls the user-mode display driver's [**CreateDevice(D3D10)**](https://msdn.microsoft.com/library/windows/hardware/ff540635) function (one of the driver's adapter-specific functions) to create a display device for handling a collection of render state and to complete the initialization. When the initialization is complete, the Direct3D version 10 runtime can call the [display driver-supplied Direct3D version 10 functions](https://msdn.microsoft.com/library/windows/hardware/ff552909), and the user-mode display driver can call the [runtime-supplied functions](https://msdn.microsoft.com/library/windows/hardware/ff552862).

The user-mode display driver's *CreateDevice(D3D10)* function is called with a [**D3D10DDIARG\_CREATEDEVICE**](https://msdn.microsoft.com/library/windows/hardware/ff541664) structure whose members are set up in the following manner to initialize the user-mode display driver's version 10 DDI:

-   The runtime sets **Interface** to the version of the interface that the runtime requires from the user-mode display driver.

-   The runtime sets **Version** to a number that the driver can use to identify when the runtime was built. For example, the driver can use the version number to differentiate between a runtime released with Windows Vista and a runtime released with a subsequent service pack, which might contain a fix that the driver requires.

-   The runtime sets **hRTDevice** to specify the handle that the driver should use when the driver calls back into the runtime.

-   The runtime sets **hDrvDevice** to specify the handle that the runtime uses in subsequent driver calls.

-   The runtime supplies a table of its device-specific callback functions in the [**D3DDDI\_DEVICECALLBACKS**](https://msdn.microsoft.com/library/windows/hardware/ff544512) structure to which **pKTCallbacks** points. The user-mode display driver calls the runtime-supplied callback functions to access kernel-mode services in the display miniport driver.

-   The user-mode display driver returns a table of its device-specific functions in the [**D3D10DDI\_DEVICEFUNCS**](https://msdn.microsoft.com/library/windows/hardware/ff541833) structure to which **pDeviceFuncs** points.

-   The runtime supplies a [**DXGI\_DDI\_BASE\_ARGS**](https://msdn.microsoft.com/library/windows/hardware/ff557485) structure to which **DXGIBaseDDI** points. The runtime and the user-mode display driver supply their [DirectX Graphics Infrastructure DDI](directx-graphics-infrastructure-ddi.md) to this structure.

-   The runtime sets **hRTCoreLayer** to specify the handle that the driver should use when the driver calls back into the runtime to access core Direct3D 10 functionality (that is, in calls to the functions that the **pUMCallbacks** member specifies).

-   The runtime supplies a table of its core callback functions in the [**D3D10DDI\_CORELAYER\_DEVICECALLBACKS**](https://msdn.microsoft.com/library/windows/hardware/ff541820) structure to which **pUMCallbacks** points. The user-mode display driver calls the runtime-supplied core callback functions to refresh state.

**Note**   The number of display devices (graphics contexts) that can exist simultaneously is limited only by available system memory.

 

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20[display\display]:%20Initializing%20Communication%20with%20the%20Direct3D%20Version%2010%20DDI%20%20RELEASE:%20%282/10/2017%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")




