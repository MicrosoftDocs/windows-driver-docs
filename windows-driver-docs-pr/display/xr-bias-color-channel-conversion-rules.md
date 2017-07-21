---
title: XR_BIAS Color Channel Conversion Rules
description: XR_BIAS Color Channel Conversion Rules
ms.assetid: B3014241-A86A-4B6E-BC9D-50057B924D98
---

# XR\_BIAS Color Channel Conversion Rules


This section applies only to Windows 7 and later operating systems.

These topics provide the requirements for converting between XR\_BIAS and other color channels:

[XR\_BIAS to Float Conversion Rules](xr-bias-to-float-conversion-rules.md)

[Float to XR\_BIAS Conversion Rules](float-to-xr-bias-conversion-rules.md)

[Conversion from BGR8888 to XR\_BIAS](conversion-from-bgr8888-to-xr-bias.md)

These are some example converted values using the conversion rules:

| Frame buffer value | Interpretation |
|--------------------|----------------|
| 000 = 0x000        | -0.7529        |
| 129 = 0x081        | -0.5000        |
| 384 = 0x180        | 0.0000         |
| 639 = 0x27f        | 0.5000         |
| 894 = 0x37e        | 1.0000         |
| 1023 = 0x3ff       | 1.2529         |

 

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20[display\display]:%20XR_BIAS%20Color%20Channel%20Conversion%20Rules%20%20RELEASE:%20%282/10/2017%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")




