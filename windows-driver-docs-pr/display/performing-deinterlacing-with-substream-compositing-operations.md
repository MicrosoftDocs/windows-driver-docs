---
title: Performing Deinterlacing with Substream Compositing Operations
description: Performing Deinterlacing with Substream Compositing Operations
ms.assetid: e6759e88-5cbb-4372-8a92-312f1684b99d
keywords:
- deinterlacing WDK DirectX VA , combining substream compositing
- combining substream compositing WDK DirectX VA
- substream compositing WDK DirectX VA
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# Performing Deinterlacing with Substream Compositing Operations


## <span id="ddk_performing_deinterlacing_with_substream_compositing_operations_gg"></span><span id="DDK_PERFORMING_DEINTERLACING_WITH_SUBSTREAM_COMPOSITING_OPERATIONS_GG"></span>


**This section applies only to Windows Server 2003 SP1 and later, and Windows XP SP2 and later.**

Use the following example code to perform operations that combine deinterlacing the video stream and compositing video substreams on top of the video stream. The example code implements the [*DdMoCompRender*](https://msdn.microsoft.com/library/windows/hardware/ff550248) callback function. The **RenderMoComp** member of the [**DD\_MOTIONCOMPCALLBACKS**](https://msdn.microsoft.com/library/windows/hardware/ff551660) structure points to the callback function. The example code only shows how *DdMoCompRender* is used for deinterlacing with substream compositing operations. For an implementation of *DdMoCompRender* that performs ProcAmp control and deinterlacing operations, see [Performing ProcAmp Control and Deinterlacing Operations](performing-procamp-control-and-deinterlacing-operations.md).

```cpp
DWORD APIENTRY
MOCOMPCB_RENDER(PDD_RENDERMOCOMPDATA lpData)
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
  switch (lpData->dwFunction) {
  case DXVA_DeinterlaceBltExFnCode:
 {  
      DXVA_DeinterlaceBobDeviceClass* pDXVADev =
                        (DXVA_DeinterlaceBobDeviceClass*)pDXVABase;
      DXVA_DeinterlaceBltEx* lpBlt = 
             (DXVA_DeinterlaceBltEx*)lpData->lpInputData;
      LPDDMOCOMPBUFFERINFO lpBuffInfo = lpData->BufferInfo;

      for (DWORD i = 0; i < lpBlt->NumSourceSurfaces; i++) {
          lpBlt->Source[i].lpDDSSrcSurface = 
                          lpBuffInfo[1 + i].lpCompSurface;
      }

       // Part of the Deinterlace DDI.
      lpData->ddRVal = pDXVADev->DeinterlaceBltEx(
                                       lpBlt->rtTarget,
                                       &lpBlt->rcTarget,
                                       lpBlt->BackgroundColor,
                                       lpBlt->DestinationFormat,
                                       lpBlt->DestinationFlags,
                                       lpBuffInfo[0].lpCompSurface,
                                       lpBlt->Source,
                                       lpBlt->NumSourceSurfaces,
                                       lpBlt->Alpha);
      return DDHAL_DRIVER_HANDLED;
  }
  default:
      lpData->ddRVal = E_INVALIDARG;
 return DDHAL_DRIVER_HANDLED;
  }

lpData->ddRVal = DDERR_CURRENTLYNOTAVAIL;
return DDHAL_DRIVER_HANDLED;
}
```

 

 





