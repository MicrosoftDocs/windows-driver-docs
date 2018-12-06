---
title: COPP Video Miniport Driver Key Exchange Template Code
description: COPP Video Miniport Driver Key Exchange Template Code
ms.assetid: 5c0de949-e460-4f01-a762-706eac3abee0
keywords:
- key exchange WDK COPP
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# COPP Video Miniport Driver Key Exchange Template Code


## <span id="ddk_copp_video_miniport_driver_key_exchange_template_code_gg"></span><span id="DDK_COPP_VIDEO_MINIPORT_DRIVER_KEY_EXCHANGE_TEMPLATE_CODE_GG"></span>


This section applies only to Windows Server 2003 SP1 and later, and Windows XP SP2 and later.

Use the following example code to retrieve the digital certificate used by the graphics hardware for the COPP DirectX VA device object.

```cpp
VP_STATUS
IoctlCOPPKeyExchange(
    PHW_DEVICE_EXTENSION pHwDeviceExtension,
    PVIDEO_REQUEST_PACKET pVideoRequestPacket
    )
{
    COPP_IO_InputBuffer* pInBuff = pVideoRequestPacket->InputBuffer;
    COPP_DeviceData* pThis = (COPP_DeviceData*)*pInBuff->ppThis;
    GUID* lpout = (GUID*)pVideoRequestPacket->OutputBuffer;
    BYTE* pCertificate = (BYTE*)pInBuff->InputBuffer;
    HRESULT* phr = pInBuff->phr;
     *phr = COPPKeyExchange(pThis, lpout, pCertificate);
    if (*phr == NO_ERROR) {
        pVideoRequestPacket->StatusBlock->Information = pVideoRequestPacket->OutputBufferLength;
    }
    return NO_ERROR;
}
```

 

 





