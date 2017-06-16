---
title: Multiple Binary Opt-In POOL\_NX\_OPTIN\_AUTO
author: windows-driver-content
description: If you are a hardware vendor who supplies different driver binaries for different versions of Windows, you can use the POOL\_NX\_OPTIN\_AUTO opt-in mechanism.
ms.assetid: 5E6759E3-3AF8-4427-BDD0-DB64B3D480A1
---

# Multiple Binary Opt-In: POOL\_NX\_OPTIN\_AUTO


If you are a hardware vendor who supplies different driver binaries for different versions of Windows, you can use the POOL\_NX\_OPTIN\_AUTO opt-in mechanism. This porting aid builds a separate driver binary for Windows 8 and for each earlier version of Windows that your driver supports.

To use this opt-in mechanism, define POOL\_NX\_OPTIN\_AUTO=1 for all source files that you want to opt-in. To do this, include the following preprocessor definition in the appropriate property page for your driver project:

`C_DEFINES=$(C_DEFINES) -DPOOL_NX_OPTIN_AUTO=1`

For most drivers, this definition is sufficient to enable the opt-in mechanism to create a different binary for each version of Windows that you support.

## Implementation details


The POOL\_NX\_OPTIN\_AUTO definition redefines the **NonPagedPool** constant name to **NonPagedPoolNx**. The redefined pool type is still a compile-time constant. The macro that converts instances of the **NonPagedPool** constant name to **NonPagedPoolNx** also converts instances of **NonPagedPoolCacheAligned** to **NonPagedPoolNxCacheAligned.**

 

 


--------------------
[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bkernel\kernel%5D:%20Multiple%20Binary%20Opt-In:%20POOL_NX_OPTIN_AUTO%20%20RELEASE:%20%286/14/2017%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")


