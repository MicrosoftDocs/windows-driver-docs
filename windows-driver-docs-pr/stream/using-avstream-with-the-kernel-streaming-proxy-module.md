---
title: Using AVStream with the Kernel Streaming Proxy Module
description: Using AVStream with the Kernel Streaming Proxy Module
ms.assetid: c8ae1385-337e-46ad-841e-fbdf5d685210
keywords:
- Kernel Streaming Proxy WDK AVStream
- KS proxy WDK AVStream
- proxy user-mode connections WDK AVStream
- media types WDK AVStream
- DirectShow filters WDK AVStream
- AVStream Kernel Streaming Proxy WDK
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# Using AVStream with the Kernel Streaming Proxy Module





Kernel-mode filters often are connected in user mode through the [Kernel Streaming Proxy](https://msdn.microsoft.com/library/windows/hardware/ff560877). This proxy makes a kernel-mode filter appear to user mode as a DirectShow filter.

When this mode of connection is used, DirectShow connects the filters by intersecting their *media types*. These media types are the DirectShow counterpart to data formats in kernel mode.

When DirectShow enumerates a media type on a kernel-mode pin, the corresponding data range on the pin is intersected with the pin's data range. This intersection yields a data format, as described in [Data Range Intersections in AVStream](data-range-intersections-in-avstream.md). The proxy converts the resulting data format into a DirectShow media type.

As in kernel mode, the proxy either asks a data handler to determine whether the media type is acceptable, or it determines whether the media type is a partial match for a data range on the pin. A partial match indicates that, in the context of kernel-mode semantics, the major type, subformat, specifier, and required attributes match. If the media type is a partial match, the connection proceeds.

Before the connection is complete, AVStream calls the minidriver's [*AVStrMiniPinSetDataFormat*](https://msdn.microsoft.com/library/windows/hardware/ff556355) dispatch to inform the minidriver of the data format being set. This format corresponds to the user-mode media type that was suggested to the proxied pin. AVStream also provides the data range that was determined to be a partial match for the format.

 

 




