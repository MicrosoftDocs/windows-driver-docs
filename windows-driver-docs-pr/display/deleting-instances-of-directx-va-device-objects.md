---
title: Deleting Instances of DirectX VA Device Objects
description: Deleting Instances of DirectX VA Device Objects
ms.assetid: fab8c6eb-97fa-427e-9fb2-6da249d8d97d
keywords:
- deleting instances of DirectX VA device objects
- removing instances of DirectX VA device objects
- DirectX Video Acceleration WDK Windows 2000 display , deleting instances
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# Deleting Instances of DirectX VA Device Objects


## <span id="ddk_deleting_instances_of_directx_va_device_objects_gg"></span><span id="DDK_DELETING_INSTANCES_OF_DIRECTX_VA_DEVICE_OBJECTS_GG"></span>


Use the following example code to delete instances of DirectX VA device objects. This code is an implementation of the [*DdMoCompDestroy*](https://msdn.microsoft.com/library/windows/hardware/ff549664) callback function. The **DestroyMoComp** member of the [**DD\_MOTIONCOMPCALLBACKS**](https://msdn.microsoft.com/library/windows/hardware/ff551660) structure points to the callback function.

```cpp
DWORD APIENTRY
  MOCOMPCB_DESTROY(
    PDD_DESTROYMOCOMPDATA  lpData
    )
{
    // The driver saves the device class object in lpDriverReserved1 
     // during the call to the DdMoCompCreate callback. For more information, 
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
        lpData->ddRVal = S_OK;
        delete pDXVABase;
        break;

    // This is the ProcAmp control device.
 case DXVA_DeviceProcAmpControl:
        {
            DXVA_ProcAmpControlDeviceClass* pDXVADev =
 (DXVA_ProcAmpControlDeviceClass*)pDXVABase;
             // Part of the ProcAmp Control DDI.
            lpData->ddRVal = pDXVADev->ProcAmpControlCloseStream();
            delete pDXVADev;
        }
        break;

    // This is the deinterlace bob device.
 case DXVA_DeviceDeinterlacer:
        {
            DXVA_DeinterlaceBobDeviceClass* pDXVADev =
 (DXVA_DeinterlaceBobDeviceClass*)pDXVABase;
             // Part of the Deinterlace DDI.
            lpData->ddRVal = pDXVADev->DeinterlaceCloseStream();
            delete pDXVADev;
        }
        break;

    // This is the COPP device.
    case DXVA_DeviceCOPP:
        DXVA_COPPDeviceClass* pDXVADev = (DXVA_COPPDeviceClass*)pDXVABase;
        ULONG BytesReturned;
        HANDLE handle = (HANDLE)GetDriverHandleFromPDEV(lpData ->lpDD->lpGbl->dhpdev)
        COPP_IO_InputBuffer InputBuffer;
        InputBuffer.ppThis = &pDXVADev->m_pThis;
        InputBuffer.InputBuffer = NULL;
        InputBuffer.phr = &lpData->ddRVal;
        EngDeviceIoControl(handle,
                           IOCTL_COPP_CloseDevice,
                           &InputBuffer,
                           sizeof(InputBuffer),
                           NULL,
                           0,
                           &BytesReturned);
            delete pDXVADev;
        }
        break;
    }
    return DDHAL_DRIVER_HANDLED;
}
```

 

 





