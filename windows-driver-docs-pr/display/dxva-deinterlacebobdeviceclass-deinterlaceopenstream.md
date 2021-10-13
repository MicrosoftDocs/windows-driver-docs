---
title: DeinterlaceOpenStream method
description: The sample DXVA_DeinterlaceBobDeviceClass::DeinterlaceOpenStream function creates and opens a deinterlace stream object.
keywords: ["DeinterlaceOpenStream method Display Devices", "DeinterlaceOpenStream method Display Devices , DXVA_DeinterlaceBobDeviceClass interface", "DXVA_DeinterlaceBobDeviceClass interface Display Devices , DeinterlaceOpenStream method"]
topic_type:
- apiref
api_name:
- DXVA_DeinterlaceBobDeviceClass.DeinterlaceOpenStream
api_type:
- COM
ms.date: 12/06/2018
ms.localizationpriority: medium
ms.custom: seodec18
---

# DXVA\_DeinterlaceBobDeviceClass::DeinterlaceOpenStream method


The sample *DeinterlaceOpenStream* function creates and opens a deinterlace stream object.

## Syntax

```cpp
HRESULT DeinterlaceOpenStream(
  [in] LPDXVA_VideoDesc lpVideoDescription
);
```

## Parameters

*lpVideoDescription* \[in\]
Supplies a pointer to a [**DXVA\_VideoDesc**](/windows-hardware/drivers/ddi/dxva/ns-dxva-_dxva_videodesc) structure that indicates the type of video to be deinterlaced or rate-converted. The pointer is passed to the driver so that the driver can support the resolution and format of the source video. For example, the driver might be able to perform a three-field adaptive deinterlace of 480i content, but it might only be able to bob 1080i content. All drivers should be able to support bob using the existing *bit-block transfer* hardware.

## Return value

Returns zero (S\_OK or DD\_OK) if successful; otherwise, returns an error code. Refer to *ddraw.h* for a complete list of error codes.

## Remarks

After a deinterlace mode GUID is found using the [**DeinterlaceQueryAvailableModes**](dxva-deinterlacecontainerdeviceclass-deinterlacequeryavailablemodes.md) function, the deinterlace stream object can be created. This object allows a display driver to reserve any hardware resources that are required to perform the requested deinterlace operations.

For more information about how the driver performs deinterlace or frame-rate-conversion operations using the information supplied by the *lpVideoDescription* parameter, see [Video Content for Deinterlace and Frame-Rate Conversion](./video-content-for-deinterlace-and-frame-rate-conversion.md).

The sample *DeinterlaceOpenStream* function maps directly to the **CreateMoComp** member of the [**DD\_MOTIONCOMPCALLBACKS**](/windows/win32/api/ddrawint/ns-ddrawint-dd_motioncompcallbacks) structure, where the GUID is the deinterlace mode requested. The **lpData** member of the [**DD\_CREATEMOCOMPDATA**](/windows/win32/api/ddrawint/ns-ddrawint-dd_createmocompdata) structure points to a [**DXVA\_VideoDesc**](/windows-hardware/drivers/ddi/dxva/ns-dxva-_dxva_videodesc) structure.

## <span id="see_also"></span>See also


[**DD\_MOTIONCOMPCALLBACKS**](/windows/win32/api/ddrawint/ns-ddrawint-dd_motioncompcallbacks)

[**DD\_CREATEMOCOMPDATA**](/windows/win32/api/ddrawint/ns-ddrawint-dd_createmocompdata)

[**DeinterlaceQueryAvailableModes**](dxva-deinterlacecontainerdeviceclass-deinterlacequeryavailablemodes.md)

[**DXVA\_VideoDesc**](/windows-hardware/drivers/ddi/dxva/ns-dxva-_dxva_videodesc)

