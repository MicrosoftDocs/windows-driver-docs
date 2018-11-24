---
title: ControlFlags Section in a Network INF File
description: ControlFlags Section in a Network INF File
ms.assetid: 384e56e3-8a64-4b47-ae9c-e9973733c7e7
keywords:
- INF files WDK network , ControlFlags section
- network INF files WDK , ControlFlags section
- ControlFlags section WDK networking
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# ControlFlags Section in a Network INF File





A **ControlFlags** section in a network INF file is based on the generic [**INF ControlFlags section**](https://msdn.microsoft.com/library/windows/hardware/ff546342).

The **ControlFlags** section in a network INF file typically has one or more **ExcludeFromSelect** entries. Each **ExcludeFromSelect** entry specifies a network component that will not be displayed to the end user as an option during a manual installation.

The **ControlFlags** section in a network INF file must contain an **ExcludeFromSelect** entry for each Plug and Play adapter that it installs, and for any software component that should be added programmatically rather than manually by the user.

Adapters that are not compatible with Plug and Play must be added manually by the user and therefore should not be listed in the *ControlFlags* section. For example, non-PnP ISA adapters and EISA adapters must be manually added by the user. Note that Windows XP and later operating systems do not support non-PnP ISA adapters and EISA adapters.

**Note**  An **ExcludeFromSelect** entry performs a different function than does the NCF\_HIDDEN value of the **Characteristics** entry in the *DDInstall* section. For more information, see [DDInstall Section](ddinstall-section-in-a-network-inf-file.md).

 

An **ExcludeFromSelect** entry prevents an adapter or software component from being listed in the **Select Component for Installation** dialog box. The adapter or component, however, can still be listed in the **Connections** dialog box. The NCF\_HIDDEN value prevents the adapter or component from being displayed in any part of the user interface, including the **Connections** dialog box.

 

 





