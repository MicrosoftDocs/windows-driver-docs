---
title: Deleting Instances of DirectX VA Device Objects
description: Deleting Instances of DirectX VA Device Objects
ms.assetid: fab8c6eb-97fa-427e-9fb2-6da249d8d97d
keywords:
- deleting instances of DirectX VA device objects
- removing instances of DirectX VA device objects
- DirectX Video Acceleration WDK Windows 2000 display , deleting instances
ms.author: windowsdriverdev
ms.date: 04/20/2017
ms.topic: article
ms.prod: windows-hardware
ms.technology: windows-devices
---

# Deleting Instances of DirectX VA Device Objects


## <span id="ddk_deleting_instances_of_directx_va_device_objects_gg"></span><span id="DDK_DELETING_INSTANCES_OF_DIRECTX_VA_DEVICE_OBJECTS_GG"></span>


Use the following example code to delete instances of DirectX VA device objects. This code is an implementation of the [*DdMoCompDestroy*](https://msdn.microsoft.com/library/windows/hardware/ff549664) callback function. The **DestroyMoComp** member of the [**DD\_MOTIONCOMPCALLBACKS**](https://msdn.microsoft.com/library/windows/hardware/ff551660) structure points to the callback function.

```
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

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20[display\display]:%20Deleting%20Instances%20of%20DirectX%20VA%20Device%20Objects%20%20RELEASE:%20%282/10/2017%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")




