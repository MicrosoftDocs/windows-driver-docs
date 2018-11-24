---
title: DXVA\_DeinterlaceBobDeviceClass DeinterlaceOpenStream method
description: The sample DeinterlaceOpenStream function creates and opens a deinterlace stream object.
ms.assetid: 975d5f6a-8d92-4da5-846c-1637fca58eb1
keywords: ["DeinterlaceOpenStream method Display Devices", "DeinterlaceOpenStream method Display Devices , DXVA_DeinterlaceBobDeviceClass interface", "DXVA_DeinterlaceBobDeviceClass interface Display Devices , DeinterlaceOpenStream method"]
topic_type:
- apiref
api_name:
- DXVA_DeinterlaceBobDeviceClass.DeinterlaceOpenStream
api_type:
- COM
ms.date: 01/05/2018
ms.localizationpriority: medium
---

# DXVA\_DeinterlaceBobDeviceClass::DeinterlaceOpenStream method


The sample *DeinterlaceOpenStream* function creates and opens a deinterlace stream object.

Syntax
------

```ManagedCPlusPlus
HRESULT DeinterlaceOpenStream(
  [in] LPDXVA_VideoDesc lpVideoDescription
);
```

Parameters
----------

*lpVideoDescription* \[in\]
Supplies a pointer to a [**DXVA\_VideoDesc**](https://msdn.microsoft.com/library/windows/hardware/ff564070) structure that indicates the type of video to be deinterlaced or rate-converted. The pointer is passed to the driver so that the driver can support the resolution and format of the source video. For example, the driver might be able to perform a three-field adaptive deinterlace of 480i content, but it might only be able to bob 1080i content. All drivers should be able to support bob using the existing [*bit-block transfer*](https://msdn.microsoft.com/library/windows/hardware/ff556272#wdkgloss-bit-block-transfer) hardware.

Return value
------------

Returns zero (S\_OK or DD\_OK) if successful; otherwise, returns an error code. Refer to *ddraw.h* for a complete list of error codes.

Remarks
-------

After a deinterlace mode GUID is found using the [**DeinterlaceQueryAvailableModes**](dxva-deinterlacecontainerdeviceclass-deinterlacequeryavailablemodes.md) function, the deinterlace stream object can be created. This object allows a display driver to reserve any hardware resources that are required to perform the requested deinterlace operations.

For more information about how the driver performs deinterlace or frame-rate-conversion operations using the information supplied by the *lpVideoDescription* parameter, see [Video Content for Deinterlace and Frame-Rate Conversion](https://msdn.microsoft.com/library/windows/hardware/ff570502).

The sample *DeinterlaceOpenStream* function maps directly to the **CreateMoComp** member of the [**DD\_MOTIONCOMPCALLBACKS**](https://msdn.microsoft.com/library/windows/hardware/ff551660) structure, where the GUID is the deinterlace mode requested. The **lpData** member of the [**DD\_CREATEMOCOMPDATA**](https://msdn.microsoft.com/library/windows/hardware/ff550529) structure points to a [**DXVA\_VideoDesc**](https://msdn.microsoft.com/library/windows/hardware/ff564070) structure.

## <span id="see_also"></span>See also


[**DD\_MOTIONCOMPCALLBACKS**](https://msdn.microsoft.com/library/windows/hardware/ff551660)

[**DD\_CREATEMOCOMPDATA**](https://msdn.microsoft.com/library/windows/hardware/ff550529)

[**DeinterlaceQueryAvailableModes**](dxva-deinterlacecontainerdeviceclass-deinterlacequeryavailablemodes.md)

[**DXVA\_VideoDesc**](https://msdn.microsoft.com/library/windows/hardware/ff564070)

 

 






