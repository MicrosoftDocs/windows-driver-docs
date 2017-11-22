---
title: KSINTERFACE\_STANDARD\_STREAMING
description: KSINTERFACE\_STANDARD\_STREAMING
MS-HAID:
- 'ks-interfaces\_e652d63a-559e-46f7-9ff8-b4348b3fbff6.xml'
- 'stream.ksinterface\_standard\_streaming'
MSHAttr:
- 'PreferredSiteName:MSDN'
- 'PreferredLib:/library/windows/hardware'
ms.assetid: 04ba6879-1699-4d12-b81e-a90878014325
keywords: ["KSINTERFACE_STANDARD_STREAMING Streaming Media Devices"]
topic_type:
- apiref
api_name:
- KSINTERFACE_STANDARD_STREAMING
api_type:
- NA
---

# KSINTERFACE\_STANDARD\_STREAMING


## <span id="ddk_ksinterface_standard_streaming_ks"></span><span id="DDK_KSINTERFACE_STANDARD_STREAMING_KS"></span>


The KSINTERFACE\_STANDARD\_STREAMING interface is used between most KS audio filters and is supported by all audio miniports. If a pin supports this interface, the relevant filter processes the data embedded in each [**KSSTREAM\_HEADER**](https://msdn.microsoft.com/library/windows/hardware/ff567138) structure once.

### <span id="see_also"></span><span id="SEE_ALSO"></span>See Also

[KSINTERFACESETID\_Standard](ksinterfacesetid-standard.md), [**KSPIN\_INTERFACE**](https://msdn.microsoft.com/library/windows/hardware/ff563537), [**KSPIN\_DESCRIPTOR**](https://msdn.microsoft.com/library/windows/hardware/ff563533), [**KSSTREAM\_HEADER**](https://msdn.microsoft.com/library/windows/hardware/ff567138)

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bstream\stream%5D:%20KSINTERFACE_STANDARD_STREAMING%20%20RELEASE:%20%2811/22/2017%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")




