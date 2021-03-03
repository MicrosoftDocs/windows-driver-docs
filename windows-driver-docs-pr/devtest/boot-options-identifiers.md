---
title: Boot Options Identifiers
description: Describes Boot Options Identifiers
keywords:
- boot options Windows
- identifiers
- default
- WDK boot options
ms.date: 04/22/2019
ms.localizationpriority: medium
---

# Boot Options Identifiers

Many of the bcdedit commands require identifiers. An identifier uniquely identifies entries contained in the boot setting store. 

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

Several entries can be identified by well-known identifiers. If an entry has a well-known identifier, bcdedit displays it in output unless the /v command-line switch is used. For more information, run "bcdedit /? /v".

The common well-known identifiers are often used:

| Identifier           | Description
|-----------------------|----------------------------------------------------------------------|
|    {default}          |     Specifies a virtual identifier that corresponds to the boot manager default application entry. | 
|    {current}          |     Specifies a virtual identifier that corresponds to the operating system boot application entry for the operating system that is currently running. |
|    {bootmgr}          |     Specifies the Windows boot manager application entry. |

These common well-known identifiers can be inherited by any boot application entry:

| Identifier           | Description
|-----------------------|----------------------------------------------------------------------|
|    {globalsettings}    |    Contains the collection of global settings that should be inherited by all boot application entries. |
|   {bootloadersettings} |   Contains the collection of global settings that should be inherited by all boot loader application entries. |

These well-known identifiers are also available for use:

| Identifier           | Description
|-----------------------|----------------------------------------------------------------------|
|    {dbgsettings}       |    Contains the global debugger settings that can be inherited by any boot application entry. |
|    {hypervisorsettings} |   Contains the hypervisor settings that can be inherited by any OS loader entry. |
|    {emssettings}       |  Contains the global Emergency Management Services settings that can be inherited by any boot application entry. |
|    {resumeloadersettings} | Contains the collection of global settings that should be inherited by all Windows resume from hibernation application entries. |
|    {badmemory}         |    Contains the global RAM defect list that can be inherited by any boot application entry. |
|   {memdiag}           |    Specifies the memory diagnostic application entry. |
|    {ramdiskoptions}    |   Contains the additional options required by the boot manager for RAM disk devices. |

These well-known identifiers are used with earlier versions of Windows:

| Identifier           | Description
|-----------------------|----------------------------------------------------------------------|
|    {ntldr}            |     Specifies a OS loader (Ntldr) that can be used to start operating systems earlier than Windows Vista.|
|    {fwbootmgr}        |     Specifies the firmware boot manager entry, specifically on systems that implement the Extensible Firmware Interface (EFI) specification.|

## Boot Option Inheritance

Some boot settings can be inherited. This allows for groups of settings to be used in different boot scenarios, for example when resuming from hibernation.

Use the bcdedit command /enum option to display information about any identifier.

In the example below, displaying information on the {current} identifier shows that it inherits the {bootloadersettings}

```console
C:\>bcdedit /enum {current}

Windows Boot Loader
-------------------
identifier              {current}
device                  partition=C:
path                    \WINDOWS\system32\winload.exe
description             Windows 10
locale                  en-US
inherit                 {bootloadersettings}
...
```

Use the bcdedit /enum command to see which settings are inherited.

In the example below, {globalsettings}, inherits whatever is set in {dbgsettings}, {emssettings} and {badmemory}.

```console
C:\>bcdedit /enum {globalsettings}

Global Settings
---------------
identifier              {globalsettings}
inherit                 {dbgsettings}
                        {emssettings}
                        {badmemory}
```

Use the inherit option with bcdedit /enum to display information about inheritance.

In the example below, the {bootloadersettings} inherits {globalsettings} and the {hypervisorsettings} and the {resumeloadersettings} inherit the {globalsettings}.

```console
C:\>bcdedit /enum inherit

...

Boot Loader Settings
--------------------
identifier              {bootloadersettings}
inherit                 {globalsettings}
                        {hypervisorsettings}


Resume Loader Settings
----------------------
identifier              {resumeloadersettings}
inherit                 {globalsettings}

...

```

Use the bcdedit /enum all command to see all of the settings.  

```console
C:\>bcdedit /enum all

Windows Boot Manager
--------------------
identifier              {bootmgr}
device                  partition=\Device\HarddiskVolume1
description             Windows Boot Manager

...

```

## GUIDs and Identifiers

An identifier uses a globally unique identifier, or GUID. A GUID has the following format, where each "x" represents a hexadecimal digit. Because working with GUIDs is error prone, it is recommended to use the english identifier name, such as {current} to work with the current boot information configured for Windows.

```guid
{xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxxxxxx}
```

For example:

```guid
{d2b69192-8f14-11da-a31f-ea816ab185e9}
```
The position of the dashes (-) and the braces at the beginning and end of the GUID are required.

Use bcdedit /enum /v to display GUIDs associated with identifiers.

```console
C:\>bcdedit /enum /v

Windows Boot Manager
--------------------
identifier              {9dea862c-5cdd-4e70-acc1-f32b344d4795}
device                  partition=\Device\HarddiskVolume1
description             Windows Boot Manager
locale                  en-US
inherit                 {7ea2e1ac-2e61-4728-aaa3-896d9d0a9f0e}
```
