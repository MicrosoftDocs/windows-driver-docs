---
title: Specifying Stream Formats
author: windows-driver-content
description: Specifying Stream Formats
ms.assetid: 60ef129c-f4a1-4eb5-97d9-6be6c7803258
keywords:
- video capture WDK AVStream , stream formats
- capturing video WDK AVStream , stream formats
- stream formats WDK video capture
- formats WDK video capture
ms.author: windowsdriverdev
ms.date: 04/20/2017
ms.topic: article
ms.prod: windows-hardware
ms.technology: windows-devices
---

# Specifying Stream Formats


Generally, DirectShow and kernel streaming share media format definitions and streaming conventions. This uniformity is somewhat obscured by the differences in naming conventions used by kernel-mode and user-mode components. Many media format and GUID definitions used in kernel mode have the prefix *KS\_* but are otherwise identical to their user-mode counterparts. For example, the Win32 user-mode version of the kernel-mode structure, [**KS\_BITMAPINFOHEADER**](https://msdn.microsoft.com/library/windows/hardware/ff567305), is BITMAPINFOHEADER.

A video capture minidriver describes a specific stream format using a [**KSDATAFORMAT**](https://msdn.microsoft.com/library/windows/hardware/ff561656) structure. However, a minidriver can also expose a large range of potential stream formats by specifying an array of [**KSDATARANGE**](https://msdn.microsoft.com/library/windows/hardware/ff561658) structures. The KSDATARANGE structure describes image characteristics such as color format, bit depth, and cropping and scaling possibilities.

A single KSDATARANGE structure can describe thousands of potential KSDATAFORMAT structures. For example, a KSDATARANGE structure could specify a video stream of RGB24 samples with a minimum dimension of 160x120 pixels and a maximum dimension of 720x480 pixels, with granularity stepping size value of 1 in the x and y dimensions. From this, an application could request any of more than 200,000 possible output image dimensions through a unique KSDATAFORMAT structure.

DirectShow uses a structure similar to KSDATAFORMAT to define stream formats. For example:

```
typedef struct  _AMMediaType    {
    GUID majortype;            // Same as KSDATAFORMAT.MajorFormat
    GUID subtype;              // Same as KSDATAFORMAT.SubFormat
    BOOL bFixedSizeSamples;
    BOOL bTemporalCompression;
    ULONG lSampleSize;         // Same as KSDATAFORMAT.SampleSize
    GUID formattype;           // Same as KSDATAFORMAT.Specifier
    IUnknown __RPC_FAR *pUnk;
    ULONG cbFormat;
    BYTE *pbFormat;
 } AM_MEDIA_TYPE;
```

Despite the differences in naming conventions, the GUIDs used in both the kernel-mode KSDATARANGE/KSDATAFORMAT and user-mode AM\_MEDIA\_TYPE structures are identical.

**Note**  : The low-order four bytes of the **SubFormat** member of the KSDATAFORMAT structure (that is analogous to the **subtype** member of the AM\_MEDIA\_TYPE user-mode structure) should match the FOURCC values used in the **biCompression** member of the [**KS\_BITMAPINFOHEADER**](https://msdn.microsoft.com/library/windows/hardware/ff567305) structure. These bytes hold hexadecimal ASCII characters that describe a format, in reverse order.

 

For example, the following GUID corresponds to the YVU9 FOURCC video format:

```
39555659-0000-0010-8000-00AA00389B71
      59 = &#39;Y&#39;
    56 = &#39;V&#39;
  55 = &#39;U&#39;
39 = &#39;9&#39;
```

 

 


--------------------
[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bstream\stream%5D:%20Specifying%20Stream%20Formats%20%20RELEASE:%20%288/23/2016%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")


