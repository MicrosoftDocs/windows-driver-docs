---
title: Initializing Communication with the Direct3D Version 10 DDI
description: Initializing Communication with the Direct3D Version 10 DDI
ms.assetid: dc3cc26f-7295-46d6-9bd7-aae7027ea92c
ms.date: 04/20/2017
ms.localizationpriority: medium
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

 

 

 





