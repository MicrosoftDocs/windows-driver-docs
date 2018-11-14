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
ms.date: 01/05/2018
ms.localizationpriority: medium
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

 

 






