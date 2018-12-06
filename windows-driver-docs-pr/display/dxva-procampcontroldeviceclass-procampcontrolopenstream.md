---
title: DXVA\_ProcAmpControlDeviceClass ProcAmpControlOpenStream method
description: The sample ProcAmpControlOpenStream function creates a ProcAmp stream object.
ms.assetid: 73011ce3-f643-4fca-bcfd-1467a9b56181
keywords: ["ProcAmpControlOpenStream method Display Devices", "ProcAmpControlOpenStream method Display Devices , DXVA_ProcAmpControlDeviceClass interface", "DXVA_ProcAmpControlDeviceClass interface Display Devices , ProcAmpControlOpenStream method"]
topic_type:
- apiref
api_name:
- DXVA_ProcAmpControlDeviceClass.ProcAmpControlOpenStream
api_type:
- COM
ms.date: 01/05/2018
ms.localizationpriority: medium
---

# DXVA\_ProcAmpControlDeviceClass::ProcAmpControlOpenStream method


The sample *ProcAmpControlOpenStream* function creates a ProcAmp stream object.

Syntax
------

```ManagedCPlusPlus
HRESULT ProcAmpControlOpenStream(
  [in] LPDXVA_VideoDesc lpVideoDescription
);
```

Parameters
----------

*lpVideoDescription* \[in\]
Supplies a pointer to a [**DXVA\_VideoDesc**](https://msdn.microsoft.com/library/windows/hardware/ff564070) structure that defines the ProcAmp control parameters for the video to be processed.

Return value
------------

Returns zero (S\_OK or DD\_OK) if successful; otherwise, returns an error code. Refer to *ddraw.h* for a complete list of error codes.

Remarks
-------

After the [*VMR*](https://msdn.microsoft.com/library/windows/hardware/ff556344#wdkgloss-video-mixer-renderer--vmr-) has determined the capabilities and ranges of the ProcAmp control hardware using the [**ProcAmpControlQueryCaps**](dxva-deinterlacecontainerdeviceclass-procampcontrolquerycaps.md) and [**ProcAmpControlQueryRange**](dxva-deinterlacecontainerdeviceclass-procampcontrolqueryrange.md) functions, a ProcAmp stream object can be created. Creation of a ProcAmp stream object allows a display driver to reserve hardware resources that are required to perform a ProcAmp adjustment operation.

The *ProcAmpControlOpenStream* function maps directly to a call to the CreateMoComp member of the [**DD\_MOTIONCOMPCALLBACKS**](https://msdn.microsoft.com/library/windows/hardware/ff551660) structure. The CreateMoComp member points to a driver-supplied function that references the [**DD\_CREATEMOCOMPDATA**](https://msdn.microsoft.com/library/windows/hardware/ff550529) structure.

## <span id="see_also"></span>See also


[**DXVA\_VideoDesc**](https://msdn.microsoft.com/library/windows/hardware/ff564070)

[**DD\_MOTIONCOMPCALLBACKS**](https://msdn.microsoft.com/library/windows/hardware/ff551660)

[**DD\_CREATEMOCOMPDATA**](https://msdn.microsoft.com/library/windows/hardware/ff550529)

[**ProcAmpControlQueryCaps**](dxva-deinterlacecontainerdeviceclass-procampcontrolquerycaps.md)

[**ProcAmpControlQueryRange**](dxva-deinterlacecontainerdeviceclass-procampcontrolqueryrange.md)

 

 






