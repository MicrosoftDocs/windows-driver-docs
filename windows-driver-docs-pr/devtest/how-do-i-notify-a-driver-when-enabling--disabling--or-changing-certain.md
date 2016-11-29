---
title: How do I notify a driver when enabling, disabling, or changing certain flags
description: How do I notify a driver when enabling, disabling, or changing certain flags
ms.assetid: 1bdf8047-8d3f-4cdf-883b-3544dea06705
---

# How do I notify a driver when enabling, disabling, or changing certain flags?


Some drivers need to do some additional work when trace flags are enabled, disabled, or changed. To notify a driver when such changes occur, use the following command:

```
#define WPP_PRIVATE_ENABLE_CALLBACK 
```

This symbolic constant must be defined before including the TMH file. The function signature that you will need to write is as follows:

```
typedef
VOID
(*PFN_WPP_PRIVATE_ENABLE_CALLBACK)(
__in LPCGUID Guid,
__in __int64 Logger,
__in BOOLEAN Enable,
__in ULONG Flags,
__in UCHAR Level);
 
```

The following is an example of how to notify a driver when certain flags are enabled:

```
#define WPP_PRIVATE_ENABLE_CALLBACK MyOwnCallback
#include "tracedrv.tmh" // this is the file that will be auto-generated 
VOID MyOwnCallback (
                 __in LPCGUID Guid,
                 __in __int64 Logger,
                 __in BOOLEAN Enable,
                 __in ULONG Flags,
                 __in UCHAR Level) 
{
//                
//                  This callback function will be called with the current values of : GUID, Logger, Enable, Flags, and Level
//                 
 
                  if (Enable) {
                        .
                        .
                   }
} 
```

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20[devtest\devtest]:%20How%20do%20I%20notify%20a%20driver%20when%20enabling,%20disabling,%20or%20changing%20certain%20flags?%20%20RELEASE:%20%2811/17/2016%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")




