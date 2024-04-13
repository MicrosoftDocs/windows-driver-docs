---
title: Initializing D3D User-Mode Display Driver Communications
description: Initializing Communication with the Direct3D User-Mode Display Driver
keywords:
- user-mode display drivers WDK Windows Vista , initializing
- Direct3D WDK display
- user-mode display drivers WDK Windows Vista , Direct3D
ms.date: 09/17/2019
---

# Initializing Communication with the Direct3D User-Mode Display Driver

To initialize communication with the Microsoft Direct3D user-mode display driver DLL's version 11 DDI, the Direct3D runtime first loads the DLL. The Direct3D runtime next calls the user-mode display driver's [**OpenAdapter**](/windows-hardware/drivers/ddi/d3dumddi/nc-d3dumddi-pfnd3dddi_openadapter) function through the DLL's export table to open an instance of the graphics adapter. The *OpenAdapter* function is the DLL's only exported function.

In the call to the driver's *OpenAdapter* function, the runtime supplies the [**pfnQueryAdapterInfoCb**](/windows-hardware/drivers/ddi/d3dumddi/nc-d3dumddi-pfnd3dddi_queryadapterinfocb) adapter callback function in the **pAdapterCallbacks** member of the [**D3DDDIARG_OPENADAPTER**](/windows-hardware/drivers/ddi/d3dumddi/ns-d3dumddi-_d3dddiarg_openadapter) structure. The runtime also supplies its version in the **Interface** and **Version** members of D3DDDIARG_OPENADAPTER. The user-mode display driver must verify that it can use this version of the runtime. The user-mode display driver returns a table of its adapter-specific functions in the **pAdapterFuncs** member of D3DDDIARG_OPENADAPTER.

The user-mode display driver should call the [**pfnQueryAdapterInfoCb**](/windows-hardware/drivers/ddi/d3dumddi/nc-d3dumddi-pfnd3dddi_queryadapterinfocb) adapter callback function to query for the graphics hardware capabilities from the display miniport driver.

The runtime calls the user-mode display driver's [**CreateDevice**](/windows-hardware/drivers/ddi/d3dumddi/nc-d3dumddi-pfnd3dddi_createdevice) function (one of the driver's adapter-specific functions) to create a display device for handling a collection of render state and to complete the initialization. When the initialization is complete, the Direct3D runtime can call the [display driver-supplied functions](direct3d-functions-implemented-by-user-mode.md), and the user-mode display driver can call the [runtime-supplied functions](direct3d-runtime-functions-called-by-user-mode.md).

The user-mode display driver's *CreateDevice* function is called with a [**D3DDDIARG_CREATEDEVICE**](/windows-hardware/drivers/ddi/d3dumddi/ns-d3dumddi-_d3dddiarg_createdevice) structure whose members are set up in the following manner to initialize the user-mode display driver interface:

- The runtime sets **Interface** to the version of the interface that the runtime requires from the user-mode display driver.

- The runtime sets **Version** to a number that the driver can use to identify when the runtime was built. For example, the driver can use the version number to differentiate between a runtime released with Windows Vista and a runtime released with a subsequent service pack, which might contain a fix that the driver requires.

- The runtime sets **hDevice** to specify the handle that the driver should use when the driver calls back into the runtime. The driver generates a unique handle and passes it back to the runtime in **hDevice**. The runtime should use the returned **hDevice** handle in subsequent driver calls.

- The runtime supplies a table of its device-specific callback functions in the [**D3DDDI_DEVICECALLBACKS**](/windows-hardware/drivers/ddi/d3dumddi/ns-d3dumddi-_d3dddi_devicecallbacks) structure to which **pCallbacks** points. The user-mode display driver calls the runtime-supplied callback functions to access kernel-mode services in the display miniport driver.

- The user-mode display driver returns a table of its device-specific functions in the [**D3DDDI_DEVICEFUNCS**](/windows-hardware/drivers/ddi/d3dumddi/ns-d3dumddi-_d3dddi_devicefuncs) structure to which **pDeviceFuncs** points.

> [!NOTE]
> The number of display devices (graphics contexts) that can simultaneously exist is limited only by available system memory.
