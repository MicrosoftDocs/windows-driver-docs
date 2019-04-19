---
title: Boot Options Identifiers
description: Describes Boot Options Identifiers
ms.assetid: bd0caf3f-bb35-4242-a10a-4efa91a21797
keywords:
- boot options Windows
- identifiers
- default
- WDK boot options
ms.date: 04/19/2019
ms.localizationpriority: medium
---

# Boot Options Identifiers

Many of the Bcdedit commands require identifiers. An identifier uniquely identifies entries contained in the store. An identifier takes the form of a globally unique identifier, or GUID. A GUID has the following format,
where each "x" represents a hexadecimal digit.

```guid
{xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxxxxxx}
```
For example:

```guid
{d2b69192-8f14-11da-a31f-ea816ab185e9}
```

Use bcdedit /enum to display the identifers.

```console
C:\>bcdedit /enum

Windows Boot Manager
--------------------
identifier              {bootmgr}

...

Windows Boot Loader
-------------------
identifier              {current}

```

The position of the dashes (-) and the braces at the beginning and end of the GUID are required.

Several entries can be identified by well-known identifiers. If an entry has a well-known identifier, BCDedit displays it in output unless the /v command-line switch is used. For more information, run "bcdedit /? /v".

The common well-known identifiers are often used:

| Indentifier           | Description
|-----------------------|----------------------------------------------------------------------|
|    {default}          |     Specifies a virtual identifier that corresponds to the boot manager default application entry. | 
|    {current}          |     Specifies a virtual identifier that corresponds to the operating system boot entry for the operating system that is currently running. |
|    {bootmgr}          |     Specifies the Windows boot manager entry. |

These common well-known identifiers can be inherited by any boot application entry:

| Indentifier           | Description
|-----------------------|----------------------------------------------------------------------|
|    {dbgsettings}       |    Contains the global debugger settings that can be inherited by any boot application entry. |
|    {globalsettings}    |    Contains the collection of global settings that should be inherited by all boot application entries. |
|   {bootloadersettings} |   Contains the collection of global settings that should be inherited by all boot loader application entries. |

These well-known identifiers are also available for use:

| Indentifier           | Description
|-----------------------|----------------------------------------------------------------------|
|    {hypervisorsettings} |   Contains the hypervisor settings that can be inherited by any OS loader entry. |
|    {emssettings}       |  Contains the global Emergency Management Services settings that can be inherited by any boot application entry. |
|    {resumeloadersettings} | Contains the collection of global settings that should be inherited by all Windows resume from hibernation application entries. |
|    {badmemory}         |    Contains the global RAM defect list that can be inherited by any boot application entry. |
|   {memdiag}           |    Specifies the memory diagnostic application entry. |
|    {ramdiskoptions}    |   Contains the additional options required by the boot manager for RAM disk devices. |

These well-known identifiers are used with eariler versions of Windows:

| Indentifier           | Description
|-----------------------|----------------------------------------------------------------------|
|    {ntldr}            |     Specifies a OS loader (Ntldr) that can be used to start operating systems earlier than Windows Vista.|
|    {fwbootmgr}        |     Specifies the firmware boot manager entry, specifically on systems that implement the Extensible Firmware Interface (EFI) specification.|


## Boot Identifier Setting Inheritance



