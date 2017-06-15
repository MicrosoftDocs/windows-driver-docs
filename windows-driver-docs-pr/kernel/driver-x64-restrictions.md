---
title: Driver x64 Restrictions
author: windows-driver-content
description: Driver x64 Restrictions
MS-HAID:
- '64bitAMD\_f8d0fea8-e14a-457b-a30c-b10f167e8d51.xml'
- 'kernel.driver\_x64\_restrictions'
MSHAttr:
- 'PreferredSiteName:MSDN'
- 'PreferredLib:/library/windows/hardware'
ms.assetid: 717ca559-93aa-48d6-8347-bfdf223f1aa4
---

# Driver x64 Restrictions


On x64-based systems, kernel code and certain kernel data structures are protected from modification. Any driver that attempts to modify such code or data will cause the system to bug check (with the CRITICAL\_STRUCTURE\_CORRUPTION bug check).

Drivers for x64-based systems must avoid operations that might trigger this bug check. In particular, drivers must not:

-   Attempt to modify kernel code at run time.

-   Implement and use their own stacks.

-   Modify hardware dispatch tables, such as the interrupt dispatch table (IDT) or global descriptor table (GDT).

-   Modify undocumented kernel data structures.

Even though the preceding operations will not trigger a bug check on x86-based or Itanium-based systems, drivers should not perform any of these operations on any platform. These operations might not work in future versions of the Microsoft Windows operating system.

For more information about modifying kernel code and data structures, see the [Patching Policy for x64-based Systems](http://go.microsoft.com/fwlink/p/?linkid=50719) white paper and the [64-Bit Patching FAQ](http://go.microsoft.com/fwlink/p/?linkid=69534) on the Windows Hardware Developer Central (WHDC) website.

For general information about programming with a 64-bit compiler, see [64-Bit Programming with Visual C++](http://go.microsoft.com/fwlink/p/?linkid=165521).

 

 


--------------------
[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bkernel\kernel%5D:%20Driver%20x64%20Restrictions%20%20RELEASE:%20%286/14/2017%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")


