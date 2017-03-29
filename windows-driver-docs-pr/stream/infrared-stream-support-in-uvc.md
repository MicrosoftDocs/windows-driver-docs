---
title: Infrared stream support in UVC
author: windows-driver-content
description: Provides information on infrared stream support in UVC
---

# Infrared stream support in UVC

In Windows 10, version 1607 and later, the inbox USB Video Class (UVC) driver supports cameras that produce infrared (IR) streams. 

These cameras capture the scene’s luma value and transmit the frames over USB as an uncompressed format or as a compressed MJPEG format. These cameras and their streams are exposed to applications through the media capture pipeline. 

The following IR format type GUIDs are used to specify the stream’s video format descriptor so that IR streams are exposed correctly to applications.

These IR format type GUIDs are defined in ksmedia.h:

| IR format type GUID             | Description                          |
|---------------------------------|--------------------------------------|
| KSDATAFORMAT_SUBTYPE_L8_IR      | 8 bit luma only frames               |
| KSDATAFORMAT_SUBTYPE_L16_IR     | 16 bit luma only frames              |
| KSDATAFORMAT_SUBTYPE_MJPEG_IR   | MJPEG compressed luma only frames    |

When these IR format type GUIDs are specified, the capture pipeline automatically marks these streams as IR streams which aids applications in selecting the correct stream for their scenarios.

```
// Example: Format Descriptor for UVC 1.1 frame based uncompressed format

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




--------------------
[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bprint\print%5D:%20Slicer%20settings%20%20RELEASE:%20%289/2/2016%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")

