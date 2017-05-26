---
title: Updated friendly name for WDDM 1.2
description: This topic describes the updated friendly name for a Graphics INF. This is a localizable string name requirement for all Windows 8 in-box display driver INFs.
ms.assetid: 26AE24C4-3C0D-4712-B66A-0B93FAD8043C
ms.author: windowsdriverdev
ms.date: 04/20/2017
ms.topic: article
ms.prod: windows-hardware
ms.technology: windows-devices
---

# Updated friendly name for WDDM 1.2


This topic describes the updated friendly name for a Graphics INF. This is a localizable string name requirement for all Windows 8 in-box display driver INFs.

All Windows 8 in-box drivers must use the E3 feature score, regardless of the friendly name. The friendly name will reflect the driver model supported by the INF that's described here.

For Windows Display Driver Model (WDDM) 1.2 drivers that were tested on Windows 8 and that are included in the box in Windows 8, (Microsoft Corporation â€“ WDDM v1.2) must be appended to the device name, as shown in this example:

``` syntax
;
; Localizable Strings
;
IHV_DeviceName.XXX = â€œMy Device Name (Microsoft Corporation â€“ WDDM v1.2)â€
```

**Note**  
To easily highlight drivers for testing only, that are going to enable Windows 8â€“specific optional features that are optimized for Windows 8, we recommend the following input so that users can easily determine that it is not a standard Windows 8 driver. (This should also make bugs easier to triage).

 

For example: WDDM 1.2 specific work

``` syntax
IHV_DeviceName.XXX = â€œMy Device Name (Engineering Sample â€“ WDDM v1.2)â€
```

For WDDM 1.1 drivers that were tested on Windows 8 and that are included in the box in Windows 8, (Microsoft Corporation â€“ WDDM v1.1) must be appended to the device name, as shown in this example:

``` syntax
;
; Localizable Strings
;
IHV_DeviceName.XXX = â€œMy Device Name (Microsoft Corporation â€“ WDDM v1.1)â€
```

For WDDM 1.0 drivers that were tested on Windows 8 and that are included in the box in Windows 8, (Microsoft Corporation â€“ WDDM v1.0) must be appended to the device name, as shown in this example:

``` syntax
;
; Localizable Strings
;
IHV_DeviceName.XXX = â€œMy Device Name (Microsoft Corporation â€“ WDDM v1.0)â€
```

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20[display\display]:%20Updated%20friendly%20name%20for%20WDDM%201.2%20%20RELEASE:%20%282/10/2017%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")




