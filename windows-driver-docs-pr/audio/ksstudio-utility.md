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
ms.author: windowsdriverdev
ms.date: 04/20/2017
ms.topic: article
ms.prod: windows-hardware
ms.technology: windows-devices
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

 

 


--------------------
[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20[audio\audio]:%20KsStudio%20Utility%20%20RELEASE:%20%287/18/2016%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")


