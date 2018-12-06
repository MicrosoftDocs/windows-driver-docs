---
title: COPP Video Miniport Driver Command Template Code
description: COPP Video Miniport Driver Command Template Code
ms.assetid: a772fc78-0024-4834-8ff3-a1cf6672b316
keywords:
- commands WDK COPP
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# COPP Video Miniport Driver Command Template Code


## <span id="ddk_copp_video_miniport_driver_command_template_code_gg"></span><span id="DDK_COPP_VIDEO_MINIPORT_DRIVER_COMMAND_TEMPLATE_CODE_GG"></span>


This section applies only to Windows Server 2003 SP1 and later, and Windows XP SP2 and later.

Use the following example code to perform an operation on the COPP DirectX VA device object.

```cpp
VP_STATUS
IoctlCOPPCommand(
    PHW_DEVICE_EXTENSION pHwDeviceExtension,
    PVIDEO_REQUEST_PACKET pVideoRequestPacket
    )
{
    COPP_IO_InputBuffer* pInBuff = pVideoRequestPacket->InputBuffer;
    COPP_DeviceData* pThis = (COPP_DeviceData*)*pInBuff->ppThis;
    DXVA_COPPCommand* lpin = (DXVA_COPPCommand*)pInBuff->InputBuffer;
     *pInBuff->phr = COPPCommand(pThis, lpin);
    return NO_ERROR;
}
```

 

 





