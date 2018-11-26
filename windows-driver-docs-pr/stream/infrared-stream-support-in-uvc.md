---
title: Infrared stream support in UVC
description: Provides information on infrared stream support in UVC
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# Infrared stream support in UVC

In Windows 10, version 1607 and later, the inbox USB Video Class (UVC) driver supports cameras that produce infrared (IR) streams. 

These cameras capture the scene’s luma value and transmit the frames over USB as an uncompressed format or as a compressed MJPEG format. These cameras and their streams are exposed to applications through the media capture pipeline. 

The following IR format type GUIDs are used to specify the stream’s video format descriptor so that IR streams are exposed correctly to applications.

These IR format type GUIDs are defined in ksmedia.h:

| IR format type GUID             | Description                          |
|---------------------------------|--------------------------------------|
| KSDATAFORMAT_SUBTYPE_L8_IR      | 8 bit luma-only frames               |
| KSDATAFORMAT_SUBTYPE_L16_IR     | 16 bit luma-only frames              |
| KSDATAFORMAT_SUBTYPE_MJPEG_IR   | MJPEG compressed luma-only frames    |

When these IR format type GUIDs are specified, the capture pipeline automatically marks these streams as IR streams which aids applications in selecting the correct stream for their scenarios.

```cpp
// Example: Format descriptor for UVC 1.1 frame based uncompressed format

typedef struct _VIDEO_FORMAT_FRAME
{
    UCHAR bLength;
    UCHAR bDescriptorType;
    UCHAR bDescriptorSubtype;
    UCHAR bFormatIndex;
    UCHAR bNumFrameDescriptors;
    GUID  guidFormat;           // guidFormat must contain one of the IIR format type GUIDs from the table above
    UCHAR bBitsPerPixel;
    UCHAR bDefaultFrameIndex;
    UCHAR bAspectRatioX;
    UCHAR bAspectRatioY;
    UCHAR bmInterlaceFlags;
    UCHAR bCopyProtect;
    UCHAR bVariableSize;
} VIDEO_FORMAT_FRAME, *PVIDEO_FORMAT_FRAME;
```





