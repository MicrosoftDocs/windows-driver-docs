---
title: DEBUG\_REQUEST\_GET\_ADDITIONAL\_CREATE\_OPTIONS control code
description: The DEBUG\_REQUEST\_GET\_ADDITIONAL\_CREATE\_OPTIONS Request operation returns the default process creation options.
ms.assetid: ad4c98d9-ca4e-4ee3-a177-2fe04a8f22e2
keywords: ["DEBUG_REQUEST_GET_ADDITIONAL_CREATE_OPTIONS control code Windows Debugging"]
topic_type:
- apiref
api_name:
- DEBUG_REQUEST_GET_ADDITIONAL_CREATE_OPTIONS
api_type:
- NA
ms.author: windowsdriverdev
ms.date: 11/28/2017
ms.topic: article
ms.prod: windows-hardware
ms.technology: windows-devices
---

# DEBUG\_REQUEST\_GET\_ADDITIONAL\_CREATE\_OPTIONS control code


The DEBUG\_REQUEST\_GET\_ADDITIONAL\_CREATE\_OPTIONS [**Request**](request.md) operation returns the default process creation options.

## <span id="Parameters"></span><span id="parameters"></span><span id="PARAMETERS"></span>Parameters


<span id="InBuffer"></span><span id="inbuffer"></span><span id="INBUFFER"></span>*InBuffer*  
Not used.

<span id="OutBuffer"></span><span id="outbuffer"></span><span id="OUTBUFFER"></span>*OutBuffer*  
The default process creation options. The type of the process creation options is [**DEBUG\_CREATE\_PROCESS\_OPTIONS**](https://msdn.microsoft.com/library/windows/hardware/ff541464).

Remarks
-------

The default process creation options are used by methods [**CreateProcess**](https://msdn.microsoft.com/library/windows/hardware/ff539321) and [**CreateProcessAndAttach**](https://msdn.microsoft.com/library/windows/hardware/ff540048) which, unlike [**CreateProcess2**](https://msdn.microsoft.com/library/windows/hardware/ff539323) and [**CreateProcessAndAttach2**](https://msdn.microsoft.com/library/windows/hardware/ff540055), do not specify the full range of process creation options.

The **CreateFlags** field of the [**DEBUG\_CREATE\_PROCESS\_OPTIONS**](https://msdn.microsoft.com/library/windows/hardware/ff541464) structure is not used as a default because all process creation operations provide this information.

## <span id="see_also"></span>See also


[**Request**](request.md)

[**DEBUG\_REQUEST\_SET\_ADDITIONAL\_CREATE\_OPTIONS**](debug-request-set-additional-create-options.md)

[**DEBUG\_CREATE\_PROCESS\_OPTIONS**](https://msdn.microsoft.com/library/windows/hardware/ff541464)

[**CreateProcess**](https://msdn.microsoft.com/library/windows/hardware/ff539321)

[**CreateProcessAndAttach**](https://msdn.microsoft.com/library/windows/hardware/ff540048)

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20[debugger\debugger]:%20DEBUG_REQUEST_GET_ADDITIONAL_CREATE_OPTIONS%20control%20code%20%20RELEASE:%20%2811/27/2017%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")





