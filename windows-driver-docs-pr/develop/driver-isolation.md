---
title: Driver Package Isolation
description: This page describes driver isolation, a requirement for a Windows Driver.
ms.date: 11/03/2021
ms.localizationpriority: medium
---

# Driver Package Isolation

Driver package isolation is a requirement for [Windows Drivers](./getting-started-with-windows-drivers.md) that makes driver packages more resilient to external changes, easier to update, and more straightforward to install.

> [!NOTE]
> While Driver Package Isolation is required for Windows Drivers, Windows Desktop Drivers still benefit from it through improved resiliency and serviceability.

The following table shows some example legacy driver practices that are no longer allowed for Windows Drivers in the left column along with the required behavior for Windows Drivers in the right column.

|Non-isolated Driver|Isolated Driver|
|-|-|
|INF copies files to %windir%\System32 or %windir%\System32\drivers|Driver files are [run from the driver store](./run-from-driver-store.md)|
|Interacts with device stacks/drivers using hardcoded paths|Interacts with device stacks/drivers using system-supplied functions or device interfaces|
|Hardcodes path to global registry locations|Uses HKR and system-supplied functions for relative location of registry and file state|
|Runtime file writes to any location|Files are written relative to locations supplied by the operating system|

For help in determining if your driver package meets Driver Package Isolation requirements, see [Validating Windows Drivers](./validating-windows-drivers.md).

## Run From Driver Store

All isolated driver packages leave their driver package files in the driver store. This means that they specify [**DIRID 13**](../install/using-dirids.md) in their INF to specify the location for driver package files on install.  For more information on how to use this in a driver package, see [**Run from Driver Store**](./run-from-driver-store.md).

## Reading and Writing State

> [!NOTE]
> If your component is using device or device interface *properties* to store state, continue to use that method and the appropriate OS API's to store and access state. The following guidance is for *other* state that needs to be stored by a component.

Access to various state should be done by calling functions that provide a caller with the location of the state and then the state is read/written relative to that location. Do not use hardcoded absolute registry paths and file paths.

### Registry State

This section contains the following subsections:

* [PnP Device Registry State](#pnp-device-registry-state)
* [Device Interface Registry State](#device-interface-registry-state)
* [Service Registry State](#service-registry-state)

#### PnP Device Registry State

Isolated driver packages and user-mode components typically use one of two locations to store device state in the registry. These are the *hardware key* (device key) for the device and the *software key* (driver key) for the device. To retrieve a handle to these registry locations, use one of the following options:


* [**IoOpenDeviceRegistryKey**](/windows-hardware/drivers/ddi/wdm/nf-wdm-ioopendeviceregistrykey) (WDM)
* [**WdfDeviceOpenRegistryKey**](/windows-hardware/drivers/ddi/wdfdevice/nf-wdfdevice-wdfdeviceopenregistrykey), [**WdfFdoInitOpenRegistryKey**](/windows-hardware/drivers/ddi/wdffdo/nf-wdffdo-wdffdoinitopenregistrykey) (WDF)
* [**CM_Open_DevNode_Key**](/windows/win32/api/cfgmgr32/nf-cfgmgr32-cm_open_devnode_key) (user-mode code)
* [**INF AddReg**](../install/inf-addreg-directive.md) directive using HKR *reg-root* entries in an *add-registry-section* referenced from an [INF DDInstall](../install/inf-ddinstall-section.md) section or [DDInstall.HW](../install/inf-ddinstall-hw-section.md) section, as shown below:

```
[ExampleDDInstall.HW]
AddReg = Example_DDInstall.AddReg

[Example_DDInstall.AddReg] 
HKR,,ExampleValue,,%13%\ExampleFile.dll
```

#### Device Interface Registry State

To read and write device interface registry state, use one of the following options:

* [**IoOpenDeviceInterfaceRegistryKey**](/windows-hardware/drivers/ddi/wdm/nf-wdm-ioopendeviceinterfaceregistrykey) (WDM) 
* [**CM_Open_Device_Interface_Key**](/windows/win32/api/cfgmgr32/nf-cfgmgr32-cm_open_device_interface_keyw) (user-mode code)
* [INF AddReg](../install/inf-addreg-directive.md) directive using HKR *reg-root* entries in an *add-registry-section* referenced from an [add-interface-section](../install/inf-addinterface-directive.md) section

#### Service Registry State

Service state should be classified into one of 3 categories
* [Immutable Service Registry State](#immutable-service-registry-state)
* [Internal Service Registry State](#internal-service-registry-state)
* [Shared Service Registry State](#shared-service-registry-state)

##### Immutable Service Registry State

Immutable service state is state that is provided by the driver package that installs the service.  These registry values that are set by the INF for driver and Win32 services must be stored under the "Parameters" subkey of the service by providing an HKR line in an [AddReg](../install/inf-addreg-directive.md) section, and then referencing that section in the service install section in the INF.  For example:

```
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

* [**IoOpenDriverRegistryKey**](/windows-hardware/drivers/ddi/wdm/nf-wdm-ioopendriverregistrykey) (WDM) with a DRIVER_REGKEY_TYPE of **DriverRegKeyParameters**
* [**WdfDriverOpenParametersRegistryKey**](/windows-hardware/drivers/ddi/wdfdriver/nf-wdfdriver-wdfdriveropenparametersregistrykey) (WDF)
* [**GetServiceRegistryStateKey**](/windows/win32/api/winsvc/nf-winsvc-getserviceregistrystatekey) (Win32 Services) with a SERVICE_REGISTRY_STATE_TYPE of **ServiceRegistryStateParameters**

These registry values supplied by the INF in the “Parameters” subkey for the service should only be read at runtime and not modified. They should be treated as read only.

If the registry values supplied by the INF are default settings that can be overwritten at runtime, the override values should be written into the [Internal Service Registry State](#internal-service-registry-state) or [Shared Service Registry State](#shared-service-registry-state) for the service.  When retrieving the settings, the setting can be looked for first in the mutable state. If it does not exist there, then the setting can be looked for in the immutable state.  [**RtlQueryRegistryValueWithFallback**](/windows-hardware/drivers/ddi/ntddk/nf-ntddk-rtlqueryregistryvaluewithfallback) can be used to help query settings such as these that have an override and a default value.


##### Internal Service Registry State

Internal service state is state that is written at runtime and owned and managed by only the service itself and is only accessible to that service. To access the location for internal service state, use one of these functions from the service:

* [**IoOpenDriverRegistryKey**](/windows-hardware/drivers/ddi/wdm/nf-wdm-ioopendriverregistrykey) (WDM) with a DRIVER_REGKEY_TYPE of **DriverRegKeyPersistentState**
* [**WdfDriverOpenPersistentStateRegistryKey**](/windows-hardware/drivers/ddi/wdfdriver/nf-wdfdriver-wdfdriveropenpersistentstateregistrykey) (WDF)
* [**GetServiceRegistryStateKey**](/windows/win32/api/winsvc/nf-winsvc-getserviceregistrystatekey) (Win32 Services) with a SERVICE_REGISTRY_STATE_TYPE of **ServiceRegistryStatePersistent**

If the service wants to allow other components to modify these settings, the service must expose an interface that another component can call into that tells the service how to alter these settings.  For example, a Win32 service could expose a COM or RPC interface and a driver service could expose an IOCTL interface via a device interface.

##### Shared Service Registry State

Shared service state is state that is written at runtime and can be shared with other user mode components if they are sufficiently privileged. To access the location for this shared service state, use one of these functions:

* [**IoOpenDriverRegistryKey**](/windows-hardware/drivers/ddi/wdm/nf-wdm-ioopendriverregistrykey) (WDM) with a DRIVER_REGKEY_TYPE of **DriverRegKeySharedPersistentState**
* [**GetSharedServiceRegistryStateKey**](/windows/win32/api/winsvc/nf-winsvc-getsharedserviceregistrystatekey) (Win32 Services) with a SERVICE_SHARED_REGISTRY_STATE_TYPE of **ServiceSharedRegistryPersistentState**

### File State

This section contains the following subsections:

* [Device File State](#device-file-state)
* [Service File State](#service-file-state)

#### Device File State

If files related to a device need to be written at runtime, those files should be stored relative to a handle or file path provided via OS API’s. Configuration files specific to that device is one example of what types of files to be stored here. To access the location of this state, use one of these functions from the service:

* [**IoGetDeviceDirectory**](/windows-hardware/drivers/ddi/wdm/nf-wdm-iogetdevicedirectory) (WDM) with the **DirectoryType** parameter set to **DeviceDirectoryData**
* [**WdfDeviceRetrieveDeviceDirectoryString**](/windows-hardware/drivers/ddi/wdfdevice/nf-wdfdevice-wdfdeviceretrievedevicedirectorystring) (WDF)

#### Service File State

Service file state can be classified into one of 3 categories
* [Immutable Service File State](#immutable-service-file-state)
* [Internal Service File State](#internal-service-file-state)
* [Shared Service File State](#shared-service-file-state)

##### Immutable Service File State

Immutable service file state are files that are part of the driver package. For more information on accessing those files, see [**Run from Driver Store**](./run-from-driver-store.md).

##### Internal Service File State

Internal service file state is state that is written at runtime and owned and managed by only the service itself and is only accessible to that service. To access the location for internal service state, use one of these functions from the service:

* [**IoGetDriverDirectory**](/windows-hardware/drivers/ddi/content/wdm/nf-wdm-iogetdriverdirectory) (WDM, KMDF) with the **DirectoryType** parameter set to **DriverDirectoryData**
* [**WdfDriverRetrieveDriverDataDirectoryString**](/windows-hardware/drivers/ddi/content/wdfdriver/nf-wdfdriver-wdfdriverretrievedriverdatadirectorystring) (UMDF)
* [**GetServiceDirectory**](/windows/win32/api/winsvc/nf-winsvc-getservicedirectory) (Win32 Services) with the **eDirectoryType** parameter set to **ServiceDirectoryPersistentState**

If the service wants to allow other components to modify these settings, the service must expose an interface that another component can call into that tells the service how to alter these settings.  For example, a Win32 service could expose a COM or RPC interface and a driver service could expose an IOCTL interface via a device interface.

##### Shared Service File State

Shared service file state is state that is written at runtime and can be shared with other user mode components if they are sufficiently privileged. To access the location for this shared service state, use one of these functions:

* [**IoGetDriverDirectory**](/windows-hardware/drivers/ddi/content/wdm/nf-wdm-iogetdriverdirectory) (WDM, KMDF) with the **DirectoryType** parameter set to **DriverDirectorySharedData**
* [**GetSharedServiceDirectory**](/windows/win32/api/winsvc/nf-winsvc-getsharedservicedirectory) (Win32 Services) with the **DirectoryType** parameter set to **ServiceSharedDirectoryPersistentState**

#### DriverData and ProgramData

Files that are to be used as part of intermediate operations that can be shared with other components can be written to either `DriverData` or `ProgramData` locations.

These locations offer components a location to write temporary state or state that is meant to be consumed by other components and potentially collected and copied from a system to be processed by another system.  For example, custom log files or crash dumps fit this description.

Avoid writing files in the root of the `DriverData` or `ProgramData` directories. Instead, create a subdirectory with your company name and then write files and further subdirectories within that directory.

For example, for a company name of Contoso, a kernel-mode driver could write a custom log to `\DriverData\Contoso\Logs` and a user-mode application could collect or analyze the log files from `%DriverData%\Contoso\Logs`.

##### DriverData

The `DriverData` directory is available in Windows 10, version 1803 and later, and is accessible to administrators and UMDF drivers.

Kernel-mode drivers access the `DriverData` directory by using a system-supplied symbolic link called `\DriverData`.
User-mode programs access the `DriverData` directory by using the environment variable `%DriverData%`.

##### ProgramData

The `%ProgramData%` user-mode environment variable is available for user-mode components to use when storing data. 

## Using Device Interfaces

If a driver wants to allow other components to read or modify the driver's internal state, the driver should expose an interface that another component can call into that tells the driver what settings to return or how to modify particular settings. For example, the driver service could expose an IOCTL interface via a device interface.

Typically, the driver that owns the state exposes a device interface in a custom device interface class. When the driver is ready for other components to have access to the state, it enables the interface. To get notified when a device interface is enabled, user mode components can register for [device interface arrival notifications](../install/registering-for-notification-of-device-interface-arrival-and-device-removal.md) and kernel mode components can use [**IoRegisterPlugPlayNotification**](/windows-hardware/drivers/ddi/wdm/nf-wdm-ioregisterplugplaynotification). For these components to access the state, the driver enabling the interface must define a contract for its custom device interface class.  This contract typically is one of two kinds:

* An *I/O contract* can be associated with that device interface class that provides a mechanism for accessing the state. Other components use the enabled device interface to send I/O requests that conform to the contract.
* A *direct-call interface* that gets returned via a query interface. Other drivers could send [IRP_MN_QUERY_INTERFACE](../kernel/irp-mn-query-interface.md) to retrieve function pointers from the driver to call.

Alternatively, if the driver that owns the state allows direct access to the state, other drivers could access state by using system-supplied functions for programmatic access to device interface state. See [Device Interface Registry State](#device-interface-registry-state) for more information.

These interfaces or state (depending on sharing method used) need to be properly versioned so the driver owning the state can be serviced independently of other components that access that state. Driver vendors cannot rely on other components being serviced at the same time as the driver and staying at the same version.  

Because devices and drivers controlling interfaces come and go, drivers and applications should avoid calling [**IoGetDeviceInterfaces**](/windows-hardware/drivers/ddi/wdm/nf-wdm-iogetdeviceinterfaces) at component start-up to get a list of enabled interfaces. Instead, the best practice is to register for notifications of device interface arrival or removal and then call the appropriate function to get the list of existing enabled interfaces on the machine.

For more information about device interfaces, see:

* [Using Device Interfaces](../wdf/using-device-interfaces.md)
* [Registering for Notification of Device Interface Arrival and Device Removal](../install/registering-for-notification-of-device-interface-arrival-and-device-removal.md)
* [Registering for Device Interface Change Notification](../kernel/registering-for-device-interface-change-notification.md)

