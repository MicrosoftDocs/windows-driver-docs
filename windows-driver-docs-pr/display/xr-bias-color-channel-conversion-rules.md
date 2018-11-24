---
title: XR_BIAS Color Channel Conversion Rules
description: XR_BIAS Color Channel Conversion Rules
ms.assetid: B3014241-A86A-4B6E-BC9D-50057B924D98
ms.localizationpriority: medium
ms.date: 10/17/2018
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

 

 

 





