---
title: Specifying Stream Formats
description: Specifying Stream Formats
ms.assetid: 60ef129c-f4a1-4eb5-97d9-6be6c7803258
keywords:
- video capture WDK AVStream , stream formats
- capturing video WDK AVStream , stream formats
- stream formats WDK video capture
- formats WDK video capture
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# Specifying Stream Formats


Generally, DirectShow and kernel streaming share media format definitions and streaming conventions. This uniformity is somewhat obscured by the differences in naming conventions used by kernel-mode and user-mode components. Many media format and GUID definitions used in kernel mode have the prefix *KS\_* but are otherwise identical to their user-mode counterparts. For example, the Win32 user-mode version of the kernel-mode structure, [**KS\_BITMAPINFOHEADER**](https://msdn.microsoft.com/library/windows/hardware/ff567305), is BITMAPINFOHEADER.

A video capture minidriver describes a specific stream format using a [**KSDATAFORMAT**](https://msdn.microsoft.com/library/windows/hardware/ff561656) structure. However, a minidriver can also expose a large range of potential stream formats by specifying an array of [**KSDATARANGE**](https://msdn.microsoft.com/library/windows/hardware/ff561658) structures. The KSDATARANGE structure describes image characteristics such as color format, bit depth, and cropping and scaling possibilities.

A single KSDATARANGE structure can describe thousands of potential KSDATAFORMAT structures. For example, a KSDATARANGE structure could specify a video stream of RGB24 samples with a minimum dimension of 160x120 pixels and a maximum dimension of 720x480 pixels, with granularity stepping size value of 1 in the x and y dimensions. From this, an application could request any of more than 200,000 possible output image dimensions through a unique KSDATAFORMAT structure.

DirectShow uses a structure similar to KSDATAFORMAT to define stream formats. For example:

```cpp
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

```Text
39555659-0000-0010-8000-00AA00389B71
      59 = 'Y'
    56 = 'V'
  55 = 'U'
39 = '9'
```
