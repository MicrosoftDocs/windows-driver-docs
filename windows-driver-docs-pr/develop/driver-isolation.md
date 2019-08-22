# Driver Isolation and Universal Drivers

## Driver Isolation Overview

An isolated stores registry and file state using a relative handle to a location provided by OS API's and functionality as opposed to hardcoding global location paths.

Drivers should interact with other drivers and their state through OS API's or interfaces exposed by the drivers and not through hardcoding paths to drivers or their state and manually modifying it through registry or file API's.  Additionally, all isolated drivers are run from the driver store.

This enables a driver to be self-contained and sandboxed which makes it more robust to multiple versions existing or running on a system simultaneously. Additionally, this enables the OS to move drivers to different locations based on new servicing or security features without risking driver functionality.  Below is a diagram of the four main principles that isolated drivers use:

![screen shot of the output window](images/non-isolated-vs-isolated.png)

## Run From Driver Store

All isolated drivers leave their driver package files in the driver store. This means that they leverage **DIRID 13** in their INF to specify the location for driver package files on install.

A WDM or KMDF driver that is running from the DriverStore and needs to access other files from its driver package could use [IoQueryFullDriverPath]() to find its path, get the directory path it was loaded from, and look for configuration files relative to that path.

Alternatively, on Windows 10 Verison 1803 and later, [IoGetDriverDirectory]() with *DriverDirectoryImage* as the directory type could be used to get the directory path that the driver was loaded from.

For a file payloaded by an INF, the *subdir* listed in the [SourceDisksFiles]() entry for the file in the INF must match the subdir listed in the [DestinationDirs entry for the file in the INF.

Additionally, a [CopyFiles]() directive cannot be used to rename a file. These restrictions are required so that the installation of an INF on a device does not result in the creation of new files in the DriverStore directory.

Since [SourceDisksFiles]() entries cannot have multiple entries with the same filename and CopyFiles cannot be used to rename a file, every file that an INF references must have a **unique file name**.

More information on how to find and load files from the driver store can be found in the [Universal Driver Scenarios](https://docs.microsoft.com/en-us/windows-hardware/drivers/develop/universal-driver-scenarios#dynamically-finding-and-loading-files-from-the-driver-store) page.

## Provisioning and Accessing Registry State

Access to various state should be done using OS API's that provide a caller with the location of the state and then the state is read/written relative to that location. Hardcoded absolute registry paths and file paths **should not be used** except for some limited exceptions noted in the File State and Registry Exceptions section.

### PnP Device Registry State

There is a need for isolated drivers and user mode components to read, and sometimes write, device state.  There are already two locations that can be used to store device state in the registry. They are called the **"hardware key"** (aka "device key") for the device and the **"software key"** (aka "driver key") for the device. These registry locations are already accessible via API's that give a caller a handle to the location.

The following API's should be used to ensure your driver is isolated:

* WDM:
  * [IoOpenDeviceRegistryKey]()
* WDF:
  * [WdfDeviceOpenRegistryKey]()
  * [WdfFdoInitOpenRegistryKey]()
* Other UserMode Code:
  * [CM_Open_DevNode_Key]()
* Provision Values via INF:
  * [INF AddReg]() directive using HKR *reg-root* entries in an *add-registry-section* referenced from an [INF DDInstall]() section or [DDInstall.HW]() section

Below is an example of an INF privisioning through its INF device registry state:

```
[ExampleDDInstall.HW]
AddReg = Example_DDInstall.AddReg

[Example_DDInstall.AddReg] 
HKR,,ExampleValue,,%13%\ExampleFile.dll
```

### Device Interface Registry State

### Service Registry State
