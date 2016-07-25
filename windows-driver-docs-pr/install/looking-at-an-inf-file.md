---
title: Looking at an INF File
description: Looking at an INF File
ms.assetid: 4d9d5f28-b643-4369-8bf8-94703e8926d2
keywords: ["INF files WDK device installations , structure", "INF files WDK device installations , sections", "sections WDK INF files"]
---

# Looking at an INF File


## <a href="" id="ddk-looking-at-an-inf-file-dg"></a>


The following example shows selected fragments from a system-supplied class installer's INF file to show how any INF file is made up of sections, each of which contains zero or more lines, some of which are entries that reference additional INF-writer-defined sections:

```
[Version]
Signature="$Windows NT$"
Class=Mouse
ClassGUID={4D36E96F-E325-11CE-BFC1-08002BE10318}
Provider=%Provider% ; defined later in Strings section
DriverVer=09/28/1999,5.00.2136.1
 
[DestinationDirs]
DefaultDestDir=12 ; DIRID_DRIVERS
 
; ... [ControlFlags] section omitted here
 
[Manufacturer]
%StdMfg%    =StdMfg         ; (Standard types)
%MSMfg%     =MSMfg          ; Microsoft
; ... %otherMfg% entries omitted here
 
[StdMfg]  ; per-Manufacturer Models section 
; Std serial mouse
%*pnp0f0c.DeviceDesc%= Ser_Inst,*PNP0F0C,SERENUM\PNP0F0C,SERIAL_MOUSE
; Std InPort mouse
%*pnp0f0d.DeviceDesc%      = Inp_Inst,*PNP0F0D
     ; ... more StdMfg entries and following
     ; MSMfg and xxMfg Models sections omitted here
 
     ; per-Models DDInstall (Ser_Inst, Inp_Inst, etc.)
     ; sections also omitted here
 
[Strings] 
; where INF %strkey% tokens are defined as user-visible (and
; possibly as locale-specific) strings.
Provider = "Microsoft"
; ...
StdMfg   = "(Standard mouse types)"
MSMfg    = "Microsoft"
 
; ...
*pnp0f0c.DeviceDesc   = "Standard Serial Mouse"
*pnp0f0d.DeviceDesc   = "InPort Adapter Mouse"
; ... 
HID\Vid_045E&amp;Pid_0009.DeviceDesc = "Microsoft USB Intellimouse"
; ... 
```

A few sections within the previous INF file have system-defined names, such as **Version**, **DestinationDirs**, **Manufacturer**, and **Strings**. Some named sections like **Version**, **DestinationDirs**, and **Strings** have only simple entries. Others reference additional INF-writer-defined sections, as shown in the previous example of the **Manufacturer** section.

Note the implied hierarchy of related sections for mouse device driver installations starting with the **Manufacturer** section in the previous example. The following figure shows the hierarchy of some sections in the INF file.

![diagram illustrating a sample hierarchy of sections in an inf file](images/inf-sections.png)

Note the following about the implied hierarchy of an INF file:

-   Each **%***xx*Mfg**%** entry in the **Manufacturer** section references a per-manufacturer *Models* section (StdMfg, MSMfg) elsewhere in the INF file.

    The entries in the previous example use %*strkey*% tokens.

-   Each *Models* section specifies some number of entries; in the example they are **%***xxx*.DeviceDesc**%** tokens.

    Each such **%***xxx*.DeviceDesc**%** token references some number of per-models *DDInstall* sections (Ser\_Inst and Inp\_Inst) for that manufacturer's product line, with each entry identifying a single device (\*PNP0F0C and \*PNP0F0D, hence the "DeviceDesc" shown here) or a set of compatible models of a device.

-   Each such *DDInstall*-type *Xxx*\_Inst section, in turn, can have certain system-defined extensions appended and/or can contain directives that reference additional INF-writer-defined sections. For example, the full INF file that is shown as fragments in the previous example also has a Ser\_Inst**.Services** section, and its Ser\_Inst section has a **CopyFiles** directive that references a Ser\_CopyFiles section elsewhere in this INF file.

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bdevinst\devinst%5D:%20Looking%20at%20an%20INF%20File%20%20RELEASE:%20%287/22/2016%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")




