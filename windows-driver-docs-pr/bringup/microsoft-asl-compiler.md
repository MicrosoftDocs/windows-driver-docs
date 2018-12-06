---
title: Microsoft ASL compiler
description: Version 5.0 of the Microsoft ASL compiler supports the features in the ACPI 5.0 specification.
ms.assetid: E6EC168F-DB4B-461A-874A-F5278E8F9200
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# Microsoft ASL compiler


Version 5.0 of the Microsoft ACPI source language (ASL) compiler supports the features in the Advanced Configuration and Power Interface Specification, Revision 5.0 ([ACPI 5.0 specification](https://www.uefi.org/specifications)). The ASL compiler is distributed with the Windows Driver Kit (WDK). Look for the Asl.exe executable file in the Tools\\arm\\ACPIVerify, Tools\\arm64\\ACPIVerify, Tools\\x86\\ACPIVerify, or Tools\\x64\\ACPIVerify directory of your installed WDK.

## Command line options


The Microsoft ASL compiler supports several command line options. To list the available command line options, run the command "`asl /?`" in a Command Prompt window.

### Usage

The ASL compiler supports the following command line options:

```console
asl /?
asl [/nologo] /d <BinFile>
asl [/nologo] /u [/Fa=<ASMFile>] [/Fl=<LSTFile>] [/Fn=<NSDFile>] <AMLFile>
asl [/nologo] /tab=<TabSig> [/c] [/Fa=<ASMfile>] [/Fl=<LSTFile>] [/Fn=<NSDFile>]
asl [/nologo] [/Fo=<AMLFile>] [/Fa=<ASMFile>] [/Fl=<LSTFile>] [/Fn=<NSDFile>] <ASLFile>
```

| Option             | Description                                                                   |
|--------------------|-------------------------------------------------------------------------------|
| ?                  | Print this help message.                                                      |
| nologo             | Suppress the logo banner.                                                     |
| Fo=&lt;AMLFile&gt; | Override the AML file name in the DefinitionBlock.                            |
| Fa=&lt;ASMFile&gt; | Generate a .ASM file with the name &lt;ASMFile&gt;.                           |
| Fn=&lt;NSDFile&gt; | Generate a NameSpace Dump file with the name &lt;NSDFile&gt;.                 |
| d                  | Dump the binary file in text form.                                            |
| u                  | Unassemble an AML file to a .ASL file (default) or a .LST file.               |
| tab=&lt;TabSig&gt; | Unassemble ASL table to a .ASL file (default) or a .LST file. Dump non-ASL table to a .TXT file. If &lt;TabSig&gt; is '\*', all tables are dumped to ACPI.TXT. &lt;TabSig&gt; can also be the physical address of the table. |
| c                  | Create binary files from tables.                                              |

 
## Using the Microsoft ASL compiler's ACPI-table-load feature

During system development, it is useful to have a way to simulate various ACPI BIOS constructs and test them on the development system. The Windows operating system allows certain ACPI tables to be loaded from the Windows registry instead of from the PC's BIOS ROM. Use of this feature requires administrator privileges, and also requires that test signing be enabled on the system. For systems that support UEFI Secure Boot, test signing cannot be enabled, and the compiler's table-load feature cannot be used unless UEFI Secure Boot is disabled or the Windows Debug Policy is installed on the system.

To use the table-load feature, the ACPI table to be overloaded must meet the following requirements:

-   The table to be overloaded must already be present in the system's BIOS ROM. For instance, the DSDT can be overloaded; however, if the machine does not have an SSDT, you cannot force an SSDT to be loaded from this registry override mechanism.
-   The table must contain AML code that is normally consumed by the Windows ACPI interpreter (the Acpi.sys driver).
-   The table with the highest version number will be loaded. The table loaded into the registry for testing must have a higher version number than the same table in the BIOS ROM.
-   The table to be loaded must be in compiled (AML) format and loaded into the registry in the correct location, with the correct parameters specified. The mechanism described herein is designed to handle all aspects of loading the table and configuring the registry.

> [!WARNING]
> The process described in this topic may leave your Windows system in a non-bootable state. Ensure that you have access to another operating system with NTFS file system support (that is, a "safe build") on the same machine before attempting the procedures outlined here. This process is provided for system developers and testers only, and should NOT be used on any machine vital for development or production purposes.


### Usage

To load an ACPI table into the registry for test purposes, the ASL compiler is invoked as follows:

```console
asl.exe /loadtable [-v] [-d] <AMLFile>
```

where AMLFile is the name of the compiled AML file that contains the table you wish to load into the registry.

| Option  | Description                                                                                              |
|---------|----------------------------------------------------------------------------------------------------------|
| -v      | Verbose mode. Turns on extra debugging output from the utility.                                          |
| -d      | Delete. Removes a previously loaded AML file from the registry, and deletes all associated registry keys.|


## Additional resources

-   [ACPICA Documentation](https://acpica.org/documentation/)
-   [ACPI Website](https://www.uefi.org/specifications/)
-   [ACPI Debugging](https://msdn.microsoft.com/library/windows/hardware/ff537808)
-   [Acpi.sys: The Windows ACPI Driver](https://msdn.microsoft.com/library/windows/hardware/ff540493)
-   [Power Management and ACPI](https://msdn.microsoft.com/library/windows/hardware/dn614610)

