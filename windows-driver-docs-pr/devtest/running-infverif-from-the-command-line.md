---
title: Running InfVerif from the Command Line
description: This topic lists the options that are available when you run InfVerif.exe from the command line.
ms.date: 05/30/2024
---

# Running InfVerif from the Command Line

This topic lists the options that are available when you run InfVerif.exe from the command line.

> [!NOTE]
> InfVerif requires that each combined path and file name must be less than 260 characters.

```syntax
USAGE: InfVerif.exe [/code <error code>] [/v] [[/h] | [/w] | [/u] | [/k]]
                    [/rulever <Major.Minor.Build> | vnext]
                    [/wbuild <Major.Minor.Build>] [/info] [/stampinf]
                    [/l <path>] [/osver <TargetOSVersion>] [/product <ias file>]
                    [/provider <ProviderName>] <files>

/code <error code>
        Display help information for an error code.

/v
        Display verbose file logging details.

/h
        Reports errors using WHQL Signature requirements. (mode)

        This mode uses requirements that always align with the requirements
        to get a WHQL signature, current as of this InfVerif version. These
        requirements may change build-to-build.

        This mode can be combined with '/rulever vnext' to preview proposed
        future requirements.

/w
        Reports errors using Windows Driver requirements. (mode)

/u
        Reports errors using Universal Driver requirements. (mode)

/k
        Reports errors using Declarative Driver requirements. (mode)

/wbuild <Major.Minor.Build>
        For Windows Drivers that have downlevel support, specifies
        the build number where /w should be enforced.
        Defaults to 10.0.17763

/rulever <Major.Minor.Build>
        To use a previous or future version of InfVerif enforcement, specifies
        the build number to use rule enforcement from.
        Defaults to the current InfVerif version

/info
        Displays INF summary information.

/stampinf
        Treat $ARCH$ as a valid architecture, to validate
        pre-stampinf files.

/l <path>
        An inline-annotated HTML version of each INF
        file will be placed in the <path>.

/osver <TargetOsVersion>
        Process the INF for only a specific target OS.
        Formatting is the same as a Models section, i.e. NTAMD64.6.0

/product <ias file>
        Validates all include/needs directives against
        the product definition in the ias file.

/provider <ProviderName>
        Reports an error for INFs not using the specified provider name.

<files>
        A space-separated list of INF files to analyze.
        All files must have .inf extension.
        Wildcards (*) may be used.

Only one mode option may be passed at a time.
```

For info on error codes, see [INF Validation Errors and Warnings](./inf-validation-errors-and-warnings.md)

The verbose option adds a line to the output that specifies if the INF is valid or not.  Certain arguments are tagged as modes, where only one should be passed.

For examples of *TargetOSVersion* formatting, see Remarks section of [INF Manufacturer Section](../install/inf-manufacturer-section.md).

To validate multiple INF files, provide multiple filenames or use a wildcard:

```command
infverif.exe /w test1.inf test2.inf
infverif.exe /w test*.inf
```

*New for Windows 10, version 1703:*  The info option is especially useful to verify INF applicability.  It reports each supported hardware ID along with valid architecture and minimum OS version.  You can use /info and /osver together to validate an INF's applicability across OS versions and architectures.

*New for Windows 10, version 1809:*  If you are developing a *Windows Driver*, use `infverif /w` (ideally with `/v`) to determine compatibility with the **declarative (D)** principle of [DCH Design Principles](../develop/dch-principles-best-practices.md).  The `/w` flag also checks if the INF complies with the [driver package isolation](../develop/driver-isolation.md) requirement of [Get started developing Windows drivers](../develop/get-started-developing-windows-drivers.md).

*New Windows 11, version 24H2:* The new '/code' argument was introduced to provide expanded details about an error code. The new mode 'infverif /h' is introduced to determine whether the INF file meets the requirements for Hardware Dev Center to WHQL sign a driver package. For additional details about 'infverif /h', see [InfVerif /h](infverif_h.md).

## InfVerif and MSBuild tasks

MSBuild runs InfVerif as a task automatically, right after the [Stampinf task](./stampinf-task.md).
It uses the **Target Platform** in the project properties (**Configuration Properties->Driver Settings**) to auto-configure as follows:

* Target Platform = Desktop uses `InfVerif /h`
* Target Platform = Universal uses `InfVerif /u`
* Target Platform = Windows Driver uses `InfVerif /w`

It is not possible to change that automatic invocation. If you want to use other settings described above, you can either run InfVerif as a standalone or call InfVerif.exe using a custom target in the .vcxproj file.
