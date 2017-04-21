---
title: Initializing Communication with the Direct3D User-Mode Display Driver
description: Initializing Communication with the Direct3D User-Mode Display Driver
ms.assetid: 96e85df4-e340-4017-b348-7c24349ffe69
keywords:
- user-mode display drivers WDK Windows Vista , initializing
- Direct3D WDK display
- user-mode display drivers WDK Windows Vista , Direct3D
ms.author: windows-driver-content
ms.date: 04/20/2017
ms.topic: article
ms.prod: windows-hardware
ms.technology: windows-devices
---

# Initializing Communication with the Direct3D User-Mode Display Driver


## <span id="ddk_initializing_communication_with_the_direct3d__user_mode_display_dr"></span><span id="DDK_INITIALIZING_COMMUNICATION_WITH_THE_DIRECT3D__USER_MODE_DISPLAY_DR"></span>


To initialize communication with the Microsoft Direct3D user-mode display driver, which is a dynamic-link library (DLL), the Direct3D runtime first loads the DLL. The Direct3D runtime next calls the user-mode display driver's [**OpenAdapter**](https://msdn.microsoft.com/library/windows/hardware/ff568601) function through the DLL's export table to open an instance of the graphics adapter. The *OpenAdapter* function is the DLL's only exported function.

In the call to the driver's *OpenAdapter* function, the runtime supplies the [**pfnQueryAdapterInfoCb**](https://msdn.microsoft.com/library/windows/hardware/ff568920) adapter callback function in the **pAdapterCallbacks** member of the [**D3DDDIARG\_OPENADAPTER**](https://msdn.microsoft.com/library/windows/hardware/ff543226) structure. The runtime also supplies its version in the **Interface** and **Version** members of D3DDDIARG\_OPENADAPTER. The user-mode display driver must verify that it can use this version of the runtime. The user-mode display driver returns a table of its adapter-specific functions in the **pAdapterFuncs** member of D3DDDIARG\_OPENADAPTER.

The user-mode display driver should call the [**pfnQueryAdapterInfoCb**](https://msdn.microsoft.com/library/windows/hardware/ff568920) adapter callback function to query for the graphics hardware capabilities from the display miniport driver.

The runtime calls the user-mode display driver's [**CreateDevice**](https://msdn.microsoft.com/library/windows/hardware/ff540634) function (one of the driver's adapter-specific functions) to create a display device for handling a collection of render state and to complete the initialization. When the initialization is complete, the Direct3D runtime can call the [display driver-supplied functions](https://msdn.microsoft.com/library/windows/hardware/ff570118), and the user-mode display driver can call the [runtime-supplied functions](https://msdn.microsoft.com/library/windows/hardware/ff552862).

The user-mode display driver's *CreateDevice* function is called with a [**D3DDDIARG\_CREATEDEVICE**](https://msdn.microsoft.com/library/windows/hardware/ff542931) structure whose members are set up in the following manner to initialize the user-mode display driver interface:

-   The runtime sets **Interface** to the version of the interface that the runtime requires from the user-mode display driver.

-   The runtime sets **Version** to a number that the driver can use to identify when the runtime was built. For example, the driver can use the version number to differentiate between a runtime released with Windows Vista and a runtime released with a subsequent service pack, which might contain a fix that the driver requires.

-   The runtime sets **hDevice** to specify the handle that the driver should use when the driver calls back into the runtime. The driver generates a unique handle and passes it back to the runtime in **hDevice**. The runtime should use the returned **hDevice** handle in subsequent driver calls.

-   The runtime supplies a table of its device-specific callback functions in the [**D3DDDI\_DEVICECALLBACKS**](https://msdn.microsoft.com/library/windows/hardware/ff544512) structure to which **pCallbacks** points. The user-mode display driver calls the runtime-supplied callback functions to access kernel-mode services in the display miniport driver.

-   The user-mode display driver returns a table of its device-specific functions in the [**D3DDDI\_DEVICEFUNCS**](https://msdn.microsoft.com/library/windows/hardware/ff544519) structure to which **pDeviceFuncs** points.

**Note**   The number of display devices (graphics contexts) that can simultaneously exist is limited only by available system memory.

 

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20[display\display]:%20Initializing%20Communication%20with%20the%20Direct3D%20User-Mode%20Display%20Driver%20%20RELEASE:%20%282/10/2017%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")




