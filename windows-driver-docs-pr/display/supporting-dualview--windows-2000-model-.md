---
title: Supporting DualView (Windows 2000 Model)
description: Supporting DualView (Windows 2000 Model)
ms.assetid: 08da97c9-1d31-40f5-99df-5f16eaa47c79
keywords:
- video miniport drivers WDK Windows 2000 , DualView
- DualView WDK video miniport
- multiple display devices simultaneously WDK video miniport
- SingleView WDK video miniport
ms.date: 04/20/2017
ms.localizationpriority: medium
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

 

 





