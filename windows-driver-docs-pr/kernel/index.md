---
title: Kernel-Mode Driver Architecture Design Guide
author: windows-driver-content
description: Kernel-Mode Driver Architecture Design Guide
MS-HAID:
- 'kerdg\_a997c77d-f70b-412d-bef9-cb87ecc0aae5.xml'
- 'kernel.kernel\_mode\_driver\_architecture\_design\_guide'
MSHAttr:
- 'PreferredSiteName:MSDN'
- 'PreferredLib:/library/windows/hardware'
ms.assetid: 21c199f3-abc3-4607-a674-eb84b6c3c25a
keywords: ["kernel-mode drivers WDK , architecture", "kernel-mode drivers WDK"]
---

# Kernel-Mode Driver Architecture Design Guide


## <a href="" id="ddk-km-design-guide-kg"></a>


This section includes general concepts to help you understand kernel-mode programming and describes specific techniques of kernel programming. This section is divided into four parts:

-   [Introduction to Windows Drivers](introduction-to-windows-drivers.md) provides a general overview of Windows components, lists the types of device drivers used in Windows, discusses the goals of Windows device drivers, and discusses generic sample device drivers included in the kit.

-   [Kernel-Mode Managers and Libraries](kernel-mode-managers-and-libraries.md) lists the primary kernel-mode components of the Windows operating system.

-   [Writing WDM Drivers](writing-wdm-drivers.md) provides information needed to write drivers using the Windows Driver Model (WDM).

-   [Driver Programming Techniques](driver-programming-techniques.md) describes techniques that you can use to program Windows kernel-mode device drivers.

    **Note**  For information about programming interfaces that your driver can implement or call, see [Kernel-Mode Driver Reference](https://msdn.microsoft.com/library/windows/hardware/ff553217).

     

 

 


--------------------
[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bkernel\kernel%5D:%20Kernel-Mode%20Driver%20Architecture%20Design%20Guide%20%20RELEASE:%20%286/14/2017%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")


