---
title: DEBUG\_REQUEST\_SET\_LOCAL\_IMPLICIT\_COMMAND\_LINE
description: DEBUG\_REQUEST\_SET\_LOCAL\_IMPLICIT\_COMMAND\_LINE
ms.assetid: c54fc9f3-2805-4411-8162-18d4f9983795
keywords: ["DEBUG_REQUEST_SET_LOCAL_IMPLICIT_COMMAND_LINE Windows Debugging"]
topic_type:
- apiref
api_name:
- DEBUG_REQUEST_SET_LOCAL_IMPLICIT_COMMAND_LINE
api_type:
- NA
ms.author: domars
ms.date: 11/28/2017
ms.localizationpriority: medium
---

# DEBUG\_REQUEST\_SET\_LOCAL\_IMPLICIT\_COMMAND\_LINE


The DEBUG\_REQUEST\_SET\_LOCAL\_IMPLICIT\_COMMAND\_LINE [**Request**](request.md) operation sets the [debugger engine](https://msdn.microsoft.com/library/windows/hardware/ff551059#debugger-engine)'s implicit command line.

**Parameters**

<span id="InBuffer"></span><span id="inbuffer"></span><span id="INBUFFER"></span>*InBuffer*  
The new implicit command line. The type of *InBuffer* is a pointer to a Unicode string (PWSTR). The pointer is copied but the string it points to is not copied.

<span id="OutBuffer"></span><span id="outbuffer"></span><span id="OUTBUFFER"></span>*OutBuffer*  
Not used.

Remarks
-------

The implicit command line can be used as the command line when creating a process. The process creation options ([**DEBUG\_CREATE\_PROCESS\_OPTIONS**](https://msdn.microsoft.com/library/windows/hardware/ff541464)) contain an option for using the implicit command line instead of a supplied command line when creating a process.

## <span id="see_also"></span>See also


[**Request**](request.md)

[**DEBUG\_CREATE\_PROCESS\_OPTIONS**](https://msdn.microsoft.com/library/windows/hardware/ff541464)

[**DEBUG\_REQUEST\_GET\_ADDITIONAL\_CREATE\_OPTIONS**](debug-request-get-additional-create-options.md)

[**DEBUG\_REQUEST\_SET\_ADDITIONAL\_CREATE\_OPTIONS**](debug-request-set-additional-create-options.md)

[**CreateProcess2**](https://msdn.microsoft.com/library/windows/hardware/ff539323)

[**CreateProcessAndAttach2**](https://msdn.microsoft.com/library/windows/hardware/ff540055)

 

 






