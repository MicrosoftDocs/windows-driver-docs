---
title: Updated friendly name for WDDM 1.2
description: This topic describes the updated friendly name for a Graphics INF. This is a localizable string name requirement for all Windows 8 in-box display driver INFs.
ms.assetid: 26AE24C4-3C0D-4712-B66A-0B93FAD8043C
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# Updated friendly name for WDDM 1.2


This topic describes the updated friendly name for a Graphics INF. This is a localizable string name requirement for all Windows 8 in-box display driver INFs.

All Windows 8 in-box drivers must use the E3 feature score, regardless of the friendly name. The friendly name will reflect the driver model supported by the INF that's described here.

For Windows Display Driver Model (WDDM) 1.2 drivers that were tested on Windows 8 and that are included in the box in Windows 8, (Microsoft Corporation - WDDM v1.2) must be appended to the device name, as shown in this example:

``` syntax
;
; Localizable Strings
;
IHV_DeviceName.XXX = "My Device Name (Microsoft Corporation - WDDM v1.2)"
```

**Note**  
To easily highlight drivers for testing only, that are going to enable Windows 8-specific optional features that are optimized for Windows 8, we recommend the following input so that users can easily determine that it is not a standard Windows 8 driver. (This should also make bugs easier to triage).

 

For example: WDDM 1.2 specific work

``` syntax
IHV_DeviceName.XXX = "My Device Name (Engineering Sample - WDDM v1.2)"
```

For WDDM 1.1 drivers that were tested on Windows 8 and that are included in the box in Windows 8, (Microsoft Corporation - WDDM v1.1) must be appended to the device name, as shown in this example:

``` syntax
;
; Localizable Strings
;
IHV_DeviceName.XXX = "My Device Name (Microsoft Corporation - WDDM v1.1)"
```

For WDDM 1.0 drivers that were tested on Windows 8 and that are included in the box in Windows 8, (Microsoft Corporation - WDDM v1.0) must be appended to the device name, as shown in this example:

``` syntax
;
; Localizable Strings
;
IHV_DeviceName.XXX = "My Device Name (Microsoft Corporation - WDDM v1.0)"
```

 

 





