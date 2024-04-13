---
title: Calling the ProcAmp Control DDI from a User-Mode Component
description: Calling the ProcAmp Control DDI from a User-Mode Component
keywords:
- calling ProcAmp control DDI WDK DirectX VA
- user-mode component calls WDK DirectX VA
- ProcAmp WDK DirectX VA , calling from a user-mode component
ms.date: 04/20/2017
---

# Calling the ProcAmp Control DDI from a User-Mode Component


## <span id="ddk_calling_the_procamp_control_ddi_from_a_user_mode_component_gg"></span><span id="DDK_CALLING_THE_PROCAMP_CONTROL_DDI_FROM_A_USER_MODE_COMPONENT_GG"></span>


A user-mode component, such as the VMR, initiates calls to the [ProcAmp Control DDI](./procamp-control-ddi.md).

So that the VMR can access ProcAmp control functionality, the display driver must implement the [motion compensation callback functions](motion-compensation-callbacks.md), which are defined by members of the [**DD\_MOTIONCOMPCALLBACKS**](/windows/win32/api/ddrawint/ns-ddrawint-dd_motioncompcallbacks) structure.

To simplify driver development, driver writers can use a motion-compensation code template, and implement the [ProcAmp control sample functions](sample-functions-for-procamp-control.md). The motion-compensation template calls its ProcAmp control sample functions to perform ProcAmp control operations. For more information about using a motion-compensation template, see [Example Code for DirectX VA Devices](example-code-for-directx-va-devices.md).

The following steps explain how the VMR initiates calls to the ProcAmp Control DDI:

1.  When the VMR is added to a filter graph, it initiates a call to the driver-supplied [*DdMoCompGetGuids*](/windows/win32/api/ddrawint/nc-ddrawint-pdd_mocompcb_getguids) callback function to retrieve the list of devices supported by the driver. The **GetMoCompGuids** member of DD\_MOTIONCOMPCALLBACKS points to this callback function. For more information about a filter graph, see [KS Minidriver Architecture](../stream/ks-minidriver-architecture.md).

2.  If the deinterlace container device GUID is present, the VMR initiates a call to the [*DdMoCompCreate*](/windows/win32/api/ddrawint/nc-ddrawint-pdd_mocompcb_create) callback function to create an instance of the device. The **CreateMoComp** member of DD\_MOTIONCOMPCALLBACKS points to the callback function. In the **DdMoCompCreate** call, a pointer to the container device GUID is specified in the **lpGuid** member of the [**DD\_CREATEMOCOMPDATA**](/windows/win32/api/ddrawint/ns-ddrawint-dd_createmocompdata) structure. The container device GUID is defined as follows:

    ```cpp
    DEFINE_GUID(DXVA_DeinterlaceContainerDevice, 0x0e85cb93,0x3046,0x4ff0,0xae,0xcc,0xd5,0x8c,0xb5,0xf0,0x35,0xfd);
    ```

3.  To determine capabilities of the ProcAmp control device, the VMR initiates a call to the driver-supplied [*DdMoCompRender*](/windows/win32/api/ddrawint/nc-ddrawint-pdd_mocompcb_render) callback function. The **RenderMoComp** member of DD\_MOTIONCOMPCALLBACKS points to the callback function. In the **DdMoCompRender** call, the **DXVA\_ProcAmpControlQueryCapsFnCode** constant (defined in *dxva.h*) is set in the **dwFunction** member of the [**DD\_RENDERMOCOMPDATA**](/windows/win32/api/ddrawint/ns-ddrawint-dd_rendermocompdata) structure. The **lpInputData** member of DD\_RENDERMOCOMPDATA passes the input parameters to the driver by pointing to a [**DXVA\_VideoDesc**](/windows-hardware/drivers/ddi/dxva/ns-dxva-_dxva_videodesc) structure. The driver returns its output through the **lpOutputData** member of DD\_RENDERMOCOMPDATA; **lpOutputData** points to a [**DXVA\_ProcAmpControlCaps**](/windows-hardware/drivers/ddi/dxva/ns-dxva-_dxva_procampcontrolcaps) structure.

    If the driver implements a [**ProcAmpControlQueryCaps**](./dxva-deinterlacecontainerdeviceclass-procampcontrolquerycaps.md) sample function, the [*DdMoCompRender*](/windows/win32/api/ddrawint/nc-ddrawint-pdd_mocompcb_render) callback function calls **ProcAmpControlQueryCaps**.

4.  For each ProcAmp adjustment property supported by the hardware, the VMR initiates a call to the driver-supplied **DdMoCompRender**callback function. In the **DdMoCompRender** call, the **DXVA\_ProcAmpControlQueryCapsFnCode** constant (defined in *dxva.h*) is set in the **dwFunction** member of DD\_RENDERMOCOMPDATA. The **lpInputData** member of DD\_RENDERMOCOMPDATA passes the input parameters to the driver by pointing to a completed [**DXVA\_ProcAmpControlQueryRange**](/windows-hardware/drivers/ddi/dxva/ns-dxva-_dxva_procampcontrolqueryrange) structure. The driver returns its output through the **lpOutputData** member of DD\_RENDERMOCOMPDATA; **lpOutputData** points to a [**DXVA\_VideoPropertyRange**](/windows-hardware/drivers/ddi/dxva/ns-dxva-_dxva_videopropertyrange) structure.

    If the driver implements a [**ProcAmpControlQueryRange**](./dxva-deinterlacecontainerdeviceclass-procampcontrolqueryrange.md) sample function, the [*DdMoCompRender*](/windows/win32/api/ddrawint/nc-ddrawint-pdd_mocompcb_render) callback function calls **ProcAmpControlQueryRange**.

5.  After the VMR has determined the ProcAmp adjustment capabilities of the hardware, it initiates a call to [*DdMoCompCreate*](/windows/win32/api/ddrawint/nc-ddrawint-pdd_mocompcb_create) to create an instance of the ProcAmp control device. In the *DdMoCompCreate* call, a pointer to the ProcAmp control device GUID is specified in the **lpGuid** member of DD\_CREATEMOCOMPDATA. The ProcAmp control device GUID is defined as follows:

    ```cpp
    DEFINE_GUID(DXVA_ProcAmpControlDevice, 0x9f200913,0x2ffd,0x4056,0x9f,0x1e,0xe1,0xb5,0x08,0xf2,0x2d,0xcf); 
    ```

    If the driver implements a [**ProcAmpControlOpenStream**](./dxva-procampcontroldeviceclass-procampcontrolopenstream.md) sample function, the [*DdMoCompCreate*](/windows/win32/api/ddrawint/nc-ddrawint-pdd_mocompcb_create) callback function calls **ProcAmpControlOpenStream**.

6.  For each ProcAmp adjusting operation, the VMR initiates a call to the driver-supplied **DdMoCompRender**callback function. In the **DdMoCompRender** call, the **DXVA\_ProcAmpControlQueryCapsFnCode** constant (defined in *dxva.h*) is set in the **dwFunction** member of [**DD\_RENDERMOCOMPDATA**](/windows/win32/api/ddrawint/ns-ddrawint-dd_rendermocompdata). The **lpBufferInfo** member of DD\_RENDERMOCOMPDATA points to an array of two buffers that describe the destination and source surfaces. The **lpInputData** member of DD\_RENDERMOCOMPDATA passes the input parameters to the driver by pointing to a completed [**DXVA\_ProcAmpControlBlt**](/windows-hardware/drivers/ddi/dxva/ns-dxva-_dxva_procampcontrolblt) structure. The driver does not return any output; that is, the **lpOutputData** member of DD\_RENDERMOCOMPDATA is **NULL**.

    If the driver implements a [**ProcAmpControlBlt**](./dxva-procampcontroldeviceclass-procampcontrolblt.md) sample function, the **DdMoCompRender** callback function calls **ProcAmpControlBlt**.

7.  When the VMR no longer needs to perform any more ProcAmp control operations, the driver-supplied [*DdMoCompDestroy*](/windows/win32/api/ddrawint/nc-ddrawint-pdd_mocompcb_destroy) callback function is called. The **DestroyMoComp** member of DD\_MOTIONCOMPCALLBACKS points to the callback function.

    If the driver implements a [**ProcAmpControlCloseStream**](./dxva-procampcontroldeviceclass-procampcontrolclosestream.md) sample function, the **DdMoCompDestroy** callback function calls **ProcAmpControlCloseStream**.

8.  The driver releases any resources used by the ProcAmp control device.

 

