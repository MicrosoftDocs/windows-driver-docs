---
title: KSINTERFACE\_STANDARD\_LOOPED\_STREAMING
description: KSINTERFACE\_STANDARD\_LOOPED\_STREAMING
ms.assetid: c12e7085-fa13-48d3-b4ed-ea0a708f026b
keywords: ["KSINTERFACE_STANDARD_LOOPED_STREAMING Streaming Media Devices"]
topic_type:
- apiref
api_name:
- KSINTERFACE_STANDARD_LOOPED_STREAMING
api_type:
- NA
ms.author: windowsdriverdev
ms.date: 11/28/2017
ms.topic: article
ms.prod: windows-hardware
ms.technology: windows-devices
---

# KSINTERFACE\_STANDARD\_LOOPED\_STREAMING


## <span id="ddk_ksinterface_standard_looped_streaming_ks"></span><span id="DDK_KSINTERFACE_STANDARD_LOOPED_STREAMING_KS"></span>


The KSINTERFACE\_STANDARD\_LOOPED\_STREAMING interface is used by clients of DSound. At release time of Windows XP, Kmixer and Portcls are the only KS Audio filters that support this interface.

If a pin supports KSINTERFACE\_STANDARD\_LOOPED\_STREAMING, the relevant filter does not complete buffers until the pin is placed into the *Stop* state. The filter processes data by continuously looping around the data in the single buffer submitted to the filter.

### <span id="see_also"></span><span id="SEE_ALSO"></span>See Also

[KSINTERFACESETID\_Standard](ksinterfacesetid-standard.md), [**KSPIN\_INTERFACE**](https://msdn.microsoft.com/library/windows/hardware/ff563537), [**KSPIN\_DESCRIPTOR**](https://msdn.microsoft.com/library/windows/hardware/ff563533)

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bstream\stream%5D:%20KSINTERFACE_STANDARD_LOOPED_STREAMING%20%20RELEASE:%20%2811/22/2017%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")




