---
title: ProcAmpControlCloseStream method
description: The sample DXVA\_ProcAmpControlDeviceClass::ProcAmpCloseStream function closes the ProcAmp stream object and instructs the device driver to release hardware resources associated with the stream.
keywords: ["ProcAmpControlCloseStream method Display Devices", "ProcAmpControlCloseStream method Display Devices , DXVA_ProcAmpControlDeviceClass interface", "DXVA_ProcAmpControlDeviceClass interface Display Devices , ProcAmpControlCloseStream method"]
topic_type:
- apiref
api_name:
- DXVA_ProcAmpControlDeviceClass.ProcAmpControlCloseStream
api_type:
- COM
ms.date: 12/06/2018
ms.localizationpriority: medium
ms.custom: seodec18
---

# DXVA\_ProcAmpControlDeviceClass::ProcAmpControlCloseStream method


The sample **ProcAmpCloseStream** function closes the ProcAmp stream object and instructs the device driver to release hardware resources associated with the stream.

## Syntax

```cpp
HRESULT ProcAmpControlCloseStream(
   void
);
```

## Parameters

**
None

## Return value

Returns zero (S\_OK or DD\_OK) if successful; otherwise, returns an error code. Refer to *ddraw.h* for a complete list of error codes.

## Remarks

The **ProcAmpControlCloseStream** function maps directly to a **DestroyMoComp** member of the [**DD\_MOTIONCOMPCALLBACKS**](/windows/win32/api/ddrawint/ns-ddrawint-dd_motioncompcallbacks) structure, which points to the driver-supplied [*DdMoCompDestroy*](/windows/win32/api/ddrawint/nc-ddrawint-pdd_mocompcb_destroy) callback.

## <span id="see_also"></span>See also


[**DD\_MOTIONCOMPCALLBACKS**](/windows/win32/api/ddrawint/ns-ddrawint-dd_motioncompcallbacks)

[**ProcAmpControlOpenStream**](dxva-procampcontroldeviceclass-procampcontrolopenstream.md)

 

