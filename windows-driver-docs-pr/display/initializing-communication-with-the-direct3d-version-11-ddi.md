---
title: Initializing Communication with the Direct3D Version 11 DDI
description: Initializing Communication with the Direct3D Version 11 DDI
ms.assetid: 3b383f78-da88-4979-b55f-8e234f230df7
keywords:
- Direct3D version 11 WDK Windows 7 display , initializing DDI communication
- Direct3D version 11 WDK Windows Server 2008 R2 display , initializing DDI communication
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# Initializing Communication with the Direct3D Version 11 DDI


This section applies only to Windows 7 and later, and Windows Server 2008 R2 and later versions of Windows operating system.

To initialize communication with the user-mode display driver DLL's version 11 DDI, the Direct3D version 11 runtime first loads the DLL if the DLL is not yet loaded. The Direct3D runtime next calls the user-mode display driver's [**OpenAdapter10\_2**](https://msdn.microsoft.com/library/windows/hardware/ff568603) function through the DLL's export table to open an instance of the graphics adapter. The **OpenAdapter10\_2** function is the DLL's only exported function.

**Note**   The [**OpenAdapter10\_2**](https://msdn.microsoft.com/library/windows/hardware/ff568603) function is identical to the [**OpenAdapter10**](https://msdn.microsoft.com/library/windows/hardware/ff568602) function except that **OpenAdapter10\_2** returns a table of the driver's adapter-specific functions in the **pAdapterFuncs\_2** member of the [**D3D10DDIARG\_OPENADAPTER**](https://msdn.microsoft.com/library/windows/hardware/ff541724) structure, and **OpenAdapter10** returns a table of the driver's adapter-specific functions in the pAdapterFuncs member of D3D10DDIARG\_OPENADAPTER. **pAdapterFuncs\_2** points to a [**D3D10\_2DDI\_ADAPTERFUNCS**](https://msdn.microsoft.com/library/windows/hardware/ff541900) structure; **pAdapterFuncs** points to a [**D3D10DDI\_ADAPTERFUNCS**](https://msdn.microsoft.com/library/windows/hardware/ff541811) structure.

 

[**OpenAdapter10\_2**](https://msdn.microsoft.com/library/windows/hardware/ff568603) was designed to make initializing drivers more efficient. You must implement **OpenAdapter10\_2** in your Direct3D version 11 drivers. You can also implement **OpenAdapter10\_2** (rather than or in addition to [**OpenAdapter10**](https://msdn.microsoft.com/library/windows/hardware/ff568602)) in your Direct3D version 10.1 drivers to increase the initialization efficiency of those drivers. For more information about implementing **OpenAdapter10\_2** in Direct3D version 10.1 drivers, see [Version Discovery Support](version-discovery-support.md). **OpenAdapter10\_2** handles the exchange of versioning and other information between the runtime and the driver.

### <span id="versioning"></span><span id="VERSIONING"></span>Versioning

[**OpenAdapter10\_2**](https://msdn.microsoft.com/library/windows/hardware/ff568603) and the driver's adapter-specific functions change the way versioning between the Direct3D API and Direct3D DDI is handled from the way that Direct3D 10 handled versioning (for more information about how Direct3D 10 handles versioning, see [Initializing Communication with the Direct3D Version 10 DDI](initializing-communication-with-the-direct3d-version-10-ddi.md)). Instead of the Direct3D API relying upon failure of the driver's **OpenAdapter10\_2** function to indicate no support for a particular version (as with **OpenAdapter10\_2**), the driver must explicitly list the DDI versions it supports. The Direct3D runtime calls the user-mode display driver's [**GetSupportedVersions**](https://msdn.microsoft.com/library/windows/hardware/ff566807) function (one of the driver's adapter-specific functions) to query for the DDI versions that the driver supports.

There are at least two new DDI versions for the Direct3D 11 DDI functions. Each DDI version distinguishes whether the DDI runs on Windows Vista or Windows 7. However, support of the Direct3D 11 DDI does not necessarily indicate full support of the hardware features that are associated with D3D\_FEATURE\_LEVEL\_11. Drivers can support the new threading features of the Direct3D 11 DDI with hardware that does not support the other features that are exposed by the Direct3D 11 DDI, like tessellation, and so on. The following code shows how each DDI version is distinguished:

```cpp
// D3D11.0 on Vista
#define D3D11_DDI_MAJOR_VERSION 11
#define D3D11_0_DDI_MINOR_VERSION ...
#define D3D11_0_DDI_INTERFACE_VERSION \
    ((D3D11_DDI_MAJOR_VERSION << 16) | D3D11_0_DDI_MINOR_VERSION)
#define D3D11_0_DDI_BUILD_VERSION ...
#define D3D11_0_DDI_SUPPORTED \
    ((((UINT64)D3D11_0_DDI_INTERFACE_VERSION) << 32) | \
    (((UINT64)D3D11_0_DDI_BUILD_VERSION) << 16))

// D3D11.0 on Windows 7
#define D3D11_0_7_DDI_MINOR_VERSION ...
#define D3D11_0_7_DDI_INTERFACE_VERSION \
    ((D3D11_DDI_MAJOR_VERSION << 16) | D3D11_0_7_DDI_MINOR_VERSION)
#define D3D11_0_7_DDI_BUILD_VERSION ...
#define D3D11_0_7_DDI_SUPPORTED \
    ((((UINT64)D3D11_0_7_DDI_INTERFACE_VERSION) << 32) | \
    (((UINT64)D3D11_0_7_DDI_BUILD_VERSION) << 16))
 
#ifndef IS_D3D11_WIN7_INTERFACE_VERSION
#define IS_D3D11_WIN7_INTERFACE_VERSION( i ) (D3D11_0_7_DDI_INTERFACE_VERSION == i)
#endif 
```

### <span id="information_exchange"></span><span id="INFORMATION_EXCHANGE"></span>Information Exchange

In addition to specifying version information, the driver's [**OpenAdapter10\_2**](https://msdn.microsoft.com/library/windows/hardware/ff568603) function also exchanges other information between the runtime and the driver.

In the call to the driver's [**OpenAdapter10\_2**](https://msdn.microsoft.com/library/windows/hardware/ff568603) function, the runtime supplies the [**pfnQueryAdapterInfoCb**](https://msdn.microsoft.com/library/windows/hardware/ff568920) adapter callback function in the **pAdapterCallbacks** member of the [**D3D10DDIARG\_OPENADAPTER**](https://msdn.microsoft.com/library/windows/hardware/ff541724) structure. The user-mode display driver should call the **pfnQueryAdapterInfoCb** adapter callback function to query for the graphics hardware capabilities from the display miniport driver.

The runtime calls the user-mode display driver's [**CreateDevice(D3D10)**](https://msdn.microsoft.com/library/windows/hardware/ff540635) function (one of the driver's adapter-specific functions) to create a display device for handling a collection of render state and to complete the initialization. When the initialization is complete, the Direct3D version 11 runtime can call the [display driver-supplied Direct3D version 11 functions](https://msdn.microsoft.com/library/windows/hardware/ff552924), and the user-mode display driver can call the [runtime-supplied functions](https://msdn.microsoft.com/library/windows/hardware/ff552862).

The user-mode display driver's CreateDevice(D3D10) function is called with a [**D3D10DDIARG\_CREATEDEVICE**](https://msdn.microsoft.com/library/windows/hardware/ff541664) structure whose members are set up in the following manner to initialize the user-mode display driver's version 11 DDI:

-   The runtime sets **Interface** to the version of the interface that the runtime requires from the user-mode display driver.

-   The runtime sets **Version** to a number that the driver can use to identify when the runtime is built. For example, the driver can use the version number to differentiate between a runtime released with Windows Vista and a runtime released with a subsequent service pack, which might contain a fix that the driver requires.

-   The runtime sets **hRTDevice** to specify the handle that the driver should use when the driver calls back into the runtime.

-   The runtime sets **hDrvDevice** to specify the handle that the runtime uses in subsequent driver calls.

-   The runtime supplies a table of its device-specific callback functions in the [**D3DDDI\_DEVICECALLBACKS**](https://msdn.microsoft.com/library/windows/hardware/ff544512) structure to which **pKTCallbacks** points. The user-mode display driver calls the runtime-supplied callback functions to access kernel-mode services in the display miniport driver.

-   The user-mode display driver returns a table of its device-specific functions in the [**D3D11DDI\_DEVICEFUNCS**](https://msdn.microsoft.com/library/windows/hardware/ff542141) structure to which **p11DeviceFuncs** points.

-   The runtime supplies a [**DXGI\_DDI\_BASE\_ARGS**](https://msdn.microsoft.com/library/windows/hardware/ff557485) structure to which **DXGIBaseDDI** points. The runtime and the user-mode display driver supply their [DirectX Graphics Infrastructure DDI](directx-graphics-infrastructure-ddi.md) to this structure.

-   The runtime sets **hRTCoreLayer** to specify the handle that the driver should use when the driver calls back into the runtime to access core Direct3D 10 functionality (that is, in calls to the functions that the **p11UMCallbacks** member specifies).

-   The runtime supplies a table of its core callback functions in the [**D3D11DDI\_CORELAYER\_DEVICECALLBACKS**](https://msdn.microsoft.com/library/windows/hardware/ff542137) structure to which **p11UMCallbacks** points. The user-mode display driver calls the runtime-supplied core callback functions to refresh state.

 

 





