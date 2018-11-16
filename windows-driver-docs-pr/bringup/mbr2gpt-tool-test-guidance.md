---
title: MBR2GPT tool test guidance
description: MBR2GPT tool test guidance
ms.date: 05/07/2018
ms.localizationpriority: medium
---



# MBR2GPT tool test guidance


**MBR2GPT.EXE** converts a disk from Master Boot Record (MBR) to GUID Partition Table (GPT) partition style without modifying or deleting data on the disk. The tool is designed to be run from a Windows Preinstallation Environment (Windows PE) command prompt but can also be run from the full Windows 10 operating system (OS).

For detailed description about the tool, including usage information and troubleshooting guidance, please review the documentation in the Technet article for [MBR2GPT](https://docs.microsoft.com/windows/deployment/mbr-to-gpt).

## Sample checklist when verifying conversion from BIOS/MBR to UEFI/GPT

- Prior to running MBR2GPT
    - Run msinfo32 to verify the Machine is currently booted in BIOS mode
    - Run msinfo32 to verify the Windows 64-bit OS is installed
    - Make that the system disk has at most 3 primary partitions in MBR and at least one of the partitions is marked as Active.
    - Make sure that the device’s firmware supports UEFI boot by looking for the relevant setting(s) in the firmware menu, or by checking with the PC/firmware manufacturer
- After running MBR2GPT, but before booting into Windows 10 in UEFI mode
    - In the firmware menu, make sure that the boot mode setting is set to "UEFI Only" (or equivalent)
    - In the firmware menu, make sure that the Compatibility Support Module (CSM) is disabled and Secure Boot is enabled
- After booting into Windows 10 in UEFI mode
    - Run msinfo32 to verify the device is booted in UEFI mode and Secure Boot is enabled
    - Verify that your line of business (LOB) applications are still functioning correctly

**Note** System firmware can vary by manufacturer and by device. Contact the device manufacturer for assistance if you have questions or concerns.

## Test scenarios

### Conversion after an in-place upgrade

1.  Start with a device running Windows 7, 8, or 8.1 in BIOS mode.

2.  Upgrade the device to Windows 10, version 1507, version 1511, or version 1607 while in BIOS mode.

3.  Boot the device into Windows PE, version 1703, which can be obtained from the Windows Assessment and Deployment Kit for Windows 10, version 1703.

4.  Run MBR2GPT.EXE against the disk where Windows 10 is installed.

5.  Reconfigure the firmware to boot in UEFI mode, enable Secure Boot, and disable CSM by:

    - Changing the relevant settings in the firmware menu

    or

    - Running a tool provided by the PC or firmware manufacturer

6.  Boot to Windows 10 in UEFI mode

### Conversion as part of re-imaging

1.  Start with a device running Windows 7, 8, or 8.1 in BIOS mode.

2.  Capture data and settings using USMT Scan State.

3.  Boot the device into Windows PE, version 1703, which can be obtained from the Windows Assessment and Deployment Kit for Windows 10, version 1703.

4.  Deploy the Windows 10, version 1703 image.

5.  Run MBR2GPT.EXE against the disk where Windows 10 is installed.

6.  Reconfigure the firmware to boot in UEFI mode, enable Secure Boot, and disable CSM by:

    - Changing the relevant settings in the firmware menu

    or

    - Running a tool provided by the PC or firmware manufacturer

7.  Boot to Windows 10 in UEFI mode

Restore data and settings using USMT Load State.

### Conversion as part of Hyper-V generation 1 VM

1.  Start with a device running Windows 7, 8, or 8.1 in BIOS mode.

2.  Upgrade the VM to Windows 10 version 1507, version 1511, or version 1607 while in BIOS mode.

3.  Boot the VM into Windows PE, version 1703, which can be obtained from the Windows Assessment and Deployment Kit for Windows 10, version 1703.

4.  Run MBR2GPT.exe against the disk number that you wish to perform the conversion.

5.  Detach VHD

6.  Create a generation 2 VM with UEFI support and attach the above VHD created from Step 5 above.

7.  Boot to Windows 10, version 1703 in UEFI mode using a gen 2 VM.

**Note** For any of the scenarios above, you can convert an MBR disk with BitLocker-encrypted volumes as long as protection has been suspended. To resume BitLocker after conversion, you will need to delete the existing protectors and recreate them.

## Troubleshooting

Please refer to the MBR2GPT.EXE [Troubleshooting](https://docs.microsoft.com/windows/deployment/mbr-to-gpt#troubleshooting) documentation for information about log file locations and additional help. If you are automating the use of this tool via scripting or SCCM/MDT task sequences, you can script handlers for the returned codes that are discussed in the documentation.

## Related resources

[MBR2GPT.EXE](https://docs.microsoft.com/windows/deployment/mbr-to-gpt)



