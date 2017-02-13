---
title: XR\_BIAS to Float Conversion Rules
description: XR\_BIAS to Float Conversion Rules
ms.assetid: fef4a1cb-6567-4d8f-aa8a-ceed00eefec8
keywords: ["Direct3D version 10.1 WDK Windows 7 display , converting XR_BIAS to float", "extended format WDK Windows 7 display , converting XR_BIAS to float", "converting XR_BIAS to float WDK Windows 7 display", "XR_BIAS WDK Windows 7 display", "XR_BIAS WDK Windows 7 display , conversion to float"]
---

# XR\_BIAS to Float Conversion Rules


This section applies only to Windows 7 and later operating systems.

The following code shows how to convert XR\_BIAS to float:

```
float XRtoFloat( UINT XRComponent ) {
// The & 0x3ff shows that only 10 bits contribute to the conversion. 
 return (float)( (XRComponent & 0x3ff) â€“ 0x180 ) / 510.f;
}
```

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20[display\display]:%20XR_BIAS%20to%20Float%20Conversion%20Rules%20%20RELEASE:%20%282/10/2017%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")




