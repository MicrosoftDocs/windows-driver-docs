---
title: DEBUG\_REQUEST\_TARGET\_EXCEPTION\_RECORD
description: DEBUG\_REQUEST\_TARGET\_EXCEPTION\_RECORD
ms.assetid: 4bfd3d22-00ab-407c-9a83-ce37c8421491
keywords: ["DEBUG_REQUEST_TARGET_EXCEPTION_RECORD Windows Debugging"]
topic_type:
- apiref
api_name:
- DEBUG_REQUEST_TARGET_EXCEPTION_RECORD
api_type:
- NA
---

# DEBUG\_REQUEST\_TARGET\_EXCEPTION\_RECORD


The DEBUG\_REQUEST\_TARGET\_EXCEPTION\_RECORD [**Request**](request.md) operation returns the exception record for the stored event in a user-mode minidump file.

<span id="InBuffer"></span><span id="inbuffer"></span><span id="INBUFFER"></span>*InBuffer*  
Not used.

<span id="OutBuffer"></span><span id="outbuffer"></span><span id="OUTBUFFER"></span>*OutBuffer*  
The exception record for the stored event. The type of the exception record is EXCEPTION\_RECORD64, which is defined in winnt.h.

## <span id="see_also"></span>See also


[**Request**](request.md)

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20[debugger\debugger]:%20DEBUG_REQUEST_TARGET_EXCEPTION_RECORD%20%20RELEASE:%20%2811/27/2017%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")





