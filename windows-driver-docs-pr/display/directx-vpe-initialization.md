---
title: DirectX VPE Initialization
description: DirectX VPE Initialization
keywords:
- DirectX VPE support WDK DirectDraw , initialization
- drawing VPEs WDK DirectDraw , initialization
- DirectDraw VPEs WDK Windows 2000 display , initialization
- video port extensions WDK DirectDraw , initialization
- VPEs WDK DirectDraw , initialization
- initializing DirectX VPE functionality
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# DirectX VPE Initialization


## <span id="ddk_directx_vpe_initialization_gg"></span><span id="DDK_DIRECTX_VPE_INITIALIZATION_GG"></span>


To enable VPE functionality, the driver must do the following:

-   When [**DrvGetDirectDrawInfo**](/windows/win32/api/winddi/nf-winddi-drvgetdirectdrawinfo) is called, initialize the following members of the [**DDCORECAPS**](/windows/win32/api/ddrawi/ns-ddrawi-ddcorecaps) structure embedded in the [**DD\_HALINFO**](/windows/win32/api/ddrawint/ns-ddrawint-dd_halinfo) structure to which the *pHalInfo* parameter points:
    -   Set the DDCAPS2\_VIDEOPORT flag in **dwCaps2** to indicate that the display hardware contains a hardware video port. The driver should also set any other hardware video-port-related DDCAPS2\_*Xxx* flags to describe the VPE support that the device is capable of.
    -   Set **dwMaxVideoPorts** to the number of hardware video ports supported by the device.
    -   Initialize **dwCurrVideoPorts** to zero.
-   Implement a [**DdGetDriverInfo**](/windows/win32/api/ddrawint/nc-ddrawint-pdd_getdriverinfo) function and set the **GetDriverInfo** member of the DD\_HALINFO structure to point to this function when [**DrvGetDirectDrawInfo**](/windows/win32/api/winddi/nf-winddi-drvgetdirectdrawinfo) is called. The driver's **DdGetDriverInfo** function must parse the GUID\_VideoPortCallbacks and GUID\_VideoPortCaps GUIDs.

-   When [**DdGetDriverInfo**](/windows/win32/api/ddrawint/nc-ddrawint-pdd_getdriverinfo) is called with the GUID\_VideoPortCallbacks GUID, fill in a [**DD\_VIDEOPORTCALLBACKS**](/windows/win32/api/ddrawint/ns-ddrawint-dd_videoportcallbacks) structure with the appropriate driver callbacks and flags set. These callbacks are listed in [VPE Callback Functions](vpe-callback-functions.md). The driver must then copy this initialized structure into the DirectDraw-allocated buffer to which the **lpvData** member of the [**DD\_GETDRIVERINFODATA**](/windows/win32/api/ddrawint/ns-ddrawint-dd_getdriverinfodata) structure points, and return the number of bytes written into the buffer in **dwActualSize**.

-   When [**DdGetDriverInfo**](/windows/win32/api/ddrawint/nc-ddrawint-pdd_getdriverinfo) is called with the GUID\_VideoPortCaps GUID, fill in the array of [**DDVIDEOPORTCAPS**](/windows/win32/api/dvp/ns-dvp-ddvideoportcaps) structures with the capabilities of each hardware video port. Each hardware video port has an entry in the array, with hardware video port zero specified first, hardware video port one specified next, and so on. If the device supports only one hardware video port, there will only be one DDVIDEOPORTCAPS structure in the array. The driver must then copy this data to the DirectDraw-allocated buffer to which the **lpvData** member of the [**DD\_GETDRIVERINFODATA**](/windows/win32/api/ddrawint/ns-ddrawint-dd_getdriverinfodata) structure points and return the number of bytes written into the buffer in **dwActualSize**.

 

