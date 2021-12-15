---
title: Performing COPP Operations Example
description: An example for performing COPP Operations
keywords:
- copy protection WDK COPP , COPP operation example code
- video copy protection WDK COPP , COPP operation example code
- COPP WDK DirectX VA , operation example code
- protected video WDK COPP , COPP operation example code
ms.date: 04/20/2017
---

# Performing COPP Operations Example


## <span id="ddk_performing_copp_operations_gg"></span><span id="DDK_PERFORMING_COPP_OPERATIONS_GG"></span>


**This section applies only to Windows Server 2003 SP1 and later, and Windows XP SP2 and later.**

Use the following example code to perform operations over the Certified Output Protection Protocol (COPP). The example code implements the [*DdMoCompRender*](/windows/win32/api/ddrawint/nc-ddrawint-pdd_mocompcb_render) callback function. The **RenderMoComp** member of the [**DD\_MOTIONCOMPCALLBACKS**](/windows/win32/api/ddrawint/ns-ddrawint-dd_motioncompcallbacks) structure points to the callback function. The example code only shows how *DdMoCompRender* is used for COPP operations. For an implementation of *DdMoCompRender* that performs ProcAmp control and deinterlacing operations, see [Performing ProcAmp Control and Deinterlacing Operations](performing-procamp-control-and-deinterlacing-operations.md) and [Performing Deinterlacing with Substream Compositing Operations](performing-deinterlacing-with-substream-compositing-operations.md).

```cpp
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
    // This is the COPP device.
    case DXVA_DeviceCOPP:
        {
            DXVA_COPPDeviceClass* pDXVACopp =
                        (DXVA_COPPDeviceClass*)pDXVABase;
            ULONG BytesReturned;
            HANDLE handle = (HANDLE)GetDriverHandleFromPDEV(lpData->lpDD->lpGbl->dhpdev)
            COPP_IO_InputBuffer InputBuffer;
            InputBuffer.ppThis = &pDXVACopp->m_pThis;
            InputBuffer.phr = &lpData->ddRVal;
            switch (lpData->dwFunction) {
            case DXVA_COPPGetCertificateLengthFnCode:
                if (lpData->dwOutputDataSize < sizeof(ULONG)) {
 lpData->ddRVal = E_INVALIDARG;
                }
                else { 
 InputBuffer.InputBuffer = NULL;
                    EngDeviceIoControl(handle,
                                      IOCTL_COPP_GetCertificateLength,
                                      &InputBuffer,
                                      sizeof(InputBuffer),
                                      lpData->lpOutputData,
                                      lpData->dwOutputDataSize,
                                      &BytesReturned);
                }
                break;
            case DXVA_COPPKeyExchangeFnCode:
                if (lpData->dwOutputDataSize < sizeof(DXVA_COPPKeyExchangeOutput)) {
  lpData->ddRVal = E_INVALIDARG;
                }
                else {
 InputBuffer.InputBuffer = NULL;
                    DD_SURFACE_LOCAL* lpCompSurf =
                        lpData->lpBufferInfo[0].lpCompSurface;
                    InputBuffer.InputBuffer = (PVOID)lpCompSurf->lpGbl->fpVidMem;
                    EngDeviceIoControl(handle
                                       IOCTL_COPP_KeyExchange,
                                       &InputBuffer,
                                        sizeof(InputBuffer),
                                       lpData->lpOutputData,
                                       lpData->dwOutputDataSize,
                                       &BytesReturned);
                }
                break;
            case DXVA_COPPSequenceStartFnCode:
                if (lpData->dwInputDataSize < sizeof(DXVA_COPPSignature)) {
 lpData->ddRVal = E_INVALIDARG;
                }
                else {
                    InputBuffer.InputBuffer = lpData->lpInputData;
                    EngDeviceIoControl(handle,
 IOCTL_COPP_StartSequence,
                                       &InputBuffer,
                                       sizeof(InputBuffer),
                                       NULL,
                                       0,
                                       &BytesReturned);
                }
                break;
            case DXVA_COPPCommandFnCode:
                if (lpData->dwInputDataSize < sizeof(DXVA_COPPCommand)) {
 lpData->ddRVal = E_INVALIDARG;
                }
                else {
                    InputBuffer.InputBuffer = lpData->lpInputData;
                    EngDeviceIoControl(handle,
 IOCTL_COPP_Command,
                                       &InputBuffer,
                                       sizeof(InputBuffer),
                                       NULL,
                                       0,
                                       &BytesReturned);
                }
                break;
            case DXVA_COPPQueryStatusFnCode:
                if (lpData->dwInputDataSize < sizeof(DXVA_COPPStatusInput) ||
                    lpData->dwOutputDataSize < sizeof(DXVA_COPPStatusOutput)) {
 lpData->ddRVal = E_INVALIDARG;
                }
                else {
                    InputBuffer.InputBuffer = lpData->lpInputData;
                    EngDeviceIoControl(handle,
 IOCTL_COPP_Status,
                                       &InputBuffer,
                                       sizeof(InputBuffer),
                                       lpData->lpOutputData,
                                       lpData->dwOutputDataSize,
                                       &BytesReturned);
 }
                break;
            default:
                lpData->ddRVal = E_INVALIDARG;
 break;
            }
            break;
        }
    }
    return DDHAL_DRIVER_HANDLED;
}
```

 

