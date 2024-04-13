---
title: COPPQueryStatus Function
description: The sample COPPQueryStatus function retrieves status on a protected video session that is associated with a COPP DirectX VA device.
keywords:
- copy protection WDK COPP , video miniport driver code template
- video copy protection WDK COPP , video miniport driver code template
- protected video WDK COPP , video miniport driver code template
- video miniport drivers WDK Windows 2000 , COPP code template
ms.date: 04/20/2017
---

# COPPQueryStatus function

The sample COPPQueryStatus function retrieves status on a protected video session that is associated with a COPP DirectX VA device.

### Syntax

```cpp
HRESULT COPPQueryStatus(
  _In_  COPP_DeviceData       pThis,
  _In_  DXVA_COPPStatusInput  *pInput,
  _Out_ DXVA_COPPStatusOutput *pOutput
);
```

## Parameters

*pThis [in]*

* Pointer to the COPP DirectX VA device object.

*pInput [in]*

* Supplies a pointer to a DXVA_COPPStatusInput structure that contains a request to retrieve specific status information.

*pOutput [out]*

* Pointer to a DXVA_COPPStatusOutput structure that receives status information about the physical connector being used.

## Return value

Returns zero (S_OK or DD_OK) if successful; otherwise, returns an error code.

## Remarks

The video session should be set to protected mode (that is, it should be active) before the associated COPP DirectX VA device receives a call to its COPPQueryStatus function. That is, the COPPSequenceStart function should be called before COPPQueryStatus. If COPPQueryStatus is called before COPPSequenceStart, COPPQueryStatus should return E_UNEXPECTED.

The COPPQueryStatus function receives a populated DXVA_COPPStatusInput structure at pInput that contains a status request. The COPPQueryStatus function processes the request and returns the appropriate status in a DXVA_COPPStatusOutput structure at pOutput.

## Mapping RenderMoComp to COPPQueryStatus

The sample COPPQueryStatus function maps directly to a call to the RenderMoComp member of the DD_MOTIONCOMPCALLBACKS structure. The RenderMoComp member points to the display driver-supplied DdMoCompRender callback function that references the DD_RENDERMOCOMPDATA structure.

The RenderMoComp callback function is called without the display driver-supplied BeginMoCompFrame or EndMoCompFrame function being called first.

The DD_RENDERMOCOMPDATA structure is filled as follows.

| Member | Value |
| ------ | ----- |
| dwNumBuffers | Zero. |
| lpBufferInfo | NULL. |
| dwFunction | DXVA_COPPQueryStatusFnCode constant (defined in dxva.h). |
| lpInputData | Pointer to a DXVA_COPPStatusInput structure. |
| lpOutputData | Pointer to a DXVA_COPPStatusOutput structure. |

## Example Code

The following code provides an example of how you can implement your COPPQueryStatus function:

```cpp
HRESULT
COPPQueryStatus(
    COPP_DeviceData* pThis,
    DXVA_COPPStatusInput* pStatusInput,
    DXVA_COPPStatusOutput* pStatusOutput
    )
{
    if (pThis->m_COPPDevState != COPP_SESSION_ACTIVE) {
        return E_UNEXPECTED;
    }
    if (pStatusInput->dwSequence != pThis->m_StatusSeqNumber) {
        return E_INVALIDARG;
    }
    //
    // reset the output buffer
    //
    memset(pStatusOutput, 0, sizeof(DXVA_COPPStatusOutput));
    if (IsEqualGUID(&DXVA_COPPQueryConnectorType, &pStatusInput->guidStatusRequestID)) {
        // Verify no input data for this status request.
        if (pStatusInput->cbSizeData != 0) {
            return E_INVALIDARG;
        }
        DXVA_COPPStatusData Tmp;
        Tmp.rApp = pStatusInput->rApp;
        Tmp.dwData = g_ConnectorInfo[pThis->m_DevID].ConnType;
        Tmp.dwFlags = COPP_StatusNormal;
        pStatusOutput->cbSizeData = sizeof(Tmp);
        memcpy(pStatusOutput->COPPStatus, &Tmp,sizeof(Tmp));
    }
    else if (IsEqualGUID(&DXVA_COPPQueryProtectionType, &pStatusInput->guidStatusRequestID)) {
        // verify that there is no input data for this status request
        if (pStatusInput->cbSizeData != 0) {
            return E_INVALIDARG;
        }
        DXVA_COPPStatusData Tmp;
        Tmp.rApp = pStatusInput->rApp;
        Tmp.dwData = g_ConnectorInfo[pThis->m_DevID].ProtectionTypeMask;
        Tmp.dwFlags = COPP_StatusNormal;
        pStatusOutput->cbSizeData = sizeof(Tmp);
        memcpy(pStatusOutput->COPPStatus, &Tmp,sizeof(Tmp));
    }
    else if (IsEqualGUID(&DXVA_COPPQueryLocalProtectionLevel, &pStatusInput->guidStatusRequestID) ||
             IsEqualGUID(&DXVA_COPPQueryGlobalProtectionLevel, &pStatusInput->guidStatusRequestID)) {
        DWORD ProtType;
        DWORD ProtIndex;
        DWORD Level;
        // verify that there is a single DWORD input data for this status request
        if (pStatusInput->cbSizeData != sizeof (DWORD)) {
            return E_INVALIDARG;
        }
        memcpy(&ProtType, (LPVOID)&pStatusInput->StatusData[0], sizeof(DWORD));
        // verify that no invalid protection type bits are set
        if (ProtType & ~COPP_ProtectionType_Mask) {
            return E_INVALIDARG;
        }
        // verify that only the protection level of a single protection type is requested
        ProtIndex = MapProtectionTypeToProtectionIndex(ProtType);
        if (ProtIndex == COPP_ProtectionTypeIndex_Unkonwn) {
            return E_INVALIDARG;
        }
        // verify that the video session supports the protection type
        if (!(g_ConnectorInfo[pThis->m_DevID].ProtectionTypeMask & ProtType)) {
            return E_INVALIDARG;
        }
        if (IsEqualGUID(&DXVA_COPPQueryLocalProtectionLevel,
                        &pStatusInput->guidStatusRequestID)) {
            Level = pThis->m_LocalLevel[ProtIndex];
        }
        else {
            Level = g_nLevels[ProtIndex] - 1;
            for ( ; Level != 0; Level--) {
                if (g_COPPLevels[pThis->m_DevID].Levels[ProtIndex][Level]) {
                    break;
                }
            }
        }
        DXVA_COPPStatusData Tmp;
        Tmp.rApp = pStatusInput->rApp;
        Tmp.dwData = Level;
        Tmp.dwFlags = COPP_StatusNormal;
        pStatusOutput->cbSizeData = sizeof(Tmp);
        memcpy(pStatusOutput->COPPStatus, &Tmp, sizeof(Tmp));
    }
    pThis->m_StatusSeqNumber++;
    pStatusOutput->macKDI = COPP_CalculateMAC(&pThis->m_AesHelper,
                                    (BYTE*)&pStatusOutput->cbSizeData,
                         sizeof(DXVA_COPPStatusOutput) - sizeof(GUID),
                                     &pThis->m_KDI);
    return NO_ERROR;
}
```

**Requirements**

| Target platform | Version |
| -- | -- |
| Desktop | This function applies only to Windows Server 2003 with SP1 and later, and Windows XP with SP2 and later. |
