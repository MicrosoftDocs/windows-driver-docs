---
title: AV/C Streaming Protocol Driver Function Codes
description: AV/C Streaming Protocol Driver Function Codes
ms.assetid: c76662fc-8bb9-411a-8672-d00a4533e952
---

# AV/C Streaming Protocol Driver Function Codes


## <span id="ddk_av_c_streaming_protocol_driver_function_codes_ks"></span><span id="DDK_AV_C_STREAMING_PROTOCOL_DRIVER_FUNCTION_CODES_KS"></span>


The AV/C Streaming filter driver intercepts IRPs on their way down the device stack.

To communicate with *avcstrm.sys*, subunit drivers must set their IRP's **IoControlCode** member to IOCTL\_AVCSTRM\_CLASS.

To make I/O requests, include the header file *avcstrm.h*, which is included with the Microsoft Windows Driver Kit (WDK).

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bstream\stream%5D:%20AV/C%20Streaming%20Protocol%20Driver%20Function%20Codes%20%20RELEASE:%20%2811/22/2017%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")




