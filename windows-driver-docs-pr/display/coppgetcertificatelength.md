---
title: COPPGetCertificateLength Function
description: The sample COPPGetCertificateLength function retrieves the size, in bytes, of the certificate used by the graphics hardware.
keywords:
- copy protection WDK COPP , video miniport driver code template
- video copy protection WDK COPP , video miniport driver code template
- protected video WDK COPP , video miniport driver code template
- video miniport drivers WDK Windows 2000 , COPP code template
ms.date: 02/16/2018
---

# COPPGetCertificateLength function

The sample COPPGetCertificateLength function retrieves the size, in bytes, of the certificate used by the graphics hardware.

### Syntax

```cpp
HRESULT COPPGetCertificateLength(
  _In_  COPP_DeviceData pThis,
  _Out_ ULONG           *pCertificateLength
);
```

## Parameters

*pThis [in]*

* Pointer to the COPP DirectX VA device object.

*pCertificateLength [out]*

* Pointer to a variable that receives the size, in bytes, of the certificate used by the graphics hardware.

## Return value

Returns zero (S_OK or DD_OK) if successful; otherwise, returns an error code.

## Remarks

A COPP DirectX VA device should be initialized before receiving a call to its COPPGetCertificateLength function. That is, the COPPOpenVideoSession function should be called before COPPGetCertificateLength. If COPPGetCertificateLength is called before COPPOpenVideoSession, COPPGetCertificateLength should return E_UNEXPECTED.

## Mapping RenderMoComp to COPPGetCertificateLength

The sample COPPGetCertificateLength function maps directly to a call to the RenderMoComp member of the DD_MOTIONCOMPCALLBACKS structure. The RenderMoComp member points to the display driver-supplied DdMoCompRender callback function that references the DD_RENDERMOCOMPDATA structure.

The RenderMoComp callback function is called without the display driver-supplied BeginMoCompFrame or EndMoCompFrame function being called first.

The DD_RENDERMOCOMPDATA structure is filled as follows.

| Member | Value |
| -- | -- |
| dwNumBuffers | Zero. |
| lpBufferInfo | NULL. |
| dwFunction | DXVA_COPPGetCertificateLengthFnCode constant (defined in dxva.h). |
| lpInputData | NULL. |
| lpOutputData | Pointer to a ULONG-typed variable. |

## Example Code

The following code provides an example of how you can implement your COPPGetCertificateLength function:

```cpp
HRESULT
COPPGetCertificateLength(
    COPP_DeviceData* pThis,
    DWORD* pCertificateLength
    )
{
    if (pThis->m_COPPDevState != COPP_OPENED) {
        return E_UNEXPECTED;
    }
    *pCertificateLength = sizeof(TestCert);
    pThis->m_COPPDevState = COPP_CERT_LENGTH_RETURNED;
    return NO_ERROR;
}
```

**Requirements**

| Target platform | Version |
| -- | -- |
| Desktop | This function applies only to Windows Server 2003 with SP1 and later, and Windows XP with SP2 and later. |



