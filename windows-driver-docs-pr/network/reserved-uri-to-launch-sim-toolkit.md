---
title: Reserved URI to launch SIM toolkit
description: Reserved URI to launch SIM toolkit
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# Reserved URI to launch SIM toolkit


Windows includes support for a reserved URI scheme that enables partners to place a UWP app on the Start screen that can then launch the SIM applications CPL to make it more discoverable. Currently, users can only get to the SIM applications by navigating to the **Settings** &gt; **network & wireless** &gt; **Cellular & SIM** &gt; **advanced options** screen and tapping the **SIM applications** button. For more information, see [SIM toolkit](sim-toolkit.md).

The URI scheme, `"ms-settings-uicctoolkit"`, has been defined for the SIM toolkit launcher. This will enable users to more easily access functionality on the mobile operator’s networks such as banking or billing security apps.

## Launching a URI


A UWP app can load the SIM applications CPL by using a call to the [Launcher.LaunchUriAsync(Uri)](/uwp/api/Windows.System.Launcher#Windows_System_Launcher_LaunchUriAsync_Windows_Foundation_Uri_) method from the **Launcher** object of the **Windows.System** namespace.

The following example shows how partners can launch the SIM applications CPL from the app.

``` syntax
Windows.System.Launcher.LaunchUriAsync("ms-settings-uicctoolkit:");
```

## Related topics


[SIM toolkit](sim-toolkit.md)

 

