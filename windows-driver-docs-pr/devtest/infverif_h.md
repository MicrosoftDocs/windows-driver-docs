---
title: InfVerif /h
description: This topic describes the functionality and usage of InfVerif with '/h' mode.
ms.date: 03/27/2024
---

# InfVerif /h
> [!NOTE]
InfVerif /h was introduced in Windows Insider Preview build 26080.

InfVerif /h is new mode of [InfVerif](infverif.md) that validates using a set of INF requirements that change with each release to align with the requirements for a WHQL signature from Hardware Dev Center. Over time, the requirements will become stricter and eventually align with [driver package isolation](../develop/driver-isolation.md) requirements.

InfVerif /h examines all the OS versions where the INF may install, and evaluates the INF using the appropriate rules for that OS version automatically. For example, in an INF file that uses [version decorations](../install/inf-manufacturer-section.md) to change the behavior for different OS versions:

```inf
Contoso = Models, NTAMD64, NTAMD64.10.0...22000
```

InfVerif /h will internally validate this INF twice, once validating the [[Models] section](../install/inf-models-section.md) [Models.NTAMD64] using the rules for build 21999 (the highest OS version where that [Models] section will be used), and once validating the [Models] section [Models.NTAMD64.10.0...22000] using the latest ruleset. An INF file that only has a single [Models] section will only be validated against the latest rule set.


## Usage
To use InfVerif /h using the default behavior:
```command
infverif.exe /h <INF file> [<INF file>]
```

InfVerif /h also allows you to specify the highest rule set that InfVerif will use using the '/rulever' argument, for example:

```command
infverif.exe /h /rulever NTAMD64.10.0...17763 <INF file>
```

Using the '/rulever' argument may cause some portions of the INF to be ignored. Using the above arguments with the previous example, the [Models] section [Models.NTAMD64] will be validated using the rules for build 17763, and [Models.NTAMD64.10.0...22000] will not be validated since the high ruleset does not apply to it.

Adding the verbose options will cause InfVerif to print out the maximum ruleset used during its evaluation:

```command
> infverif.exe /h /v <INF file>

Running in Verbose
Running signature requirements check
Using rules from OS build: 10.0.26080

> infverif.exe /h /rulever NTAMD64.10.0...17763 <INF file>

Running in Verbose
Running signature requirements check
Using rules from OS build: 10.0.17763
```

InfVerif /h can also use a future ruleset. There is a built-in 'vnext' OS version that will use the rules expected to be required one OS release in the future. The rules enforced by 'vnext' are not final and subject to change for the final release, but are intended to provide a good insight into future requirements.

```command
infverif.exe /h /rulever vnext <INF file>
```

## Requirements
The InfVerif /h rulesets are aligned with the requirements of the WHCP program. The requirements are defined as the full [driver package isolation](../develop/driver-isolation.md) requirements, with some set of exceptions applied to the requirements. Some exceptions will be removed each release until InfVerif /h enforces all driver package isolation requirements.

> [!NOTE]
Any exceptions listed below should not be used, as the usage of them will no longer be allowed in an upcoming release.

### Current Requirements as of April 2024

**Registry**
<br/>INF files must not modify any global registry locations, and instead only use the HKR registry root to modify or create registry information with an [AddReg directive](../install/inf-addreg-directive.md). The following paths are current exceptions to this requirement:

| Root | Subkey |
|------|--------|
|HKLM|SYSTEM\CurrentControlSet|
|HKLM|SOFTWARE\Classes|
|HKLM|SOFTWARE\Khronos|
|HKLM|SOFTWARE\Microsoft\Analog\Providers|
|HKLM|SOFTWARE\Microsoft\Cellular\MVSettings\DeviceSpecific\CellUX|
|HKLM|SOFTWARE\Microsoft\Cryptography\Calais\Readers|
|HKLM|SOFTWARE\Microsoft\Cryptography\Calais\SmartCards|
|HKLM|SOFTWARE\Microsoft\Cryptography\DRM_RNG|
|HKLM|SOFTWARE\Microsoft\EAPOL|
|HKLM|SOFTWARE\Microsoft\Palm\DelayManipulationDuration|
|HKLM|SOFTWARE\Microsoft\Shell\OEM\QuickActions\ColorProfileQuickAction|
|HKLM|SOFTWARE\Microsoft\Speech_OneCore\AudioInput|
|HKLM|SOFTWARE\Microsoft\Windows Media Foundation|
|HKLM|SOFTWARE\Microsoft\Windows NT\CurrentVersion\AdaptiveDisplayBrightness|
|HKLM|SOFTWARE\Microsoft\Windows NT\CurrentVersion\drivers.desc|
|HKLM|SOFTWARE\Microsoft\Windows NT\CurrentVersion\Drivers32|
|HKLM|SOFTWARE\Microsoft\Windows NT\CurrentVersion\ICM|
|HKLM|SOFTWARE\Microsoft\Windows NT\CurrentVersion\OpenGlDrivers|
|HKLM|SOFTWARE\Microsoft\Windows NT\CurrentVersion\Winlogon\Notify\ScCertProp|
|HKLM|SOFTWARE\Microsoft\Windows\CurrentVersion\App Paths|
|HKLM|SOFTWARE\Microsoft\Windows\CurrentVersion\Audio|
|HKLM|SOFTWARE\Microsoft\Windows\CurrentVersion\Authentication|
|HKLM|SOFTWARE\Microsoft\Windows\CurrentVersion\Control Panel|
|HKLM|SOFTWARE\Microsoft\Windows\CurrentVersion\Controls Folder|
|HKLM|SOFTWARE\Microsoft\Windows\CurrentVersion\Explorer|
|HKLM|SOFTWARE\Microsoft\Windows\CurrentVersion\Reliability\UserDefined|
|HKLM|SOFTWARE\Microsoft\Windows\CurrentVersion\Run|
|HKLM|SOFTWARE\Microsoft\Windows\CurrentVersion\RunOnce|
|HKLM|SOFTWARE\Microsoft\Windows\CurrentVersion\Uninstall|
|HKLM|SOFTWARE\Wow6432Node\Microsoft\Windows Media Foundation|
|HKLM|SOFTWARE\Wow6432Node\Khronos|
|HKLM|SOFTWARE\WowAA32Node\Microsoft\Windows Media Foundation|
|HKLM|SOFTWARE\WowAA32Node\Khronos|
|HKCR||

<br/>

**File Paths**
<br/>DIRID 13 must be specified in the INF as the destination location for all entries in the [[DestinationDirs] section](../install/inf-destinationdirs-section.md). The following values are exceptions to this requirement:

|DIRID Value|
|-----------|
|DIRID 10|
|DIRID 11|
|DIRID 12|
|DIRID 23|
|DIRID 51|
|DIRID 52|
|DIRID 55|
|DIRID 16422|
|DIRID 16425|
|DIRID 16426|
|DIRID 16427|
|DIRID 16428|
|DIRID 66000|
|DIRID 66001|
|DIRID 66002|
|DIRID 66003|
|DIRID 66004|
