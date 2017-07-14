---
title: Implementing Dynamic MOF Data
author: windows-driver-content
description: Implementing Dynamic MOF Data
ms.assetid: 408c0f64-6257-4ece-bb4d-b1850f8ae3c6
keywords: ["WMI WDK kernel , publishing schema", "publishing WMI schema WDK", "schema publishing WDK WMI", "MOF files WDK WMI", "dyanmic MOF data WDK WMI"]
ms.author: windowsdriverdev
ms.date: 06/16/2017
ms.topic: article
ms.prod: windows-hardware
ms.technology: windows-devices
---

# Implementing Dynamic MOF Data


## <a href="" id="ddk-implementing-dynamic-mof-data-kg"></a>


A driver's schema can be published dynamically by including binary MOF data in the driver's binary and returning selected schema information at runtime. To supply dynamic MOF data, a driver should follow these steps:

1.  Compile the MOF file as described in [Compiling a Driver's MOF File](compiling-a-driver-s-mof-file.md).

2.  Use wmimofck.exe to create a .x file which will contain a hexadecimal dump of the .bmf file created by the MOF compiler.

3.  Use **\#include** to include the hex data created in step 2 with the driver's source.

4.  Register as supporting MSWmi\_MofData\_GUID, which is a GUID defined in wmidata.h.

5.  Return selected binary data to WMI in response to both the [**IRP\_MN\_QUERY\_ALL\_DATA**](https://msdn.microsoft.com/library/windows/hardware/ff551650) or [**IRP\_MN\_QUERY\_SINGLE\_INSTANCE**](https://msdn.microsoft.com/library/windows/hardware/ff551718) requests for MSWmi\_MofData\_GUID.

For more information about the wmimofck utility see [Using wmimofck.exe](using-wmimofck-exe.md).

 

 


--------------------
[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bkernel\kernel%5D:%20Implementing%20Dynamic%20MOF%20Data%20%20RELEASE:%20%286/14/2017%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")


