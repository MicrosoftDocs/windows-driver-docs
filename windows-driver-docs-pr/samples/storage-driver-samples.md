---
title: Storage driver samples
description: The storage driver samples in this directory provide a starting point for writing a custom driver for your device.
ms.date: 03/22/2023
---

# Storage driver samples

The driver samples in this directory provide a starting point for writing a custom driver for your device.

| Sample | Description |
| --- | --- |
| [CDROM Class Driver](/samples/microsoft/windows-driver-samples/cdrom-storage-class-driver) | The CD ROM class driver is used to provide access to CD, DVD and Blu-ray drives. It supports Plug and Play, Power Management, and AutoRun (media change notification). |
| [ClassPnP Class Driver Library](/samples/microsoft/windows-driver-samples/classpnp-storage-class-driver-library) | A library storage class drivers. It simplifies writing a storage class driver by most of the code needed to support Plug and Play (PnP), power management, and other features. This library is used by disk, CDROM, and the tape class drivers. |
| [Disk Class Driver](/samples/microsoft/windows-driver-samples/disk-class-driver) | A class driver for disk devices. |
| [AddFilter Storage Filter Tool](/samples/microsoft/windows-driver-samples/addfilter-storage-filter-tool) | A command-line application that adds and removes filter drivers for a given drive or volume. |
| [iSCSI WMI Client](/samples/microsoft/windows-driver-samples/iscsi-wmi-client) | A WMI implementation in an iSCSI miniport that can be tested using the iSCSICLI.exe tool, the iSCSI Initiator Properties page, the WBEMTEST.exe tool, and customized WMI scripts. |
| [LSI_U3 StorPort Miniport](/samples/microsoft/windows-driver-samples/lsi_u3-storport-miniport-driver) | An adapter driver for use with Parallel SCSI Host Bus Adapters or on-motherboard solutions that use the LSI 53C1010 SCSI ASIC. |
| [StorAHCI StorPort Miniport](/samples/microsoft/windows-driver-samples/storahci-storport-miniport-driver) | A sample Storport ACHI miniport driver. |
| [Multipath I/O (MPIO) DSM Sample](/samples/microsoft/windows-driver-samples/multipath-io-mpio-dsm-sample)     | An example to follow when building a vendor specific, device specific module (DSM). This sample DSM supports iSCSI and Fibre Channel devices. |
| [Super Floppy (sfloppy) Storage Class Driver](/samples/microsoft/windows-driver-samples/super-floppy-sfloppy-storage-class-driver) | A class driver for Super Floppy disk drives. |
| [SCSI Pass-Through Interface Tool](/samples/microsoft/windows-driver-samples/scsi-pass-through-interface-tool) | Demonstrates how to communicate with a SCSI device from using the pass through IOCTLs in an application using the DeviceIoControl API. |
