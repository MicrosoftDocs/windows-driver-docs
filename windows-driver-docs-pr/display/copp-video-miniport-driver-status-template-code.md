---
title: COPP Video Miniport Driver Status Template Code
description: COPP Video Miniport Driver Status Template Code
keywords:
- status information WDK COPP
ms.date: 04/20/2017
---

# COPP Video Miniport Driver Status Template Code


## <span id="ddk_copp_video_miniport_driver_status_template_code_gg"></span><span id="DDK_COPP_VIDEO_MINIPORT_DRIVER_STATUS_TEMPLATE_CODE_GG"></span>


This section applies only to Windows Server 2003 SP1 and later, and Windows XP SP2 and later.

Use the following example code to retrieve status on a protected video session that is associated with the COPP DirectX VA device object.

```cpp
VP_STATUS
IoctlCOPPStatus(
    PHW_DEVICE_EXTENSION pHwDeviceExtension,
    PVIDEO_REQUEST_PACKET pVideoRequestPacket
    )
{
    COPP_IO_InputBuffer* pInBuff = pVideoRequestPacket->InputBuffer;
    COPP_DeviceData* pThis = (COPP_DeviceData*)*pInBuff->ppThis;
    DXVA_COPPStatusInput* lpin = (DXVA_COPPStatusInput*)pInBuff->InputBuffer;
    DXVA_COPPStatusOutput* lpout = (DXVA_COPPStatusOutput*)pVideoRequestPacket->OutputBuffer;
    HRESULT* phr = pInBuff->phr;
     *phr =  COPPQueryStatus(pThis, lpin, lpout);
    if (*phr == NO_ERROR) {
        pVideoRequestPacket->StatusBlock->Information = sizeof(DXVA_COPPStatusOutput);
    }
    return S_OK;
}
```

 

 





