---
title: WDI_BAND_ID
author: windows-driver-content
description: This topic describes the WDI_BAND_ID data type for WDI miniport drivers.
ms.assetid: 28E34D2C-94A5-4035-ACAA-60CECABF3A02
keywords:
- WDI_BAND_ID, WDK WDI_BAND_ID network drivers
ms.author: windowsdriverdev
ms.date: 11/27/2017
ms.topic: article
ms.prod: windows-hardware
ms.technology: windows-devices
---

# WDI_BAND_ID

The WDI_BAND_ID data type is a UINT32 value that defines a band ID.

```c++
typedef UINT32 WDI_BAND_ID;
```

## Remarks

Possible band ID values are as follows:

| Value |   | Description |
| --- | --- | --- |
| WDI_BAND_ID_ANY | 0xFFFFFFFF | All bands |
| WDI_BAND_ID_2400 | 1 | 2.4 GHz |
| WDI_BAND_ID_5000 | 2 | 5 GHz |
| WDI_BAND_ID_60000 | 3 | 60 GHz |
| WDI_BAND_ID_900 | 4 | 900 MHz |
| WDI_BAND_ID_CUSTOM_START | 0x80000000 |Specifies the start of the range that is used to define a band ID reported by an IHV. |
| WDI_BAND_ID_CUSTOM_END | 0x81000000 | Specifies the end of the range that is used to define a band ID reported by an IHV. |

## Requirements

|   |   |
| --- | --- |
| Minimum supported client | Windows 10 |
| Minimum supported server | Windows Server 2016 |
| Header | Wditypes.hpp |

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bp_mb\p_mb%5D:%20Planning%20your%20APN%20database%20submission%20%20RELEASE:%20%281/18/2017%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")