---
title: Using AVStream with the Kernel Streaming Proxy Module
author: windows-driver-content
description: Using AVStream with the Kernel Streaming Proxy Module
ms.assetid: c8ae1385-337e-46ad-841e-fbdf5d685210
keywords: ["Kernel Streaming Proxy WDK AVStream", "KS proxy WDK AVStream", "proxy user-mode connections WDK AVStream", "media types WDK AVStream", "DirectShow filters WDK AVStream", "AVStream Kernel Streaming Proxy WDK"]
---

# Using AVStream with the Kernel Streaming Proxy Module


## <a href="" id="ddk-using-avstream-with-the-kernel-streaming-proxy-module-ksg"></a>


Kernel-mode filters often are connected in user mode through the [Kernel Streaming Proxy](https://msdn.microsoft.com/library/windows/hardware/ff560877). This proxy makes a kernel-mode filter appear to user mode as a DirectShow filter.

When this mode of connection is used, DirectShow connects the filters by intersecting their *media types*. These media types are the DirectShow counterpart to data formats in kernel mode.

When DirectShow enumerates a media type on a kernel-mode pin, the corresponding data range on the pin is intersected with the pin's data range. This intersection yields a data format, as described in [Data Range Intersections in AVStream](data-range-intersections-in-avstream.md). The proxy converts the resulting data format into a DirectShow media type.

As in kernel mode, the proxy either asks a data handler to determine whether the media type is acceptable, or it determines whether the media type is a partial match for a data range on the pin. A partial match indicates that, in the context of kernel-mode semantics, the major type, subformat, specifier, and required attributes match. If the media type is a partial match, the connection proceeds.

Before the connection is complete, AVStream calls the minidriver's [*AVStrMiniPinSetDataFormat*](https://msdn.microsoft.com/library/windows/hardware/ff556355) dispatch to inform the minidriver of the data format being set. This format corresponds to the user-mode media type that was suggested to the proxied pin. AVStream also provides the data range that was determined to be a partial match for the format.

 

 


--------------------
[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bstream\stream%5D:%20Using%20AVStream%20with%20the%20Kernel%20Streaming%20Proxy%20Module%20%20RELEASE:%20%288/23/2016%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")


