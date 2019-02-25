---
title: COPP Video Miniport Driver Sequence Start Template Code
description: COPP Video Miniport Driver Sequence Start Template Code
ms.assetid: f1fc0d03-43f6-44a0-b911-1ca473e4e701
keywords:
- sequence start WDK COPP
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# COPP Video Miniport Driver Sequence Start Template Code


## <span id="ddk_copp_video_miniport_driver_sequence_start_template_code_gg"></span><span id="DDK_COPP_VIDEO_MINIPORT_DRIVER_SEQUENCE_START_TEMPLATE_CODE_GG"></span>


This section applies only to Windows Server 2003 SP1 and later, and Windows XP SP2 and later.

Use the following example code to set the current video session to protected mode for the COPP DirectX VA device object.

```cpp
VP_STATUS
IoctlCOPPStartSeqence(
    PHW_DEVICE_EXTENSION pHwDeviceExtension,
    PVIDEO_REQUEST_PACKET pVideoRequestPacket
    )
{
    COPP_IO_InputBuffer* pInBuff = pVideoRequestPacket->InputBuffer;
    COPP_DeviceData* pThis = (COPP_DeviceData*)*pInBuff->ppThis;
    DXVA_COPPSignature* lpin = (DXVA_COPPSignature*)pInBuff->InputBuffer;
     *pInBuff->phr = COPPSequenceStart(pThis, lpin);
    return NO_ERROR;
}
```

 

 





