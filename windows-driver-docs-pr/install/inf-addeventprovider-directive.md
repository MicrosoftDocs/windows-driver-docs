---
title: INF AddEventProvider Directive
author: andylsn
description: An AddEventProvider directive is used within an INF DDInstall.Events section.
ms.assetid:
keywords:
- INF AddEventProvider Directive Device and Driver Installation
topic_type:
- apiref
api_name:
- INF AddEventProvider Directive
api_type:
- NA
ms.date: 06/04/2018
ms.localizationpriority: medium
---

# INF AddEventProvider Directive

An **AddEventProvider** directive is used within an [**INF *DDInstall*.Events section**](inf-ddinstall-services-section.md). It specifies characteristics of the [Event Tracing for Windows](https://msdn.microsoft.com/library/windows/desktop/aa363668) (ETW) providers associated with drivers. This directive is supported for Windows 10 version 1809 and later.

```cpp
[DDInstall.Events] 

AddEventProvider={ProviderGUID},event-provider-install-section
...
```

## Entries


<a href="" id="ProviderGUID"></a>*ProviderGUID*  
Specifies the GUID value that identifies the provider. This can be expressed as an explicit GUID value of the form `{nnnnnnnn-nnnn-nnnn-nnnn-nnnnnnnnnnnn}` or as a %strkey% token defined to `{nnnnnnnn-nnnn-nnnn-nnnn-nnnnnnnnnnnn}` in a [**Strings**](inf-strings-section.md) section of the INF file.

<a href="" id="event-provider-install-section"></a>*event-provider-install-section*  
References an INF-writer-defined section that contains information for registering the provider for this device (or devices). For more information, see the following **Remarks** section.

Remarks
-------

The system-defined and case-insensitive extensions can be inserted into a <em>DDInstall</em>**.Events** section that contains an **AddEventProvider** directive in cross-operating system and/or cross-platform INF files to specify platform-specific or OS-specific installations.

Each INF-writer-created section name must be unique within the INF file and must follow the general rules for defining section names. For more information about these rules, see [General Syntax Rules for INF Files](general-syntax-rules-for-inf-files.md).

An **AddEventProvider** directive must reference a named *event-provider-install-section* elsewhere in the INF file. Each such section has the following form:

```cpp
[event-provider-install-section]
 
ProviderName=name
ResourceFile=path-to-file
[MessageFile=path-to-file]
[ParameterFile=path-to-file]
(ImportChannel=channel-name) |
(AddChannel=channel-name,channel-type[,channel-install-section])
...
```

Each *event-provider-install-section* must provide **ProviderName** and **ResourceFile**. Optionally, specify a list of channels for the provider using any combination of **ImportChannel(s)** and **AddChannel(s)**, each on a separate line. For more information about channel lists in an INF file, see [**Specifying a Channel List**](#specifying-a-channel-list) below. For more information about [Windows Event Log](https://msdn.microsoft.com/library/windows/desktop/aa385780) channels, see [Defining Channels](https://msdn.microsoft.com/library/windows/desktop/dd996911).

### Event-Provider-Install Section Entries and Values

<a href="" id="providername-name"></a>**ProviderName**=*name*  
Specifies the name of the provider. The name cannot be longer than 255 characters, and cannot contain the characters: '>', '<', '&', '"', '|', '\', ':', ''', '?', '*', or characters with ASCII values less than 31. In addition, the name must follow the general constraints on file and registry key names. These constraints can be found at [Naming a File](https://msdn.microsoft.com/library/windows/desktop/aa365247) and [Registry Element Size Limits](https://msdn.microsoft.com/library/windows/desktop/ms724872).

<a href="" id="resourcefile-path-to-file"></a>**ResourceFile**=*path-to-file*  
Specifies the path to the exe or dll that contains the provider's metadata resources, expressed as %dirid%\filename.

The *dirid* number is either a custom directory identifier or one of the system-defined directory identifiers described in [Using Dirids](using-dirids.md).

<a href="" id="messagefile-path-to-file"></a>**MessageFile**=*path-to-file*  
Optionally specifies the path to the exe or dll that contains the provider's localized message resources, expressed as %dirid%\filename.

<a href="" id="parameterfile-path-to-file"></a>**ParameterFile**=*path-to-file*  
Optionally specifies the path to the exe or dll that contains the provider's parameter string resources, expressed as %dirid%\filename.

<a href="" id="importchannel-channel-name"></a>**ImportChannel**=*channel-name*  
Optionally specifies a channel that has been defined by another provider. For more information, see the following **Specifying a Channel List** section.

<a href="" id="addchannel-channel-name-channel-type--channel-install-section-"></a>**AddChannel**=*channel-name*,*channel-type*\[,*channel-install-section*\]  
Optionally specifies a channel with a sub-directive that optionally references an INF-writer-defined channel-install-section elsewhere in the INF file. For more information, see the following **Specifying a Channel List** section.

### Specifying a Channel List

You can specify a list of channels for the provider within its *event-provider-install-section*. You can import a channel or add a channel to the list and the order of these channels is preserved. For more information, see [Defining Channels](https://msdn.microsoft.com/library/windows/desktop/dd996911).

The *channel-name* must be unique within the list of channels that the provider uses. The *channel-name* must be less than 255 characters and cannot contain the following characters: '>', '<', '&', '"', '|', '\', ':', '`', '?', '*', or characters with ASCII values less than 31.

The *channel-type* can be specified as one of the following numeric values, expressed either in decimal or, as shown in the following list, in hexadecimal notation.

<a href="" id="0x1--admin-"></a>**0x1** (Admin)  
Admin type channels support events that target end users, administrators, and support personnel. Events written to the Admin channels should have a well-defined solution on which the administrator can act.

<a href="" id="0x2--operational-"></a>**0x2** (Operational)  
Operational type channels support events that are used for analyzing and diagnosing a problem or occurrence. They can be used to trigger tools or tasks based on the problem or occurrence.

<a href="" id="0x3--analytic-"></a>**0x3** (Analytic)  
Analytic type channels support events that are published in high volume. They describe program operation and indicate problems that cannot be handled by user intervention.

<a href="" id="0x4--debug-"></a>**0x4** (Debug)  
Debug type channels support events that are used solely by developers to diagnose a problem for debugging.

An **AddChannel** sub-directive can also reference a *channel-install-section* elsewhere in the INF file. Each such section has the following form:

```cpp
[channel-install-section]

[Isolation=isolation-type]
[Access=access-string]
[Enabled=0|1]
[Value=value]
[LoggingMaxSize=max-size]
[LoggingRetention=retention-type]
[LoggingAutoBackup=0|1]
```

For more information about channel attributes, see [ChannelType](https://msdn.microsoft.com/library/windows/desktop/aa382741) defined within [EventManifest Schema](https://msdn.microsoft.com/library/windows/desktop/aa384043).

### Channel-Install Section Entries and Values

<a href="" id="isolation-isolation-type"></a>**Isolation**=*isolation-type*  
Optionally specifies the default access permissions for the channel as one of the following numeric values, expressed either in decimal or, as shown in the following list, in hexadecimal notation. If omitted, this defaults to **0x1** (Application).

<a href="" id="0x1--application-"></a>**0x1** (Application)  

<a href="" id="0x2--system-"></a>**0x2** (System)  

<a href="" id="0x3--Custom-"></a>**0x3** (Custom)  

<a href="" id="access-access-string"></a>**Access**=*access-string*  
Optionally specifies a [Security Descriptor Definition Language](https://msdn.microsoft.com/library/windows/desktop/aa379567) (SDDL) access descriptor that controls access to the log file that backs the channel.

This string controls read access to the file (the write permissions are ignored) if the **Isolation** is set to **0x1** (Application) or **0x2** (System), while it controls write access to the channel and read access to the file if the isolation attribute is set to **0x3** (Custom).

<a href="" id="enabled-0-1"></a>**Enabled**=**0|1**  
Optionally specifies whether the channel is enabled. If omitted, this defaults to 0 (disabled).

Because **0x3** (Analytic) and **0x4** (Debug) *channel-type* are high volume channels, you should set the **Enabled** to 1 only when investigating an issue with a component that writes to that channel. Each time you enable a **0x3** (Analytic) and **0x4** (Debug) channel, the service clears the events from the channel.

<a href="" id="value-value"></a>**Value**=*value*  
Optionally specifies a numeric identifier that uniquely identifies the channel within the list of channels that the provider defines.

<a href="" id="loggingmaxsize-max-size"></a>**LoggingMaxSize**=*max-size*  
Optionally specifies the maximum size, in bytes, of the log file. The default (and minimum) value is 1 MB.

<a href="" id="loggingretention-retention-type"></a>**LoggingRetention**=*retention-type*  
Optionally specifies whether the log file is **0x1** (circular) or **0x2** (sequential). The default is **0x1** (circular) for **0x1** (Admin) and **0x2** (Operational) *channel-type* and **0x2** (sequential) for **0x3** (Analytic) and **0x4** (Debug) *channel-type*.

<a href="" id="loggingautobackup-0-1"></a>**LoggingAutoBackup**=**0|1**  
Optionally specifies whether to create a new log file when the current log file reaches its maximum size. Set to 1 to request that the service create a new file when the log file reaches its maximum size; otherwise, 0. You can set the **LoggingAutoBackup** to 1 only if the **LoggingRetention** is set to **0x2** (sequential) and only for **0x1** (Admin) and **0x2** (Operational) *channel-type*.

Examples
--------

This example shows the event-provider-install sections referenced by the **AddEventProvider** directives as already shown earlier in the example for [***DDInstall*.Events**](inf-ddinstall-events-section.md).

```cpp
[foo_Event_Provider_Inst]
ProviderName  = FooCollector
ResourceFile  = %13%\FooResource.dll
MessageFile   = %13%\FooMessage.exe

[bar_Event_Provider_Inst]
ProviderName  = BarCollector
ResourceFile  = %13%\BarResource.exe
MessageFile   = %13%\BarMessage.dll
ParameterFile = %13%\BarParameter.dll
ImportChannel = Microsoft-Windows-BaseProvider/Admin
AddChannel    = Bar-Provider/Admin,0x1,bar_Channel2_Inst    ; Admin type
ImportChannel = Microsoft-Windows-BaseProvider/Operational
ImportChannel = Microsoft-Windows-SampleProvider/Admin
AddChannel    = Bar-Provider/Debug,0x4                      ; Debug type

[bar_Channel2_Inst]
Isolation         = 2                                       ; System isolation
Enabled           = 1
Value             = 17
LoggingMaxSize    = 20971520
LoggingRetention  = 2                                       ; Sequential
LoggingAutoBackup = 1
```

## See also


[***DDInstall*.Events**](inf-ddinstall-events-section.md)

 

 





