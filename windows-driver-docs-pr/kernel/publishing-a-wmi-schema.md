---
title: Publishing a WMI Schema
description: Publishing a WMI Schema
ms.assetid: db2b8086-71e4-4532-a0ae-75983691a5a6
keywords: ["WMI WDK kernel , publishing schema", "publishing WMI schema WDK", "schema publishing WDK WMI", "MOF files WDK WMI", "binary MOF WDK WMI"]
ms.date: 06/16/2017
ms.localizationpriority: medium
---

# Publishing a WMI Schema





To publish a WMI schema, a driver writer first creates a text file in Managed Object Format (MOF) language that contains a class definition for each data block and event block in the schema, as described in [MOF Syntax for WMI Data and Event Blocks](mof-syntax-for-wmi-data-and-event-blocks.md).

A driver writer can then publish a driver's WMI schema in one of the following ways:

-   Compile the MOF file and include it as a resource in the driver's binary image. For more information, see [Compiling a Driver's MOF File](compiling-a-driver-s-mof-file.md).

-   Include the compiled MOF file as a resource in a different file, such as a DLL, and add the registry value **MofImagePath** with a path to the file that contains the MOF under the driver's Service key. A schema published in this way can be updated without recompiling the driver. For more information, see [Setting the MofImagePath Registry Value](setting-the-mofimagepath-registry-value.md).

-   Include binary data within the driver and return it when WMI requests it. A schema published in this way can be changed dynamically at runtime. For more information, see [Implementing Dynamic MOF Data](implementing-dynamic-mof-data.md).

 

 




