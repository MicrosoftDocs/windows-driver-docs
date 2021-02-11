---
title: COPPOpenVideoSession function
description: The sample COPPOpenVideoSession function initializes the COPP DirectX VA device object that is used for the current video session.
keywords:
- copy protection WDK COPP , video miniport driver code template
- video copy protection WDK COPP , video miniport driver code template
- protected video WDK COPP , video miniport driver code template
- video miniport drivers WDK Windows 2000 , COPP code template
- certified output protection protocol
ms.date: 02/16/2018
ms.localizationpriority: medium
---

# COPPOpenVideoSession function

The sample COPPOpenVideoSession function initializes the COPP DirectX VA device object that is used for the current video session.

### Syntax

```cpp
HRESULT COPPOpenVideoSession(
  _In_ COPP_DeviceData pThis,
  _In_ ULONG           DevID
);
```

## Parameters

*pThis [in]*

* Pointer to the COPP DirectX VA device object.

*DevID [in]*

* Supplies the identifier of the graphics device to which the COPP device is attached.

## Return value

Returns zero (S_OK or DD_OK) if successful; otherwise, returns an error code.

## Remarks

A COPP device must be initialized through a call to COPPOpenVideoSession before any other member function of the COPP device class is called. COPPOpenVideoSession should initialize (set to 0) the video session's local protection levels for each supported protection type and increment the corresponding global protection level counter. For more information, see Handling Protection Levels.

COPPOpenVideoSession should return DDERR_UNSUPPORTEDMODE if the device identified by the DevID parameter drives multiple graphics adapters that use a mode other than DualView. For more information, see COPP and Multiple-Monitor Support.

The sample COPPOpenVideoSession function maps directly to the CreateMoComp member of the DD_MOTIONCOMPCALLBACKS structure. The CreateMoComp member points to the display driver-supplied DdMoCompCreate callback function that references the DD_CREATEMOCOMPDATA structure. The lpGuid member of DD_CREATEMOCOMPDATA points to the COPP DirectX VA device GUID.

## Example code

The following code provides an example of how you can implement your COPPOpenVideoSession function:

```cpp
HRESULT
COPPOpenVideoSession(
    COPP_DeviceData* pThis,
    DWORD DevID
    )
{
    DWORD i;
    pThis->m_DevID = DevID;
    pThis->m_CmdSeqNumber = (DWORD)-1;
    pThis->m_StatusSeqNumber = (DWORD)-1;
    pThis->m_COPPDevState = COPP_OPENED;
    memset(&pThis->m_AesHelper, 0, sizeof(pThis->m_AesHelper));
    //
    // make sure the session protection levels are reset
    //
    memset(&pThis->m_LocalLevel, 0, sizeof(pThis->m_LocalLevel));
    //
    // initialize the session local protection levels and
    // increment the corresponding global protection level counter
    //
    // enumerate all the protection types supported by this connector
    DWORD j;
    for (j = COPP_ProtectionType_HDCP, i = COPP_ProtectionTypeIndex_HDCP;
         j & COPP_ProtectionType_Mask; j <<= 1, i++) {
        // for each type supported, make sure the initial level
        // is set correctly
        if (g_ConnectorInfo[pThis->m_DevID].ProtectionTypeMask & j) {
            pThis->m_LocalLevel[i] = 0;
            g_COPPLevels[pThis->m_DevID].Levels[i][0]++;
        }
        else {
            pThis->m_LocalLevel[i] = COPP_NoProtectionLevelAvailable;
        }
    }
    return NO_ERROR;
}
```

**Requirements**

| Target platform | Version |
| -- | -- |
| Desktop | This function applies only to Windows Server 2003 with SP1 and later, and Windows XP with SP2 and later. |
