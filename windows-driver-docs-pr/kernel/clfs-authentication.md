---
title: CLFS Logfile Authentication
description: CLFS logfile authentication
keywords: ["Common Log File System WDK kernel , authentication", "CLFS WDK kernel , authentication", "authentication WDK CLFS", "Common Log File System WDK kernel , security mitigation", "CLFS WDK kernel , security mitigation", "security mitigation WDK CLFS"]
ms.date: 09/19/2025
ms.topic: concept-article
---

# CLFS logfile authentication

CLFS logfile authentication is a security mitigation which improves the safety of file parsing by ensuring the CLFS driver is the author and writer of logfiles. The logfile authentication is accomplished by recording hash-based message authentication codes (HMAC) in a reserved section at the end of each logfile. If a logfile is created or modified by anything other than the CLFS API (for example, CLFS driver), then the logfile is deemed unsafe to parse and CLFS produces an error to the caller (`ERROR_LOG_METADATA_CORRUPT` in user mode, `STATUS_LOG_METADATA_CORRUPT` in kernel mode).
CLFS authentication checking is enabled by default on the following versions:

* Windows 11, version 25H2

## User impact

Authentication codes are created by hashing together logfile data and a system-unique cryptographic key. Because the cryptographic key
is unique to each system, CLFS fails the authentication check on logfiles that were created on other systems, making CLFS logfiles nonportable without Administrator intervention (For more information, see the following sections).

### Storage overhead

A new file, with the extension .cnpf, is stored alongside the BLF and data containers. If the BLF for a logfile is located at C:\Users\User\example.blf, its patch file should be located at C:\Users\User\example.blf.cnpf. If a logfile isn't cleanly closed, the patch file holds data needed for CLFS to recover the logfile. The patch file is created with the same security attributes as the file it provides recovery information for. The file is around the same size as "FlushThreshold" (`HKLM\SYSTEM\CurrentControlSet\Services\CLFS\Parameters [FlushThreshold]`).

More file storage is allocated to store more authentication codes. Extra space is added on top of the file size requested by caller, such as when calling [ClfsAddLogContainer](/windows-hardware/drivers/ddi/wdm/nf-wdm-clfsaddlogcontainer) or [ClfsAddLogContainerSet](/windows-hardware/drivers/ddi/wdm/nf-wdm-clfsaddlogcontainerset). The amount of space needed for authentication codes depends on the requested size of the file. Refer to the following list for an estimate on how much more data is allocated for your logfiles:

- 512-KB container files allocate an additional ~8,192 bytes.

- 1024-KB container files allocate an additional ~12,288 bytes.

- 10-MB container files allocate an additional ~90,112 bytes.

- 100-MB container files allocate an additional ~57,344 bytes.

- 4-GB container files allocate an additional ~2,101,248 bytes.

### I/O overhead

Due to the increase in I/O operations for maintaining authentication codes, the time it takes to create, open, and write records to logfiles is increased. The increase in time for logfile creation and logfile open depends entirely on the size of the containers, with larger logfiles having a much more noticeable impact. On average, the amount of time it takes to write to a record to a logfile is doubled.

## Mitigation mode

By default, CLFS runs with the CLFS logfile authentication security mitigation enabled. CLFS produces a failure when opening logfiles have missing or invalid authentication codes.

A system receiving an update with this version of CLFS likely has existing logfiles on the system that don't have authentication codes. To ensure these logfiles get transitioned over to the new format, the system places the CLFS driver in a learning mode, which instructs CLFS to automatically add authentication codes to logfiles that don't have them. The automatic addition of authentication codes occurs at logfile open and only if the calling thread has write access to the underlying files. The adoption period is defined in the registry `HKEY_LOCAL_MACHINE\SYSTEM\CurrentControlSet\Services\CLFS\Authentication [EnforcementTransitionPeriod]` (in seconds).

While not recommended, the mitigation can be disabled. When disabled, CLFS doesn't perform authentication checks and parses potentially corrupted or malicious logfiles.

## Configuration

The CLFS logfile authentication mitigation mode can be managed (enabled/disabled) in several ways:

1. __MDM__, using the `/Vendor/MSFT/Policy/Config/FileSystem/ClfsAuthenticationChecking` policy.

1. __Group Policy__, using the __"Enable /disable CLFS logfile authentication"__ setting (under `Administrative Templates\System\Filesystem\`).

1. Modifying the `Mode` registry value found under `HKEY_LOCAL_MACHINE\SYSTEM\CurrentControlSet\Services\CLFS\Authentication`.

    1. A value of `0`: Mitigation is enforced. CLFS produces an error when opening logfiles that have missing or invalid authentication codes.

    1. A value of `1`: Mitigation is in learning mode. CLFS always opens logfiles. If a logfile is missing authentication codes, then CLFS generates and write the codes to the file (assuming caller has write access). This process is an audit mode that is intended for systems that are adopting this mitigation.

    1. A value of `2`: Mitigation is disabled by an Administrator.

    A local administrator can disable the mitigation with the following PowerShell command:

    ```pwsh
    Set-ItemProperty -Path "HKLM:\SYSTEM\CurrentControlSet\Services\CLFS\Authentication" -Name Mode -Value 2
    ```

## Correcting authentication codes with fsutil

The [fsutil clfs authenticate](/windows-server/administration/windows-commands/fsutil-clfs) command line utility is used by Administrators to add or correct authentication codes for a logfile. This command is useful for the following scenarios:

1. If a logfile isn't opened during the mitigation adoption period, or is missing authentication codes for any reason, this command can be used to add authentication codes to the logfile.

1. If you want to be able to open logfiles that were created on a different system (and therefore different cryptographic key), this command can be used to correct existing authentication codes using the local system's cryptographic key.

## See also

[ClfsAddLogContainer](/windows-hardware/drivers/ddi/wdm/nf-wdm-clfsaddlogcontainer)

[ClfsAddLogContainerSet](/windows-hardware/drivers/ddi/wdm/nf-wdm-clfsaddlogcontainerset)

[fsutil clfs authenticate](/windows-server/administration/windows-commands/fsutil-clfs)
