---
title: Implementing Custom WMI Blocks
description: Implementing Custom WMI Blocks
ms.assetid: c596924f-9f82-4ca7-b0f0-afc596d7bf99
keywords: ["WMI WDK kernel , event blocks", "event blocks WDK WMI", "data blocks WDK WMI", "WMI WDK kernel , data blocks", "blocks WDK WMI", "custom blocks WDK WMI"]
ms.date: 06/16/2017
ms.localizationpriority: medium
---

# Implementing Custom WMI Blocks





A driver can implement *custom blocks* that expose device-specific instrumentation. For example, a driver for a disk drive that can report temperature might implement a custom event block that notifies WMI clients when the drive's temperature increases beyond a safe threshold.

To implement a custom block, a driver:

-   Defines a class in its MOF file, compiles the MOF file into a resource, and includes the resource in the driver, as described in [Publishing a WMI Schema](publishing-a-wmi-schema.md).

-   Registers the block with WMI along with the other standard and custom blocks supported by the driver, as described in [Registering as a WMI Data Provider](registering-as-a-wmi-data-provider.md).

-   Handles all WMI requests that specify the driver's device object pointer at **Parameters.WMI.ProviderId** and the GUID of the standard block at **Parameters.WMI.DataPath**, as described in [Handling WMI Requests](handling-wmi-requests.md).

Drivers cannot control the order in which binary MOF files are loaded. The only guarantee is that wmicore.mof is loaded before any driver-specific MOF file. Therefore, custom WMI classes must only inherit from either classes in the same MOF file, or in wmicore.mof.

To improve performance and ease of use of custom WMI data blocks, consider the following guidelines:

-   Put data items that are operationally grouped together in the same data block.

    For example, an i8042 port controller might maintain state information about both the keyboard and mouse ports. Rather than a single large data block containing all mouse and keyboard information, a driver might define one data block for the mouse port and another data block for the keyboard port.

-   Put frequently used data items in separate data blocks, particularly if they would otherwise be grouped with items that are infrequently used.

    For example, a driver might expose CPU utilization in a data block with a single item, so a WMI client could track CPU utilization without incurring the overhead of retrieving additional data items in the block. A WMI client cannot query for a single data item, so to obtain one item it must query for an entire instance of a data block.

-   Use event blocks to notify WMI clients of exceptional events, not as an alternative to error logging.

    Only a limited number of events can be queued at one time, and if the queue is full events will be lost. Also, the timing of delivery of events to WMI clients cannot be guaranteed.

-   Limit event blocks to a maximum size of 1K bytes.

    Event items should be defined as small data types, because there is a registry-defined size limit (initially, 1K) for the entire [**WNODE\_EVENT\_ITEM**](https://msdn.microsoft.com/library/windows/hardware/ff566373) structure that contains the generated event. For large notifications, a driver can send a [**WNODE\_EVENT\_REFERENCE**](https://msdn.microsoft.com/library/windows/hardware/ff566374) structure that specifies a single instance of a data block, which WMI then queries to obtain the actual event. However, this increases the time lag between the occurrence of the event and the notification.

-   Place fixed-size data items at the beginning of a data block, followed by any variable-size data items.

    For example, a data block that has three DWORD data items and one variable-length string should put the three DWORDs first, followed by the string. Placing fixed-size data items at the beginning of a block permits WMI clients to extract them more easily.

-   Consider which types of system users you'd like to access your driver's data blocks. The system provides a default security descriptor for all WMI class GUIDs. If necessary, you can provide alternate security descriptors within the device's INF file. For more information, see [Creating Secure Device Installations](https://msdn.microsoft.com/library/windows/hardware/ff540212).

WMI does not support versioning, so a driver writer must define a new MOF class and generate a new GUID to revise an existing custom block.

 

 




