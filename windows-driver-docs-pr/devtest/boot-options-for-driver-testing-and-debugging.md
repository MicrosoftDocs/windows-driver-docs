---
title: Tools for Changing Boot Options for Driver Testing and Debugging
description: Tools for Changing Boot Options for Driver Testing and Debugging
ms.assetid: 4fd58868-7a43-42e3-adf9-5a82593c1675
keywords: ["tools WDK , boot options", "driver development tools WDK , boot options", "boot options WDK", "driver testing WDK boot options", "testing drivers WDK boot options", "debugging drivers WDK boot options", "driver debugging WDK boot options", "operating system boot options WDK", "load configurations WDK boot options"]
---

# Tools for Changing Boot Options for Driver Testing and Debugging


## <span id="ddk_boot_options_for_driver_testing_and_debugging_tools"></span><span id="DDK_BOOT_OPTIONS_FOR_DRIVER_TESTING_AND_DEBUGGING_TOOLS"></span>


To test and debug drivers on a Microsoft Windows operating system, you must enable and configure features that are established when the operating system loads. The settings for these features are included in the *boot options*--values that determine how the boot loader loads and configures the operating system and other bootable programs and devices.

**Tip**  If you are using the Windows Driver Kit (WDK) 8, you can configure computers for testing and debugging from Visual Studio. When you configure the test computers, the WDK driver test framework automatically enables the test computer for remote debugging and transfers the necessary test binaries and support files. For more information, see [Provision a computer for driver deployment and testing (WDK 8.1)](https://msdn.microsoft.com/library/windows/hardware/dn745909), or [Provision a computer for driver deployment and testing (WDK 8)](https://msdn.microsoft.com/library/windows/hardware/hh698272), and [How to How to test a driver at runtime using Visual Studio](https://msdn.microsoft.com/windows-drivers/develop/testing_a_driver_at_runtime).

 

This section explains how to add, delete, and change boot options to create new load configurations for an operating system and how to use the boot entry parameters to customize a load configuration for driver testing and debugging.

By editing boot options, you can:

-   Enable and configure debugging.

-   Load a particular kernel or hardware abstraction layer (HAL) file.

-   Limit the physical memory available to Windows.

-   Enable, disable, and configure Physical Address Extension (PAE) on 32-bit versions of Windows.

-   Reapportion virtual address space between user-mode and kernel-mode components (3GB) to test a driver in a very small kernel-mode address space.

-   Enable and configure Data Execution Prevention (/noexecute).

-   Designate ports for Emergency Management Services (EMS) console redirection on headless servers.

-   Display the names of drivers as they load.

This section includes:

[Introduction to Boot Options](introduction-to-boot-options.md)

[Editing Boot Options](editing-boot-options.md)

[Boot.ini Boot Parameter Reference](https://msdn.microsoft.com/library/windows/hardware/ff542248)

[BCD Boot Options Reference](https://msdn.microsoft.com/library/windows/hardware/ff542205)

[Using Boot Parameters](using-boot-parameters.md)

[Bypassing Boot Options](bypassing-boot-options.md)

Beginning in Windows Vista, Windows includes a new boot loader architecture, new boot options, and a new boot options editor. For information, see [Boot Options in Windows Vista](boot-options-in-windows-vista-and-later.md).

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20[devtest\devtest]:%20Tools%20for%20Changing%20Boot%20Options%20for%20Driver%20Testing%20and%20Debugging%20%20RELEASE:%20%2811/17/2016%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")




