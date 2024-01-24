---
title: Microsoft ASL Compiler
description: Version 5.0 of the Microsoft ASL compiler supports the features in the ACPI 5.0 specification.
ms.date: 03/23/2023
---

# Microsoft ASL compiler

Version 5.0 of the Microsoft ACPI source language (ASL) compiler supports the features in the Advanced Configuration and Power Interface Specification, Revision 5.0 ([ACPI 5.0 specification](https://uefi.org/specifications)). The ASL compiler is distributed with the Windows Driver Kit (WDK).

[**Download the Windows Driver Kit (WDK)**](../download-the-wdk.md)

The ASL compiler (asl.exe) is located in the Tools\\arm\\ACPIVerify, Tools\\arm64\\ACPIVerify, Tools\\x86\\ACPIVerify, and Tools\\x64\\ACPIVerify directories of the installed WDK, for example, `C:\Program Files (x86)\Windows Kits\10\Tools\<build #>\<build architecture>\ACPIVerify`.

You need to first install the SDK, followed by the WDK. The build numbers for the two kits must match.

## Command line options

The ASL compiler supports several command line options. To list version information and available command line options, run the command "`asl /?`" in a Command Prompt window.

### ASL compiler usage

The ASL compiler supports the following command line options:

```console
asl /?
asl [/nologo] /d <BinFile>
asl [/nologo] /u [/Fa=<ASMFile>] [/Fl=<LSTFile>] [/Fn=<NSDFile>] <AMLFile>
asl [/nologo] /tab=<TabSig> [/c] [/Fa=<ASMfile>] [/Fl=<LSTFile>] [/Fn=<NSDFile>]
asl [/nologo] [/Fo=<AMLFile>] [/Fa=<ASMFile>] [/Fl=<LSTFile>] [/Fn=<NSDFile>] <ASLFile>
```

| Option | Description |
|--|--|
| ? | Print this help message. |
| nologo | Suppress the logo banner. |
| Fo=&lt;AMLFile&gt; | Override the AML file name in the DefinitionBlock. |
| Fa=&lt;ASMFile&gt; | Generate a .ASM file with the name &lt;ASMFile&gt;. |
| Fn=&lt;NSDFile&gt; | Generate a NameSpace Dump file with the name &lt;NSDFile&gt;. |
| d | Dump the binary file in text form. |
| u | Unassemble an AML file to a .ASL file (default) or a .LST file. |
| tab=&lt;TabSig&gt; | Unassemble ASL table to a .ASL file (default) or a .LST file. Dump non-ASL table to a .TXT file. If &lt;TabSig&gt; is '\*', all tables are dumped to ACPI.TXT. &lt;TabSig&gt; can also be the physical address of the table. |
| c | Create binary files from tables. |

## Using the Microsoft ASL compiler's ACPI-table-load feature

During system development, it's useful to have a way to simulate various ACPI BIOS constructs and test them on the development system. The Windows operating system allows certain ACPI tables to be loaded from the Windows registry instead of from the PC's BIOS ROM. Use of this feature requires administrator privileges, and also requires that test signing be enabled on the system. For systems that support UEFI Secure Boot, test signing can't be enabled, and the compiler's table-load feature can't be used unless UEFI Secure Boot is disabled or the Windows Debug Policy is installed on the system.

To use the table-load feature, the ACPI table to be overloaded must meet the following requirements:

- The table to be overloaded must already be present in the system's BIOS ROM. For instance, the DSDT can be overloaded; however, if the machine doesn't have an SSDT, you can't force an SSDT to be loaded from this registry override mechanism.

- The table must contain AML code that is normally consumed by the Windows ACPI interpreter (the Acpi.sys driver).

- The table with the highest version number will be loaded. The table loaded into the registry for testing must have a higher version number than the same table in the BIOS ROM.

- The table to be loaded must be in compiled (AML) format and loaded into the registry in the correct location, with the correct parameters specified. The mechanism described herein is designed to handle all aspects of loading the table and configuring the registry.

> [!WARNING]
> The process described in this topic may leave your Windows system in a non-bootable state. Ensure that you have access to another operating system with NTFS file system support (that is, a "safe build") on the same machine before attempting the procedures outlined here. This process is provided for system developers and testers only, and should NOT be used on any machine vital for development or production purposes.

### ACPI-table-load usage

To load an ACPI table into the registry for test purposes, the ASL compiler is invoked as follows:

```console
asl.exe /loadtable [-v] [-d] <AMLFile>
```

where AMLFile is the name of the compiled AML file that contains the table you wish to load into the registry.

| Option | Description |
|--|--|
| -v | Verbose mode. Turns on extra debugging output from the utility. |
| -d | Delete. Removes a previously loaded AML file from the registry, and deletes all associated registry keys. |

## Additional resources

- [ACPICA documentation](https://www.intel.com/content/www/us/en/developer/topic-technology/open/acpica/overview.html)

- [ACPI specification](https://uefi.org/specifications/)

- [ACPI debugging](../debugger/acpi-debugging.md)

- [Acpi.sys: The Windows ACPI Driver](../kernel/acpi-driver.md)

- [Power management and ACPI](/previous-versions/windows/hardware/design/dn614610(v=vs.85))
