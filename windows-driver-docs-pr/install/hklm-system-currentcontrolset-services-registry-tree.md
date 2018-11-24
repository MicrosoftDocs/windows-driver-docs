---
title: HKLM\SYSTEM\CurrentControlSet\Services Registry Tree
description: HKLM\SYSTEM\CurrentControlSet\Services registry tree stores information about each service on the system.
ms.assetid: c966b029-8171-4db7-9fbb-3a4222ff184b
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# HKLM\\SYSTEM\\CurrentControlSet\\Services Registry Tree





The **HKLM\\SYSTEM\\CurrentControlSet\\Services** registry tree stores information about each service on the system. Each driver has a key of the form **HKLM\\SYSTEM\\CurrentControlSet\\Services\\**<em>DriverName</em>. The PnP manager passes this path of a driver in the *RegistryPath* parameter when it calls the driver's [**DriverEntry**](https://msdn.microsoft.com/library/windows/hardware/ff544113) routine. A driver can store global driver-defined data under its key in the **Services** tree. Information that is stored under this key is available to the driver during its initialization.

The following keys and value entries are of particular interest:

<a href="" id="imagepath"></a>**ImagePath**  
A value entry that specifies the fully qualified path of the driver's image file. Windows creates this value by using the required **ServiceBinary** entry in the driver's INF file. This entry is in the *service-install-section* referenced by the driver's [**INF AddService directive**](inf-addservice-directive.md). A typical value for this path is *%SystemRoot%*\\*system32\\Drivers\\DriverName*.sys, where *DriverName* is the name of the driver's **Services** key.

<a href="" id="parameters"></a>**Parameters**  
A key that is used to store driver-specific data. For some types of drivers, the system expects to find specific value entries. You can add value entries to this subkey using **AddReg** entries in the driver's INF file.

<a href="" id="performance"></a>**Performance**  
A key that specifies information for optional performance monitoring. The values under this key specify the name of the driver's performance DLL and the names of certain exported functions in that DLL. You can add value entries to this subkey using **AddReg** entries in the driver's INF file.

 

 





