---
title: NX and Execute Pool Types
author: windows-driver-content
description: To indicate whether memory allocated from a nonpaged pool should be no-execute (NX), you can use two new pool types starting with Windows 8.
ms.assetid: 954AC53F-270D-4149-AE5D-6BEA7EFAA761
---

# NX and Execute Pool Types


To indicate whether memory allocated from a nonpaged pool should be no-execute (NX), you can use two new pool types starting with Windows 8. These pool types are designated by the following [**POOL\_TYPE**](https://msdn.microsoft.com/library/windows/hardware/ff559707) enumeration values:

<a href="" id="nonpagedpoolnx"></a>**NonPagedPoolNx**  
NX nonpaged pool. Instructions cannot be executed in memory allocated from this pool.

<a href="" id="nonpagedpoolexecute"></a>**NonPagedPoolExecute**  
Executable nonpaged pool. Instruction execution is enabled in memory allocated from this pool.

Most drivers use allocated memory only to store data, and do not execute instructions in this memory. If you build your driver to run on Windows 8 and later versions of Windows, allocate **NonPagedPoolNx** memory from the NX nonpaged pool whenever possible. Only drivers that need to execute instructions from nonpaged memory should allocate **NonPagedPoolExecute** memory from the executable nonpaged pool.

For existing drivers that are built for Windows 7 and earlier versions of Windows, when you use the **NonPagedPool** pool type your driver allocates memory from the executable pool. The **NonPagedPool** constant name has the same value as the **NonPagedPoolExecute** constant name that is defined starting with Windows 8. Therefore, these constants refer to the same pool type.

If a driver written for Windows 7 or an earlier version of Windows is built for Windows 8 or a later version of Windows, instances of the **NonPagedPool** pool type should be replaced by either **NonPagedPoolNx** or **NonPagedPoolExecute**. The driver developer either can explicitly perform this replacement, or can implicitly perform the replacement by using one of the opt-in mechanisms that is provided to aid developers in porting their drivers to Windows 8. For more information, see [NX Pool Opt-In Mechanisms](nx-pool-opt-in-mechanisms.md).

 

 


--------------------
[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bkernel\kernel%5D:%20NX%20and%20Execute%20Pool%20Types%20%20RELEASE:%20%286/14/2017%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")


