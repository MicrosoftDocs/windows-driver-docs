---
title: HKLM\SYSTEM\CurrentControlSet\Services Registry Tree
description: HKLM\SYSTEM\CurrentControlSet\Services registry tree stores information about each service on the system.
ms.date: 09/18/2024
ai-usage: ai-assisted
---

# HKLM\\SYSTEM\\CurrentControlSet\\Services Registry Tree

The **HKLM\\SYSTEM\\CurrentControlSet\\Services** registry tree stores information about each service on the system. Each driver has a key of the form **HKLM\\SYSTEM\\CurrentControlSet\\Services\\**<em>DriverName</em>.

The PnP manager passes this path of a driver in the *RegistryPath* parameter when it calls the driver's [**DriverEntry**](/windows-hardware/drivers/ddi/wdm/nc-wdm-driver_initialize) routine. A driver can store global driver-defined data under the **Parameters** subkey of its key in the **Services** tree using an [**AddReg**](./inf-addreg-directive.md) directive in the driver's INF file. To access that key at runtime, a WDM driver should use [IoOpenDriverRegistryKey](/windows-hardware/drivers/ddi/wdm/nf-wdm-ioopendriverregistrykey) with a DRIVER_REGKEY_TYPE of **DriverRegKeyParameters** and a WDF driver should use [**WdfDriverOpenParametersRegistryKey**](/windows-hardware/drivers/ddi/wdfdriver/nf-wdfdriver-wdfdriveropenparametersregistrykey). Information that is stored under this key is available to the driver during its initialization.

For more info about registry keys that drivers typically use, see [Introduction to Registry Keys for Drivers](../wdf/introduction-to-registry-keys-for-drivers.md).

## Additional Keys in HKLM\SYSTEM\CurrentControlSet\Services

<a href="" id="parameters"></a>**Parameters**  
A key that is used to store driver-specific data. For some types of drivers, the system expects to find specific value entries. You can add value entries to this subkey using [**AddReg**](./inf-addreg-directive.md) directives in the driver's INF file.

<a href="" id="performance"></a>**Performance**  
A key that specifies information for optional performance monitoring. The values under this key specify the name of the driver's performance DLL and the names of certain exported functions in that DLL. You can add value entries to this subkey using [**AddReg**](./inf-addreg-directive.md) directives in the driver's INF file.

### Common Registry Keys and Values in HKLM\SYSTEM\CurrentControlSet\Services\<DriverName>

#### Start
The `Start` value specifies when the service should be started. It can have one of the following values:
- `0x0` (Boot): Loaded by the boot loader.
- `0x1` (System): Loaded by the I/O subsystem.
- `0x2` (Automatic): Loaded automatically by the Service Control Manager during system startup.
- `0x3` (Demand): Loaded automatically by PnP if it is needed for a device.
- `0x4` (Disabled): The service is disabled and will not be loaded.

#### Type
The `Type` value specifies the type of service. It can be a combination of the following values:
- `0x1` (Kernel driver): A device driver.
- `0x2` (File system driver): A file system driver.
- `0x10` (Win32 own process): A Win32 program that runs in its own process.
- `0x20` (Win32 share process): A Win32 program that shares a process with other services.

#### ErrorControl
The `ErrorControl` value specifies the severity of the error if the service fails to start. It can have one of the following values:
- `0x0` (Ignore): The error is ignored, and the startup continues.
- `0x1` (Normal): The error is logged, a message box may be displayed, but startup continues.
- `0x2` (Severe): The error is logged, and the system is restarted with the last-known-good configuration.
- `0x3` (Critical): The error is logged, and the system attempts to restart with the last-known-good configuration. If this fails, startup fails, and the system halts.

#### Additional Common Values
- `ImagePath`: Specifies the path to the service binary. Windows creates this value by using the required **ServiceBinary** entry in the driver's INF file. This entry is in the *service-install-section* referenced by the driver's [**INF AddService directive**](inf-addservice-directive.md).
- `DisplayName`: The friendly name of the service.
- `Description`: A description of the service.

### Example
Here is an example of a registry entry for a service:
```plaintext
[HKEY_LOCAL_MACHINE\SYSTEM\CurrentControlSet\Services\ExampleService]
"Start"=dword:00000002
"Type"=dword:00000010
"ErrorControl"=dword:00000001
"ImagePath"="C:\\Program Files\\ExampleService\\example.exe"
"DisplayName"="Example Service"
"Description"="This is an example service."
```

