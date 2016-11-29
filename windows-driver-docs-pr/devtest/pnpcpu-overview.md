---
title: PNPCPU Overview
description: PNPCPU Overview
ms.assetid: c6bc9567-3c6a-45ea-a39e-e77b52a2279a
keywords: ["PNPCPU WDK , about PNPCPU"]
---

# PNPCPU Overview


PNPCPU is a command line tool that performs the following functions:

-   Install
    -   To install the tool, run Pnpcpu.exe with the **-install** option.
    -   Pnpcpu installs all relevant drivers.
    -   Pnpcpu updates the Boot Configuration Data store with the appropriate parameters.
-   Add
    -   PNPCPU attempts to hot add all logical processors in the system, up to the maximum supported by the license for the installed edition.
-   Removal
    -   To remove the tool, run Pnpcpu.exe with the **-uninstall** option. This results in a complete undo of all steps performed by **-install**.
    -   This option leaves the binaries on the disk for subsequent reinstallation and use.

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20[devtest\devtest]:%20PNPCPU%20Overview%20%20RELEASE:%20%2811/17/2016%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")




