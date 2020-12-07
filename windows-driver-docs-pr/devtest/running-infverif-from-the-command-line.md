---
title: Running InfVerif from the command line
description: This topic lists the options that are available when you run InfVerif.exe from the command line.
ms.date: 04/28/2020
ms.localizationpriority: medium
---

# Running InfVerif from the command line

This topic lists the options that are available when you run InfVerif.exe from the command line.

> [!NOTE]
> InfVerif requires that each combined path and file name must be less than 260 characters.

```syntax
USAGE: InfVerif.exe [/v] [/u | /universal] [/w] [/k] [/info] [/stampinf] [/l <path>]
                    [/osver TargetOSVersion>] [/product <ias file>] <files>

/v
        Display verbose file logging details.

/k
        Reports errors for Hardware Dev Center submission. (mode; checks error codes 1100-1299)

/u
        Reports errors if INF is not Universal. (mode)

/w
        Reports Windows Driver compatibility. See below. (mode)

/info
        Displays INF summary information.

/stampinf
        Treat $ARCH$ as a valid architecture, to validate
        pre-stampinf files.

/l <path>
        An inline-annotated HTML version of each INF
        file will be placed in the <path>.

/osver <TargetOsVersion>
        Process the INF for a specific target OS.
        Formatting is the same as a Models section, i.e. NTAMD64.6.0
        Matches the TargetOSVersion you would use in a Models section name (see link below)

/product <ias file>
        Validates all include/needs directives against
        the product definition in the ias file.

/recurse
        Process INF files that match the specified file pattern in the current directory and all subdirectories.

<files>
        A space-separated list of INF files to analyze.
        Wildcards (*) may be used.

Only one mode option may be passed at a time.
```

For info on error codes, see [INF Validation Errors and Warnings](./inf-validation-errors-and-warnings.md)

The verbose option adds a line to the output that specifies if the INF is valid or not.  Certain arguments are tagged as modes, where only one should be passed.

For examples of *TargetOSVersion* formatting, see Remarks section of [INF Manufacturer Section](../install/inf-manufacturer-section.md).

*New for Windows 10, version 1703:*  The info option is especially useful to verify INF applicability.  It reports each supported hardware ID along with valid architecture and minimum OS version.  You can use /info and /osver together to validate an INF's applicability across OS versions and architectures.

*New for Windows 10, version 1809:*  If you are developing a *Windows Driver*, use `infverif /w` (ideally with `/v`) to determine compatability with the **declarative (D)** principle of [DCH Design Principles](../develop/dch-principles-best-practices.md).  The `/w` flag also checks if the INF complies with the [driver package isolation](../develop/driver-isolation.md) requirement of [Getting Started with Windows Drivers](../develop/getting-started-with-windows-drivers.md).

To validate multiple INF files, provide multiple filenames or use a wildcard:

```command
infverif.exe /w test1.inf test2.inf
infverif.exe /w test*.inf
```
