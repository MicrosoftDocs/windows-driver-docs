---
title: User Values
author: windows-driver-content
description: User Values
MS-HAID:
- 'di\_f77f7f1f-952f-4a34-a766-07a8a5e86575.xml'
- 'hid.user\_values'
MSHAttr:
- 'PreferredSiteName:MSDN'
- 'PreferredLib:/library/windows/hardware'
ms.assetid: 42b57fc2-fda0-464a-83dc-3e63ef693e9f
keywords: ["user registry settings WDK joysticks"]
---

# User Values


## <a href="" id="ddk-user-values-di"></a>


A single value named REGSTR\_VAL\_JOYUSERVALUES stores the structure described below. This structure specifies how data should be manipulated by VJoyD when an application requests that data be scaled, centered, or have a dead zone defined.

```
struct {
    /* value at which to time-out internal joystick polling */
    DWORD   dwTimeOut;
 
    /* range of values app wants returned for axes */
    struct { 
        /* minimums for each axis */
        struct {
            DWORD    dwX;
            DWORD    dwY;
            DWORD    dwZ;
            DWORD    dwR;
            DWORD    dwU;
            DWORD    dwV;
        } jpMin;
        /* maximums for each axis */
        struct {
            DWORD    dwX;
            DWORD    dwY;
            DWORD    dwZ;
            DWORD    dwR;
            DWORD    dwU;
            DWORD    dwV;
        } jpMax;
        /* center positions for each axis */
        struct {
            DWORD    dwX;
            DWORD    dwY;
            DWORD    dwZ;
            DWORD    dwR;
            DWORD    dwU;
            DWORD    dwV;
        } jpCenter;
    } jrvRanges;
 
    /* area around center to be considered as "dead". specified as */
    /* a percentage (0-100). Only X & Y handled by system driver */
    struct {
        DWORD    dwX;
        DWORD    dwY;
        DWORD    dwZ;
        DWORD    dwR;
        DWORD    dwU;
        DWORD    dwV;
    } jpDeadZone;
}
```

 

 


--------------------
[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bhid\hid%5D:%20User%20Values%20%20RELEASE:%20%287/18/2016%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")


