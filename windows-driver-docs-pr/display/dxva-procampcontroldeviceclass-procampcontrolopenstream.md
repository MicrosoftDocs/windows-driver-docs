---
title: ProcAmpControlOpenStream method
description: The sample DXVA\_ProcAmpControlDeviceClass::ProcAmpControlOpenStream function creates a ProcAmp stream object.
keywords: ["ProcAmpControlOpenStream method Display Devices", "ProcAmpControlOpenStream method Display Devices , DXVA_ProcAmpControlDeviceClass interface", "DXVA_ProcAmpControlDeviceClass interface Display Devices , ProcAmpControlOpenStream method"]
topic_type:
- apiref
api_name:
- DXVA_ProcAmpControlDeviceClass.ProcAmpControlOpenStream
api_type:
- COM
ms.date: 12/06/2018
ms.localizationpriority: medium
ms.custom: seodec18
---

# DXVA\_ProcAmpControlDeviceClass::ProcAmpControlOpenStream method


The sample *ProcAmpControlOpenStream* function creates a ProcAmp stream object.

## Syntax

```cpp
HRESULT ProcAmpControlOpenStream(
  [in] LPDXVA_VideoDesc lpVideoDescription
);
```

## Parameters

*lpVideoDescription* \[in\]
Supplies a pointer to a [**DXVA\_VideoDesc**](/windows-hardware/drivers/ddi/dxva/ns-dxva-_dxva_videodesc) structure that defines the ProcAmp control parameters for the video to be processed.

## Return value

Returns zero (S\_OK or DD\_OK) if successful; otherwise, returns an error code. Refer to *ddraw.h* for a complete list of error codes.

## Remarks

After the *VMR* has determined the capabilities and ranges of the ProcAmp control hardware using the [**ProcAmpControlQueryCaps**](dxva-deinterlacecontainerdeviceclass-procampcontrolquerycaps.md) and [**ProcAmpControlQueryRange**](dxva-deinterlacecontainerdeviceclass-procampcontrolqueryrange.md) functions, a ProcAmp stream object can be created. Creation of a ProcAmp stream object allows a display driver to reserve hardware resources that are required to perform a ProcAmp adjustment operation.

The *ProcAmpControlOpenStream* function maps directly to a call to the CreateMoComp member of the [**DD\_MOTIONCOMPCALLBACKS**](/windows/win32/api/ddrawint/ns-ddrawint-dd_motioncompcallbacks) structure. The CreateMoComp member points to a driver-supplied function that references the [**DD\_CREATEMOCOMPDATA**](/windows/win32/api/ddrawint/ns-ddrawint-dd_createmocompdata) structure.

## <span id="see_also"></span>See also


[**DXVA\_VideoDesc**](/windows-hardware/drivers/ddi/dxva/ns-dxva-_dxva_videodesc)

[**DD\_MOTIONCOMPCALLBACKS**](/windows/win32/api/ddrawint/ns-ddrawint-dd_motioncompcallbacks)

[**DD\_CREATEMOCOMPDATA**](/windows/win32/api/ddrawint/ns-ddrawint-dd_createmocompdata)

[**ProcAmpControlQueryCaps**](dxva-deinterlacecontainerdeviceclass-procampcontrolquerycaps.md)

[**ProcAmpControlQueryRange**](dxva-deinterlacecontainerdeviceclass-procampcontrolqueryrange.md)

 

