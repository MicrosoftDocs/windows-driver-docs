---
title: Load order groups and altitudes for minifilter drivers
description: Describes load order groups and altitudes for minifilter drivers
keywords:
- altitudes WDK file system minifilter
- altitudes WDK file system filter driver
- load order groups WDK file system
- start types WDK file system
- driver start types WDK file system
- create a filter altitude
- update filter altitude information
ms.date: 05/27/2021
ms.localizationpriority: medium
---

# Load order groups and altitudes for minifilter drivers

## About load order groups

Windows uses a dedicated set of *load order groups* for file system minifilters and legacy filter drivers that are loaded at system startup. A filter's load order group assignment depends on the filter's type (for example: AV, encryption, etc).

## About altitudes

Each load order group has a defined range of *altitudes*. Every filter driver must have a unique altitude identifier. The filter's altitude defines its position relative to other filter drivers in the I/O stack when it is loaded.

The altitude is an infinite-precision string interpreted as a decimal number. A filter driver that has a low numerical altitude is loaded into the I/O stack below a filter driver that has a higher numerical value.

Microsoft allocates "integer" altitude values based on filter requirements and load order group. Companies with a Microsoft-assigned integer altitude can [create their own altitudes](#create-an-altitude) within the same load order group.

Altitude values for a filter driver are specified in the **Instance** definitions of the [**Strings** Section in the filter driver's INF file](creating-an-inf-file-for-a-minifilter-driver.md). Instance definitions can also be specified in calls to the [**InstanceSetupCallback**](/windows-hardware/drivers/ddi/fltkernel/nc-fltkernel-pflt_instance_setup_callback) routine in the [**FLT_REGISTRATION**](/windows-hardware/drivers/ddi/fltkernel/ns-fltkernel-_flt_registration) structure. Multiple instances and altitudes can be defined for a filter driver. These instance definitions apply across all volumes.

## Types of load order groups and their altitude ranges

The following table lists the system-defined load order groups and altitude ranges. Each entry in the table's "Load order group" column uses the value that should be specified for a group in the **LoadOrderGroup** entry in the [**ServiceInstall** Section of a filter's INF file](creating-an-inf-file-for-a-minifilter-driver.md). The Altitude range column contains the range of altitudes for a particular load order group.

The load order groups and altitude ranges are listed as they appear on the stack, which is the reverse of the order in which they are loaded.

Load order group | Altitude range | Group description |
| -------------- | -------------- | ----------------- |
| Filter | 420000-429999 | Same as the Filter load order group that was available on Windows 2000 and earlier. This group loads last and thus attaches furthest from the file system. |
| FSFilter Top | 400000-409999 | For filter drivers that must attach above all other FSFilter types. |
| FSFilter Activity Monitor | 360000-389999 | Includes filter drivers that observe and report on file I/O. |
| FSFilter Undelete | 340000-349999 | Includes filters that recover deleted files. |
| FSFilter Anti-Virus | 320000-329999 | Includes filter drivers that detect and disinfect viruses during file I/O. |
| FSFilter Replication | 300000-309999 | Includes filter drivers that replicate file data to remote servers. |
| FSFilter Continuous Backup | 280000-289999 | Includes filter drivers that replicate file data to backup media. |
| FSFilter Content Screener | 260000-269999 | Includes filter drivers that prevent the creation of specific files or file content. |
| FSFilter Quota Management | 240000-249999 | Includes filter drivers that provide enhanced file system quotas. |
| FSFilter System Recovery | 220000-229999 | Includes filter drivers that perform operations to maintain operating system integrity, such as the System Restore (SR) filter. |
| FSFilter Cluster File System | 200000-209999 | Includes filter drivers that are used in products that provide file server metadata across a network. |
| FSFilter HSM | 180000-189999 | Includes filter drivers that perform hierarchical storage management. |
| FSFilter Imaging | 170000-175000 | Includes ZIP-like filter drivers that provide a virtual namespace. |
| FSFilter Compression | 160000-169999 | Includes filter drivers that perform file data compression. |
| FSFilter Encryption | 140000-149999 | Includes filter drivers that encrypt and decrypt data during file I/O. |
| FSFilter Virtualization | 130000- 139999 | Includes filter drivers that virtualize the file path, such as the Least Authorized User (LUA) filter driver added in Windows Vista. |
| FSFilter Physical Quota Management | 120000-129999 | Includes filter drivers that manage quotas by using physical block counts. |
| FSFilter Open File | 100000-109999 | Includes filter drivers that provide snapshots of already open files. |
| FSFilter Security Enhancer | 80000-89999 | Includes filter drivers that apply lockdown and enhanced access control lists (ACLs). |
| FSFilter Copy Protection | 60000-69999 | Includes filter drivers that check for out-of-band data on media. |
| FSFilter Bottom | 40000-49999 | Provided for filter drivers that must attach below all other FSFilter types. |
| FSFilter System | 20000-29999 | Reserved for internal use. |
| FSFilter Infrastructure  | <20000 | Reserved for internal use. This group loads first and thus attaches closest to the file system. |

## Create an altitude

If you don't already have a Microsoft-assigned integer altitude in the same load order group, you need to [request a filter altitude](minifilter-altitude-request.md).

If you already have a Microsoft-assigned altitude, you can create your own altitude to place a new filter in the same load order group. To do so, simply append a fractional value to your existing altitude. For example:

* Let's say that you were previously assigned altitude 325000 in the FSFilter Anti-Virus group.
* If you have two new filters, you could choose to load them at altitudes such as 325000.3 and 325000.7 without making an altitude request.

If you create your own fractional value altitude for a new filter, please email [fsfcomm@microsoft.com](mailto:fsfcomm@microsoft.com?subject=Filter%20altitude%20request) with the following information so that we can keep the [filter community list](allocated-altitudes.md) up to date:

* Your company name
* Contact e-mail (long-term company e-mail alias; not an individual email)
* Product name
* Product URL
* Product/filter description to help Microsoft determine that the filter is in the appropriate load order group
* Filter filename
* Filter start-type
* The altitude number you assigned to your new filter

## Update information associated with existing altitudes

To update information associated with existing altitudes (for example, changes to your company name, contact e-mail, product URL, filter description, etc), send email to [fsfcomm@microsoft.com](mailto:fsfcomm@microsoft.com?subject=Filter%20altitude%20request) and include the information to be updated.
