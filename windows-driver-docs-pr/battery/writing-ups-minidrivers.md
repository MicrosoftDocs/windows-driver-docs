---
title: Writing UPS Minidrivers
description: Writing UPS Minidrivers
ms.assetid: 85142cbf-cb3b-4ccf-a005-8fcb7a7ad12b
keywords: ["UPS minidrivers WDK", "simple signaling WDK", "smart signaling WDK", "UPS service WDK", "system-supplied UPS service WDK", "UPS minidrivers WDK , about writing UPS minidrivers", "uninterruptible power supply WDK"]
---

# Writing UPS Minidrivers


## <span id="ddk_writing_ups_minidrivers_kg"></span><span id="DDK_WRITING_UPS_MINIDRIVERS_KG"></span>


If an uninterruptible power supply (UPS) is connected to a Microsoft Windows system, the **UPS** tab for **Power Options** in Control Panel provides information about the UPS. On Windows Server 2003, Windows XP, and Windows 2000, a system-supplied UPS service provides support for UPS units that are connected to COM ports and that support "simple signaling," which provides very limited control capabilities and status information.

On Windows Server 2003, Windows XP, and Windows 2000, if your UPS model is connected to a COM port and supports "smart signaling," you should provide a UPS minidriver. This minidriver, which is a user-mode DLL called by the system's UPS service, performs the following operations:

-   Initializes the communication path to the UPS.

-   Updates registry entries that **Power Options** uses to obtain model-specific information to display.

-   Turns off the UPS power upon request.

-   Monitors the UPS unit for state changes.

For more information about UPS minidrivers, see the following topics:

[UPS Minidriver Functionality](ups-minidriver-functionality.md)

[UPS Registry Entries](ups-registry-entries.md)

[Sample UPS Minidriver](sample-ups-minidriver.md)

[Installing UPS Minidrivers](installing-ups-minidrivers.md)

**Note**   Windows Vista and later versions of Windows do not support UPS units that are connected to COM ports. These Windows versions continue to support UPS units connected over [USB](https://msdn.microsoft.com/library/windows/hardware/ff538930).

 

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20[battery\battery]:%20Writing%20UPS%20Minidrivers%20%20RELEASE:%20%286/7/2016%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")




