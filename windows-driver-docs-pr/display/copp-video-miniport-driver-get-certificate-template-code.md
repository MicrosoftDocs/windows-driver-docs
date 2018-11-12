---
title: COPP Video Miniport Driver Get Certificate Template Code
description: COPP Video Miniport Driver Get Certificate Template Code
ms.assetid: 13810013-389a-458d-be9d-e81a0b248dec
keywords:
- certificates WDK COPP
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# COPP Video Miniport Driver Get Certificate Template Code


## <span id="ddk_copp_video_miniport_driver_get_certificate_template_code_gg"></span><span id="DDK_COPP_VIDEO_MINIPORT_DRIVER_GET_CERTIFICATE_TEMPLATE_CODE_GG"></span>


This section applies only to Windows Server 2003 SP1 and later, and Windows XP SP2 and later.

Use the following example code to retrieve the size, in bytes, of the graphics hardware certificate for the COPP DirectX VA device object.

```cpp
VP_STATUS
IoctlCOPPGetCertificateLength(
    PHW_DEVICE_EXTENSION pHwDeviceExtension,
    PVIDEO_REQUEST_PACKET pVideoRequestPacket
    )
{
    COPP_IO_InputBuffer* pInBuff = pVideoRequestPacket->InputBuffer;
    COPP_DeviceData* pThis = (COPP_DeviceData*)*pInBuff->ppThis;
    HRESULT* phr = pInBuff->phr;
     *phr = COPPGetCertificateLength(pThis, (ULONG*)pVideoRequestPacket->OutputBuffer);
    if (*phr == NO_ERROR) {
        pVideoRequestPacket->StatusBlock->Information = sizeof(ULONG);
    }
    return NO_ERROR;
}
```

 

 





