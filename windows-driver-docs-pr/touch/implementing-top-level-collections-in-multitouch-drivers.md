---
title: Implementing Top-Level Collections in Multi-touch Drivers (Windows 7)
description: Implementing Top-Level Collections in Multi-touch Drivers (Windows 7)
ms.assetid: 7af88121-fed4-42ff-8bac-f42c213da77e
keywords: ["Windows Touch WDK , multitouch digitizer drivers, implementing top-level collections", "multitouch digitizer drivers WDK , implementing top-level collections", "top-level collections WDK Touch", "top-level collections WDK Touch , multitouch digitizer drivers"]
---

# Implementing Top-Level Collections in Multi-touch Drivers (Windows 7)


The report descriptor for a multiple input device must include at least one top-level collection for the primary device and a separate top-level collection for the mouse.

If your device supports versions of Windows earlier than Windows 7, the report descriptor must also include a top-level collection that contains a feature report that can be used to configure the device as a multiple input device, single-input device, or mouse device. For more information, see [Using Report Descriptors to Support Capability Discovery](using-report-descriptors-to-support-capability-discovery.md).

For example, in the EloMT sample, the EloMT.c file includes a report descriptor that contains three top-level collections: the first contains two logical collections (one for each of the two supported physical contacts), the second is the feature report (also known as a configuration collection), and the third specifies usages for mouse support. Be aware that this driver can still support more than two concurrent contacts by using Hybrid mode. For information about how to select modes, see [Selecting Packet Reporting Modes in Multi-touch Drivers](selecting-packet-reporting-modes-in-multitouch-drivers.md).

On Windows 7, HID reports that supply information from multiple inputs must specify Collection Application (CA) 0x4 (Touch Screen) on the digitizer usage page.

Devices can send multi-touch data by using one report for each contact, or they can use the reporting modes that were outlined in [Selecting Packet Reporting Modes in Multi-touch Drivers](selecting-packet-reporting-modes-in-multitouch-drivers.md) for a more efficient way to report data. Report descriptors for touch devices should use Finger (0x22) CL (Collection Logical) to group the data and control usages in the top-level collections, whereas the Stylus (0x20) CL should be used to group pen-related control and data usages.

Configuration collection enables you to configure devices to work with earlier versions of Windows. You can also use configuration collections to operate your touch device in different modes. For example, on Windows Vista, your device can default to single touch. On Windows XP, your device can assume mouse functionality. For information about how to access the configuration collection, see the subtopic "Feature Report Exclusivity" in [Using Report Descriptors to Support Capability Discovery](using-report-descriptors-to-support-capability-discovery.md).

 

 




