---
title: HKLM\\SYSTEM\\CurrentControlSet\\Services Registry Tree
description: HKLM\\SYSTEM\\CurrentControlSet\\Services Registry Tree
ms.assetid: c966b029-8171-4db7-9fbb-3a4222ff184b
---

# HKLM\\SYSTEM\\CurrentControlSet\\Services Registry Tree


## <a href="" id="ddk-the-hklm-system-currentcontrolset-services-tree-dg"></a>


The **HKLM\\SYSTEM\\CurrentControlSet\\Services** registry tree stores information about each service on the system. Each driver has a key of the form **HKLM\\SYSTEM\\CurrentControlSet\\Services\\***DriverName*. The PnP manager passes this path of a driver in the *RegistryPath* parameter when it calls the driver's [**DriverEntry**](https://msdn.microsoft.com/library/windows/hardware/ff544113) routine. A driver can store global driver-defined data under its key in the **Services** tree. Information that is stored under this key is available to the driver during its initialization.

The following keys and value entries are of particular interest:

<a href="" id="imagepath"></a>**ImagePath**  
A value entry that specifies the fully qualified path of the driver's image file. Windows creates this value by using the required **ServiceBinary** entry in the driver's INF file. This entry is in the *service-install-section* referenced by the driver's [**INF AddService directive**](inf-addservice-directive.md). A typical value for this path is *%SystemRoot%*\\*system32\\Drivers\\DriverName*.sys, where *DriverName* is the name of the driver's **Services** key.

<a href="" id="parameters"></a>**Parameters**  
A key that is used to store driver-specific data. For some types of drivers, the system expects to find specific value entries. You can add value entries to this subkey using **AddReg** entries in the driver's INF file.

<a href="" id="performance"></a>**Performance**  
A key that specifies information for optional performance monitoring. The values under this key specify the name of the driver's performance DLL and the names of certain exported functions in that DLL. You can add value entries to this subkey using **AddReg** entries in the driver's INF file.

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bdevinst\devinst%5D:%20HKLM\SYSTEM\CurrentControlSet\Services%20Registry%20Tree%20%20%20RELEASE:%20%287/22/2016%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")




