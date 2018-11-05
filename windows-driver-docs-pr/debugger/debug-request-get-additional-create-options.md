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
ms.author: domars
ms.date: 11/28/2017
ms.localizationpriority: medium
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

 

 






