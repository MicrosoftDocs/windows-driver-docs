---
title: COPPCommand Function
description: The sample COPPCommand function performs an operation on a COPP DirectX VA device.
keywords:
- copy protection WDK COPP , video miniport driver code template
- video copy protection WDK COPP , video miniport driver code template
- protected video WDK COPP , video miniport driver code template
- video miniport drivers WDK Windows 2000 , COPP code template
- certified output protection protocol
ms.date: 02/16/2018
---

# COPPCommand function

The sample COPPCommand function performs an operation on a COPP DirectX VA device.

## Syntax

```cpp
HRESULT COPPCommand(
  _In_ COPP_DeviceData  pThis,
  _In_ DXVA_COPPCommand *pCommand
);
```

## Parameters

*pThis [in]*

 * Pointer to the COPP DirectX VA device object.

*pCommand [in]*
* Supplies a pointer to a DXVA_COPPCommand structure that contains information about the operation to perform on the COPP device.

## Return value

Returns zero (S_OK or DD_OK) if successful; otherwise, returns an error code.

## Remarks

The video session should be set to protected mode (that is, it should be active) before the associated COPP DirectX VA device receives a call to its COPPCommand function. That is, the COPPSequenceStart function should be called before COPPCommand. If COPPCommand is called before COPPSequenceStart, COPPCommand should return E_UNEXPECTED.

The COPPCommand function receives a populated DXVA_COPPCommand structure that contains a COPP command. The following COPP commands are supported:

* **DXVA_COPPSetProtectionLevel** <br>An instruction from the video session to set the protection level on the physical connector associated with the COPP device. A video miniport driver should be able to support multiple video sessions all playing back content through the same physical connector.
* **DXVA_COPPSetSignaling** <br>An instruction about how to protect the signal that goes through the physical connector associated with the DirectX VA COPP device.

The COPPCommand function should verify that the parameters passed to it are valid for the given physical connector being used and should return E_INVALIDARG if one or more of the parameters are not valid.

If the protection command that is passed to COPPCommand is incompatible with the display resolution of the monitor, COPPCommand should return DDERR_TOOBIGSIZE.

## Mapping RenderMoComp to COPPCommand

The sample COPPCommand function maps directly to a call to the RenderMoComp member of the DD_MOTIONCOMPCALLBACKS structure. The RenderMoComp member points to the display driver-supplied DdMoCompRender callback function that references the DD_RENDERMOCOMPDATA structure.

The RenderMoComp callback function is called without the display driver-supplied BeginMoCompFrame or EndMoCompFrame function being called first.

The DD_RENDERMOCOMPDATA structure is filled as follows.

| Member | Value |
| -- | -- |
| dwNumBuffers | Zero. |
| lpBufferInfo | NULL. |
| dwFunction | DXVA_COPPCommandFnCode constant (defined in dxva.h).|
| lpInputData | Pointer to a DXVA_COPPCommand structure. |
| lpOutputData | NULL. |

## Example Code

The following code provides an example of how you can implement your COPPCommand function:

```cpp
GUID
COPP_CalculateMAC(
    AESHelper* pAesHelper,
    BYTE* pInputData,
    DWORD dwDataLength,
    GUID* pKDI
    )
{
    GUID rgbTag;
    memset(&rgbTag, 0, sizeof(GUID));
    SignData(pAesHelper, pInputData, dwDataLength, (BYTE*)&rgbTag);
    return rgbTag;
}

HRESULT
COPPCommand(
    COPP_DeviceData* pThis,
    DXVA_COPPCommand* pCommand
    )
{
    DXVA_COPPSetProtectionLevelCmdData CmdData;
    DWORD ProtIndex = COPP_ProtectionTypeIndex_Unkonwn;
    if (pThis->m_COPPDevState != COPP_SESSION_ACTIVE) {
        return E_UNEXPECTED;
    }
    if (pCommand->dwSequence != pThis->m_CmdSeqNumber) {
        return E_INVALIDARG;
    }
    if (!IsEqualGUID(&pCommand->guidCommandID, &DXVA_COPPSetProtectionLevel)) {
        return E_INVALIDARG;
    }
    //
    // ensure that enough data is passed
    //
    if (pCommand->cbSizeData < sizeof(DXVA_COPPSetProtectionLevelCmdData)) {
        return E_INVALIDARG;
    }
    //
    // verify that the command message was sent by the application
    // over the secure channel by validating the MAC on the message
    //
    GUID macCalculated = COPP_CalculateMAC(&pThis->m_AesHelper,
                                      (BYTE*)&pCommand->guidCommandID,
                              sizeof(DXVA_COPPCommand) - sizeof(GUID),
                                       &pThis->m_KDI);
        if (!IsEqualGUID(&macCalculated, &pCommand->macKDI)) {
            return E_UNEXPECTED;
        }
    memcpy(&CmdData, pCommand->CommandData, sizeof(DXVA_COPPSetProtectionLevelCmdData));
    //
    // determine which protection level (CmdData.ProtType) was passed and
    // set ProtIndex accordingly (for example, ProtIndex = COPP_ProtectionTypeIndex_ACP)
    //
    //
    // ensure that the request is valid
    //
    if (CmdData.ProtLevel >= g_nLevels[ProtIndex]) {
        return E_INVALIDARG;
    }
    // set the new local level and store the former local level
    DWORD oldLevel = pThis->m_LocalLevel[ProtIndex];
    pThis->m_LocalLevel[ProtIndex] = CmdData.ProtLevel;
    // decrement the former global level and increment the new
    g_COPPLevels[pThis->m_DevID].Levels[ProtIndex][oldLevel]--;
    g_COPPLevels[pThis->m_DevID].Levels[ProtIndex][CmdData.ProtLevel]++;
    pThis->m_CmdSeqNumber++;
    return NO_ERROR;
}
```

**Requirements**

|Target platform | Version |
| -- | -- |
| Desktop | This function applies only to Windows Server 2003 with SP1 and later, and Windows XP with SP2 and later. |



