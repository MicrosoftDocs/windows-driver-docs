---
title: Attribute Tokens in SDEL
description: Describes SDEL attribute tokens used to define characteristics of target devices and computers.
keywords:
- SDEL
- attribute tokens
ms.date: 09/03/2020
ms.localizationpriority: medium
---

# Attribute Tokens in SDEL

The SDEL language uses target attribute tokens to define characteristics of target devices and computers.

## Root Attribute Tokens for All Targets

The following table describes the attributes in the root namespace that are valid for all targets.

|Keyword|VARIANT type|Description|
|----|----|----|
|Type|VT_BSTR|Defines the type of target. This value can be "System" or "Device".|

## Root Attribute Tokens for a Device Target

The following table describes the attributes in the root namespace that are valid only for device-type targets.

>[!NOTE]
>Most of the following attributes are retrieved from the operating system through the SetupDi APIs. For more information about this APIs, see SetupDiGetDeviceRegistryProperty.

|Keyword|VARIANT type|Description|
|----|----|----|
|Address|VT_I4|Class-specific (or bus-specific) address.|
|BusNumber|VT_I4|Bus number for the device.|
|Capabilities|VT_I4|Capabilities of the device.|
|Character|VT_I4|A bitwise OR of the device's characteristics flags in a DWORD. (SPDRP_CHARACTERISTICS)|
|Class|VT_BSTR|Class of the device.|
|ClassGUID|VT_BSTR|Class of the device, in GUID form. Use this keyword instead of the Class field when you are using localized builds.|
|CompatIDs|VT_ARRAY of VARIANT with VT_BSTR|All of the compatible IDs that are defined for this device.|
|ConfigFlags|VT_I4|Configuration flags for the device.|
|Description|VT_BSTR|Device description.|
|DeviceID|VT_BSTR|Device identifier, including the instance identifier for the device. This string is a unique string for every device in the system.|
|DeviceStatusString|VT_BSTR|Contains both StatusString and the ProblemCodeString in a single string.|
|DevInst|VT_I4|Opaque handle to the device instance.|
|DevType|VT_I4|Represents the device's type. (SPDRP_DEVTYPE)|
|DisplayName|VT_BSTR|Resolves to the first value that is found (from left to right) in the following attributes: FriendlyName, Description, or DeviceID.|
|Driver|VT_BSTR|A key in HKLM\System\CurrentControlSet\Control\Class\ that holds more information about the driver.|
|DriverBinaryNames|VT_ARRAY of VARIANT with VT_BSTR|Aggregates all of the data from UpperClassFilters, UpperFilters, LowerFilters, LowerClassFilters, and Service.|
|Enumerator|VT_BSTR|The name of the device's enumerator. (SPDRP_ENUMERATOR_NAME)|
|Exclusive|VT_I4|A number that indicates whether a user can obtain exclusive use of the device. (SPDRP_EXCLUSIVE)|
|Filters|VT_ARRAY of VARIANT with VT_BSTR|Aggregates all of the data from UpperClassFilters, UpperFilters, LowerFilters, and LowerClassFilters.|
|FriendlyName|VT_BSTR|Friendly name of the device.|
|HardwareIDs|VT_ARRAY of VARIANT with VT_BSTR|All of the hardware IDs that are defined for this device.|
|IsAttached|VT_BOOL|The opposite of the IsPhantom attribute. This keyword is equivalent to "IsPhantom=False".|
|IsDisableable|VT_BOOL|Extracts the DN_DISABLEABLE flag out of the Status flags. A value of VARIANT_TRUE indicates that the device claims that it can be disabled. This keyword is equivalent to "status&0x00002000".|
|IsDisabled|VT_BOOL|Checks for the CM_PROB_DISABLED value in the ProblemCode attribute. A value of VARIANT_TRUE indicates that the device is disabled and must be enabled before use. This keyword is equivalent to "ProblemCode=0x00000016".|
|IsFailedStart|VT_BOOL|Checks for the CM_PROB_FAILED_START flag out of the ProblemCode flags. A value of VARIANT_TRUE indicates that the device driver failed to start. This keyword is equivalent to "ProblemCode=0x0000000A".|
|IsFailedInstall|VT_BOOL|Checks for the CM_PROB_FAILED_INSTALL flag out of the ProblemCode flags. A value of VARIANT_TRUE indicates that the device driver failed to install on the device. This keyword is equivalent to "ProblemCode=0x0000001C".|
|IsFiltered|VT_BOOL|Extracts the DN_FILTERED flag out of the Status flags. This keyword is equivalent to "status&0x00000800".|
|IsManual|VT_BOOL|Extracts the DN_MANUAL flag out of the Status flags. This keyword is equivalent to "status&0x00000010".|
|IsMoved|VT_BOOL|Extracts the DN_MOVED flag out of the Status flags. This keyword is equivalent to "status&0x00001000".|
|IsPhantom|VT_BOOL|A value of VARIANT_TRUE indicates that the device is not currently plugged into the system or that it has been uninstalled.|
|IsRebootNeeded|VT_BOOL|Extracts the DN_NEED_RESTART flag out of the Status flags. A value of VARIANT_TRUE indicates that the device's co-installer claims that the computer needs to be restarted for the device to complete a removal or installation action. This keyword is equivalent to "status&0x00000100".|
|IsReinstallNeeded|VT_BOOL|Extracts the CONFIGFLAG_REINSTALL flag out of the ConfigFlags attribute. A value of VARIANT_TRUE indicates that the device claims that it can be removed. This keyword is equivalent to "ConfigFlags&0x00000020".|
|IsRemovable|VT_BOOL|Extracts the DN_REMOVABLE flag out of the Status flags. A value of VARIANT_TRUE indicates that the device claims that it can be removed. This keyword is equivalent to "status&0x00004000".|
|IsRemovePending|VT_BOOL|Extracts the DN_WILL_BE_REMOVED flag out of the Status flags. This keyword is equivalent to "status&0x00040000".|
|IsRootEnumerated|VT_BOOL|Extracts the DN_ROOT_ENUMERATED flag out of the Status flags. A value of VARIANT_TRUE indicates that the parent of the device is RootDevice. This keyword is equivalent to "status&0x00000001".|
|IsStarted|VT_BOOL|Extracts the DN_STARTED flag out of the Status flags. A value of VARIANT_TRUE indicates that the device is currently configured. This keyword is equivalent to "status&0x00000008".|
|LegacyBusType|VT_I4|Legacy bus type.|
|Location|VT_BSTR|More information about the physical location of the device.|
|LocationPaths|VT_ARRAY of VARIANT with VT_BSTR|Location of the device instance in the device tree.|
|LowerClassFilters|VT_ARRAY of VARIANT with VT_BSTR|The service names of every driver that is attached as a lower class filter on the target device.|
|LowerClassFiltersBinaryNames|VT_ARRAY of VARIANT with VT_BSTR|Names of binaries of all lower class filter drivers for device target.|
|LowerFilters|VT_ARRAY of VARIANT with VT_BSTR|The service names of every driver that is attached as a lower filter on the target device.|
|LowerFiltersBinaryNames|VT_ARRAY of VARIANT with VT_BSTR|Names of all lower filter drivers for device target.|
|Manufacturer|VT_BSTR|Manufacturer of the device.|
|PDO|VT_BSTR|Name of the physical device object in the kernel.|
|ProblemCode|VT_I4|Problem code for the device. One of the CM_PROB_-prefixed problem values defined in Cfg.h.|
|ProblemCodeString|VT_BSTR|The string representation of ProblemCode.|
|RemovalPolicy|VT_I4|Current removal policy of the device. (SPDRP_REMOVAL_POLICY)|
|RemovalPolicyHWDefault|VT_I4|ardware-specified default removal policy of the device. (SPDRP_REMOVAL_POLICY_HW_DEFAULT)|
|RemovalPolicyOverride|VT_I4|Override removal policy (if it exists) of the device. (SPDRP_REMOVAL_POLICY_OVERRIDE)|
|Service|VT_BSTR|The service name of the driver for the device.|
|ServiceBinaryName|VT_BSTR|Name of function driver for device target.|
|Status|VT_I4|Status flags for the device.|
|StatusString|VT_BSTR|The Device Status String.|
|SymbolicLink|VT_BSTR|Name that you can use to open the device by using the Microsoft Win32 CreateFile method. You cannot use all devices in this way. Most devices that have a programmable interface will have SymbolicLink available.|
|UIFormat|VT_BSTR|String used to display the UINumber value. (SPDRP_UI_NUMBER_DESC_FORMAT)|
|UINumber|VT_I4|UINumber for the device.|
|UpperClassFilters|VT_ARRAY of VARIANT with VT_BSTR|The service names of every driver attached as an upper class filter on the target device.|
|UpperClassFiltersBinaryNames|VT_ARRAY of VARIANT with VT_BSTR|Names of binaries of all upper class filter drivers for device target.|
|UpperFilters|VT_ARRAY of VARIANT with VT_BSTR|The service names of every driver that is attached as an upper filter on the target device.|
|UpperFiltersBinaryNames|VT_ARRAY of VARIANT with VT_BSTR|Names of all upper filter drivers for device target|

## Root Keywords for a System Target

The following table describes the attributes in the root namespace that are valid only for system-type targets.

|Keyword|VARIANT type|Description|
|----|----|----|
|IsPhantom|VT_BOOL|Specifies whether the system is currently available for use.|
|IsRemote|VT_BOOL|Specifies whether the target is a remote system.|
|PageSize|VT_I4|Page size of the target system hardware.|
|ProcArch|VT_BSTR|Processor architecture of the target system hardware. This field can contain "x86", "IA64", or "x64".|
|OSMajorVersion|VT_I4|Specifies the major version number of the operating system.|
|OSMinorVersion|VT_I4|Specifies the minor version number of the operating system.|

## Disk Namespace Keywords

The following table describes the attributes in the Disk namespace that are valid only for disk devices.

>[!NOTE]
>Most of the attributes in the Disk namespace are retrieved from the operating system through an IOCTL to the disk itself. For more information, see [STORAGE_DEVICE_DESCRIPTOR](/windows-hardware/drivers/ddi/ntddstor/ns-ntddstor-_storage_device_descriptor).

|Keyword|VARIANT type|Description|
|----|----|----|
|BusType|VT_I4|STORAGE_DEVICE_DESCRIPTOR.BusType field.|
|DeviceType|VT_I4|STORAGE_DEVICE_DESCRIPTOR.DeviceTypeModifier field.|
|IsRemovable|VT_BOOL|Specifies whether the device contains removable media.|
|IsCommandQueuing|VT_BOOL|STORAGE_DEVICE_DESCRIPTOR.CommandQueueing field.|
|Number|VT_UI4|Disk number (likely the same as the Address field).|
|ProductID|VT_BSTR|Product identifier.|
|ProductRev|VT_BSTR|Product revision value.|
|SerialNumber|VT_BSTR|Serial number.|
|Size|VT_I8|Total size of the disk, in bytes.|
|VendorID|VT_BSTR|Vendor identifier.|

## Volume Namespace Keywords

The following table describes the attributes in the Volume namespace that are valid only for volume devices.

|Keyword|VARIANT Type|Description|
|----|----|----|
|Boot|VT_BOOL|Determines if the volume is the boot partition. A value of VARIANT_TRUE indicates that the volume is the boot partition. A boot partition is a partition that contains Windows operating system files.|
|DeviceName|VT_BSTR|The current mapping for this Volume's MS-DOS device name.|
|Disk|VT_BSTR|The current mapping for this Volume's MS-DOS device name.|
|DriveLetter|VT_BSTR|Drive letter of the volume, including a trailing slash (\\).|
|ExtentCount|VT_I4|The number of disks that the volume extends across.|
|ExtentDiskNumbers|VT_ARRAY of VARIANT with VT_I4|An array containing each of the Disk::Number values that the volume extends across. The array has ExtentCount elements, and is 0-indexed. The array has the same ordering as the other Extent* arrays.|
|ExtentLengths|VT_ARRAY of VARIANT with VT_I8|An array containing the length of each individual extent that the volume extends across. The array has ExtentCount elements, and is 0-indexed. The array has the same ordering as the other Extent* arrays.|
|ExtentOffsets|VT_ARRAY of VARIANT with VT_I8|An array containing the starting offset of each individual extent that the volume extends across. The array has ExtentCount elements, and is 0-indexed. The array has the same ordering as the other Extent* arrays.|
|FileSystem|VT_BSTR|The name of the volume's file system. (GetVolumeInformation)|
|FreeSize|VT_I8|Total amount of free space on the volume, in bytes.|
|GBFreeSize|VT_I4|e total number of free gigabytes (GB) on a disk that are available to the user.|
|GBTotalSize|VT_I4|The total number of gigabytes (GB) on a volume that are available to the user.|
|HasFiles|VT_BOOL|Determines if the volume has files on it. A value of VARIANT_TRUE indicates the volume has files on it.|
|IsMediaPresent|VT_BOOL|Determines if media is present or not for the volume. A value of VARIANT_TRUE indicates the volume has media on it.|
|IsMediaRemovable|VT_BOOL|Determines if volume media is removable. A value of VARIANT_TRUE indicates the volume media is removable.|
|Label|VT_BSTR|The Volume Label. (GetVolumeInformation)|
|MBFreeSize|VT_I8|The total number of free megabytes (MB) on a disk that are available to the user.|
|MBTotalSize|VT_I8|The total number of megabytes (MB) on a volume that are available to the user. (GetDiskFreeSpaceEx)|
|MountPaths|VT_BSTR|All mount paths to this volume.|
|PagePath|VT_BOOL|Determines if the volume contains an active page file. A value of VARIANT_TRUE indicates that the volume contains an active page file.|
|SerialNumber|VT_I4|Serial number of the volume.|
|System|VT_BOOL|Determines if the volume is the system partition. A value of VARIANT_TRUE indicates that the volume contains the Windows system partition. The system partition contains the hardware-related files (bootable code) that starts the Windows Boot Manager (bootmgr).|
|TotalSize|VT_I8|Total size of the volume, in bytes.|
|Type|VT_I4|Value returned from GetDriveType(DriveLetter). For more information, see GetDriveType in the MSDN Library.|

## Power Namespace Keywords

The following table describes the attributes in the Power namespace that are valid only for power devices.

|Keyword|VARIANT Type|Description|
|----|----|----|
|SupportedDeviceUnits|VT_ARRAY of VARIANT with VT_BSTR|Array of PowerUnit namespaces available for query.|

## PowerDevice, PowerComponentX, PowerProcessor, and PowerSoC Namespace Keywords

The following table describes the attributes in the various PowerUnit namespaces.

|Keyword|VARIANT Type|Description|
|----|----|----|
|SupportedStates|VT_ARRAY of VARIANT with VT_BSTR|Array of namespaces for power states (C0–C6, D0–D3, F0–F9, SWIS0–SWIS3)|
|CoveredStates|VT_ARRAY of VARIANT with VT_BSTR|Array of namespaces for covered states. Only states that have a non-zero hit count are included|

## PowerProcessorCX, PowerDeviceDX, PowerComponentXFY, PowerSoCSWISX Namespace Keywords

The following table describes the attributes in the various PowerState namespaces.

|Keyword|VARIANT Type|Description|
|----|----|----|
|HitCount|VT_UI4|The number of times the given power state was entered during the test.|
|Duration|VT_UI4|The period of time in milliseconds spent in the given power state.|
|Percentage|VT_UI4|he percentage of time spent in the given power state.|

## Interface Namespace Keywords

The following table describes the attributes in the various Interfaces namespaces.

|Keyword|VARIANT Type|Description|
|----|----|----|
|All|VT_BSTR|All the device interfaces for all the device interface GUID a single device supports.|
|VOLUME|VT_BSTR|Interfaces for the GUID_DEVINTERFACE_VOLUME GUID.|
|DISK|VT_BSTR|Interfaces for the GUID_DEVINTERFACE_DISK GUID.|
|CDROM|VT_BSTR|Interfaces for the GUID_DEVINTERFACE_CDROM GUID.|
|GUID|VT_BSTR|Interfaces for a single interface GUID.|

## CAP Namespace Keywords

The following table describes the attributes in the various CAP (Capabilities) namespaces.

|Keyword|VARIANT Type|Description|
|----|----|----|
|LockSupported|VT_BOOL|Specifies whether the device supports physical-device locking that prevents device ejection. (CM_DEVCAP_LOCKSUPPORTED)|
|EjectSupported|VT_BOOL|Specifies whether the device supports software-controlled device ejection while the system is in the PowerSystemWorking state. (CM_DEVCAP_EJECTSUPPORTED)|
|Removable|VT_BOOL|Specifies whether the device can be dynamically removed from its immediate parent. (CM_DEVCAP_REMOVABLE)|
|DockDevice|VT_BOOL|Specifies whether the device is a docking peripheral. (CM_DEVCAP_DOCKDEVICE)|
|UniqueId|VT_BOOL|Specifies whether the device's instance ID is unique system-wide. (CM_DEVCAP_UNIQUEID)|
|SilentInstall|VT_BOOL|Specifies whether Device Manager should suppress all installation dialog boxes. (CM_DEVCAP_SILENTINSTALL)|
|RawDeviceOK|VT_BOOL|Specifies whether the driver for the underlying bus can drive the device if there is no function driver. (CM_DEVCAP_RAWDEVICEOK)|
|SurpriseRemovalOK|VT_BOOL|Specifies whether the function driver for the device can handle the case where the device is removed before Windows can send IRP_MN_QUERY_REMOVE_DEVICE to it. (CM_DEVCAP_SURPRISEREMOVALOK)|
|HardwareDisabled|VT_BOOL|Specifies if the device's hardware is disabled. (CM_DEVCAP_HARDWAREDISABLED)|
|NonDynamic|VT_BOOL|Reserved for future use. (CM_DEVCAP_NONDYNAMIC)|

## INF Namespace Keywords

The following table describes the attributes in the various INF namespaces.

|Keyword|VARIANT Type|Description|
|----|----|----|
|FileName|VT_BSTR|INF file name.|
|FileNamePath|VT_BSTR|INF file name path.|
|SectionName|VT_BSTR|INF section name.|
|Date|VT_BSTR|INF date.|
|OriginalInfFileName|VT_BSTR|Original INF file name.|

## NET Namespace Keywords

The following table describes the attributes in the various NET namespaces.

|Keyword|VARIANT Type|Description|
|----|----|----|
|AdapterName|VT_BSTR|AdapterName field from IP_ADAPTER_ADDRESSES structure.|
|IPV6Address|VT_BSTR|FirstUnicastAddress field from IP_ADAPTER_ADDRESSES structure.|
|FirstAnycastAddress|VT_BSTR|FirstAnycastAddress field from IP_ADAPTER_ADDRESSES structure.|
|FirstMulticastAddress|VT_BSTR|FirstMulticastAddress field from IP_ADAPTER_ADDRESSES structure.|
|FirstDnsServerAddress|VT_BSTR|FirstDnsServerAddress field from IP_ADAPTER_ADDRESSES structure.|
|FirstPrefix|VT_BSTR|FirstPrefix field from IP_ADAPTER_ADDRESSES structure.|
|PrimaryWINSServer|VT_BSTR|FirstWinsServerAddress field from IP_ADAPTER_ADDRESSES structure.|
|FirstGatewayAddress|VT_BSTR|FirstGatewayAddress field from IP_ADAPTER_ADDRESSES structure.|
|ConnectionSpecificDNSSuffix|VT_BSTR|DnsSuffix field from IP_ADAPTER_ADDRESSES structure|
|Description|VT_BSTR|Description field from IP_ADAPTER_ADDRESSES structure.|
|FriendlyName|VT_BSTR|FriendlyName field from IP_ADAPTER_ADDRESSES structure.|
|PhysicalAddress|VT_BSTR|MacAddress field from IP_ADAPTER_ADDRESSES structure|
|Flags|VT_UI4|Flags field from IP_ADAPTER_ADDRESSES structure|
|Mtu|VT_UI4|Mtu field from IP_ADAPTER_ADDRESSES structure.|
|IfType|VT_UI4|IfType field from IP_ADAPTER_ADDRESSES structure.|
|OperStatus|VT_UI4|OperStatus field from IP_ADAPTER_ADDRESSES structure|
|OperationalStatusString|VT_BSTR|String equivalent of OperStatus field from IP_ADAPTER_ADDRESSES structure|
|Ipv6IfIndex|VT_UI4|Ipv6IfIndex field from IP_ADAPTER_ADDRESSES structure|
|TransmitLinkSpeedMbps|VT_UI4|TransmitLinkSpeedGpbs field from IP_ADAPTER_ADDRESSES structure.|
|ReceiveLinkSpeedMbps|VT_UI4|ReceiveLinkSpeedMbps field from IP_ADAPTER_ADDRESSES structure.|
|Ipv4Metric|VT_UI4|Ipv4Metric field from IP_ADAPTER_ADDRESSES structure.|
|Ipv6Metric|VT_UI4|Ipv6Metric field from IP_ADAPTER_ADDRESSES structure.|
|DHCPServer|VT_BSTR|Dhcpv4Server field from IP_ADAPTER_ADDRESSES structure.|
|CompartmentId|VT_UI4|CompartmentId field from IP_ADAPTER_ADDRESSES structure.|
|NetworkGuid|VT_BSTR|NetworkGuid field from IP_ADAPTER_ADDRESSES structure.|
|ConnectionType|VT_UI4|ConnectionType field from IP_ADAPTER_ADDRESSES structure.|
|TunnelType|VT_UI4|TunnelType field from IP_ADAPTER_ADDRESSES structure.|
|Dhcpv6ClientDuidLength|VT_UI4|Dhcpv6ClientDuidLength field from IP_ADAPTER_ADDRESSES structure.|
|Dhcpv6Iaid|VT_UI4|Dhcpv6Iaid field from IP_ADAPTER_ADDRESSES structure.|
|IsOperational|VT_BOOL|Is Operational.|
|PhysicalMediaType|VT_UI4|Physical media type of the network device.|
|MediaType|VT_UI4|Physical media type of the network device.|

## OpticalMedia Namespace Keywords

The following table describes the attributes in the various OpticalMedia namespaces.

|Keyword|VARIANT Type|Description|
|----|----|----|
|IsMediaPresent|VT_BOOL|If media is present or not in the optical media device.|
|Type|VT_UI4|The current profile type number as returned in GET_CONFIGURATION_HEADER from IOCTL_CDROM_GET_CONFIGURATION.|
|ClassTypeString|VT_BSTR|Type of optical media class.|
|TypeString|VT_BSTR|Type of optical media.|

## StorageMedia Namespace Keywords

The following table describes the attributes in the various StorageMedia namespaces.

|Keyword|VARIANT Type|Description|
|----|----|----|
|DeviceType|VT_UI4|Specifies one of the system-defined FILE_DEVICE_XXX constants indicating the type of device.|
|DeviceTypeString|VT_BSTR|The Device Type associated String.|
|Count|VT_UI4|Contains the number of DEVICE_MEDIA_INFO structures in MediaInfo.|
|SupportedTypes|VT_UI4|Specifies all MEDIA_TYPE or STORAGE_MEDIA_TYPE values that indicates the type of removable disk.|
|Valid|VT_BOOL|If the gatherer for this device has valid data.|

## Windows Namespace Keywords

The following table describes the attributes in the various Windows namespaces.

|Keyword|VARIANT Type|Description|
|----|----|----|
|IsDriverVerifierEnabled|VT_BOOL|True or False to indicate if Driver Verifier is enabled with at least standard settings against all drivers of this device.|
|IsKernelDebugDevice|VT_BOOL|True or False to indicate if this device is in use by the kernel debugger.|
