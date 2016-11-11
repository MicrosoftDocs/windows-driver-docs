---
title: Selecting Packet Reporting Modes in Multi-touch Drivers (Windows 7)
description: Selecting Packet Reporting Modes in Multi-touch Drivers (Windows 7)
ms.assetid: 88277b23-aca2-4fba-9682-b9105608e169
keywords: ["Windows Touch WDK , multitouch digitizer drivers, selecting packet reporting modes", "packet reporting modes WDK Touch", "packet reporting modes WDK Touch , selecting in multitouch drivers", "multitouch digitizer drivers WDK , selecting packet reporting modes"]
---

# Selecting Packet Reporting Modes in Multi-touch Drivers (Windows 7)


Windows supports three ways of reporting multi-touch data to the system: serial mode, parallel mode, and hybrid mode. The vendor-supplied HID report descriptor differs, depending on the mode that was selected.

We recommend that vendors use hybrid or parallel mode, because these modes can improve the efficiency of data delivery from operating system component to applications.

### <span id="serial_mode"></span><span id="SERIAL_MODE"></span>Serial Mode

Each packet contains information that describes a single physical contact point. Multiple contacts are streamed serially.

In this mode, devices report all contact information in a series of packets. Each packet contains information that describes a single physical contact. The device sends a separate packet for each concurrent contact.

For example, if two fingers are down, a device that uses serial mode sends an update for the first contact, and then sends an update for the second contact. This process repeats as long as both fingers are in contact with the digitizer.

Serial mode might reduce the effective reporting speed for each physical contact on the device. For example, if a device can send an update one time every millisecond (ms) and two physical contacts are present, each contact point updates only every 2 ms.

For a sample serial mode report descriptor, see [Sample Report Descriptor (Serial Reporting Mode)](sample-report-descriptor--serial-reporting-mode-.md).

In comparison, hybrid and parallel reporting modes benefit from reduced data delivery overhead.

### <span id="parallel_mode"></span><span id="PARALLEL_MODE"></span>Parallel Mode

In parallel mode, devices report all contact information in a single packet. Each physical contact is represented by a logical collection that is embedded in the top-level collection. This logical collection contains all the usages that the device supports for each contact (for example, X, Y, and pressure). Because the device generally reports fewer contacts than the maximum, the number of contacts that are reported in a parallel packet should be communicated either in the contact count usage or by setting null values for all invalid contacts in a packet.

Consider a device that supports three contacts. If the user currently has only two fingers on the digitizer, the parallel packet has only two valid contact data in a packet that can carry data for three contacts. In this case, the contact count should be set to two so that the client application knows that any information about more than two contacts is not valid.

Alternatively, the device can set the values of the contact usages beyond the second entry to null values. The client application can detect the actual contacts either by examining the value of the contact count usage or by reading the data until it encounters a null value.

For a sample parallel mode report descriptor, see [Sample Report Descriptor (Parallel/Hybrid Mode)](sample-report-descriptor--parallel-hybrid-mode-.md).

A disadvantage of reporting multiple contacts in one packet is that space is wasted per packet every time that there are fewer contacts to report than the maximum number of contacts possible. Devices can use the hybrid reporting mode to reduce this inefficiency.

### <span id="hybrid_mode"></span><span id="HYBRID_MODE"></span>Hybrid Mode

In hybrid mode, the number of contacts that can be reported in one packet is less than the maximum number of contacts that the device supports. For example, a device that supports a maximum of 48 concurrent physical contacts can set up its top-level collection to report a maximum of 12 contacts in one packet. If 48 contact points are currently valid, the device can break these down into 4 serial packets that report 12 contacts each.

When a device reports data in this manner, the contact count usage value in the first packet should reflect the total number of contacts that are being reported in the hybrid packets. The other serial packets should have a contact count of 0. Using the previous example, the contact count usage in the first packet has a value of 48, whereas the latter three packets have a contact usage count of 0.

Hybrid and parallel reporting modes have the advantage of reducing the data delivery overhead.

For a sample hybrid mode report descriptor, see [Sample Report Descriptor (Parallel/Hybrid Mode)](sample-report-descriptor--parallel-hybrid-mode-.md).

### <span id="null_values"></span><span id="NULL_VALUES"></span>Null Values

Null values should be specified as outlined in the HID specification. The null bit must be set on all main items in the report descriptor. Be aware that a device can use either the contact count usage or null values to notify the host of the actual number of valid contacts in a packet.

 

 




