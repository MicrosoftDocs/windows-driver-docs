---
title: Driver package isolation
description: This page describes driver isolation, a requirement for a Windows Driver.
ms.date: 07/14/2023
---

# Driver package isolation

Driver package isolation is a requirement for [Windows Drivers](./getting-started-with-windows-drivers.md) that makes driver packages more resilient to external changes, easier to update, and more straightforward to install.

> [!NOTE]
> While driver package isolation is required for Windows Drivers, Windows Desktop Drivers still benefit from it through improved resiliency and serviceability.

The following table shows some example legacy driver package practices that are no longer allowed for Windows Drivers in the left column along with the required behavior for Windows Drivers in the right column.

| Non-isolated driver | Isolated driver |
|--|--|
| INF copies files to %windir%\System32 or %windir%\System32\drivers | Driver files are [run from the driver store](./run-from-driver-store.md) |
| Interacts with device stacks/drivers using hardcoded paths | Interacts with device stacks/drivers using system-supplied functions or device interfaces |
| Hardcodes path to global registry locations | Uses HKR and system-supplied functions for relative location of registry and file state |
| Runtime file writes to any location | Files are written relative to locations supplied by the operating system |

For help in determining if your driver package meets driver package isolation requirements, see [Validating Windows Drivers](./validating-windows-drivers.md). For examples of how to update an INF to meet driver package isolation requirements, see [Porting an INF to follow driver package isolation](porting-inf-to-windows-driver.md).

## Run from driver store

All isolated driver packages leave their driver package files in the driver store. This means that they specify [**DIRID 13**](../install/using-dirids.md) in their INF to specify the location for driver package files on install.  For more information on how to use this in a driver package, see [**Run from driver store**](./run-from-driver-store.md).

## Reading and writing state

> [!NOTE]
> If your component is using device or device interface *properties* to store state, continue to use that method and the appropriate OS API's to store and access state. The following guidance for registry and file state is for *other* state that needs to be stored by a component.

Access to various registry and file state should be done by calling functions that provide a caller with the location of the state and then the state is read/written relative to that location. Do not use hardcoded absolute registry paths and file paths.

This section contains the following subsections:

- [Registry state](#registry-state)

- [File state](#file-state)

- [Property state](#property-state)

### Registry state

This section contains the following subsections:

- [PnP device registry state](#pnp-device-registry-state)

- [Device interface registry state](#device-interface-registry-state)

- [Service registry state](#service-registry-state)

#### PnP device registry state

Isolated driver packages and user-mode components typically use one of two locations to store device state in the registry. These are the *hardware key* (device key) for the device and the *software key* (driver key) for the device. The *hardware key* is typically for settings related to how an individual device instance interacts with the hardware. For example, to enable a hardware feature or put the hardware into a specific mode. The *software key* is typically for settings related to how an individual device instance interacts with the system and other software. For example, to configure the location of a data file, to inter operate with a framework, or to access app settings for a device. To retrieve a handle to these registry locations, use one of the following options:

- [**IoOpenDeviceRegistryKey**](/windows-hardware/drivers/ddi/wdm/nf-wdm-ioopendeviceregistrykey) (WDM)

- [**WdfDeviceOpenRegistryKey**](/windows-hardware/drivers/ddi/wdfdevice/nf-wdfdevice-wdfdeviceopenregistrykey), [**WdfFdoInitOpenRegistryKey**](/windows-hardware/drivers/ddi/wdffdo/nf-wdffdo-wdffdoinitopenregistrykey) (WDF)

- [**CM_Open_DevNode_Key**](/windows/win32/api/cfgmgr32/nf-cfgmgr32-cm_open_devnode_key) (user-mode code)

- [**INF AddReg**](../install/inf-addreg-directive.md) directive using HKR *reg-root* entries in an *add-registry-section* referenced from an [INF DDInstall](../install/inf-ddinstall-section.md) section or [DDInstall.HW](../install/inf-ddinstall-hw-section.md) section, as shown below:

```inf
[ExampleDDInstall.HW]
AddReg = Example_DDInstall.AddReg

[Example_DDInstall.AddReg] 
HKR,,ExampleValue,,%13%\ExampleFile.dll
```

#### Device interface registry state

To read and write device interface registry state, use one of the following options:

- [**IoOpenDeviceInterfaceRegistryKey**](/windows-hardware/drivers/ddi/wdm/nf-wdm-ioopendeviceinterfaceregistrykey) (WDM)

- [**CM_Open_Device_Interface_Key**](/windows/win32/api/cfgmgr32/nf-cfgmgr32-cm_open_device_interface_keyw) (user-mode code)

- [INF AddReg](../install/inf-addreg-directive.md) directive using HKR *reg-root* entries in an *add-registry-section* referenced from an [add-interface-section](../install/inf-addinterface-directive.md) section

#### Service registry state

Service state should be classified into one of 3 categories

- [Immutable service registry state](#immutable-service-registry-state)

- [Internal service registry state](#internal-service-registry-state)

- [Shared service registry state](#shared-service-registry-state)

##### Immutable service registry state

Immutable service state is state that is provided by the driver package that installs the service.  These registry values that are set by the INF for driver and Win32 services must be stored under the "Parameters" subkey of the service by providing an HKR line in an [AddReg](../install/inf-addreg-directive.md) section, and then referencing that section in the service install section in the INF.  For example:

```inf
[ExampleDDInstall.Services]
Addservice = ExampleService, 0x2, Example_Service_Inst

[Example_Service_Inst]
DisplayName    = %ExampleService.SvcDesc%
ServiceType    = 1
StartType      = 3
ErrorControl   = 1
ServiceBinary  = %13%\ExampleService.sys
AddReg=Example_Service_Inst.AddReg

[Example_Service_Inst.AddReg]
HKR, Parameters, ExampleValue, 0x00010001, 1
```

To access the location of this state from the service at runtime, use one of these functions:

- [**IoOpenDriverRegistryKey**](/windows-hardware/drivers/ddi/wdm/nf-wdm-ioopendriverregistrykey) (WDM) with a DRIVER_REGKEY_TYPE of **DriverRegKeyParameters**

- [**WdfDriverOpenParametersRegistryKey**](/windows-hardware/drivers/ddi/wdfdriver/nf-wdfdriver-wdfdriveropenparametersregistrykey) (WDF)

- [**GetServiceRegistryStateKey**](/windows/win32/api/winsvc/nf-winsvc-getserviceregistrystatekey) (Win32 Services) with a SERVICE_REGISTRY_STATE_TYPE of **ServiceRegistryStateParameters**

These registry values supplied by the INF in the "Parameters" subkey for the service should only be read at runtime and not modified. They should be treated as read only.

If the registry values supplied by the INF are default settings that can be overwritten at runtime, the override values should be written into the [Internal service registry state](#internal-service-registry-state) or [Shared service registry state](#shared-service-registry-state) for the service.  When retrieving the settings, the setting can be looked for first in the mutable state. If it does not exist there, then the setting can be looked for in the immutable state.  [**RtlQueryRegistryValueWithFallback**](/windows-hardware/drivers/ddi/ntddk/nf-ntddk-rtlqueryregistryvaluewithfallback) can be used to help query settings such as these that have an override and a default value.

##### Internal service registry state

Internal service state is state that is written at runtime and owned and managed by only the service itself and is only accessible to that service. To access the location for internal service state, use one of these functions from the service:

- [**IoOpenDriverRegistryKey**](/windows-hardware/drivers/ddi/wdm/nf-wdm-ioopendriverregistrykey) (WDM) with a DRIVER_REGKEY_TYPE of **DriverRegKeyPersistentState**

- [**WdfDriverOpenPersistentStateRegistryKey**](/windows-hardware/drivers/ddi/wdfdriver/nf-wdfdriver-wdfdriveropenpersistentstateregistrykey) (WDF)

- [**GetServiceRegistryStateKey**](/windows/win32/api/winsvc/nf-winsvc-getserviceregistrystatekey) (Win32 Services) with a SERVICE_REGISTRY_STATE_TYPE of **ServiceRegistryStatePersistent**

If the service wants to allow other components to modify these settings, the service must expose an interface that another component can call into that tells the service how to alter these settings.  For example, a Win32 service could expose a COM or RPC interface and a driver service could expose an IOCTL interface via a device interface.

##### Shared service registry state

Shared service state is state that is written at runtime and can be shared with other user mode components if they are sufficiently privileged. To access the location for this shared service state, use one of these functions:

- [**IoOpenDriverRegistryKey**](/windows-hardware/drivers/ddi/wdm/nf-wdm-ioopendriverregistrykey) (WDM) with a DRIVER_REGKEY_TYPE of **DriverRegKeySharedPersistentState**

- [**GetSharedServiceRegistryStateKey**](/windows/win32/api/winsvc/nf-winsvc-getsharedserviceregistrystatekey) (Win32 Services) with a SERVICE_SHARED_REGISTRY_STATE_TYPE of **ServiceSharedRegistryPersistentState**

### File state

This section contains the following subsections:

- [Device file state](#device-file-state)

- [Service file state](#service-file-state)

- [DriverData and ProgramData](#driverdata-and-programdata)

- [Temporary files](#temporary-files)

#### Device file state

If files related to a device need to be written at runtime, those files should be stored relative to a handle or file path provided via OS API's. Configuration files specific to that device is one example of what types of files to be stored here. To access the location of this state, use one of these functions from the service:

- [**IoGetDeviceDirectory**](/windows-hardware/drivers/ddi/wdm/nf-wdm-iogetdevicedirectory) (WDM) with the **DirectoryType** parameter set to **DeviceDirectoryData**

- [**WdfDeviceRetrieveDeviceDirectoryString**](/windows-hardware/drivers/ddi/wdfdevice/nf-wdfdevice-wdfdeviceretrievedevicedirectorystring) (WDF)

#### Service file state

Service file state can be classified into one of 3 categories

- [Immutable service file state](#immutable-service-file-state)

- [Internal service file state](#internal-service-file-state)

- [Shared service file state](#shared-service-file-state)

##### Immutable service file state

Immutable service file state are files that are part of the driver package. For more information on accessing those files, see [**Run from Driver Store**](./run-from-driver-store.md).

##### Internal service file state

Internal service file state is state that is written at runtime and owned and managed by only the service itself and is only accessible to that service. To access the location for internal service state, use one of these functions from the service:

- [**IoGetDriverDirectory**](/windows-hardware/drivers/ddi/content/wdm/nf-wdm-iogetdriverdirectory) (WDM, KMDF) with the **DirectoryType** parameter set to **DriverDirectoryData**

- [**WdfDriverRetrieveDriverDataDirectoryString**](/windows-hardware/drivers/ddi/content/wdfdriver/nf-wdfdriver-wdfdriverretrievedriverdatadirectorystring) (UMDF)

- [**GetServiceDirectory**](/windows/win32/api/winsvc/nf-winsvc-getservicedirectory) (Win32 Services) with the **eDirectoryType** parameter set to **ServiceDirectoryPersistentState**

If the service wants to allow other components to modify these settings, the service must expose an interface that another component can call into that tells the service how to alter these settings.  For example, a Win32 service could expose a COM or RPC interface and a driver service could expose an IOCTL interface via a device interface.

##### Shared service file state

Shared service file state is state that is written at runtime and can be shared with other user mode components if they are sufficiently privileged. To access the location for this shared service state, use one of these functions:

- [**IoGetDriverDirectory**](/windows-hardware/drivers/ddi/content/wdm/nf-wdm-iogetdriverdirectory) (WDM, KMDF) with the **DirectoryType** parameter set to **DriverDirectorySharedData**

- [**GetSharedServiceDirectory**](/windows/win32/api/winsvc/nf-winsvc-getsharedservicedirectory) (Win32 Services) with the **DirectoryType** parameter set to **ServiceSharedDirectoryPersistentState**

#### DriverData and ProgramData

Files that can be shared with other components but that do not fit into the [shared service file state](#shared-service-file-state) paradigm can be written to either `DriverData` or `ProgramData` locations.

These locations offer components a location to write temporary state or state that is meant to be consumed by other components and potentially collected and copied from a system to be processed by another system.  For example, custom log files or crash dumps fit this description.

Avoid writing files in the root of the `DriverData` or `ProgramData` directories. Instead, create a subdirectory with your company name and then write files and further subdirectories within that directory.

For example, for a company name of Contoso, a kernel-mode driver could write a custom log to `\DriverData\Contoso\Logs` and a user-mode application could collect or analyze the log files from `%DriverData%\Contoso\Logs`.

##### DriverData

The `DriverData` directory is available in Windows 10, version 1803 and later, and is accessible to administrators and UMDF drivers.

Kernel-mode drivers access the `DriverData` directory by using a system-supplied symbolic link called `\DriverData`.

User-mode programs access the `DriverData` directory by using the environment variable `%DriverData%`.

##### ProgramData

The `%ProgramData%` user-mode environment variable is available for user-mode components to use when storing data.

#### Temporary files

Temporary files are files that are temporary and typically used as part of intermediate operations.  These can be written to a sub-path under the `%TEMP%` or `%TMP%` environment variables.  Since these locations are accessed through environment variables, this ability is limited to user mode components.  There are no guarantees on the lifetime or persistence of these temporary files after handles to them are closed.  The operating system or user may choose to clean them up at any time and they may or may not persist across a reboot.

Avoid writing files in the root of the `%TEMP%` or `%TMP%` directories. Instead, create a subdirectory with your company name and then write files and further subdirectories within that directory.

### Property state

Both devices and device interfaces support storing state via the PnP [property model](../install/unified-device-property-model--windows-vista-and-later-.md).  The property model allows for structured property data to be stored against a device or device interface.  This is meant for smaller data that reasonably fits into the property types supported by the property model.

To access device properties, these APIs can be used:

- WDM drivers

  - [IoGetDevicePropertyData](/windows-hardware/drivers/ddi/wdm/nf-wdm-iogetdevicepropertydata)

  - [IoSetDevicePropertyData](/windows-hardware/drivers/ddi/wdm/nf-wdm-iosetdevicepropertydata)

- WDF drivers

  - [WdfDeviceQueryProperty](/windows-hardware/drivers/ddi/wdfdevice/nf-wdfdevice-wdfdevicequeryproperty)

  - [WdfDeviceAllocAndQueryProperty](/windows-hardware/drivers/ddi/wdfdevice/nf-wdfdevice-wdfdeviceallocandqueryproperty)

  - [WdfDeviceQueryPropertyEx](/windows-hardware/drivers/ddi/wdfdevice/nf-wdfdevice-wdfdevicequerypropertyex)

  - [WdfDeviceAllocAndQueryPropertyEx](/windows-hardware/drivers/ddi/wdfdevice/nf-wdfdevice-wdfdeviceallocandquerypropertyex)

  - [WdfDeviceAssignProperty](/windows-hardware/drivers/ddi/wdfdevice/nf-wdfdevice-wdfdeviceassignproperty)

  - [WdfFdoInitQueryProperty](/windows-hardware/drivers/ddi/wdffdo/nf-wdffdo-wdffdoinitqueryproperty)

  - [WdfFdoInitAllocAndQueryProperty](/windows-hardware/drivers/ddi/wdffdo/nf-wdffdo-wdffdoinitallocandqueryproperty)

  - [WdfFdoInitQueryPropertyEx](/windows-hardware/drivers/ddi/wdffdo/nf-wdffdo-wdffdoinitquerypropertyex)

  - [WdfFdoInitAllocAndQueryPropertyEx](/windows-hardware/drivers/ddi/wdffdo/nf-wdffdo-wdffdoinitallocandquerypropertyex)

- User mode code

  - [CM_Get_DevNode_Property](/windows/win32/api/cfgmgr32/nf-cfgmgr32-cm_get_devnode_propertyw)

  - [CM_Set_DevNode_Property](/windows/win32/api/cfgmgr32/nf-cfgmgr32-cm_set_devnode_propertyw)

To access device interface properties, these APIs can be used:

- WDM drivers

  - [IoGetDeviceInterfacePropertyData](/windows-hardware/drivers/ddi/wdm/nf-wdm-iogetdeviceinterfacepropertydata)

  - [IoSetDeviceInterfacePropertyData](/windows-hardware/drivers/ddi/wdm/nf-wdm-iosetdeviceinterfacepropertydata)

- WDF drivers

  - [WdfDeviceQueryInterfaceProperty](/windows-hardware/drivers/ddi/wdfdevice/nf-wdfdevice-wdfdevicequeryinterfaceproperty)

  - [WdfDeviceAllocAndQueryInterfaceProperty](/windows-hardware/drivers/ddi/wdfdevice/nf-wdfdevice-wdfdeviceallocandqueryinterfaceproperty)

  - [WdfDeviceAssignInterfaceProperty](/windows-hardware/drivers/ddi/wdfdevice/nf-wdfdevice-wdfdeviceassigninterfaceproperty)

- User mode code

  - [CM_Get_Device_Interface_Property](/windows/win32/api/cfgmgr32/nf-cfgmgr32-cm_get_device_interface_propertyw)

  - [CM_Set_Device_Interface_Property](/windows/win32/api/cfgmgr32/nf-cfgmgr32-cm_set_device_interface_propertyw)

## Using device interfaces

If a driver wants to allow other components to read or modify the driver's internal state, the driver should expose an interface that another component can call into that tells the driver what settings to return or how to modify particular settings. For example, the driver service could expose an IOCTL interface via a device interface.

Typically, the driver that owns the state exposes a device interface in a custom device interface class. When the driver is ready for other components to have access to the state, it enables the interface. To get notified when a device interface is enabled, user mode components can register for [device interface arrival notifications](../install/registering-for-notification-of-device-interface-arrival-and-device-removal.md) and kernel mode components can use [**IoRegisterPlugPlayNotification**](/windows-hardware/drivers/ddi/wdm/nf-wdm-ioregisterplugplaynotification). For these components to access the state, the driver enabling the interface must define a contract for its custom device interface class.  This contract typically is one of two kinds:

- An *I/O contract* can be associated with that device interface class that provides a mechanism for accessing the state. Other components use the enabled device interface to send I/O requests that conform to the contract.

- A *direct-call interface* that gets returned via a query interface. Other drivers could send [IRP_MN_QUERY_INTERFACE](../kernel/irp-mn-query-interface.md) to retrieve function pointers from the driver to call.

Alternatively, if the driver that owns the state allows direct access to the state, other drivers could access state by using system-supplied functions for programmatic access to device interface state. See [Device Interface Registry State](#device-interface-registry-state) for more information.

These interfaces or state (depending on sharing method used) need to be properly versioned so the driver owning the state can be serviced independently of other components that access that state. Driver vendors cannot rely on other components being serviced at the same time as the driver and staying at the same version.  

Because devices and drivers controlling interfaces come and go, drivers and applications should avoid calling [**IoGetDeviceInterfaces**](/windows-hardware/drivers/ddi/wdm/nf-wdm-iogetdeviceinterfaces) at component start-up to get a list of enabled interfaces. Instead, the best practice is to register for notifications of device interface arrival or removal and then call the appropriate function to get the list of existing enabled interfaces on the machine.

For more information about device interfaces, see:

- [Using Device Interfaces](../wdf/using-device-interfaces.md)

- [Registering for Notification of Device Interface Arrival and Device Removal](../install/registering-for-notification-of-device-interface-arrival-and-device-removal.md)

- [Registering for Device Interface Change Notification](../kernel/registering-for-device-interface-change-notification.md)

## Quick reference of operating system support for state management APIs

Most driver packages need to support a range of operating system versions.  See [Supporting multiple operating system versions](support-multiple-os-versions.md) for more information on how to achieve this in a driver package.  The following tables provide a quick reference of when operating system support was added for various state management APIs.

### WDM drivers

| Operating system | Support added |
|--|--|
| Windows 2000 | [**IoOpenDeviceRegistryKey**](/windows-hardware/drivers/ddi/wdm/nf-wdm-ioopendeviceregistrykey)<br>[**IoOpenDeviceInterfaceRegistryKey**](/windows-hardware/drivers/ddi/wdm/nf-wdm-ioopendeviceinterfaceregistrykey) |
| Windows Vista | [**IoGetDevicePropertyData**](/windows-hardware/drivers/ddi/wdm/nf-wdm-iogetdevicepropertydata)<br>[**IoSetDevicePropertyData**](/windows-hardware/drivers/ddi/wdm/nf-wdm-iosetdevicepropertydata) |
| Windows 8 | [**IoGetDeviceInterfacePropertyData**](/windows-hardware/drivers/ddi/wdm/nf-wdm-iogetdeviceinterfacepropertydata)<br>[**IoSetDeviceInterfacePropertyData**](/windows-hardware/drivers/ddi/wdm/nf-wdm-iosetdeviceinterfacepropertydata) |
| Windows 8.1 | [**IoQueryFullDriverPath**](/windows-hardware/drivers/ddi/ntddk/nf-ntddk-ioqueryfulldriverpath) |
| Windows 10 1803 | [**IoOpenDriverRegistryKey**](/windows-hardware/drivers/ddi/wdm/nf-wdm-ioopendriverregistrykey) for *RegKeyType* of *DriverRegKeyParameters* and *DriverRegKeyPersistentState*<br>[**IoGetDeviceDirectory**](/windows-hardware/drivers/ddi/wdm/nf-wdm-iogetdevicedirectory)<br>[**IoGetDriverDirectory**](/windows-hardware/drivers/ddi/content/wdm/nf-wdm-iogetdriverdirectory) for *DirectoryType* of *DriverDirectoryImage* and *DriverDirectoryData* |
| Windows 10 1809 | [**RtlQueryRegistryValueWithFallback**](/windows-hardware/drivers/ddi/ntddk/nf-ntddk-rtlqueryregistryvaluewithfallback) |
| Windows 11 21H2 | [**IoOpenDriverRegistryKey**](/windows-hardware/drivers/ddi/wdm/nf-wdm-ioopendriverregistrykey) for *RegKeyType* of *DriverRegKeySharedPersistentState*<br>[**IoGetDriverDirectory**](/windows-hardware/drivers/ddi/content/wdm/nf-wdm-iogetdriverdirectory) for *DirectoryType* of *DriverDirectorySharedData* |

### KMDF drivers

| KMDF version | Support added |
|--|--|
| 1.0 | [**WdfDeviceOpenRegistryKey**](/windows-hardware/drivers/ddi/wdfdevice/nf-wdfdevice-wdfdeviceopenregistrykey)<br>[**WdfFdoInitOpenRegistryKey**](/windows-hardware/drivers/ddi/wdffdo/nf-wdffdo-wdffdoinitopenregistrykey)<br>[**WdfDriverOpenParametersRegistryKey**](/windows-hardware/drivers/ddi/wdfdriver/nf-wdfdriver-wdfdriveropenparametersregistrykey)<br>[**WdfDeviceQueryProperty**](/windows-hardware/drivers/ddi/wdfdevice/nf-wdfdevice-wdfdevicequeryproperty)<br>[**WdfDeviceAllocAndQueryProperty**](/windows-hardware/drivers/ddi/wdfdevice/nf-wdfdevice-wdfdeviceallocandqueryproperty)<br>[**WdfFdoInitQueryProperty**](/windows-hardware/drivers/ddi/wdffdo/nf-wdffdo-wdffdoinitqueryproperty)<br>[**WdfFdoInitAllocAndQueryProperty**](/windows-hardware/drivers/ddi/wdffdo/nf-wdffdo-wdffdoinitallocandqueryproperty) |
| 1.13 | [**WdfDeviceQueryPropertyEx**](/windows-hardware/drivers/ddi/wdfdevice/nf-wdfdevice-wdfdevicequerypropertyex)<br>[**WdfDeviceAllocAndQueryPropertyEx**](/windows-hardware/drivers/ddi/wdfdevice/nf-wdfdevice-wdfdeviceallocandquerypropertyex)<br>[**WdfDeviceAssignProperty**](/windows-hardware/drivers/ddi/wdfdevice/nf-wdfdevice-wdfdeviceassignproperty)<br>[**WdfFdoInitQueryPropertyEx**](/windows-hardware/drivers/ddi/wdffdo/nf-wdffdo-wdffdoinitquerypropertyex)<br>[**WdfFdoInitAllocAndQueryPropertyEx**](/windows-hardware/drivers/ddi/wdffdo/nf-wdffdo-wdffdoinitallocandquerypropertyex) |
| 1.25 | [**WdfDriverOpenPersistentStateRegistryKey**](/windows-hardware/drivers/ddi/wdfdriver/nf-wdfdriver-wdfdriveropenpersistentstateregistrykey) (Windows 10 1803) |

### UMDF drivers

| UMDF version | Support added |
|--|--|
| 2.0 | [**WdfDeviceOpenRegistryKey**](/windows-hardware/drivers/ddi/wdfdevice/nf-wdfdevice-wdfdeviceopenregistrykey)<br>[**WdfFdoInitOpenRegistryKey**](/windows-hardware/drivers/ddi/wdffdo/nf-wdffdo-wdffdoinitopenregistrykey)<br>[**WdfDriverOpenParametersRegistryKey**](/windows-hardware/drivers/ddi/wdfdriver/nf-wdfdriver-wdfdriveropenparametersregistrykey)<br>[**WdfDeviceQueryProperty**](/windows-hardware/drivers/ddi/wdfdevice/nf-wdfdevice-wdfdevicequeryproperty)<br>[**WdfDeviceAllocAndQueryProperty**](/windows-hardware/drivers/ddi/wdfdevice/nf-wdfdevice-wdfdeviceallocandqueryproperty)<br>[**WdfDeviceQueryPropertyEx**](/windows-hardware/drivers/ddi/wdfdevice/nf-wdfdevice-wdfdevicequerypropertyex)<br>[**WdfDeviceAllocAndQueryPropertyEx**](/windows-hardware/drivers/ddi/wdfdevice/nf-wdfdevice-wdfdeviceallocandquerypropertyex)<br>[**WdfDeviceAssignProperty**](/windows-hardware/drivers/ddi/wdfdevice/nf-wdfdevice-wdfdeviceassignproperty)<br>[**WdfFdoInitQueryProperty**](/windows-hardware/drivers/ddi/wdffdo/nf-wdffdo-wdffdoinitqueryproperty)<br>[**WdfFdoInitAllocAndQueryProperty**](/windows-hardware/drivers/ddi/wdffdo/nf-wdffdo-wdffdoinitallocandqueryproperty)<br>[**WdfFdoInitQueryPropertyEx**](/windows-hardware/drivers/ddi/wdffdo/nf-wdffdo-wdffdoinitquerypropertyex)<br>[**WdfFdoInitAllocAndQueryPropertyEx**](/windows-hardware/drivers/ddi/wdffdo/nf-wdffdo-wdffdoinitallocandquerypropertyex)<br>[**WdfDeviceQueryInterfaceProperty**](/windows-hardware/drivers/ddi/wdfdevice/nf-wdfdevice-wdfdevicequeryinterfaceproperty) (Windows 8.1)<br>[**WdfDeviceAllocAndQueryInterfaceProperty**](/windows-hardware/drivers/ddi/wdfdevice/nf-wdfdevice-wdfdeviceallocandqueryinterfaceproperty) (Windows 8.1)<br>[**WdfDeviceAssignInterfaceProperty**](/windows-hardware/drivers/ddi/wdfdevice/nf-wdfdevice-wdfdeviceassigninterfaceproperty) (Windows 8.1) |
| 2.25 | [**WdfDeviceRetrieveDeviceDirectoryString**](/windows-hardware/drivers/ddi/wdfdevice/nf-wdfdevice-wdfdeviceretrievedevicedirectorystring)<br>[**WdfDriverOpenPersistentStateRegistryKey**](/windows-hardware/drivers/ddi/wdfdriver/nf-wdfdriver-wdfdriveropenpersistentstateregistrykey) (Windows 10 1803) |
| 2.27 | [**WdfDriverRetrieveDriverDataDirectoryString**](/windows-hardware/drivers/ddi/content/wdfdriver/nf-wdfdriver-wdfdriverretrievedriverdatadirectorystring) |

### User mode code

| Operating system | Support added |
|--|--|
| Windows 2000 | [**CM_Open_DevNode_Key**](/windows/win32/api/cfgmgr32/nf-cfgmgr32-cm_open_devnode_key) |
| Windows Vista | [**CM_Open_Device_Interface_Key**](/windows/win32/api/cfgmgr32/nf-cfgmgr32-cm_open_device_interface_keyw)<br>[**CM_Get_DevNode_Property**](/windows/win32/api/cfgmgr32/nf-cfgmgr32-cm_get_devnode_propertyw)<br>[**CM_Set_DevNode_Property**](/windows/win32/api/cfgmgr32/nf-cfgmgr32-cm_set_devnode_propertyw)<br>[**CM_Get_Device_Interface_Property**](/windows/win32/api/cfgmgr32/nf-cfgmgr32-cm_get_device_interface_propertyw)<br>[**CM_Set_Device_Interface_Property**](/windows/win32/api/cfgmgr32/nf-cfgmgr32-cm_set_device_interface_propertyw) |
| Windows 10 2004 | [**GetServiceRegistryStateKey**](/windows/win32/api/winsvc/nf-winsvc-getserviceregistrystatekey)<br>[**GetServiceDirectory**](/windows/win32/api/winsvc/nf-winsvc-getservicedirectory) |
| Windows 11 21H2 | [**GetSharedServiceRegistryStateKey**](/windows/win32/api/winsvc/nf-winsvc-getsharedserviceregistrystatekey)<br>[**GetSharedServiceDirectory**](/windows/win32/api/winsvc/nf-winsvc-getsharedservicedirectory) |
