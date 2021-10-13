---
title: DeinterlaceCloseStream method
description: The sample DXVA\_DeinterlaceBobDeviceClass::DeinterlaceCloseStream function closes the deinterlace stream object and instructs the device driver to release any hardware resource associated with the stream.
keywords: ["DeinterlaceCloseStream method Display Devices", "DeinterlaceCloseStream method Display Devices , DXVA_DeinterlaceBobDeviceClass interface", "DXVA_DeinterlaceBobDeviceClass interface Display Devices , DeinterlaceCloseStream method"]
topic_type:
- apiref
api_name:
- DXVA_DeinterlaceBobDeviceClass.DeinterlaceCloseStream
api_type:
- COM
ms.date: 12/06/2018
ms.localizationpriority: medium
ms.custom: seodec18
---

# DXVA\_DeinterlaceBobDeviceClass::DeinterlaceCloseStream method


The sample *DeinterlaceCloseStream* function closes the deinterlace stream object and instructs the device driver to release any hardware resource associated with the stream.

## Syntax

```cpp
HRESULT DeinterlaceCloseStream();
```

## Parameters

This method has no parameters.

## Return value

Returns zero (S\_OK or DD\_OK) if successful; otherwise, returns an error code. Refer to *ddraw.h* for a complete list of error codes.

## Remarks

The *DeinterlaceCloseStream* function maps directly to the **DestroyMoComp** member of the [**DD\_MOTIONCOMPCALLBACKS**](/windows/win32/api/ddrawint/ns-ddrawint-dd_motioncompcallbacks) structure that points to the driver-supplied *DdMoCompDestroy* callback.

## <span id="see_also"></span>See also


[**DD\_MOTIONCOMPCALLBACKS**](/windows/win32/api/ddrawint/ns-ddrawint-dd_motioncompcallbacks)

[**DeinterlaceOpenStream**](dxva-deinterlacebobdeviceclass-deinterlaceopenstream.md)

 

