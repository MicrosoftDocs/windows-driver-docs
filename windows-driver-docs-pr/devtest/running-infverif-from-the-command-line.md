---
title: Running InfVerif from the command line
description: This topic lists the options that are available when you run InfVerif.exe from the command line.
ms.assetid: CC2DB624-FFEE-4049-ACE7-4A24B330BADB
ms.author: windows-driver-content
ms.date: 04/20/2017
ms.topic: article
ms.prod: windows-hardware
ms.technology: windows-devices
---

# Running InfVerif from the command line


This topic lists the options that are available when you run InfVerif.exe from the command line.
> [!NOTE]
> InfVerif requires that each combined path and file name must be less than 260 characters.

``` syntax
USAGE: InfVerif.exe [/v] [/u | /universal] [/info] [/stampinf] [/l <path>] [/osver TargetOSVersion>] [/product <ias file>] <files>

/v
        Display verbose file logging details.

/u
        Reports errors if INF is not Universal.

/info
        Displays INF summary information.

/stampinf
        Treat $ARCH$ as a valid architecture, to validate pre-stampinf files.

/l <path>
        An inline-annotated HTML version of each INF
        file will be placed in the <path>.

/osver <TargetOsVersion>
        Process the INF for a specific target OS.
        Formatting is the same as a Models section, i.e. NTAMD64.6.0

/product <ias file>
        Validates all include/needs directives against
        the product definition in the ias file.

<files>
        A space-separated list of INF files to analyze.
        Wildcards (*) may be used.
```

The verbose option adds a line to the output that specifies if the INF is valid or not.

*New for Windows 10, version 1703:*  The info option is especially useful to verify INF applicability.  It reports each supported hardware ID along with valid architecture and minimum OS version.  You can use /info and /osver together to validate an INF's applicability across OS versions and architectures.

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20[devtest\devtest]:%20Running%20InfVerif%20from%20the%20command%20line%20%20RELEASE:%20%2811/17/2016%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")
