---
title: Calling the Deinterlace DDI from a User-Mode Component
description: Calling the Deinterlace DDI from a User-Mode Component
ms.assetid: 3ec18c7e-02dc-4607-b280-3ca1bc5d2839
keywords:
- calling deinterlace DDI WDK DirectX VA
- user-mode component calls WDK DirectX VA
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# Calling the Deinterlace DDI from a User-Mode Component


## <span id="ddk_calling_the_deinterlace_ddi_from_a_user_mode_component_gg"></span><span id="DDK_CALLING_THE_DEINTERLACE_DDI_FROM_A_USER_MODE_COMPONENT_GG"></span>


A user-mode component, such as the VMR, initiates calls to the deinterlacing DDI.

So that the VMR can deinterlace and perform frame-rate conversion on video content, the display driver must implement the [motion compensation callback functions](motion-compensation-callbacks.md), which are defined by members of the [**DD\_MOTIONCOMPCALLBACKS**](https://msdn.microsoft.com/library/windows/hardware/ff551660) structure.

To simplify driver development, driver writers can use a motion-compensation code template and implement the [deinterlacing sample functions](sample-functions-for-deinterlacing.md). The motion-compensation template calls the deinterlacing sample functions to perform deinterlacing and frame-rate conversion on video content. For more information about using a motion-compensation template, see [Example Code for DirectX VA Devices](example-code-for-directx-va-devices.md).

The following steps explain how the VMR initiates calls to the deinterlace DDI:

1.  When the VMR is added to a filter graph, it initiates a call to the driver-supplied [*DdMoCompGetGuids*](https://msdn.microsoft.com/library/windows/hardware/ff550236) callback function to retrieve the list of devices supported by the driver. The **GetMoCompGuids** member of the DD\_MOTIONCOMPCALLBACKS structure points to this callback function. For more information about a filter graph, see [KS Minidriver Architecture](https://msdn.microsoft.com/library/windows/hardware/ff567656).

2.  If the deinterlace container device GUID is present, the VMR initiates a call to the [*DdMoCompCreate*](https://msdn.microsoft.com/library/windows/hardware/ff549656) callback function to create an instance of the device. The **CreateMoComp** member of DD\_MOTIONCOMPCALLBACKS points to the callback function. In the *DdMoCompCreate* call, a pointer to the container device GUID is specified in the **lpGuid** member of the [**DD\_CREATEMOCOMPDATA**](https://msdn.microsoft.com/library/windows/hardware/ff550529) structure. The container device GUID is defined as follows:
    ```cpp
    DEFINE_GUID(DXVA_DeinterlaceContainerDevice, 0x0e85cb93,0x3046,0x4ff0,0xae,0xcc,0xd5,0x8c,0xb5,0xf0,0x35,0xfd);
    ```

3.  To determine the available deinterlacing or frame-rate conversion modes for a particular input video format, the VMR initiates a call to the driver-supplied [*DdMoCompRender*](https://msdn.microsoft.com/library/windows/hardware/ff550248) callback function. The **RenderMoComp** member of [**DD\_MOTIONCOMPCALLBACKS**](https://msdn.microsoft.com/library/windows/hardware/ff551660) points to the callback function. In the **DdMoCompRender** call, the **DXVA\_ProcAmpControlQueryCapsFnCode** constant (defined in *dxva.h*) is set in the **dwFunction** member of the [**DD\_RENDERMOCOMPDATA**](https://msdn.microsoft.com/library/windows/hardware/ff551693) structure. The **lpInputData** member of DD\_RENDERMOCOMPDATA passes the input parameters to the driver by pointing to a completed [**DXVA\_VideoDesc**](https://msdn.microsoft.com/library/windows/hardware/ff564070) structure. The driver returns its output through the **lpOutputData** member of DD\_RENDERMOCOMPDATA; **lpOutputData** points to a [**DXVA\_DeinterlaceQueryAvailableModes**](https://msdn.microsoft.com/library/windows/hardware/ff563951) structure.

    If the driver implements a [**DeinterlaceQueryAvailableModes**](https://msdn.microsoft.com/library/windows/hardware/ff563943) sample function, the **DdMoCompRender** callback function calls **DeinterlaceQueryAvailableModes**.

4.  For each deinterlace mode supported by the driver, the VMR initiates a call to the driver-supplied **DdMoCompRender**callback function. In the **DdMoCompRender** call, the **DXVA\_DeinterlaceQueryModeCapsFnCode** constant (defined in *dxva.h*) is set in the **dwFunction** member of DD\_RENDERMOCOMPDATA. The **lpInputData** member of DD\_RENDERMOCOMPDATA passes the input parameters to the driver by pointing to a completed [**DXVA\_DeinterlaceQueryModeCaps**](https://msdn.microsoft.com/library/windows/hardware/ff563956) structure. The driver returns its output through the **lpOutputData** member of DD\_RENDERMOCOMPDATA; **lpOutputData** points to a [**DXVA\_DeinterlaceCaps**](https://msdn.microsoft.com/library/windows/hardware/ff563939) structure.

    If the driver implements a [**DeinterlaceQueryModeCaps**](https://msdn.microsoft.com/library/windows/hardware/ff563946) sample function, the **DdMoCompRender** callback function calls **DeinterlaceQueryModeCaps**.

5.  After the VMR has determined the deinterlacing capabilities of a particular deinterlace mode (for example, bob deinterlacing), it initiates a call to [*DdMoCompCreate*](https://msdn.microsoft.com/library/windows/hardware/ff549656) to create an instance of the deinterlace mode device (for example, the deinterlace bob device). In the *DdMoCompCreate* call, a pointer to the deinterlace mode device GUID is specified in the **lpGuid** member of DD\_CREATEMOCOMPDATA. The deinterlace bob device GUID is defined as follows:

    ```cpp
    DEFINE_GUID(DXVAp_DeinterlaceBobDevice, 0x335aa36e,0x7884,0x43a4,0x9c,0x91,0x7f,0x87,0xfa,0xf3,0xe3,0x7e);
    ```

    If the driver implements a [**DeinterlaceOpenStream**](https://msdn.microsoft.com/library/windows/hardware/ff563935) sample function, the [*DdMoCompCreate*](https://msdn.microsoft.com/library/windows/hardware/ff549656) callback function calls **DeinterlaceOpenStream**.

6.  For each deinterlacing operation, the VMR initiates a call to the driver-supplied [*DdMoCompRender*](https://msdn.microsoft.com/library/windows/hardware/ff550248) callback function. In the *DdMoCompRender* call, the **DXVA\_ProcAmpControlQueryCapsFnCode** constant (defined in *dxva.h*) is set in the **dwFunction** member of DD\_RENDERMOCOMPDATA. The **lpBufferInfo** member of DD\_RENDERMOCOMPDATA points to an array of buffers that describes the destination surface and each input video source sample. The **lpInputData** member of DD\_RENDERMOCOMPDATA passes the input parameters to the driver by pointing to a completed [**DXVA\_DeinterlaceBlt**](https://msdn.microsoft.com/library/windows/hardware/ff563912) structure. The driver does not return any output; that is, the **lpOutputData** member of DD\_RENDERMOCOMPDATA is **NULL**.

    If the driver implements a [**DeinterlaceBlt**](https://msdn.microsoft.com/library/windows/hardware/ff563924) sample function, the **DdMoCompRender** callback function calls **DeinterlaceBlt**.

7.  For each combination deinterlacing and substream compositing operation, the VMR on Microsoft Windows Server 2003 SP1 and later and Windows XP SP2 and later initiates a call to the driver-supplied [*DdMoCompRender*](https://msdn.microsoft.com/library/windows/hardware/ff550248) callback function. In the *DdMoCompRender* call, the **DXVA\_DeinterlaceBltExFnCode** constant (defined in *dxva.h*) is set in the **dwFunction** member of DD\_RENDERMOCOMPDATA. The **lpBufferInfo** member of DD\_RENDERMOCOMPDATA points to an array of buffers that describes the destination surface and the surface for each input video source sample. The **lpInputData** member of DD\_RENDERMOCOMPDATA passes the input parameters to the driver by pointing to a completed [**DXVA\_DeinterlaceBltEx**](https://msdn.microsoft.com/library/windows/hardware/ff563915) structure. The driver does not return any output; that is, the **lpOutputData** member of DD\_RENDERMOCOMPDATA is **NULL**.

    If the driver implements a [**DeinterlaceBltEx**](https://msdn.microsoft.com/library/windows/hardware/ff563927) sample function, the **DdMoCompRender** callback function calls **DeinterlaceBltEx**.

8.  When the VMR no longer needs to perform any more deinterlace operations, the driver-supplied [*DdMoCompDestroy*](https://msdn.microsoft.com/library/windows/hardware/ff549664) callback function is called. The **DestroyMoComp** member of DD\_MOTIONCOMPCALLBACKS points to the callback function.

    If the driver implements a [**DeinterlaceCloseStream**](https://msdn.microsoft.com/library/windows/hardware/ff563931) sample function, the [*DdMoCompDestroy*](https://msdn.microsoft.com/library/windows/hardware/ff549664) callback function calls **DeinterlaceCloseStream**.

9.  The driver then releases any resources used by the deinterlace mode device.

 

 





