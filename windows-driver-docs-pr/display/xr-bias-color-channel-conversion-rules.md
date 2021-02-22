---
title: XR_BIAS color channel conversion rules
description: Describes XR_BIAS color channel conversion rules
ms.localizationpriority: medium
ms.date: 10/17/2018
---

# XR_BIAS Color Channel Conversion Rules

This section applies to Windows 7 and later operating systems.

These topics provide the requirements for converting between XR_BIAS and other color channels:

* [XR_BIAS to Float Conversion Rules](xr-bias-to-float-conversion-rules.md)

* [Float to XR_BIAS Conversion Rules](float-to-xr-bias-conversion-rules.md)

* [Conversion from BGR8888 to XR_BIAS](conversion-from-bgr8888-to-xr-bias.md)

These are some example converted values using the conversion rules:

| Frame buffer value | Interpretation |
|--------------------|----------------|
| 000 = 0x000        | -0.7529        |
| 129 = 0x081        | -0.5000        |
| 384 = 0x180        | 0.0000         |
| 639 = 0x27f        | 0.5000         |
| 894 = 0x37e        | 1.0000         |
| 1023 = 0x3ff       | 1.2529         |
