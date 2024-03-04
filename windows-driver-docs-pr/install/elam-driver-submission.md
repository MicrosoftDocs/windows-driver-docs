---
title: ELAM Driver Submission Process
description: Early Launch Antimalware (ELAM) drivers can be submitted using the listed steps to ensure validation and adherence to documented requirements
ms.date: 04/27/2017
---
# ELAM driver submission Process

The following steps can be used to submit an Early Launch Antimalware (ELAM) driver:

1. Ensure your driver adheres to the documented requirements for ELAM drivers.  See [ELAM driver requirements](elam-driver-requirements.md) and [INF SignatureAttributes Section](inf-signatureattributes-section.md) for more information.

2. Validate your driver using the Hardware Logo Kit (HLK) and Hardware Certification Kit (HCK). If your driver will be used in Windows 8 as well as Windows 10, you need to run both versions of the kit. Include the results with your submission. See [HLK tools technical reference](/windows-hardware/test/hlk/user/hlk-tools-technical-reference) for more information. For information about required HCK tests, see below.

3. Follow the kernel mode driver signing policy as stated in the [Driver signing policy](./kernel-mode-code-signing-policy--windows-vista-and-later-.md) topic.

4. Submit the driver package for evaluation at the [Windows Hardware Dev Center](https://developer.microsoft.com/windows)

Each driver .sys file must be code signed by Microsoft, using a special certificate indicating that it is an Early Launch AM Driver.

The AM driver must be a single binary (not import any other DLLs).

## Hardware Certification Kit Tests


Each driver targeting a pre-Windows 10 operating system must pass the following HCK tests, which are administered by the ISV:

PERFORMANCE TEST
-   CALLBACK LATENCY - Each early launch AM driver is required to return the driver verification callbacks from the kernel within .5ms. This time is measured from when the kernel issues the callback to the driver to the time the driver returns the callback.
-   MEMORY ALLOCATION - Each early launch AM driver is required to limit its footprint in memory to 128 KB, for both the driver image as well as its configuration (signature) data.
-   UNLOAD BLOCKING - Each early launch AM driver receives a synchronous callback after the last boot driver has been initialized, which indicates that the AM driver will be unloaded. The AM driver can use this as an indication that it needs to do “cleanup” and save any status information that can be used by the runtime AM driver. However, the early launch AM driver must return the callback for the driver to be unloaded and for boot to continue.
-   SIGNATURE DATA TEST - Each early launch AM driver must get its malware signature data from a single, well-known location and no other. This allows measurement and protection of that data by Windows. This test ensures that each AM driver only reads its configuration data from the registry hive that is created for that driver.
-   BACKUP DRIVER TEST - The early launch AM driver, upon installation, must also install a backup copy of the driver to the backup driver store. This requirement is to help with remediation in the case that the primary driver gets corrupted. This test ensures that for an installed early launch AM driver, there is a corresponding driver in the backup store.
