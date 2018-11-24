---
title: Creating Instances of DirectX VA Device Objects
description: Creating Instances of DirectX VA Device Objects
ms.assetid: af98ab63-33bb-4294-a902-695ea278654e
keywords:
- DirectX Video Acceleration WDK Windows 2000 display , creating instances
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# Creating Instances of DirectX VA Device Objects


## <span id="ddk_creating_instances_of_directx_va_device_objects_gg"></span><span id="DDK_CREATING_INSTANCES_OF_DIRECTX_VA_DEVICE_OBJECTS_GG"></span>


Use the following example code to create instances of DirectX VA device objects. This code is an implementation of the [*DdMoCompCreate*](https://msdn.microsoft.com/library/windows/hardware/ff549656) callback function. The **CreateMoComp** member of the [**DD\_MOTIONCOMPCALLBACKS**](https://msdn.microsoft.com/library/windows/hardware/ff551660) structure points to the callback function.

```cpp
// Determine that the passed in GUID is valid. 
BOOL
ValidDXVAGuid(LPGUID lpGuid) {
     // See Retrieving DirectX VA Devices, for more information 
    // about g_dwDXVANumSupportedGUIDs and g_DXVASupportedGUIDs[].
    for (DWORD i = 0; i < g_dwDXVANumSupportedGUIDs; i++) {
        if (*g_DXVASupportedGUIDs[i] == *lpGuid) {
            return TRUE;
        }
    }
    return FALSE;
}

DWORD APIENTRY
  MOCOMPCB_CREATE(
    PDD_CREATEMOCOMPDATA  lpData
    )
{
    // Determine that the passed in GUID is valid. 
 if (!ValidDXVAGuid(lpData->lpGuid)) {
        lpData->ddRVal = E_INVALIDARG;
 return DDHAL_DRIVER_HANDLED;
    }
    // Determine that this is the deinterlace container device GUID.
    if (*lpData->lpGuid == DXVA_DeinterlaceContainerDevice) {
        DXVA_DeinterlaceContainerDeviceClass* lpDev =
            new DXVA_DeinterlaceContainerDeviceClass(*lpData->lpGuid,
                                               DXVA_DeviceContainer);
        if (lpDev) {
            lpData->ddRVal = DD_OK;
        }
        else {
            lpData->ddRVal = E_OUTOFMEMORY;
        }
        lpData->lpMoComp->lpDriverReserved1 = 
                                 (LPVOID)(DXVA_DeviceBaseClass*)lpDev;
        return DDHAL_DRIVER_HANDLED;
    }
    //
    // Determine that this is the ProcAmp control device GUID.
 if (*lpData->lpGuid == DXVA_ProcAmpControlDevice) {
        DXVA_ProcAmpControlDeviceClass* lpDev =
                  new DXVA_ProcAmpControlDeviceClass(*lpData->lpGuid,
 DXVA_DeviceProcAmpControl);
        if (lpDev) {
            LPDXVA_VideoDesc lpVideoDescription = 
                                    (LPDXVA_VideoDesc)lpData->lpData;
             // Part of the ProcAmp Control DDI.
            lpData->ddRVal = lpDev->ProcAmpControlOpenStream(
                                                 lpVideoDescription);
            if (lpData->ddRVal != DD_OK) {
                delete lpDev;
                lpDev = NULL;
            }
        }
        else lpData->ddRVal = E_OUTOFMEMORY;
        lpData->lpMoComp->lpDriverReserved1 = 
                                (LPVOID)(DXVA_DeviceBaseClass*)lpDev;
        return DDHAL_DRIVER_HANDLED;
    }

    // Determine that this is the deinterlace bob device GUID
    if (*lpData->lpGuid == DXVA_DeinterlaceBobDevice) {
        DXVA_DeinterlaceBobDeviceClass* lpDev =
 new DXVA_DeinterlaceBobDeviceClass(*lpData->lpGuid,
                                            DXVA_DeviceDeinterlacer);
 if (lpDev) {
            LPDXVA_VideoDesc lpVideoDescription = 
                                    (LPDXVA_VideoDesc)lpData->lpData;
             // Part of the Deinterlace DDI.
            lpData->ddRVal = lpDev->DeinterlaceOpenStream( 
                                                 lpVideoDescription);
            if (lpData->ddRVal != DD_OK) {
                delete lpDev;
                lpDev = NULL;
            }
        }
        else lpData->ddRVal = E_OUTOFMEMORY;
        lpData->lpMoComp->lpDriverReserved1 = 
                                (LPVOID)(DXVA_DeviceBaseClass*)lpDev;
        return DDHAL_DRIVER_HANDLED;
    }

    // Determine that this is the COPP device GUID
    if (*lpData->lpGuid == DXVA_COPPDevice) {
        DXVA_COPPDeviceClass* lpDev =
            new DXVA_COPPDeviceClass(*lpData->lpGuid, DXVA_DeviceCOPP);
        if (lpDev) {
            // Determine the correct DevID of the graphics device that 
            // the COPP device is attached to.
            ULONG DevID = 0;
            ULONG BytesReturned;
            COPP_IO_InputBuffer InputBuffer;
            InputBuffer.ppThis = &lpDev->m_pThis;
            InputBuffer.InputBuffer = &DevID;
            // Pass, to the video miniport driver, a 
            // pointer to the error variable.
            InputBuffer.phr = &lpData->ddRVal;
            EngDeviceIoControl(
                (HANDLE)GetDriverHandleFromPDEV(lpData->lpDD->lpGbl->dhpdev),
                               IOCTL_COPP_OpenDevice,
                               &InputBuffer,
                               sizeof(InputBuffer),
                               NULL,
                               0,
                               &BytesReturned);
            if (lpData->ddRVal != DD_OK) {
                delete lpDev;
                lpDev = NULL;
            }
        }
        else {
            lpData->ddRVal = E_OUTOFMEMORY;
        }
        lpData->lpMoComp->lpDriverReserved1 = (LPVOID)(DXVA_DeviceBaseClass*)lpDev;
        return DDHAL_DRIVER_HANDLED;
    }
    lpData->ddRVal = DDERR_CURRENTLYNOTAVAIL;
    return DDHAL_DRIVER_HANDLED;
}
```

 

 





