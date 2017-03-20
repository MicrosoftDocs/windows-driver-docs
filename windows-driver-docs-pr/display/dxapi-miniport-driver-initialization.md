---
title: DxApi Miniport Driver Initialization
description: DxApi Miniport Driver Initialization
ms.assetid: 8d2bb81c-618e-43e0-9a1a-ff0ceb732d90
keywords: ["DxApi miniport drivers WDK DirectDraw , initializing", "initializing DxApi miniport drivers"]
---

# DxApi Miniport Driver Initialization


## <span id="ddk_dxapi_miniport_driver_initialization_gg"></span><span id="DDK_DXAPI_MINIPORT_DRIVER_INITIALIZATION_GG"></span>


To enable DxApi interface functionality, the DirectDraw driver must perform the following tasks at initialization time:

1.  The driver must specify a [**DdGetDriverInfo**](https://msdn.microsoft.com/library/windows/hardware/ff549404) function in the [**DD\_HALINFO**](https://msdn.microsoft.com/library/windows/hardware/ff551627) structure that DirectDraw can call to get additional information.

2.  The *DdGetDriverInfo* callback is called with the GUID\_KernelCallbacks GUID specified. The driver must fill in a [**DD\_KERNELCALLBACKS**](https://msdn.microsoft.com/library/windows/hardware/ff551633) structure with the appropriate callbacks and flags set. The driver then copies this structure to the **lpvData** member of the [**DD\_GETDRIVERINFODATA**](https://msdn.microsoft.com/library/windows/hardware/ff551550) structure.

3.  The *DdGetDriverInfo* callback is called with GUID\_KernelCaps GUID specified. The driver must fill in a [**DDKERNELCAPS**](https://msdn.microsoft.com/library/windows/hardware/ff549593) structure. The driver then copies this structure to the **lpvData** member of the DD\_GETDRIVERINFODATA structure.

4.  The DirectDraw runtime calls the video port driver IOCTL handler with **MajorFunction** = IRP\_MJ\_PNP, **MinorFunction** = IRP\_MN\_QUERY\_INTERFACE, and **InterfaceType** = GUID\_DxApi. The video port driver then calls the video miniport driver's [*HwVidQueryInterface*](https://msdn.microsoft.com/library/windows/hardware/ff567358) function to fill in the [**DXAPI\_INTERFACE**](https://msdn.microsoft.com/library/windows/hardware/ff557395) structure with pointers to the DxApi interface callback functions that DirectDraw can call. These callback functions are listed in [Kernel-Mode Video Transport Callback Functions](kernel-mode-video-transport-callback-functions.md).

The video miniport driver can specify a value in the **Context** member of the [**DXAPI\_INTERFACE**](https://msdn.microsoft.com/library/windows/hardware/ff557395) structure that is passed to the video miniport driver each time one of these functions is called.

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20[display\display]:%20DxApi%20Miniport%20Driver%20Initialization%20%20RELEASE:%20%282/10/2017%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")




