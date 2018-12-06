---
title: RunOnce Registry Key
description: RunOnce Registry Key
ms.assetid: dbeb7be7-4d38-49e2-944c-ea95d9914ebe
keywords:
- RunOnce registry key
- registry WDK device installations
- device installations WDK , registry
- installing devices WDK , registry
- Device setup WDK device installations , registry
- driver registry RunOnce key WDK device installations
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# RunOnce Registry Key





All versions of Windows support a registry key, **RunOnce**, which can be used to specify commands that the system will execute one time and then delete.

In Windows 8 and Windows 8.1, **RunOnce** entries for installation of software-only SWENUM devices are processed during device installation. Other **RunOnce** entries are added to the **RunOnce** key. These are applied the next time the system processes the **RunOnce** key. Device installation does not force the system to process **RunOnce** entries.

In Windows 7 and previous versions, immediately after a device is installed, Windows executes the command stored under the **RunOnce** key and then removes the key. Additionally, each time the system starts, it executes the command stored under the **RunOnce** key and then removes the key. Therefore, if you put a command under the **RunOnce** key, you cannot easily predict when it is executed.

Immediately after a device has been installed, Windows executes the command stored under the **RunOnce** key and then removes the key. Additionally, each time the system starts, it executes the command stored under the **RunOnce** key and then removes the key. Therefore, if you put a command under the **RunOnce** key, you cannot easily predict when it is executed.

For device installations, **RunOnce** registry keys can be created by using *add-registry-sections*, which are specified through [**INF AddReg directives**](inf-addreg-directive.md). Each *add-registry-section* has the following syntax:

`reg-root, [subkey], [value-entry-name], [flags], [value]`

The registry root (*reg-root*) and subkey values for the **RunOnce** registry key are as follows:

**HKLM, "Software\\Microsoft\\Windows\\CurrentVersion\\RunOnce"**

The *value-entry-name* string is omitted from a **RunOnce** registry entry. The type of the entry, which is indicated by the *Flags* value, must be either [REG_SZ](https://docs.microsoft.com/windows/desktop/SysInfo/registry-value-types) (*Flags* value of 0x00000000) or [REG_EXPAND_SZ](https://docs.microsoft.com/windows/desktop/SysInfo/registry-value-types) (*Flags* value of 0x00010000). For an entry of type [REG_SZ](https://docs.microsoft.com/windows/desktop/SysInfo/registry-value-types) (the default), the *Flags* value can be omitted.

The *value* parameter in a **RunOnce** key specifies the command to be executed. This parameter is a quoted string that has the following format:

```cpp
Rundll32[.exe] DllName,EntryPoint[Arguments]
```

By default, a **RunOnce** key is deleted after the specified command is executed. You can prefix a **RunOnce** key *value* parameter with an exclamation point (!) to defer deletion of the key until after the command runs successfully. Without the exclamation point prefix, if the specified command fails, the **RunOnce** key will still be deleted and the command will not be executed the next time that the system starts.

Also, by default, the **RunOnce** keys are ignored when the system is started in Safe Mode. The *value* parameter of **RunOnce** keys can be prefixed with an asterisk (\*) to force the command to be executed even in Safe Mode.

Consider the following guidelines when you create a *value* string entry:

-   *Rundll32* can appear either with or without its *.exe* file name extension.

-   *DllName* is the full path of a DLL or executable image. Except for a required terminating comma, the expression must not otherwise contain any commas. If no file name extension is supplied, the default extension is *.dll*.

-   *EntryPoint* is the name of the entry point within the DLL indicated by *DllName*.

-   *Arguments* is an optional substring that contains any arguments that must be passed to the specified DLL.

-   Exactly one space must separate the *EntryPoint* string from the *Arguments* substring.

The following code example shows the *add-registry-section* entry that stores a command and its arguments under the **RunOnce** key:

```cpp
;; WDMAud swenum install

HKLM,%RunOnce%,"WDM_WDMAUD",,\
"rundll32.exe streamci.dll,StreamingDeviceSetup %WDM_WDMAUD.DeviceId%,%KSNAME_Filter%,%KSCATEGORY_WDMAUD%,%17%\WDMAUDIO.inf,WDM_WDMAUD.Interface.Install"

[Strings]
RunOnce = "SOFTWARE\Microsoft\Windows\CurrentVersion\RunOnce"
WDM_WDMAUD.DeviceId = "{CD171DE3-69E5-11D2-B56D-0000F8754380}"
KSNAME_Filter = "{9B365890-165F-11D0-A195-0020AFD156E4}"
KSCATEGORY_WDMAUD = "{3E227E76-690D-11D2-8161-0000F8775BF1}"
```

The following rules apply when you use **RunOnce** registry keys for device installations:

-   These registry keys must be used only for installations of software-only devices that are enumerated by SWENUM, the software device enumerator.

-   **RunOnce** keys must consist only of calls to *Rundll32.exe*. Otherwise, WHQL will not digitally sign the [driver package](driver-packages.md).

-   The code to be executed must not prompt for user input.

-   Server-side installations execute in a system context. For this reason, you must be certain that the code to be executed contains no security vulnerabilities and that file permissions prevent the code from being maliciously modified.

-   Starting with Windows Vista, the system will not execute the commands specified by the **RunOnce** keys if a user without administrator privileges is logged on to the system. This could lead to incomplete or corrupted installations following a system restart.

    Before the [*device installation application*](https://msdn.microsoft.com/library/windows/hardware/ff556277#wdkgloss-device-installation-application) creates the **RunOnce** entries, it informs the current user that a user who has administrator privileges must log on after a system restart.

    For more information, see [Developing Applications that Run at Logon on Windows Vista](http://go.microsoft.com/fwlink/p/?linkid=133224).

 

 





