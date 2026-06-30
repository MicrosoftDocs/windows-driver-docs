---
title: KSPROPERTY_CAMERACONTROL_EXTENDED_SECURE_MODE
description: KSPROPERTY_CAMERACONTROL_EXTENDED_SECURE_MODE is used to control secure mode on the driver.
keywords: ["IMFSecureBuffer KSPROPERTY_CAMERACONTROL_EXTENDED_SECURE_MODE Streaming Media Devices"]
ai-usage: ai-assisted
topic_type:
- apiref
ms.topic: reference
api_name:
- KSPROPERTY_CAMERACONTROL_EXTENDED_SECURE_MODE
api_location:
- Ksmedia.h
api_type:
- HeaderDef
ms.date: 06/18/2026
---

# KSPROPERTY_CAMERACONTROL_EXTENDED_SECURE_MODE

KSPROPERTY_CAMERACONTROL_EXTENDED_SECURE_MODE is mainly used by the OS to check whether the camera driver supports secure authentication before enabling and using it. This control is not meant to be used by regular applications.

## Overview

When enabled, the camera driver issues secure kernel frame buffers as opposed to buffers in user-mode system memory. Secure kernel frame buffers are useful in scenarios such as biometrics authentication where the frame content authenticity needs to remain unaltered by any user-mode driver components.
This secure buffer can be queried from the COM interface ***IMFSecureBuffer***
~~~cpp
// mfobject.h
interface IMFSecureBuffer : IUnknown
{ 
    /// Get a GUID identifier for the secure buffer 
    HRESULT GetIdentifier(GUID *pGuidIdentifier); 
}; 
~~~

This interface can be queried from an existing IMFMediaBuffer:

~~~cpp
ComPtr<IMFSample> spSample; 
DWORD dwTotalBufferLength = 0; 
DWORD dwBufferCount = 0;
DWORD dwStreamIndex = 0 //Read first stream for samples 
DWORD dwActualStreamIndex = 0;
DWORD dwStreamFlags = 0; 
LONGLONG llTimeStamp = 0ll
ComPtr<IMFSourceReader> spSourceReader;

// assuming the IMFSourceReader object spSourceReader is correctly provisioned from the camera
//...

// retrieve an IMFSample from the IMFSourceReader
VERIFY_SUCCEEDED(spSourceReader->ReadSample(dwStreamIndex, 0, &dwActualStreamIndex, &dwStreamFlags,  &llTimeStamp, spSample.GetAddressOf()));
if (nullptr != spSample.Get())
{
    VERIFY_SUCCEEDED(spSample->GetBufferCount(&dwBufferCount));
    for (DWORD dwIndex = 0; dwIndex < dwBufferCount; dwIndex++)
    {
        ComPtr<IMFMediaBuffer> spMediaBuffer; 
        ComPtr<IMFSecureBuffer> spSecureBuffer;
        if (SUCCEEDED(spMediaBuffer->QueryInterface(IID_PPV_ARGS(&spSecureBuffer)))) 
        {
            // this is a secure buffer
            GUID guidIdentifier = GUID_NULL; 
            WCHAR strGuid[64];

            // Get a GUID identifier for the secure buffer.
            // Use this identifier to access the buffer in secure kernel.
            VERIFY_SUCCEEDED(spSecureBuffer->GetIdentifier(&guidIdentifier)); 
        } 
    }
}
~~~

## Usage summary table

| Scope | Control | Type |
| --- | --- | --- |
| Version 1 | Pin | Synchronous |

The following are flags that can be placed in the KSCAMERA_EXTENDEDPROP_HEADER.Flags field to enable or disable secure mode on the driver.

```cpp
#define KSCAMERA_EXTENDEDPROP_SECUREMODE_DISABLED               0x0000000000000001 
#define KSCAMERA_EXTENDEDPROP_SECUREMODE_ENABLED                0x0000000000000002 
```

If the driver supports this control, it must support both KSCAMERA_EXTENDEDPROP_SECUREMODE_DISABLED and KSCAMERA_EXTENDEDPROP_SECUREMODE_ENABLED.

This is a synchronous control. Must be set before starting the stream.

The following table describes the flag capabilities.

| Flag | Description |
| --- | --- |
| KSCAMERA_EXTENDEDPROP_SECUREMODE_DISABLED | This is a mandatory capability |
| KSCAMERA_EXTENDEDPROP_SECUREMODE_ENABLED | This is a mandatory capability |

The following table contains the descriptions and requirements for the [**KSCAMERA_EXTENDEDPROP_HEADER**](/windows-hardware/drivers/ddi/ksmedia/ns-ksmedia-tagkscamera_extendedprop_header) structure fields when using the control.

| Member | Description |
| --- | --- |
| Version | Must be 1. |
| PinId | Must be advertised on only one pin on the filter. The pin must be type PINNAME_VIDEO_CAPTURE or PINNAME_VIDEO_PREVIEW |
| Size | Must be sizeof(KSCAMERA_EXTENDEDPROP_HEADER)+ sizeof(KSCAMERA_EXTENDEDPROP_VALUE). |
| Result | Indicates the error results of the last SET operation. If no SET operation takes place, `Result` must be 0. |
| Capability | Must be a bitwise OR of the supported KSCAMERA_EXTENDEDPROP_SECUREMODE_XXX flags defined earlier. |
| Flags | This field is read/write. The value must be any one of the KSCAMERA_EXTENDEDPROP_SECUREMODE_XXX flags defined earlier. These flags are mutually exclusive and can't be set in any bitwise OR combination. |

## Requirements

**Header**: Ksmedia.h
