---
title: XR_BIAS to Float Conversion Rules
description: XR_BIAS to Float Conversion Rules
ms.assetid: fef4a1cb-6567-4d8f-aa8a-ceed00eefec8
keywords:
- Direct3D version 10.1 WDK Windows 7 display , converting XR_BIAS to float
- extended format WDK Windows 7 display , converting XR_BIAS to float
- converting XR_BIAS to float WDK Windows 7 display
- XR_BIAS WDK Windows 7 display
- XR_BIAS WDK Windows 7 display , conversion to float
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# XR\_BIAS to Float Conversion Rules


This section applies only to Windows 7 and later operating systems.

The following code shows how to convert XR\_BIAS to float:

```cpp
float XRtoFloat( UINT XRComponent ) {
// The & 0x3ff shows that only 10 bits contribute to the conversion. 
 return (float)( (XRComponent & 0x3ff) - 0x180 ) / 510.f;
}
```

 

 





