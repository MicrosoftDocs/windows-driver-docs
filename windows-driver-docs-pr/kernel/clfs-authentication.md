---
title: CLFS Logfile Authentication
description: CLFS Logfile Authentication
keywords: ["Common Log File System WDK kernel , authentication", "CLFS WDK kernel ,authentication ", "authentication WDK CLFS",
 "Common Log File System WDK kernel , security mitigation", "CLFS WDK kernel , security mitigation ", "security mitigation WDK CLFS"]
ms.date: 03/16/2025
---

# CLFS Logfile Authentication

"CLFS Logfile Authentication" is a security mitigation which improves the safety of file parsing by ensuring the CLFS driver is the author and writer of logfiles. This is accomplished by recording hash-based message authentication codes (HMAC) in a reserved section at the end of each logfile. If a logfile is created or modified by anything other than the CLFS API (i.e CLFS driver), then the logfile is deemed unsafe to parse and CLFS will produce an error to the caller (`ERROR_LOG_METADATA_CORRUPT` in usermode, `STATUS_LOG_METADATA_CORRUPT` in kernel mode).

## User impact

Authentication codes are created by hashing together logfile data and a system-unique cryptographic key. Because the cryptographic key
is unique to each system, CLFS will fail the authentication check on logfiles that were created on other systems, making CLFS logfiles non-portable without Administrator intervention (see below).

### Storage Overhead

A new file, with the extension “.cnpf”, will be stored alongside the BLF and data containers. If the BLF for a logfile is located at “C:\Users\User\example.blf”, its “patch file” should be located at “C:\Users\User\example.blf.cnpf”. If a logfile is not cleanly closed, the patch file will hold data needed for CLFS to recover the logfile. The patch file will be created with the same security attributes as the file it provides recovery information for. This file will be around the same size as “FlushThreshold” (`HKLM\SYSTEM\CurrentControlSet\Services\CLFS\Parameters [FlushThreshold]`).

Additional file storage will be allocated to store additional authentication codes. This additional space is added on top of the file size requested by caller, such as when calling [ClfsAddLogContainer](/windows-hardware/drivers/ddi/wdm/nf-wdm-clfsaddlogcontainer) or [ClfsAddLogContainerSet ](/windows-hardware/drivers/ddi/wdm/nf-wdm-clfsaddlogcontainerset). The amount of space needed for authentication codes depends on the requested size of the file. Refer to the list below for an estimate on how much additional data will be allocated for your logfiles:

* 512KB container files allocate an additional ~8192 bytes.
* 1024KB container files allocate an additional ~12288 bytes.
* 10MB container files allocate an additional ~90112 bytes.
* 100MB container files allocate an additional ~57344 bytes.
* 4GB container files allocate an additional ~2101248 bytes.

### I/O Overhead

Due to the increase in I/O operations for maintaining authentication codes, the time it takes to create, open, and write records to logfiles has increased.  The increase in time for logfile creation and logfile open depends entirely on the size of the containers, with larger logfiles having a much more noticeable impact. On average, the amount of time it takes to write to a record to a logfile has doubled.

## Mitigation Mode

By default, CLFS runs with the "CLFS Logfile Authentication" security mitigation enabled. CLFS will producing a failure when opening logfiles have missing or invalid authentication codes. 

A system receiving an update with this version of CLFS will likely have existing logfiles on the system that do not have authentication codes. To ensure these logfiles get transitioned over to the new format, the system will place the CLFS driver in a “learning mode”, which will instruct CLFS to automatically add authentication codes to logfiles that do not have them. The automatic addition of authentication codes will occur at logfile open and only if the calling thread has write access to the underlying files. The adoption period is defined in the registry `HKEY_LOCAL_MACHINE\SYSTEM\CurrentControlSet\Services\CLFS\Authentication [EnforcementTransitionPeriod]` (in seconds).

While not recommended, the mitigation can be disabled. When disabled, CLFS will not perform authentication checks and will parse potentially corrupted or malicious logfiles.

## Configuration

The CLFS Logfile Authentication mitigation mode can be managed (enabled/disabled) in a number of ways:

1. __MDM__, using the `/Vendor/MSFT/Policy/Config/FileSystem/ClfsAuthenticationChecking` policy.
1. __Group Policy__, using the __"Enable /disable CLFS logfile authentication"__ setting (under `Administrative Templates\System\Filesystem\`).
1. Modifying the `Mode` registry value found under `HKEY_LOCAL_MACHINE\SYSTEM\CurrentControlSet\Services\CLFS\Authentication`.
    1. A value of `0`, The mitigation is enforced. CLFS will produce an error when opening logfiles that have missing or invalid authentication codes.
    2. A value of `1`: The mitigation is in learning mode. CLFS will always open logfiles. If a logfile is missing authentication codes, then CLFS will generate and write the codes to the file (assuming caller has write access). This is an "audit" mode
    that is intended for systems that are adopting this mitigation.
    3. A value of `2`. The mitigation was disabled by an Administrator.

    A local administrator can disable the mitigation with the following powershell command:

    ```pwsh
    Set-ItemProperty -Path “HKLM:\SYSTEM\CurrentControlSet\Services\CLFS\Authentication” -Name Mode -Value 2
    ```

## Correcting Authentication Codes with fsutil

The [fsutil clfs authenticate](/windows-server/administration/windows-commands/fsutil-clfs) command line utility can be used by Administrators to add or correct authentication codes for a logfile. This command will be useful for the following scenarios:

1. If a logfile is not opened during the mitigation adoption period, or is missing authentication codes for any reason, this command can be used to add authentication codes to the logfile.
1. If you want to be able to open logfiles that were created on a different system (and therefore different cryptographic key), this
command can be used to correct existing authentication codes using the local system's cryptographic key.
