---
title: AV/C Streaming Protocol Driver Function Codes
description: AV/C Streaming Protocol Driver Function Codes
ms.assetid: c76662fc-8bb9-411a-8672-d00a4533e952
ms.date: 11/28/2017
ms.localizationpriority: medium
---

# AV/C Streaming Protocol Driver Function Codes


## <span id="ddk_av_c_streaming_protocol_driver_function_codes_ks"></span><span id="DDK_AV_C_STREAMING_PROTOCOL_DRIVER_FUNCTION_CODES_KS"></span>


The AV/C Streaming filter driver intercepts IRPs on their way down the device stack.

To communicate with *avcstrm.sys*, subunit drivers must set their IRP's **IoControlCode** member to IOCTL\_AVCSTRM\_CLASS.

To make I/O requests, include the header file *avcstrm.h*, which is included with the Microsoft Windows Driver Kit (WDK).

 

 





