---
title: Implementing Dynamic MOF Data
description: Implementing Dynamic MOF Data
ms.assetid: 408c0f64-6257-4ece-bb4d-b1850f8ae3c6
keywords: ["WMI WDK kernel , publishing schema", "publishing WMI schema WDK", "schema publishing WDK WMI", "MOF files WDK WMI", "dyanmic MOF data WDK WMI"]
ms.date: 06/16/2017
ms.localizationpriority: medium
---

# Implementing Dynamic MOF Data





A driver's schema can be published dynamically by including binary MOF data in the driver's binary and returning selected schema information at runtime. To supply dynamic MOF data, a driver should follow these steps:

1.  Compile the MOF file as described in [Compiling a Driver's MOF File](compiling-a-driver-s-mof-file.md).

2.  Use wmimofck.exe to create a .x file which will contain a hexadecimal dump of the .bmf file created by the MOF compiler.

3.  Use **\#include** to include the hex data created in step 2 with the driver's source.

4.  Register as supporting MSWmi\_MofData\_GUID, which is a GUID defined in wmidata.h.

5.  Return selected binary data to WMI in response to both the [**IRP\_MN\_QUERY\_ALL\_DATA**](https://msdn.microsoft.com/library/windows/hardware/ff551650) or [**IRP\_MN\_QUERY\_SINGLE\_INSTANCE**](https://msdn.microsoft.com/library/windows/hardware/ff551718) requests for MSWmi\_MofData\_GUID.

For more information about the wmimofck utility see [Using wmimofck.exe](using-wmimofck-exe.md).

 

 




