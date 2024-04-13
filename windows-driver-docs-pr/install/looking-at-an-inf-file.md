---
title: Looking at an INF File
description: Looking at an INF File
keywords:
- INF files WDK device installations , structure
- INF files WDK device installations , sections
- sections WDK INF files
ms.date: 05/08/2023
---

# Looking at an INF File

The following example shows selected fragments from a system-supplied INF file to show how any INF file is made up of sections, each of which contains zero or more lines, some of which are entries that reference additional INF-writer-defined sections:

```cpp
[Version]
Signature   = "$Windows NT$"
Class       = Mouse
ClassGUID   = {4D36E96F-E325-11CE-BFC1-08002BE10318}
Provider    = %Provider% ; defined later in Strings section
DriverVer   = 09/28/1999,5.0.2136.1
CatalogFile = ExampleCatalog.cat
PnpLockdown = 1

[DestinationDirs]
DefaultDestDir = 13

; ... [ControlFlags] section omitted here

[Manufacturer]
%StdMfg% = StdMfg ; (Standard types)
%MSMfg%  = MSMfg  ; Microsoft
; ... other Manufacturer entries omitted here

[StdMfg]  ; per-Manufacturer Models section
; Std serial mouse
%*pnp0f0c.DeviceDesc% = Ser_Inst,*PNP0F0C,SERENUM\PNP0F0C,SERIAL_MOUSE
; Std InPort mouse
%*pnp0f0d.DeviceDesc% = Inp_Inst,*PNP0F0D
; ... more StdMfg entries and following MSMfg and xxMfg Models sections omitted here

; per-Models DDInstall (Ser_Inst, Inp_Inst, etc.) sections also omitted here


[Strings]
; where INF %strkey% tokens are defined as user-visible (and
; possibly as locale-specific) strings.
Provider = "Microsoft"
; ...
StdMfg   = "(Standard mouse types)"
MSMfg    = "Microsoft"
; ...
*pnp0f0c.DeviceDesc = "Standard Serial Mouse"
*pnp0f0d.DeviceDesc = "InPort Adapter Mouse"
; ...
```

A few sections within the previous INF file have system-defined names, such as [**Version**](inf-version-section.md), [**DestinationDirs**](inf-destinationdirs-section.md), [**Manufacturer**](inf-manufacturer-section.md), and [**Strings**](inf-strings-section.md). Some named sections like **Version**, **DestinationDirs**, and **Strings** have only simple entries. Others reference additional INF-writer-defined sections, as shown in the previous example of the **Manufacturer** section.

Note the implied hierarchy of related sections for mouse device driver installations starting with the **Manufacturer** section in the previous example. The following figure shows the hierarchy of some sections in the INF file.

![diagram illustrating a sample hierarchy of sections in an inf file.](images/inf-sections.png)

Note the following about the implied hierarchy of an INF file:

- Each **%**<em>xx</em>Mfg<strong>%</strong> entry in the **Manufacturer** section references a per-manufacturer [*Models*](inf-models-section.md) section (StdMfg, MSMfg) elsewhere in the INF file.

- Each [*Models*](inf-models-section.md) section specifies some number of entries; in the example they start with **%**<em>xxx</em>.DeviceDesc<strong>%</strong> tokens.

  Each such **%**<em>xxx</em>.DeviceDesc<strong>%</strong> token references some number of per-models [*DDInstall*](inf-ddinstall-section.md) sections (Ser_Inst and Inp_Inst) for that manufacturer's product line, with each entry identifying a single device (\*PNP0F0C and \*PNP0F0D, hence the "DeviceDesc" shown here) or a set of compatible models of a device.

- Each such *DDInstall*-type *Xxx*_Inst section, in turn, can have certain system-defined extensions appended and/or can contain directives that reference additional INF-writer-defined sections. For example, the full INF file that is shown as fragments in the previous example also has a Ser_Inst<strong>.Services</strong> section, and its Ser_Inst section has a [**CopyFiles**](inf-copyfiles-directive.md) directive that references a Ser_CopyFiles section elsewhere in this INF file.
