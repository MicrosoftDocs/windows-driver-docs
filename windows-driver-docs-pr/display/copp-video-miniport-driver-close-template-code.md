---
title: COPP Video Miniport Driver Close Template Code
description: COPP Video Miniport Driver Close Template Code
ms.assetid: a7b088d6-a6cd-479d-b256-04def1de1736
keywords:
- releasing COPP DirectX VA device objects
- closing COPP DirectX VA device objects
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# COPP Video Miniport Driver Close Template Code


## <span id="ddk_copp_video_miniport_driver_close_template_code_gg"></span><span id="DDK_COPP_VIDEO_MINIPORT_DRIVER_CLOSE_TEMPLATE_CODE_GG"></span>


This section applies only to Windows Server 2003 SP1 and later, and Windows XP SP2 and later.

Use the following example code to release instances of COPP DirectX VA device objects.

```cpp
VP_STATUS
IoctlCOPPCloseDevice(
    PHW_DEVICE_EXTENSION pHwDeviceExtension,
    PVIDEO_REQUEST_PACKET pVideoRequestPacket
    )
{
    COPP_IO_InputBuffer* pInBuff = pVideoRequestPacket->InputBuffer;
    COPP_DeviceData* pThis = (COPP_DeviceData*)*pInBuff->ppThis;
     *pInBuff->phr = COPPCloseVideoSession(pThis);
    VideoPortFreePool(pHwDeviceExtension, pThis);
    *pInBuff->ppThis = NULL;
    return NO_ERROR;
}
```

 

 





