---
title: Supporting DualView (Windows 2000 Model)
description: Supporting DualView (Windows 2000 Model)
ms.assetid: 08da97c9-1d31-40f5-99df-5f16eaa47c79
keywords: ["video miniport drivers WDK Windows 2000 , DualView", "DualView WDK video miniport", "multiple display devices simultaneously WDK video miniport", "SingleView WDK video miniport"]
---

# Supporting DualView (Windows 2000 Model)


Many modern display adapters are able to drive two or more different display devices simultaneously. DualView, a feature of Microsoft Windows XP and later, provides system-level support for features similar to those of Multimonitor, but requires only a single display adapter. The graphics device interfaces (GDIs), and the end-user experiences, are identical for both DualView and Multimonitor.

SingleView Mode

In SingleView mode, a display adapter drives a single display device, regardless of the number of monitors. This is the usual mode for most of the display adapters that Windows 2000 and later operating system versions currently support.

DualView Mode

A computer in DualView mode can use a single display adapter (with multiple video ports) to drive multiple images on different monitors, with each display device portraying a different part of the desktop. The primary image displays the *primary view*; other images display *secondary views*.

The following subsections provide more information about DualView:

[Enabling DualView](enabling-dualview.md)

[DualView Advanced Implementation Details](dualview-advanced-implementation-details.md)

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20[display\display]:%20Supporting%20DualView%20%28Windows%202000%20Model%29%20%20RELEASE:%20%282/10/2017%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")




