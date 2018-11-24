---
title: COPP Video Miniport Driver Open Template Code
description: COPP Video Miniport Driver Open Template Code
ms.assetid: 41facdef-c5f7-42f1-a251-07e4685649de
keywords:
- opening COPP DirectX VA device objects
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# COPP Video Miniport Driver Open Template Code


## <span id="ddk_copp_video_miniport_driver_open_template_code_gg"></span><span id="DDK_COPP_VIDEO_MINIPORT_DRIVER_OPEN_TEMPLATE_CODE_GG"></span>


This section applies only to Windows Server 2003 SP1 and later, and Windows XP SP2 and later.

Use the following example code to create instances of COPP DirectX VA device objects.

```cpp
VP_STATUS
IoctlCOPPOpenDevice(
    PHW_DEVICE_EXTENSION pHwDeviceExtension,
    PVIDEO_REQUEST_PACKET pVideoRequestPacket
    )
{
    COPP_IO_InputBuffer* pInBuff = pVideoRequestPacket->InputBuffer;
    ULONG uDevID = *(ULONG*)pInBuff->InputBuffer;
    COPP_DeviceData* pThis = VideoPortAllocatePool(pHwDeviceExtension,
                                              VpPagedPool,
                                              sizeof(COPP_DeviceData),
                                              &#39;PPOC&#39;);
    *pInBuff->ppThis = NULL;
    if (pThis == NULL) {
        *pInBuff->phr = ERROR_NOT_ENOUGH_MEMORY;
        return NO_ERROR;
    }
     *pInBuff->phr = COPPOpenVideoSession(pThis, uDevID);
    if (*pInBuff->phr == NO_ERROR) {
        *pInBuff->ppThis = pThis;
    }
    else {
        VideoPortFreePool(pHwDeviceExtension, pThis);
        *pInBuff->ppThis = NULL;
    }
    return NO_ERROR;
}
```

 

 





