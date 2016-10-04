---
title: Capturing Uncompressed Data to VRAM
author: windows-driver-content
description: Capturing Uncompressed Data to VRAM
MS-HAID:
- 'gpucap\_70206040-4a1d-4e01-a01e-db8e00a27d27.xml'
- 'stream.capturing\_uncompressed\_data\_to\_vram'
MSHAttr:
- 'PreferredSiteName:MSDN'
- 'PreferredLib:/library/windows/hardware'
ms.assetid: efec607d-3337-40a5-812c-57292f201d54
keywords: ["VRAM capture WDK AVStream , uncompressed data", "uncompressed data WDK VRAM capture", "formats WDK VRAM capture", "pin VRAM processing WDK AVStream"]
---

# Capturing Uncompressed Data to VRAM


AVStream minidrivers that are VRAM-enabled can capture uncompressed data by providing the following support in the capture pin descriptor.

-   In the corresponding [**KSPIN\_DESCRIPTOR**](https://msdn.microsoft.com/library/windows/hardware/ff563533) structure, list the formats that the capture pin supports in the **DataRanges** member, an array of [**KSDATARANGE**](https://msdn.microsoft.com/library/windows/hardware/ff561658) structures. Provide pointers to KS\_DATARANGE\_VIDEO structures, cast as pointers to KSDATARANGE.

-   In the **VideoInfoHeader** member of each [**KS\_DATARANGE\_VIDEO**](https://msdn.microsoft.com/library/windows/hardware/ff567628) structure, provide a [**KS\_VIDEOINFOHEADER**](https://msdn.microsoft.com/library/windows/hardware/ff567700) structure. Each KS\_VIDEOINFOHEADER contains a [**KS\_BITMAPINFOHEADER**](https://msdn.microsoft.com/library/windows/hardware/ff567305).

-   To expose binary formats for MPEG2 capture, set **biCompression** equal to D3DDDIFMT\_BINARYBUFFER, **biHeight** equal to one, and **biWidth** equal to the size of the binary buffer.

The *Capture.cpp* file of the [AVStream Simulated Hardware Sample Driver (AVSHwS)](http://go.microsoft.com/fwlink/p/?linkid=256083) in the MSDN Code Gallery contains examples of the items in the preceding list.

 

 


--------------------
[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bstream\stream%5D:%20Capturing%20Uncompressed%20Data%20to%20VRAM%20%20RELEASE:%20%288/23/2016%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")


