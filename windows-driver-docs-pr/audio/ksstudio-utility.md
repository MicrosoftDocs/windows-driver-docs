---
title: KsStudio Utility
description: KsStudio Utility
ms.assetid: c6420768-2852-4269-91d9-cb5e34e565b5
keywords:
- KsStudio utility WDK audio
- audio filters WDK audio , KsStudio utility
- KS filter graphs WDK audio , KsStudio utility
- filter graphs WDK audio , KsStudio utility
- testing KS filter graphs WDK audio
- audio filter graphs WDK
- graphical representation WDK audio
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# KsStudio Utility


## <span id="ksstudio_utility"></span><span id="KSSTUDIO_UTILITY"></span>


The KsStudio utility (Ksstudio.exe) is included with the software tools in the Microsoft Windows Driver Kit (WDK). KsStudio is a kernel streaming tool that can be used to build, examine, and test WDM KS filter graphs in Windows Me/98 and in Windows 2000 and later. One of KsStudio's most useful features is its ability to construct a graphical representation of a filter graph that shows both the pin-to-pin connections between filters and the filters' internal nodes. Although KsStudio is designed primarily for audio filter graphs, it can be used to build and explore graphs containing any type of WDM KS filter.

To install KsStudio and its help file, KsStudio.chm:

-   Run the WDK setup application.

-   From the list of components, click **Driver Development Kit**, click **Tools for Driver Developers**, and then click **Audio/Video streaming tools**.

Setup installs the platform-specific versions of KsStudio.exe in the x86, amd64, and ia64 subdirectories of the \\tools\\avstream directory. It installs the help file, KsStudio.chm, in the \\tools\\avstream directory. To open the help file, double-click KsStudio.chm.

An earlier version of KsStudio, which is named Grapher (Grapher.exe), is included in the Windows 2000 and Windows Me Driver Development Kits (DDKs).

For more information about KsStudio, see the help file for the KsStudio utility in the WDK.

 

 




