---
title: INF AddAutoLogger and UpdateAutoLogger Directives
description: AddAutoLogger and UpdateAutoLogger directives used within an INF DDInstall.Events section.
keywords:
- INF AddAutoLogger and UpdateAutoLogger Directives Device and Driver Installation
topic_type:
- apiref
api_name:
- INF AddAutoLogger and UpdateAutoLogger Directives
api_type:
- NA
ms.date: 06/16/2021
---

# INF AddAutoLogger and UpdateAutoLogger Directives 

**AddAutoLogger** and **UpdateAutoLogger** directives are used within an [**INF *DDInstall*.Events section**](inf-ddinstall-services-section.md). They specify characteristics for [Event Tracing for Windows](/windows/desktop/ETW/about-event-tracing) (ETW) AutoLogger sessions that record events occurring early in the operating system boot process. These directives are supported starting in Windows 11.

```inf
[DDInstall.Events] 

AddAutoLogger=session-name,{SessionGUID},add-autologger-install-section 
UpdateAutoLogger=session-name,update-autologger-install-section 
... 
```

## Entries

<a href="" id="session-name"></a>*session-name*  
Specifies the name of the AutoLogger session that will be added. This name needs to be unique among the set of AutoLogger sessions on a machine. It is recommended that the session name include the name of your company or an abbreviation of your company name so it does not conflict with the name of a session from another company.

<a href="" id="SessionGUID"></a>*SessionGUID*  
Specifies the GUID value that identifies the AutoLogger session. This can be expressed as an explicit GUID value of the form `{nnnnnnnn-nnnn-nnnn-nnnn-nnnnnnnnnnnn}` or as a %strkey% token defined to `{nnnnnnnn-nnnn-nnnn-nnnn-nnnnnnnnnnnn}` in a [**Strings**](inf-strings-section.md) section of the INF file.

<a href="" id="add-autologger-install-section"></a>*add-autologger-install-section*  
References an INF-writer-defined section that contains information for registering the AutoLogger. For more information, see the following **Remarks** section.

<a href="" id="update-autologger-install-section"></a>*update-autologger-install-section*  
References an INF-writer-defined section that contains information for adding providers to an existing AutoLogger. For more information, see the following **Remarks** section.

## Remarks

For more information about AutoLoggers, see [Configuring and Starting an AutoLogger Session](/windows/win32/etw/configuring-and-starting-an-autologger-session).

Each INF-writer-created section name must be unique within the INF file and must follow the general rules for defining section names. For more information about these rules, see [General Syntax Rules for INF Files](general-syntax-rules-for-inf-files.md).

An **AddAutoLogger** directive must reference a names *add-autologger-install-section* elsewhere in the INF file. Each section has the following form:

```inf
[add-autologger-install-section] 

Start=<0 | 1> 
[BufferSize=buffer-size] 
[ClockType=clock-type] 
[DisableRealtimePersistence= <0 | 1>] 
[FileName=path-to-file] 
[FileMax=file-max]
[FlushTimer=flush-timer] 
[LogFileMode=log-file-mode] 
[MaxFileSize=max-file-size] 
[MaximumBuffers=max-buffers] 
[MinimumBuffers=min-buffers] 

(AddAutoLoggerProvider={ProviderGUID},autologger-provider-install-section) 
… 
```

Each *add-autologger-install-section* must provide **Start**. Optionally, specify one or more AutoLogger providers for the AutoLogger using **AddAutoLoggerProvider**, each on a separate line. For more information about AutoLogger providers in an INF file, see [Adding AutoLogger Providers](#adding-autologger-providers) below.

An **UpdateAutoLogger** directive must reference a named *update-autologger-install-section* elsewhere in the INF file. Each such section has the following form:

```inf
[update-autologger-install-section] 

(AddAutoLoggerProvider={ProviderGUID},autologger-provider-install-section) 
… 
```

Each *update-autologger-install-section* can specify one or more AutoLogger providers using **AddAutoLoggerProvider**, each on a separate line. For more information about AutoLogger providers in an INF file, see [Adding AutoLogger Providers](#adding-autologger-providers) below.

## Add-AutoLogger-Install-Section Entries and Values

<a href="" id="start-value"></a>**Start**=*0 | 1*  
Specifies whether the AutoLogger will start the next time the computer is restarted. To start the AutoLogger, set this value to 1, otherwise, set this value to 0.

<a href="" id="buffersize-buffer-size"></a>**BufferSize**=*buffer-size*  
Optionally specifies the size of each buffer, in kilobytes. **BufferSize** should be less than one megabyte. ETW uses the size of physical memory to calculate this value if it is not set.

<a href="" id="clocktype-clock-type"></a>**ClockType**=*clock-type*  
Optionally specifies the timer to use when logging the time stamp for each event using the following numeric values, expressed either in decimal or, as shown in the following list, in hexadecimal notation. If omitted, this defaults to **0x1** (Performance Counter Value). 

**0x1** (Performance Counter Value)

**0x2** (System Timer) 

**0x3** (CPU Cycle Counter)

For a description of each clock type, see the ClientContext member of [WNODE_HEADER](/windows/win32/etw/wnode-header). 

<a href="" id="disablerealtimepersistence-value"></a>**DisableRealtimePersistence**=*0 | 1*  
Optionally allows disabling of real time persistence by setting value to 1. The default is 0 (enabled). If real time persistence is enabled, real-time events that were not delivered by the time the computer was shutdown will be persisted. The events will then be delivered to the consumer the next time the consumer connects to the session.

<a href="" id="filename-file-name"></a>**FileName**=*file-name*  
Optionally specifies the fully qualified path of the log file. If the path does not exist, there will be a best effort creation the first time the AutoLogger starts. The length of **FileName** is limited to 1024 characters. The file is a sequential log file. The default file path is %DriverData%\\\<SessionName>.etl.

<a href="" id="filemax-file-max"></a>**FileMax**=*file-max*  
Optionally specifies the maximum number of instances of the log file that ETW creates. Once the maximum number of files has been created, ETW overwrites the first file, if it exists. The maximum number of instances of the log file that is supported is 16. Do not use this feature with the EVENT_TRACE_FILE_MODE_NEWLINE **LogFileMode**.

<a href="" id="flushtimer-flush-timer"></a>**FlushTimer**=*flush-timer*  
Optionally specifies how often, in seconds, the trace buffers are forcibly flushed. The minimum flush time is 1 second. The default value is 0. By default, buffers are flushed only when they are full. 

<a href="" id="logfilemode-log-file-mode"></a>**LogFileMode**=*log-file-mode*  
Optionally specifies one or more log modes. For possible values, see [Logging Mode Constants](/windows/win32/etw/logging-mode-constants). The default value is **0x1** (EVENT_TRACE_FILE_MODE_SEQUENTIAL).

<a href="" id="maxfilesize-max-file-size"></a>**MaxFileSize**=*max-file-size*  
Optionally specifies the maximum file size of the log file, in megabytes. The session is closed when the maximum size is reached, unless EVENT_TRACE_FILE_MODE_CIRCULAR is specified in **LogFileMode**. To specify no limit, set value to 0. The default value is 100 mb. The behavior that occurs when the maximum file size is reached depends on the value of **LogFileMode**. 

<a href="" id="maximumbuffers-maximum-buffers"></a>**MaximumBuffers**=*maximum-buffers*  
Optionally specifies the maximum number of buffers to allocate, typically the minimum number of buffers plus twenty. This value must be greater than or equal to the value of **MinimumBuffers**. 

<a href="" id="minimumbuffers-minimum-buffers"></a>**MinimumBuffers**=*minimum-buffers*  
Optionally specifies the minimum number of buffers to allocate at startup. The minimum number of buffers you can specify is two buffers per processor. 

<a href="" id="addautologgerprovider-providerguid-autologger-provider-installsection"></a>**AddAutoLoggerProvider**=*{ProviderGUID}*,*autologger-provider-install-section*  
Optionally specifies a provider with a sub-directive that references an INF-writer-defined autologger-provider-install-section elsewhere in the INF file. For more information, see the following [Adding AutoLogger Providers](#adding-autologger-providers) section.

## Adding AutoLogger Providers

Within the *add-autologger-install-section* and *update-autologger-install-section* sections, you can specify providers that you want to enable in the session using the **AddAutoLoggerProvider** directive.

The *ProviderGUID* must be a GUID value that identifies the AutoLogger provider. This can be expressed as an explicit GUID value of the form {nnnnnnnn-nnnn-nnnn-nnnn-nnnnnnnnnnnn} or as a %strkey% token defined to {nnnnnnnn-nnnn-nnnn-nnnn-nnnnnnnnnnnn} in a Strings section of the INF file.

An AddAutoLoggerProvider sub-directive must also reference an *autologger-provider-install-section* elsewhere in the file. Each such section has the following form: 

```inf
[autologger-provider-install-section] 

[Enabled=<0 | 1>] 
[EnableFlags=enable-flags] 
[EnableLevel=enable-level] 
[EnablePropety=enable-property] 
[MatchAnyKeyword=match-any-keyword] 
[MatchAllKeyword=match-all-keyword] 
```

## AutoLogger-Provider-Install-Section Entries and Values 

<a href="" id="enabled-value"></a>**Enabled**=*0 | 1*  
Optionally supplies whether the provider is enabled. To enable the provider, set this value to 1. To disable, set the value to 0. The default value is 0.

<a href="" id="enableflags-enable-flags"></a>**EnableFlags**=*enable-flags*  
Optionally specifies the class of events for which the provider generates events. For details, see the *EnableFlags* parameter of the [EnableTraceEx](/windows/win32/api/evntrace/nf-evntrace-enabletraceex) function. Specify this value name if the provider does not support **MatchAnyKeyword** or **MatchAllKeyword**. 

<a href="" id="enablelevel-enable-level"></a>**EnableLevel**=*enable-level*  
Optionally supplies the level of detail included in the event. For a list of predefined levels, see the *Level* parameter of the [EnableTraceEx](/windows/win32/api/evntrace/nf-evntrace-enabletraceex) function. 

<a href="" id="enableproperty-enable-property"></a>**EnableProperty**=*enable-property*  
Optionally supplies the inclusion of one or more of the following items in the log file: 

**0x00000001** (EVENT_ENABLE_PROPERTY_SID) = Include in the extended data the security identifier (SID) of the user.

**0x00000002** (EVENT_ENABLE_PROPERTY_TS_ID) = Include in the extended data the terminal session identifier.

**0x00000004** (EVENT_ENABLE_PROPERTY_STACK_TRACE) = Include in the extended data a call stack trace for events written using [EventWrite](/windows/win32/api/evntprov/nf-evntprov-eventwrite).

**0x00000010** (EVENT_ENABLE_PROPERTY_IGNORE_KEYWORD_0) = Filters out all events that do not have a non-zero keyword specified.

**0x00000020** (EVENT_ENABLE_PROPERTY_PROVIDER_GROUP) = Indicates that this call to [EnableTraceEx2](/windows/win32/api/evntrace/nf-evntrace-enabletraceex2) should enable a [Provider Group](/windows/win32/etw/provider-traits) rather than an individual Event Provider.

**0x00000080** (EVENT_ENABLE_PROPERTY_PROCESS_START_KEY) = Include the Process Start Key in the extended data.

**0x00000100** (EVENT_ENABLE_PROPERTY_EVENT_KEY) = Include the Event Key in the extended data.

**0x00000200** (EVENT_ENABLE_PROPERTY_EXCLUDE_INPRIVATE) = Filters out all events that are either marked as an InPrivate event or come from a process that is marked as InPrivate.

<a href="" id="matchanykeyword-match-any-keyword"></a>**MatchAnyKeyword**=*match-any-keyword*  
Optionally supplies a bitmask of keywords that determine the category of events that you want the provider to write. The provider writes the event if any of the event’s keyword bits match any of the bits set in this mask. To specify that the provider writes all events, set this value to zero. For an example, see the Remarks section of the [EnableTraceEx](/windows/win32/api/evntrace/nf-evntrace-enabletraceex) function. 

<a href="" id="matchallkeyword-match-all-keyword"></a>**MatchAllKeyword**=*match-all-keyword*  
Optionally restricts the category of events that you want the provider to write. If the event’s keyword meets the **MatchAnyKeyword** condition, the provider will write the event only if all of the bits in this mask exist in the event’s keyword. This mask is not used if **MatchAnyKeyword** is zero. For an example, see the Remarks section of the [EnableTraceEx](/windows/win32/api/evntrace/nf-evntrace-enabletraceex) function.

## Examples
```inf
[Contoso_Add_AutoLogger_Inst] 
Start = 1 
FileName = %%DriverData%%\Contoso\AutoLoggerLogFile.etl  
AddAutoLoggerProvider = {4b8b1947-ae4d-54e2-826a-1aee78ef05b2}, Contoso_Provider_1_Inst

[Contoso_Update_AutoLogger_Inst] 
AddAutoLoggerProvider= {a55d5a23-1a5b-580a-2be5-d7188f43fae1}, Contoso_Provider_2_Inst

[Contoso_Provider_1_Inst] 
Enabled = 1
EnableProperty = 0x00000001

[Contoso_Provider_2_Inst] 
Enabled = 1 
```

## Legacy Compatibility

The AddAutoLogger and UpdateAutoLogger directives are supported starting in Windows 11. To configure an AutoLogger on a downlevel OS, use the [AddReg](inf-addreg-directive.md) directive.

```inf
[Contoso_AutoLogger_AddReg] 
HKLM,SYSTEM\CurrentControlSet\Control\WMI\Autologger\<autologger-session-name>,Start,0x00010001,1 
HKLM,SYSTEM\CurrentControlSet\Control\WMI\Autologger\<autologger-session-name>,GUID,,{autologger-guid} 
HKLM,SYSTEM\CurrentControlSet\Control\WMI\Autologger\<autologger-session-name>\{autologger-provider-guid},Enabled,0x00010001,1 
```

## See Also

[***DDInstall*.Events**](inf-ddinstall-events-section.md)
