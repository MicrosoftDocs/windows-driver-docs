---
title: Selective Opt-Out POOL\_NX\_OPTOUT
author: windows-driver-content
description: You can globally enable one of the no-execute (NX) pool opt-in mechanisms for a set of driver source files, and then override this opt-in mechanism for one or more selected source files with POOL\_NX\_OPTOUT.
MSHAttr:
- 'PreferredSiteName:MSDN'
- 'PreferredLib:/library/windows/hardware'
ms.assetid: 15AA7CFA-5BEC-4E45-B222-0DE2D620E099
---

# Selective Opt-Out: POOL\_NX\_OPTOUT


You can globally enable one of the no-execute (NX) pool opt-in mechanisms for a set of driver source files, and then override this opt-in mechanism for one or more selected source files with POOL\_NX\_OPTOUT. This allows the selected source files to continue to use executable nonpaged memory. You can use the POOL\_NX\_OPTOUT opt-out mechanism with either the POOL\_NX\_OPTIN or the POOL\_NX\_OPTIN\_AUTO opt-in mechanism. For more information, see [NX Pool Opt-In Mechanisms](nx-pool-opt-in-mechanisms.md).

To use the POOL\_NX\_OUTPUT opt-out mechanism to override the opt-in mechanism in a selected source file, add the following definition to this file:

`#define POOL_NX_OPTOUT 1`

This definition overrides the global opt-in settings in the selected file, and prevents instances of the **NonPagedPool** constant name from being replaced. Insert this definition into the file before the first instance of **NonPagedPool** in the file.

An alternative to using the POOL\_NX\_OPTOUT opt-out mechanism in a source file is to explicitly replace each instance of **NonPagedPool** in the file with **NonPagedPoolExecute**.

 

 


--------------------
[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bkernel\kernel%5D:%20Selective%20Opt-Out:%20POOL_NX_OPTOUT%20%20RELEASE:%20%286/14/2017%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")


