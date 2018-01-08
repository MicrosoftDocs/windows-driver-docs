---
title: DXVA\_ProcAmpControlDeviceClass ProcAmpControlCloseStream method
description: The sample ProcAmpCloseStream function closes the ProcAmp stream object and instructs the device driver to release hardware resources associated with the stream.
ms.assetid: aa13efb8-2014-4790-b121-cd9fd3171458
keywords: ["ProcAmpControlCloseStream method Display Devices", "ProcAmpControlCloseStream method Display Devices , DXVA_ProcAmpControlDeviceClass interface", "DXVA_ProcAmpControlDeviceClass interface Display Devices , ProcAmpControlCloseStream method"]
topic_type:
- apiref
api_name:
- DXVA_ProcAmpControlDeviceClass.ProcAmpControlCloseStream
api_type:
- COM
ms.author: windowsdriverdev
ms.date: 01/05/2018
ms.topic: article
ms.prod: windows-hardware
ms.technology: windows-devices
---

# DXVA\_ProcAmpControlDeviceClass::ProcAmpControlCloseStream method


The sample **ProcAmpCloseStream** function closes the ProcAmp stream object and instructs the device driver to release hardware resources associated with the stream.

Syntax
------

```ManagedCPlusPlus
HRESULT ProcAmpControlCloseStream(
   void
);
```

Parameters
----------

**
None

Return value
------------

Returns zero (S\_OK or DD\_OK) if successful; otherwise, returns an error code. Refer to *ddraw.h* for a complete list of error codes.

Remarks
-------

The **ProcAmpControlCloseStream** function maps directly to a **DestroyMoComp** member of the [**DD\_MOTIONCOMPCALLBACKS**](https://msdn.microsoft.com/library/windows/hardware/ff551660) structure, which points to the driver-supplied [*DdMoCompDestroy*](https://msdn.microsoft.com/library/windows/hardware/ff549664) callback.

## <span id="see_also"></span>See also


[**DD\_MOTIONCOMPCALLBACKS**](https://msdn.microsoft.com/library/windows/hardware/ff551660)

[**ProcAmpControlOpenStream**](dxva-procampcontroldeviceclass-procampcontrolopenstream.md)

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20[display\display]:%20DXVA_ProcAmpControlDeviceClass::ProcAmpControlCloseStream%20method%20%20RELEASE:%20%281/4/2018%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")





