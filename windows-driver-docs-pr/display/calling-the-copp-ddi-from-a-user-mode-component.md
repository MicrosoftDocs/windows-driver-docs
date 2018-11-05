---
title: Calling the COPP DDI from a User-Mode Component
description: Calling the COPP DDI from a User-Mode Component
ms.assetid: f7ce10d3-bf52-4bfd-9ae8-63213a59d1c9
keywords:
- calling COPP DDI WDK DirectX VA
- user-mode component calls WDK DirectX VA
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# Calling the COPP DDI from a User-Mode Component


## <span id="ddk_calling_the_copp_ddi_from_a_user_mode_component_gg"></span><span id="DDK_CALLING_THE_COPP_DDI_FROM_A_USER_MODE_COMPONENT_GG"></span>


This section applies only to Windows Server 2003 SP1 and later, and Windows XP SP2 and later.

A user-mode component, such as the VMR, initiates calls to the COPP DDI.

So that the VMR can notify the video miniport driver to apply protection to the graphics adapter's video output, the display driver must implement the [motion compensation callback functions](motion-compensation-callbacks.md), which are defined by members of the [**DD\_MOTIONCOMPCALLBACKS**](https://msdn.microsoft.com/library/windows/hardware/ff551660) structure.

To simplify driver development, driver writers can use a motion-compensation code template and implement COPP IOCTLs and the [COPP sample functions](sample-functions-for-copp.md). The display driver and video miniport driver use the COPP IOCTLs to communicate. For more information, see [Calling the COPP DDI from the Display Driver](calling-the-copp-ddi-from-the-display-driver.md). The motion-compensation code template initiates calls to the COPP sample functions. For more information about using a motion-compensation code template, see [Example Code for DirectX VA Devices](example-code-for-directx-va-devices.md).

The following steps explain how the VMR initiates calls to the COPP DDI:

1.  When the VMR is added to a filter graph, it initiates a call to the display driver-supplied [*DdMoCompGetGuids*](https://msdn.microsoft.com/library/windows/hardware/ff550236) callback function to retrieve the list of devices supported by the driver. The **GetMoCompGuids** member of the DD\_MOTIONCOMPCALLBACKS structure points to this callback function. For more information about a filter graph, see [KS Minidriver Architecture](https://msdn.microsoft.com/library/windows/hardware/ff567656).

2.  If the DirectX VA COPP device GUID is present, then the VMR initiates a call to the [*DdMoCompCreate*](https://msdn.microsoft.com/library/windows/hardware/ff549656) callback function to initialize a COPP device on the current video session. The **CreateMoComp** member of DD\_MOTIONCOMPCALLBACKS points to the callback function. In the *DdMoCompCreate* call, a pointer to the COPP device GUID is specified in the **lpGuid** member of the [**DD\_CREATEMOCOMPDATA**](https://msdn.microsoft.com/library/windows/hardware/ff550529) structure. The COPP device GUID is defined as follows:

    ```cpp
    DEFINE_GUID(DXVA_COPPDevice, 0xd2457add,0x8999,0x45ed,0x8a,0x8a,0xd1,0xaa,0x04,0x7b,0xa4,0xd5);
    ```

    The display driver must communicate with the video miniport driver by using a COPP IOCTL. If the video miniport driver implements a [*COPPOpenVideoSession*](https://msdn.microsoft.com/library/windows/hardware/ff539650) sample function, then the [*DdMoCompCreate*](https://msdn.microsoft.com/library/windows/hardware/ff549656) callback function initiates the call to **COPPOpenVideoSession**.

3.  To determine the length of the variable-length graphics hardware certificate that should be used for the current video session, the VMR initiates a call to the display driver-supplied [*DdMoCompRender*](https://msdn.microsoft.com/library/windows/hardware/ff550248) callback function. The **RenderMoComp** member of [**DD\_MOTIONCOMPCALLBACKS**](https://msdn.microsoft.com/library/windows/hardware/ff551660) points to the callback function. In the **DdMoCompRender** call, the **dwFunction** member of [**DD\_RENDERMOCOMPDATA**](https://msdn.microsoft.com/library/windows/hardware/ff551693) is set to the value **DXVA\_COPPGetCertificateLengthFnCode** (defined in *dxva.h*). The display driver does not receive any input in this call; that is, the **lpInputData** member of DD\_RENDERMOCOMPDATA is **NULL**. The display driver returns the length of the certificate through the **lpOutputData** member of DD\_RENDERMOCOMPDATA; **lpOutputData** points to a DWORD data type.

    The display driver must communicate with the video miniport driver by using a COPP IOCTL. If the video miniport driver implements a [*COPPGetCertificateLength*](https://msdn.microsoft.com/library/windows/hardware/ff539644) sample function, then the **DdMoCompRender** callback function initiates the call to *COPPGetCertificateLength*.

4.  To retrieve the certificate used by the graphics hardware, the VMR initiates a call to the display driver-supplied **DdMoCompRender** callback function. In the **DdMoCompRender** call, the **dwFunction** member of DD\_RENDERMOCOMPDATA is set to the value **DXVA\_COPPKeyExchangeFnCode** (defined in *dxva.h*). The display driver does not receive any input in this call; that is, the **lpInputData** member of DD\_RENDERMOCOMPDATA is **NULL**. The **lpBufferInfo** member of DD\_RENDERMOCOMPDATA points to a single RGB32 system memory surface that contains the space required for the display driver to store the certificate. The display driver returns the 128-bit random number that it generated through the **lpOutputData** member of DD\_RENDERMOCOMPDATA.

    The display driver must communicate with the video miniport driver by using a COPP IOCTL. If the video miniport driver implements a [*COPPKeyExchange*](https://msdn.microsoft.com/library/windows/hardware/ff539646) sample function, then the [*DdMoCompRender*](https://msdn.microsoft.com/library/windows/hardware/ff550248) callback function initiates the call to *COPPKeyExchange*.

5.  To set the current video session to protected mode, the VMR initiates a call to the display driver-supplied [*DdMoCompRender*](https://msdn.microsoft.com/library/windows/hardware/ff550248) callback function. In the *DdMoCompRender* call, the **dwFunction** member of DD\_RENDERMOCOMPDATA is set to the value **DXVA\_COPPSequenceStartFnCode** (defined in *dxva.h*). The **lpInputData** member of DD\_RENDERMOCOMPDATA passes the input command and status sequence start codes to the display driver by pointing to a completed [**DXVA\_COPPSignature**](https://msdn.microsoft.com/library/windows/hardware/ff563150) structure. The display driver does not return any output; that is, the **lpOutputData** member of DD\_RENDERMOCOMPDATA is **NULL**.

    The display driver must communicate with the video miniport driver by using a COPP IOCTL. If the video miniport driver implements a [*COPPSequenceStart*](https://msdn.microsoft.com/library/windows/hardware/ff540421) sample function, then the [*DdMoCompRender*](https://msdn.microsoft.com/library/windows/hardware/ff550248) callback function initiates the call to **COPPSequenceStart**.

6.  To set the protection level on the physical connector associated with the DirectX VA COPP device, the VMR initiates a call to the display driver-supplied [*DdMoCompRender*](https://msdn.microsoft.com/library/windows/hardware/ff550248) callback function. In the *DdMoCompRender* call, the **dwFunction** member of DD\_RENDERMOCOMPDATA is set to the value **DXVA\_COPPCommandFnCode** (defined in *dxva.h*). The **lpInputData** member of DD\_RENDERMOCOMPDATA passes the input parameters to the display driver by pointing to a completed [**DXVA\_COPPCommand**](https://msdn.microsoft.com/library/windows/hardware/ff563141) structure. The display driver does not return any output; that is, the **lpOutputData** member of DD\_RENDERMOCOMPDATA is **NULL**.

    The display driver must communicate with the video miniport driver by using a COPP IOCTL. If the video miniport driver implements a [*COPPCommand*](https://msdn.microsoft.com/library/windows/hardware/ff539642) sample function, then the [*DdMoCompRender*](https://msdn.microsoft.com/library/windows/hardware/ff550248) callback function initiates the call to *COPPCommand*.

7.  To retrieve protection information regarding the physical connector being used, the VMR initiates a call to the display driver-supplied [*DdMoCompRender*](https://msdn.microsoft.com/library/windows/hardware/ff550248) callback function. In the *DdMoCompRender* call, the **dwFunction** member of DD\_RENDERMOCOMPDATA is set to the value **DXVA\_COPPQueryStatusFnCode** (defined in *dxva.h*). The **lpInputData** member of DD\_RENDERMOCOMPDATA passes the input parameters to the display driver by pointing to a completed [**DXVA\_COPPStatusInput**](https://msdn.microsoft.com/library/windows/hardware/ff563899) structure. The display driver returns its output through the **lpOutputData** member of DD\_RENDERMOCOMPDATA; **lpOutputData** points to a [**DXVA\_COPPStatusOutput**](https://msdn.microsoft.com/library/windows/hardware/ff563903) structure.

    The display driver must communicate with the video miniport driver by using a COPP IOCTL. If the video miniport driver implements a [*COPPQueryStatus*](https://msdn.microsoft.com/library/windows/hardware/ff539652) sample function, then the [*DdMoCompRender*](https://msdn.microsoft.com/library/windows/hardware/ff550248) callback function initiates the call to *COPPQueryStatus*.

8.  When the VMR no longer needs to perform any more COPP operations, the display driver-supplied [*DdMoCompDestroy*](https://msdn.microsoft.com/library/windows/hardware/ff549664) callback function is called. The **DestroyMoComp** member of DD\_MOTIONCOMPCALLBACKS points to the callback function.

    The display driver must communicate with the video miniport driver by using a COPP IOCTL. If the video miniport driver implements a [*COPPCloseVideoSession*](https://msdn.microsoft.com/library/windows/hardware/ff539638) sample function, then the **DdMoCompDestroy** callback function initiates the call to *COPPCloseVideoSession*.

9.  The drivers then release any resources used by the DirectX VA COPP device.

 

 





