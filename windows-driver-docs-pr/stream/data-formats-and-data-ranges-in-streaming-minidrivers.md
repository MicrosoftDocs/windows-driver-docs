---
title: Data Formats and Data Ranges in Streaming Minidrivers
author: windows-driver-content
description: Data Formats and Data Ranges in Streaming Minidrivers
MS-HAID:
- 'strmini-design\_5e252099-fd08-44f4-b35a-3be2a13419b0.xml'
- 'stream.data\_formats\_and\_data\_ranges\_in\_streaming\_minidrivers'
MSHAttr:
- 'PreferredSiteName:MSDN'
- 'PreferredLib:/library/windows/hardware'
ms.assetid: ea3aa4af-0c8c-429e-b399-0a196eadc5ef
keywords: ["Stream.sys class driver WDK Windows 2000 Kernel , data formats and ranges", "streaming minidrivers WDK Windows 2000 Kernel , data formats and ranges", "minidrivers WDK Windows 2000 Kernel Streaming , data formats and ranges", "data formats WDK streaming minidriver", "data ranges WDK streaming minidriver", "ranges WDK streaming minidriver", "formats WDK streaming minidriver"]
---

# Data Formats and Data Ranges in Streaming Minidrivers


## <a href="" id="ddk-data-formats-and-data-ranges-in-streaming-minidrivers-ksg"></a>


Each stream details the data ranges it supports in the **StreamFormatsArray** member of its [**HW\_STREAM\_INFORMATION**](https://msdn.microsoft.com/library/windows/hardware/ff559692) structure.

For more information about formats and range intersection, see [Data Range Intersections in AVStream](data-range-intersections-in-avstream.md).

 

 


--------------------
[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bstream\stream%5D:%20Data%20Formats%20and%20Data%20Ranges%20in%20Streaming%20Minidrivers%20%20RELEASE:%20%288/23/2016%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")


