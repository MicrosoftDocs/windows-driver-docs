---
title: COPPCloseVideoSession Function
description: The sample COPPCloseVideoSession function closes the COPP DirectX VA device object that is used for the current video session.
keywords:
- copy protection WDK COPP , video miniport driver code template
- video copy protection WDK COPP , video miniport driver code template
- protected video WDK COPP , video miniport driver code template
- video miniport drivers WDK Windows 2000 , COPP code template
- certified output protection protocol
ms.date: 02/16/2018
---

# COPPCloseVideoSession function

The sample COPPCloseVideoSession function closes the COPP DirectX VA device object that is used for the current video session.

### Syntax

```cpp
HRESULT COPPCloseVideoSession(
  _In_ COPP_DeviceData pThis
);
```

## Parameters

*pThis [in]*

* Pointer to the COPP DirectX VA device object.

## Return value

Returns zero (S_OK or DD_OK) if successful; otherwise, returns an error code.

## Remarks

The COPPCloseVideoSession function can be called while output protection is still applied by the video session. COPPCloseVideoSession should undo the protection settings of the COPP DirectX VA device object and adjust the global protection settings accordingly.

The COPPCloseVideoSession function maps directly to the DestroyMoComp member of the DD_MOTIONCOMPCALLBACKS structure. The DestroyMoComp member points to the display driver-supplied DdMoCompDestroy callback function.

## Example code

The following code provides an example of how you can implement your COPPCloseVideoSession function:

```cpp
HRESULT
COPPCloseVideoSession(
    COPP_DeviceData* pThis
    )
{
    DWORD j, i;
    // enumerate all the protection types supported by this connector
    for (j = COPP_ProtectionType_HDCP, i = COPP_ProtectionTypeIndex_HDCP;
         j & COPP_ProtectionType_Mask; j <<= 1, i++) {
        // for each type supported, make sure the initial level
        // is set correctly
        if (g_ConnectorInfo[pThis->m_DevID].ProtectionTypeMask & j) {
            DWORD oldLevel = pThis->m_LocalLevel[i];
            g_COPPLevels[pThis->m_DevID].Levels[i][oldLevel]--;
        }
    }
    ResetKey(&pThis->m_AesHelper);
    return NO_ERROR;
}
```

**Requirements**

| Target platform | Version |
| -- | -- |
| Desktop | This function applies only to Windows Server 2003 with SP1 and later, and Windows XP with SP2 and later. |
