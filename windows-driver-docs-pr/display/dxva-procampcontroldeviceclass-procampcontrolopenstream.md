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
ms.author: windowsdriverdev
ms.date: 01/05/2018
ms.topic: article
ms.prod: windows-hardware
ms.technology: windows-devices
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

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20[display\display]:%20DXVA_ProcAmpControlDeviceClass::ProcAmpControlOpenStream%20method%20%20RELEASE:%20%281/4/2018%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")





