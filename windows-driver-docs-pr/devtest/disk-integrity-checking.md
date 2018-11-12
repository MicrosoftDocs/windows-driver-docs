---
title: Disk Integrity Checking
description: Disk Integrity Checking
ms.assetid: bb838594-637c-4fc4-b2ec-964b69faabcf
keywords:
- Disk Integrity Checking feature WDK Driver Verifier
- disk storage accuracy WDK Driver Verifier
- storage accuracy WDK Driver Verifier
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# Disk Integrity Checking


## <span id="ddk_disk_integrity_verification_tools"></span><span id="DDK_DISK_INTEGRITY_VERIFICATION_TOOLS"></span>


The Disk Integrity Checking feature of Driver Verifier monitors all hard disk access to determine whether the disk accurately stores information. If the data on the disk appears to change, a bug check is issued.

This Driver Verifier option was introduced in Windows Server 2003 and was removed as an option starting with Windows 7.

### <span id="how_disk_integrity_checking_works"></span><span id="HOW_DISK_INTEGRITY_CHECKING_WORKS"></span>How Disk Integrity Checking Works

When you activate Disk Integrity Checking, you can choose to verify any or all of the physical disks attached to your computer.

As soon as Windows and its drivers are loaded, Driver Verifier begins to monitor all read and write actions made to these drives. Driver Verifier calculates a CRC (cyclic redundancy check) checksum value for each sector that is accessed and saves this value. The next time this sector is accessed, Driver Verifier recalculates this checksum and compares it to the previous value.

If the checksum value changes, this indicates a disk integrity problem -- either the read operation is returning faulty information, or the disk medium has altered its contents since the last access was made. When this happens, Driver Verifier issues bug check 0xC4 with Parameter 1 equal to 0xA0. The other parameters identify the IRP making the request, the device object of the lower device, and the sector in which the error occurred. For details, see [**Bug Check 0xC4**](https://msdn.microsoft.com/library/windows/hardware/ff560187) (DRIVER\_VERIFIER\_DETECTED\_VIOLATION).

### <span id="performance_issues"></span><span id="PERFORMANCE_ISSUES"></span>Performance Issues

The Disk Integrity Checking feature makes hard disk access perceptibly slower. If the computer is low on RAM, this performance decrease is even more significant. Use Disk Integrity Checking to investigate disk problems, but do not activate whenever when you are running Driver Verifier to test drivers.

**Note**   The Disk Integrity Checking feature is not designed to work on systems that use clustered shared disks. If you enable the Disk Integrity Checking feature on such a system, the disk integrity check might falsely cause a bug check to occur. Therefore, it is strongly recommended that you do not enable this feature on systems with clustered shared disks.
In addition, there are some circumstances that might lead to false bug checks on systems with non-clustered disks. These circumstances include:

-   Memory writes to in-flight write buffers

-   Concurrent in-flight reads and writes to the same sector

 

### <span id="activating_this_option"></span><span id="ACTIVATING_THIS_OPTION"></span>Activating This Option

You can activate the Disk Integrity Checking option by using Driver Verifier Manager or the Verifier.exe command line. Driver Verifier Manager lets you determine which disks are verified. If you use the command line, all disks are verified. For details, see [Selecting Driver Verifier Options](selecting-driver-verifier-options.md).

-   **At the command line**

    At the command line, the Disk Integrity Checking option is represented by the **/disk** parameter. For example:

    ```
    verifier /disk /driver MyDriver.sys
    ```

    The feature will be active after the next boot. You cannot activate the Disk Integrity Checking option without rebooting the computer on any version of Windows.

-   **Using Driver Verifier Manager**
    1.  Select **Create custom settings (for code developers)** and then click **Next**.
    2.  Select **Select individual settings from a full list**.
    3.  Select (check) **Disk integrity checking**.

 

 





