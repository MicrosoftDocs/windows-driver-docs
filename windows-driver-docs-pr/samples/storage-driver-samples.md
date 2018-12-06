---
title: Storage driver samples
description: The storage driver samples in this directory provide a starting point for writing a custom driver for your device.
ms.assetid: 4FEB911D-78D5-403E-91AB-8A064E31F4FA
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# Storage driver samples


The driver samples in this directory provide a starting point for writing a custom driver for your device.

## Storage


| Sample Name                                 | Solution                                                     | Description                                                                                                                                                                                                                                     |
|---------------------------------------------|--------------------------------------------------------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| CDROM Class Driver                          | [cdrom](http://go.microsoft.com/fwlink/p/?LinkId=617971)     | The CD ROM class driver is used to provide access to CD, DVD and Blu-ray drives. It supports Plug and Play, Power Management, and AutoRun (media change notification).                                                                          |
| ClassPnP Class Driver Library               | [classpnp](http://go.microsoft.com/fwlink/p/?LinkId=617978)  | A library storage class drivers. It simplifies writing a storage class driver by most of the code needed to support Plug and Play (PnP), power management, and other features. This library is used by disk, CDROM, and the tape class drivers. |
| Disk Class Driver                           | [disk](http://go.microsoft.com/fwlink/p/?LinkId=617979)      | A class driver for disk devices.                                                                                                                                                                                                                |
| AddFilter Storage Filter Tool               | [addfilter](http://go.microsoft.com/fwlink/p/?LinkId=617980) | A command-line application that adds and removes filter drivers for a given drive or volume.                                                                                                                                                    |
| iSCSI WMI Client                            | [iscsi](http://go.microsoft.com/fwlink/p/?LinkId=617981)     | A WMI implementation in an iSCSI miniport that can be tested using the iSCSICLI.exe tool, the iSCSI Initiator Properties page, the WBEMTEST.exe tool, and customized WMI scripts.                                                               |
| LSI\_U3 StorPort Miniport                   | [lsi\_u3](http://go.microsoft.com/fwlink/p/?LinkId=617982)   | An adapter driver for use with Parallel SCSI Host Bus Adapters or on-motherboard solutions that use the LSI 53C1010 SCSI ASIC.                                                                                                                  |
| StorAHCI StorPort Miniport                  | [storahci](http://go.microsoft.com/fwlink/p/?LinkId=617983)  | A sample Storport ACHI miniport driver.                                                                                                                                                                                                         |
| Multipath I/O (MPIO) DSM Sample             | [msdsm](http://go.microsoft.com/fwlink/p/?LinkId=620203)     | An example to follow when building a vendor specific, device specific module (DSM). This sample DSM supports iSCSI and Fibre Channel devices.                                                                                                   |
| Super Floppy (sfloppy) Storage Class Driver | [sfloppy](http://go.microsoft.com/fwlink/p/?LinkId=617989)   | A class driver for Super Floppy disk drives.                                                                                                                                                                                                    |
| SCSI Pass-Through Interface Tool            | [spti](http://go.microsoft.com/fwlink/p/?LinkId=617990)      | Demonstrates how to communicate with a SCSI device from using the pass through IOCTLs in an application using the DeviceIoControl API.                                                                                                          |

 

 

 




