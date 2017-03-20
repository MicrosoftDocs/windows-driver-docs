---
title: Performing Deinterlacing with Substream Compositing Operations
description: Performing Deinterlacing with Substream Compositing Operations
ms.assetid: e6759e88-5cbb-4372-8a92-312f1684b99d
keywords: ["deinterlacing WDK DirectX VA , combining substream compositing", "combining substream compositing WDK DirectX VA", "substream compositing WDK DirectX VA"]
---

# Performing Deinterlacing with Substream Compositing Operations


## <span id="ddk_performing_deinterlacing_with_substream_compositing_operations_gg"></span><span id="DDK_PERFORMING_DEINTERLACING_WITH_SUBSTREAM_COMPOSITING_OPERATIONS_GG"></span>


**This section applies only to Windows Server 2003 SP1 and later, and Windows XP SP2 and later.**

Use the following example code to perform operations that combine deinterlacing the video stream and compositing video substreams on top of the video stream. The example code implements the [*DdMoCompRender*](https://msdn.microsoft.com/library/windows/hardware/ff550248) callback function. The **RenderMoComp** member of the [**DD\_MOTIONCOMPCALLBACKS**](https://msdn.microsoft.com/library/windows/hardware/ff551660) structure points to the callback function. The example code only shows how *DdMoCompRender* is used for deinterlacing with substream compositing operations. For an implementation of *DdMoCompRender* that performs ProcAmp control and deinterlacing operations, see [Performing ProcAmp Control and Deinterlacing Operations](performing-procamp-control-and-deinterlacing-operations.md).

```
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

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20[display\display]:%20Performing%20Deinterlacing%20with%20Substream%20Compositing%20Operations%20%20RELEASE:%20%282/10/2017%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")




