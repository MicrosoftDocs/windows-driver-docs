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
ms.topic: article
ms.prod: windows-hardware
ms.technology: windows-devices
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

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20[debugger\debugger]:%20DEBUG_REQUEST_SET_LOCAL_IMPLICIT_COMMAND_LINE%20%20RELEASE:%20%2811/27/2017%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")





