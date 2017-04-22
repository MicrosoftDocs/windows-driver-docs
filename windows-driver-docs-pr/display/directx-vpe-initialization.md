---
title: DirectX VPE Initialization
description: DirectX VPE Initialization
ms.assetid: 1309a302-f9fc-49cf-a6b8-691d0956beab
keywords:
- DirectX VPE support WDK DirectDraw , initialization
- drawing VPEs WDK DirectDraw , initialization
- DirectDraw VPEs WDK Windows 2000 display , initialization
- video port extensions WDK DirectDraw , initialization
- VPEs WDK DirectDraw , initialization
- initializing DirectX VPE functionality
ms.author: windowsdriverdev
ms.date: 04/20/2017
ms.topic: article
ms.prod: windows-hardware
ms.technology: windows-devices
---

# DirectX VPE Initialization


## <span id="ddk_directx_vpe_initialization_gg"></span><span id="DDK_DIRECTX_VPE_INITIALIZATION_GG"></span>


To enable VPE functionality, the driver must do the following:

-   When [**DrvGetDirectDrawInfo**](https://msdn.microsoft.com/library/windows/hardware/ff556229) is called, initialize the following members of the [**DDCORECAPS**](https://msdn.microsoft.com/library/windows/hardware/ff549248) structure embedded in the [**DD\_HALINFO**](https://msdn.microsoft.com/library/windows/hardware/ff551627) structure to which the *pHalInfo* parameter points:
    -   Set the DDCAPS2\_VIDEOPORT flag in **dwCaps2** to indicate that the display hardware contains a hardware video port. The driver should also set any other hardware video-port-related DDCAPS2\_*Xxx* flags to describe the VPE support that the device is capable of.
    -   Set **dwMaxVideoPorts** to the number of hardware video ports supported by the device.
    -   Initialize **dwCurrVideoPorts** to zero.
-   Implement a [**DdGetDriverInfo**](https://msdn.microsoft.com/library/windows/hardware/ff549404) function and set the **GetDriverInfo** member of the DD\_HALINFO structure to point to this function when [**DrvGetDirectDrawInfo**](https://msdn.microsoft.com/library/windows/hardware/ff556229) is called. The driver's **DdGetDriverInfo** function must parse the GUID\_VideoPortCallbacks and GUID\_VideoPortCaps GUIDs.

-   When [**DdGetDriverInfo**](https://msdn.microsoft.com/library/windows/hardware/ff549404) is called with the GUID\_VideoPortCallbacks GUID, fill in a [**DD\_VIDEOPORTCALLBACKS**](https://msdn.microsoft.com/library/windows/hardware/ff551758) structure with the appropriate driver callbacks and flags set. These callbacks are listed in [VPE Callback Functions](vpe-callback-functions.md). The driver must then copy this initialized structure into the DirectDraw-allocated buffer to which the **lpvData** member of the [**DD\_GETDRIVERINFODATA**](https://msdn.microsoft.com/library/windows/hardware/ff551550) structure points, and return the number of bytes written into the buffer in **dwActualSize**.

-   When [**DdGetDriverInfo**](https://msdn.microsoft.com/library/windows/hardware/ff549404) is called with the GUID\_VideoPortCaps GUID, fill in the array of [**DDVIDEOPORTCAPS**](https://msdn.microsoft.com/library/windows/hardware/ff550376) structures with the capabilities of each hardware video port. Each hardware video port has an entry in the array, with hardware video port zero specified first, hardware video port one specified next, and so on. If the device supports only one hardware video port, there will only be one DDVIDEOPORTCAPS structure in the array. The driver must then copy this data to the DirectDraw-allocated buffer to which the **lpvData** member of the [**DD\_GETDRIVERINFODATA**](https://msdn.microsoft.com/library/windows/hardware/ff551550) structure points and return the number of bytes written into the buffer in **dwActualSize**.

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20[display\display]:%20DirectX%20VPE%20Initialization%20%20RELEASE:%20%282/10/2017%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")




