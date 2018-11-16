---
title: Multiple Binary Opt-In POOL_NX_OPTIN_AUTO
description: If you are a hardware vendor who supplies different driver binaries for different versions of Windows, you can use the POOL_NX_OPTIN_AUTO opt-in mechanism.
ms.assetid: 5E6759E3-3AF8-4427-BDD0-DB64B3D480A1
ms.localizationpriority: medium
ms.date: 10/17/2018
---

# Multiple Binary Opt-In: POOL\_NX\_OPTIN\_AUTO


If you are a hardware vendor who supplies different driver binaries for different versions of Windows, you can use the POOL\_NX\_OPTIN\_AUTO opt-in mechanism. This porting aid builds a separate driver binary for Windows 8 and for each earlier version of Windows that your driver supports.

To use this opt-in mechanism, define POOL\_NX\_OPTIN\_AUTO=1 for all source files that you want to opt-in. To do this, include the following preprocessor definition in the appropriate property page for your driver project:

`C_DEFINES=$(C_DEFINES) -DPOOL_NX_OPTIN_AUTO=1`

For most drivers, this definition is sufficient to enable the opt-in mechanism to create a different binary for each version of Windows that you support.

## Implementation details


The POOL\_NX\_OPTIN\_AUTO definition redefines the **NonPagedPool** constant name to **NonPagedPoolNx**. The redefined pool type is still a compile-time constant. The macro that converts instances of the **NonPagedPool** constant name to **NonPagedPoolNx** also converts instances of **NonPagedPoolCacheAligned** to **NonPagedPoolNxCacheAligned.**

 

 




