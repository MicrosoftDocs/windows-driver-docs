---
title: Performing ProcAmp Control and Deinterlacing Operations
description: Performing ProcAmp Control and Deinterlacing Operations
ms.assetid: efef9bb0-4e98-47f9-80bd-e07c8d3b22e5
keywords:
- ProcAmp WDK DirectX VA , deinterlacing operations
- deinterlacing WDK DirectX VA , ProcAmp
ms.author: windows-driver-content
ms.date: 04/20/2017
ms.topic: article
ms.prod: windows-hardware
ms.technology: windows-devices
---

# Performing ProcAmp Control and Deinterlacing Operations


## <span id="ddk_performing_procamp_control_and_deinterlacing_operations_gg"></span><span id="DDK_PERFORMING_PROCAMP_CONTROL_AND_DEINTERLACING_OPERATIONS_GG"></span>


Use the following example code to perform ProcAmp control and deinterlacing operations. This code is an implementation of the [*DdMoCompRender*](https://msdn.microsoft.com/library/windows/hardware/ff550248) callback function. The **RenderMoComp** member of the [**DD\_MOTIONCOMPCALLBACKS**](https://msdn.microsoft.com/library/windows/hardware/ff551660) structure points to the callback function.

```
DWORD APIENTRY
  MOCOMPCB_RENDER(
    PDD_RENDERMOCOMPDATA  lpData
    )
{
    // The driver saves the device class object in lpDriverReserved1 
     // during the DdMoCompCreate callback. For more information, 
     // see Creating Instances of DirectX VA Device Objects.
 DXVA_DeviceBaseClass* pDXVABase =
         (DXVA_DeviceBaseClass*)lpData->lpMoComp->lpDriverReserved1;
 if (pDXVABase == NULL) {
        lpData->ddRVal = E_POINTER;
        return DDHAL_DRIVER_HANDLED;
    }
    // Process according to the device type in the class object.
     // For more information, see Defining DirectX VA Device Classes.
    switch (pDXVABase->m_DeviceType) {
    // This is the deinterlace container device.
    case DXVA_DeviceContainer:
        switch (lpData->dwFunction) {
        case DXVA_DeinterlaceQueryAvailableModesFnCode:
            {
                DXVA_DeinterlaceContainerDeviceClass* pDXVADev =
                    (DXVA_DeinterlaceContainerDeviceClass*)pDXVABase;

                DXVA_DeinterlaceQueryAvailableModes* pQAM =
           (DXVA_DeinterlaceQueryAvailableModes*)lpData->lpOutputData;

                 // Part of the Deinterlace DDI.
                lpData->ddRVal = 
                             pDXVADev->DeinterlaceQueryAvailableModes(
                                (DXVA_VideoDesc*)lpData->lpInputData,
                                 &pQAM->NumGuids,
                                 &pQAM->Guids[0]);
            }
            return DDHAL_DRIVER_HANDLED;

        case DXVA_DeinterlaceQueryModeCapsFnCode:
            {
                DXVA_DeinterlaceContainerDeviceClass* pDXVADev =
                    (DXVA_DeinterlaceContainerDeviceClass*)pDXVABase;

                DXVA_DeinterlaceQueryModeCaps* pQMC =
                 (DXVA_DeinterlaceQueryModeCaps*)lpData->lpInputData;

                DXVA_DeinterlaceCaps*pDC =
                    (DXVA_DeinterlaceCaps*)lpData->lpOutputData;

                 // Part of the Deinterlace DDI.
                lpData->ddRVal = pDXVADev->DeinterlaceQueryModeCaps(
                                    &pQMC->Guid,
                                    &pQMC->VideoDesc,
                                    pDC);
            }
            return DDHAL_DRIVER_HANDLED;

        case DXVA_ProcAmpControlQueryCapsFnCode:
            {
                DXVA_DeinterlaceContainerDeviceClass* pDXVADev =
                    (DXVA_DeinterlaceContainerDeviceClass*)pDXVABase;

                DXVA_VideoDesc* pVideoDesc =
                    (DXVA_VideoDesc *)lpData->lpInputData;

 DXVA_ProcAmpControlCaps* pCC =
                    (DXVA_ProcAmpControlCaps*)lpData->lpOutputData;

  // Part of the ProcAmp Control DDI.
 lpData->ddRVal = pDXVADev->ProcAmpControlQueryCaps(
                                    pVideoDesc,
 pCC);
            }
            return DDHAL_DRIVER_HANDLED;

        case DXVA_ProcAmpControlQueryRangeFnCode:
            {
                DXVA_DeinterlaceContainerDeviceClass* pDXVADev =
 (DXVA_DeinterlaceContainerDeviceClass*)pDXVABase;

                DXVA_ProcAmpControlQueryRange* pccqr =
                (DXVA_ProcAmpControlQueryRange *)lpData->lpInputData;

                DXVA_VideoPropertyRange*pPR =
 (DXVA_VideoPropertyRange*)lpData->lpOutputData;

                  // Part of the ProcAmp Control DDI.
 lpData->ddRVal = pDXVADev->ProcAmpControlQueryRange(
                                    pccqr->ProcAmpControlProp,
 &pccqr->VideoDesc,
                                    pPR);
            }
            return DDHAL_DRIVER_HANDLED;

  default:
            lpData->ddRVal = E_INVALIDARG;
 return DDHAL_DRIVER_HANDLED;
        }
        break;
    // This is the ProcAmp control device.
    case DXVA_DeviceProcAmpControl:
        switch (lpData->dwFunction) {
 case DXVA_ProcAmpControlBltFnCode:
            {
                DXVA_ProcAmpControlDeviceClass* pDXVADev =
                    (DXVA_ProcAmpControlDeviceClass*)pDXVABase;

                DXVA_ProcAmpControlBlt* lpBlt = 
                      (DXVA_ProcAmpControlBlt*)lpData->lpInputData;
                LPDDMOCOMPBUFFERINFO lpBuffInfo = lpData->lpBufferInfo;
  // Part of the ProcAmp Control DDI.
                lpData->ddRVal = pDXVADev->ProcAmpControlBlt(
                                         lpBuffInfo[0].lpCompSurface,
                                         lpBuffInfo[1].lpCompSurface,
                                         lpBlt);
            }
            return DDHAL_DRIVER_HANDLED;

 default:
            lpData->ddRVal = E_INVALIDARG;
 return DDHAL_DRIVER_HANDLED;
        }
        break;
    // This is the deinterlace bob device.
    case DXVA_DeviceDeinterlacer:
        switch (lpData->dwFunction) {
        case DXVA_DeinterlaceBltFnCode:
            {
                DXVA_DeinterlaceBobDeviceClass* pDXVADev =
                        (DXVA_DeinterlaceBobDeviceClass*)pDXVABase;

                DXVA_DeinterlaceBlt* lpBlt = 
                         (DXVA_DeinterlaceBlt*)lpData->lpInputData;
                LPDDMOCOMPBUFFERINFO lpBuffInfo = lpData->lpBufferInfo;

                for (DWORD i = 0; i < lpBlt->NumSourceSurfaces; i++) {
                    lpBlt->Source[i].lpDDSSrcSurface = 
                                      lpBuffInfo[1 + i].lpCompSurface;
                }
                 // Part of the Deinterlace DDI.
                lpData->ddRVal = pDXVADev->DeinterlaceBlt(
                                          lpBlt->rtTarget,
                                          &lpBlt->DstRect,
                                          lpBuffInfo[0].lpCompSurface,
                                          &lpBlt->SrcRect,
                                          lpBlt->Source,
                                          lpBlt->NumSourceSurfaces,
                                          lpBlt->Alpha);
            }
            return DDHAL_DRIVER_HANDLED;

        default:
            lpData->ddRVal = E_INVALIDARG;
            return DDHAL_DRIVER_HANDLED;
        }
        break;
    }

    lpData->ddRVal = DDERR_CURRENTLYNOTAVAIL;
    return DDHAL_DRIVER_HANDLED;
}
```

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20[display\display]:%20Performing%20ProcAmp%20Control%20and%20Deinterlacing%20Operations%20%20RELEASE:%20%282/10/2017%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")




