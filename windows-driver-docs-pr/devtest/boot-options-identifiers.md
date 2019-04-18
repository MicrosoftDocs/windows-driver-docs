---
title: Boot Options Identifiers
description: Describes Boot Options Identifiers
ms.assetid: bd0caf3f-bb35-4242-a10a-4efa91a21797
keywords:
- boot options Windows
- identifiers
- default
- WDK boot options
ms.date: 04/18/2019
ms.localizationpriority: medium
---

# Boot Options Identifiers

IDENTIFIERS

Many of the Bcdedit commands require identifiers. An identifier
uniquely identifies entries contained in the store. An identifier takes the
form of a globally unique identifier, or GUID. A GUID has the following format,
where each "x" represents a hexadecimal digit.

    {xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxxxxxx}

For example:

    {d2b69192-8f14-11da-a31f-ea816ab185e9}

The position of the dashes (-) and the braces at the beginning and end of the
GUID are required.

Several entries can be identified by well-known identifiers. If an entry has a
well-known identifier, BCDedit displays it in output unless the /v command-line
switch is used. For more information, run "bcdedit /? /v".

The well-known identifiers are as follows:

    {bootmgr}               Specifies the Windows boot manager entry.

    {fwbootmgr}             Specifies the firmware boot manager entry,
                            specifically on systems that implement the
                            Extensible Firmware Interface (EFI) specification.

    {memdiag}               Specifies the memory diagnostic application entry.

    {ntldr}                 Specifies a OS loader (Ntldr) that can be used
                            to start operating systems earlier than Windows
                            Vista.

    {current}               Specifies a virtual identifier that corresponds to
                            the operating system boot entry for the operating
                            system that is currently running.

    {default}               Specifies a virtual identifier that corresponds to
                            the boot manager default application entry.

    {ramdiskoptions}        Contains the additional options required by the
                            boot manager for RAM disk devices.

    {dbgsettings}           Contains the global debugger settings that can be
                            inherited by any boot application entry.

    {emssettings}           Contains the global Emergency Management Services
                            settings that can be inherited by any boot
                            application entry.

    {badmemory}             Contains the global RAM defect list that can be
                            inherited by any boot application entry.

    {globalsettings}        Contains the collection of global settings that
                            should be inherited by all boot application
                            entries.

    {bootloadersettings}    Contains the collection of global settings that
                            should be inherited by all Windows boot loader
                            application entries.

    {resumeloadersettings}  Contains the collection of global settings that
                            should be inherited by all Windows resume from
                            hibernation application entries.

    {hypervisorsettings}    Contains the hypervisor settings that can
                            be inherited by any OS loader entry.