---
title: Driver Package Isolation
ms.date: 09/12/2019
---
# Driver Package Isolation

Driver isolation describes a set of best practices that make drivers less prone to crashes and easier to update. These are general recommendations that any driver can follow.

The following table shows legacy driver practices that are no longer recommended in the left column, and the corresponding recommended principle of driver isolation in the right column.

|Non-isolated Driver|Isolated Driver|
|-|-|
|INF copies files to System32\drivers|Driver files are run from the driver store|
|Interacts with other drivers and their state via hardcoded paths|Driver interacts with other drivers via OS APIs or device interfaces|
|Hardcodes path to global registry locations|Uses HKR and system-supplied functions for relative location of registry and file state|
|Runtime file writes to any location|Driver writes files to OS provided locations|

Using driver isolation principles yields the following benefits:

* Because an isolated driver package is sandboxed, multiple versions of the same driver can run on a system simultaneously.
* By depending on relative handles instead of global locations, a driver is more easily updated.
* Isolated driver packages are more resilient to changes in the OS. Installation to the driver store has fewer issues.
* By using device interfaces to interact with another driver, an isolated driver package is more resilient to any changes in the other driver.

## Run From Driver Store

All isolated driver packages leave their driver package files in the driver store. This means that they specify [**DIRID 13**](https://docs.microsoft.com/windows-hardware/drivers/install/using-dirids) in their INF to specify the location for driver package files on install.

A WDM or KMDF driver that is running from the DriverStore and needs to access other files from its driver package could use [**IoQueryFullDriverPath**](https://docs.microsoft.com/windows-hardware/drivers/ddi/content/ntddk/nf-ntddk-ioqueryfulldriverpath) to find its path, get the directory path it was loaded from, and look for configuration files relative to that path.

Alternatively, on Windows 10, version 1803 and later, call [**IoGetDriverDirectory**](https://docs.microsoft.com/windows-hardware/drivers/ddi/content/wdm/nf-wdm-iogetdriverdirectory) with *DriverDirectoryImage* as the directory type to get the directory path that the driver was loaded from.

For a file payloaded by an INF, the *subdir* listed in the [**SourceDisksFiles**](https://docs.microsoft.com/windows-hardware/drivers/install/inf-sourcedisksfiles-section) entry for the file in the INF must match the subdir listed in the [**DestinationDirs**](https://docs.microsoft.com/windows-hardware/drivers/install/inf-destinationdirs-section) entry for the file in the INF.

Additionally, a [**CopyFiles**](https://docs.microsoft.com/windows-hardware/drivers/install/inf-copyfiles-directive) directive cannot be used to rename a file. These restrictions are required so that the installation of an INF on a device does not result in the creation of new files in the DriverStore directory.

Since [**SourceDisksFiles**](https://docs.microsoft.com/windows-hardware/drivers/install/inf-sourcedisksfiles-section) entries cannot have multiple entries with the same filename and CopyFiles cannot be used to rename a file, every file that an INF references must have a **unique file name**.

For more information about finding and loading files from the driver store, see [Universal Driver Scenarios](https://docs.microsoft.com/windows-hardware/drivers/develop/universal-driver-scenarios#dynamically-finding-and-loading-files-from-the-driver-store).

## Using Device Interfaces

When state needs to be shared between drivers, there should be a single driver that owns the shared state, and it should expose a way for other drivers to *read* and *modify* that state.

Typically, the driver that owns the state exposes a device interface in a custom device interface class. When the driver is ready for other drivers to have access to the state, it enables the interface. Other drivers can register for [device interface arrival notifications](https://docs.microsoft.com/windows-hardware/drivers/install/registering-for-notification-of-device-interface-arrival-and-device-removal). To access the state, the custom device interface class can define one of two contracts:

* An *I/O contract* can be associated with that device interface class that provides a mechanism for accessing the state. Other drivers use the enabled device interface to send I/O requests that conform to the contract.
* A *direct-call interface* that gets returned via a query interface. Other drivers could send [IRP_MN_QUERY_INTERFACE](https://docs.microsoft.com/windows-hardware/drivers/kernel/irp-mn-query-interface) to retrieve function pointers from the driver to call.

Alternatively, if the driver that owns the state allows direct access to the state, other drivers could access state by using system-supplied functions for programmatic access to device interface state.

These interfaces or state (depending on sharing method used) need to be **properly versioned** so the driver owning the state can be serviced independently of other drivers that access that state. Driver vendors cannot rely on both drivers being serviced at the same time and staying at the same version.  

Because devices and drivers controlling interfaces come and go, drivers and applications should avoid calling [**IoGetDeviceInterfaces**](https://docs.microsoft.com/windows-hardware/drivers/ddi/content/wdm/nf-wdm-iogetdeviceinterfaces) at component start-up to get a list of enabled interfaces.

Instead, the best practice is to **register for notifications** of device interface arrival or removal and then call the appropriate function to get the list of existing enabled interfaces on the machine.

For more info, see:

* [Using Device Interfaces](https://docs.microsoft.com/windows-hardware/drivers/wdf/using-device-interfaces)
* [Registering for Notification of Device Interface Arrival and Device Removal](https://docs.microsoft.com/windows-hardware/drivers/install/registering-for-notification-of-device-interface-arrival-and-device-removal)
* [Registering for Device Interface Change Notification](https://docs.microsoft.com/windows-hardware/drivers/kernel/registering-for-device-interface-change-notification)

## Reading and Writing State

> [!NOTE]
> If your component is using device or device interface *properties* to store state, continue to use that method and the appropriate OS API's to store and access state. The following guidance is for *other* state that needs to be stored by a component.

Access to various state should be done by calling functions that provide a caller with the location of the state and then the state is read/written relative to that location. Do not use hardcoded absolute registry paths and file paths.

This section contains the following subsections:

* [PnP Device Registry State](#pnp-device-registry-state)
* [Device Interface Registry State](#device-interface-registry-state)
* [Service Registry State](#service-registry-state)
* [Device File State](#device-file-state)
* [Service File State](#service-file-state)

### PnP Device Registry State

Isolated driver packages and user mode components typically use two locations to store device state in the registry. These are the **"hardware key"** ("device key") for the device and the **"software key"** ("driver key") for the device. To retrieve a handle to these registry locations, use these functions:

* WDM:
  * [**IoOpenDeviceRegistryKey**](https://docs.microsoft.com/windows-hardware/drivers/ddi/content/wdm/nf-wdm-ioopendeviceregistrykey)
* WDF:
  * [**WdfDeviceOpenRegistryKey**](https://docs.microsoft.com/windows-hardware/drivers/ddi/content/wdfdevice/nf-wdfdevice-wdfdeviceopenregistrykey)
  * [**WdfFdoInitOpenRegistryKey**](https://docs.microsoft.com/windows-hardware/drivers/ddi/content/wdffdo/nf-wdffdo-wdffdoinitopenregistrykey)
* Other user mode Code:
  * [**CM_Open_DevNode_Key**](https://docs.microsoft.com/windows/win32/api/cfgmgr32/nf-cfgmgr32-cm_open_devnode_key)
* Provision Values via INF:
  * [**INF AddReg**](https://docs.microsoft.com/windows-hardware/drivers/install/inf-addreg-directive) directive using HKR *reg-root* entries in an *add-registry-section* referenced from an [INF DDInstall](https://docs.microsoft.com/windows-hardware/drivers/install/inf-ddinstall-section) section or [DDInstall.HW](https://docs.microsoft.com/windows-hardware/drivers/install/inf-ddinstall-hw-section) section

Below is an example of an INF writing device registry state in its INF:

```
[ExampleDDInstall.HW]
AddReg = Example_DDInstall.AddReg

[Example_DDInstall.AddReg] 
HKR,,ExampleValue,,%13%\ExampleFile.dll
```
### Device Interface Registry State

Isolated driver packages use device interfaces to share state with other drivers and components instead of hardcoding paths to global registry locations. For example:

![screen shot of the output window](images/device-interface-communication.png)

To read and write device interface registry state, use these functions:

* WDM:
  * [**IoOpenDeviceInterfaceRegistryKey**](https://docs.microsoft.com/windows-hardware/drivers/ddi/content/wdm/nf-wdm-ioopendeviceinterfaceregistrykey)
* Other user mode Code:
  * [**CM_Open_Device_Interface_Key**](https://docs.microsoft.com/windows/win32/api/cfgmgr32/nf-cfgmgr32-cm_open_device_interface_keya?redirectedfrom=MSDN)
* Provision Values via INF:
  * [INF AddReg](https://docs.microsoft.com/windows-hardware/drivers/install/inf-addreg-directive) directive using HKR *reg-root* entries in an *add-registry-section* referenced from an [add-interface-section](https://docs.microsoft.com/windows-hardware/drivers/install/inf-addinterface-directive) section.

### Service Registry State

Registry values that are set by the INF for driver and Win32 services should be stored under the "Parameters" subkey of the service by providing an HKR line in an [AddReg](https://docs.microsoft.com/windows-hardware/drivers/install/inf-addreg-directive) section, and then referencing that section in the service install section in the INF.  For example:

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

To access the location of this state, use these functions:

* WDM 
  * [**IoOpenDriverRegistryKey**](https://docs.microsoft.com/windows-hardware/drivers/ddi/content/wdm/nf-wdm-ioopendeviceregistrykey)
* WDF
  * [**WdfDriverOpenParamatersRegistryKey**](https://docs.microsoft.com/windows-hardware/drivers/ddi/content/wdfdriver/nf-wdfdriver-wdfdriveropenparametersregistrykey)
* Win32 Services
  * GetServiceRegistryStateKey

### Device File State

If files related to a device need to be written, those files should be stored relative to a handle or file path provided via OS API’s. Configuration files specific to that device is one example of what types of files to be stored here.

* WDM
  * [**IoGetDeviceDirectory**](https://docs.microsoft.com/windows-hardware/drivers/ddi/content/wdm/nf-wdm-iogetdevicedirectory)
* WDF
  * [**WdfDeviceRetrieveDeviceDirectoryString**](https://docs.microsoft.com/windows-hardware/drivers/ddi/content/wdfdevice/nf-wdfdevice-wdfdeviceretrievedevicedirectorystring)

### Service File State

Both Win32 and driver services read and write state about themselves.

To access its own internal state values, a service uses the following functions: 

* WDM
  * [**IoGetDriverDirectory**](https://docs.microsoft.com/windows-hardware/drivers/ddi/content/wdm/nf-wdm-iogetdriverdirectory)
* WDF
  * KMDF Drivers
    * [**IoGetDriverDirectory**](https://docs.microsoft.com/windows-hardware/drivers/ddi/content/wdm/nf-wdm-iogetdriverdirectory)
  * UMDF Drivers
    * [**WdfDriverRetrieveDriverDataDirectoryString**](https://docs.microsoft.com/windows-hardware/drivers/ddi/content/wdfdriver/nf-wdfdriver-wdfdriverretrievedriverdatadirectorystring)
* Win32 Services
  * GetServiceDirectory

To share internal state of the service with other components, use a controlled, versioned interface instead of direct registry or file reads.

## DriverData and ProgramData

Files that are to be used as part of intermediate operations that can be shared with other components should be written to either **DriverData** or **ProgramData** locations.

These locations offer components a location to write temporary state or state that is meant to be consumed by other components and potentially collected and copied from a system to be processed by another system.  For example, custom log files or crash dumps fit this description.

### DriverData

The `DriverData` directory is available in Windows 10, version 1803 and later. This directory is accessible by both user mode and kernel mode components through different mechanisms.

Kernel mode drivers should access the `DriverData` directory by using a system-supplied symbolic link called `\DriverData`.
User mode programs should access the `DriverData` directory by using the environment variable `%DriverData%`.

### ProgramData

The `%ProgramData%` user mode environment variable is available for user mode components to use when storing data. 

Avoid writing files in the root of the `DriverData` or `ProgramData` directories. Instead, create a subdirectory with your company name and then write files and further subdirectories within that directory.

For example, for a company name of Contoso, a kernel mode driver could write a custom log to `\DriverData\Contoso\Logs` and a user mode application could collect or analyze the log files from `%DriverData%\Contoso\Logs`.

