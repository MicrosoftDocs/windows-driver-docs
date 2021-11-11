---
title: Registry Entries for StorPort Miniport Drivers
description: StorPort defines a set of registry entries to configure the behavior of StorPort and miniport operations.
ms.date: 10/27/2021
ms.localizationpriority: medium
---

# Registry Entries for StorPort Miniport Drivers

StorPort defines a set of registry entries to configure the behavior of StorPort and miniport operations. Values are set in the scope of the miniport driver or per instance.

## Service Entries

Registry entries for the miniport are keyed by the *\\Parameters* subkey and the *\\Parameters\\Device* subkey of the miniport's services key. For individual adapter entries, the subkey is extended to include the adapter index, such as *\\Parameters\\Device1*.

### Name: DriverParameter

* Type: Any
* Path:
  * Miniport scope: HKLM\System\CurrentControlSet\Services\<*miniport name*>\Parameters\Device
  * Adapter scope: HKLM\System\CurrentControlSet\Services\<*miniport name*>\Parameters\Device<*adapter#*>
* Value : Any miniport specific data.
* Description: Storport retrieves this registry data, and passes the buffer to the miniport as **Parameter** when it calls the miniport’s [**HwStorFindAdapter**](/windows-hardware/drivers/ddi/storport/nc-storport-hw_find_adapter)
* Applies: Starting with Windows Server 2003.

### Name: LinkDownTimeoutValue

* Type: REG_DWORD
* Path:
  * Miniport scope: HKLM\System\CurrentControlSet\Services<*miniport name*>\Parameters\Device<
  * Adapter scope: HKLM\System\CurrentControlSet\Services<*miniport name*>\Parameters\Device<*adapter#*>
* Value:
  * Default: 30
  * Maximum: 600
  * Units: seconds
* Description: This value is used by miniport driver to inform Storport, after the link goes down, how long StorPort should wait before restarting I/O to the miniport driver.
* Applies: Starting with Windows Server 2003.

### Name: MaximumLogicalUnit

* Type: REG_DWORD
* Path:
  * Miniport scope: HKLM\System\CurrentControlSet\Services\<*miniport name*>\Parameters\Device
  * Adapter scope: HKLM\System\CurrentControlSet\Services\<*miniport name*>\Parameters\Device<*adapter#*>
* Value:
  * Default: 255
  * Maximum: 8 when set in the registry
* Description: This value sets the maximum number of logical units (LUN) for a target device.
* Applies: Starting with Windows Server 2003.

### Name: MaximumUCXAddress

* Type: REG_BINARY
* Path:
  * Miniport scope: HKLM\System\CurrentControlSet\Services\<*miniport name*>\Parameters\Device
  * Adapter scope: HKLM\System\CurrentControlSet\Services\<*miniport name*>\Parameters\Device<*adapter#*>
* Value:
  * Default: 0xffffffff
  * When 0, StorPort uses the default value.
* Description: This value sets the maximum address value of an uncached extension.
* Applies: Starting with Windows Server 2003.

### Name: MinimumUCXAddress

* Type: REG_BINARY
* Path:
  * Miniport scope: HKLM\System\CurrentControlSet\Services\<*miniport name*>\Parameters\Device
  * Adapter scope: HKLM\System\CurrentControlSet\Services\<*miniport name*>\Parameters\Device<*adapter#*>
* Value:
  * Default: 0x00000000
  * When MinimumUCXAddress >= MaximumUCXAddress - PAGE_SIZE, StorPort uses the default value.
* Description: This value sets the minimum address value of an uncached extension.
* Applies: Starting with Windows Server 2003.

### Name: UncachedExtAlignment

* Type: REG_DWORD
* Path:
  * Miniport scope: HKLM\System\CurrentControlSet\Services\<*miniport name*>\Parameters\Device
  * Adapter scope: HKLM\System\CurrentControlSet\Services\<*miniport name*>\Parameters\Device<*adapter#*>
* Value:
  * Default: 0
  * Minimum: 3
  * Maximum: 16
* Description: StorPort uses this value to calculate a base 2 exponent (e.g. 1 << value) to use as an alignment value for the uncached extension buffer allocation.
* Applies: Starting with Windows Server 2003.

### Name: NumberOfRequests

* Type: REG_DWORD
* Path:
  * Miniport scope: HKLM\System\CurrentControlSet\Services\<*miniport name*>\Parameters\Device
  * Adapter scope: HKLM\System\CurrentControlSet\Services\<*miniport name*>\Parameters\Device<*adapter#*>
* Value:
  * Default: 1000
  * Minimum: 16
  * Maximum: 255
* Description: The number or requests that an adapter can process. When set, the range is smaller than the default.

### Name: BusType

* Type: REG_DWORD
* Path:
  * Miniport scope: HKLM\System\CurrentControlSet\Services<*miniport name*>\Parameters
* Value:
  * Default: 6, **BusTypeFiber**
  * Maximum: 0x7f, any value greater is treated as the default
* Description: This value is used to indicate the bus type for the adapters that the miniport driver manages. The value corresponds to the **STORAGE_BUS_TYPE** bus enumeration type.
* Applies: Starting with Windows Server 2003.

### Name: IoTimeoutValue

* Type: REG_DWORD
* Path:
  * Miniport scope: HKLM\System\CurrentControlSet\Services<*miniport name*>\Parameters
* Value:
  * Minimum: 0
  * Maximum: 65535
  * Units: seconds
* Description: Indicates the I/O timeout value for devices managed by the miniport driver. If this registry value doesn’t exist, the system will use the global disk I/O timeout value.
* Applies: Starting with Windows 8.

### Name: IoLatencyCap

* Type: REG_DWORD
* Path:
  * Miniport scope: HKLM\System\CurrentControlSet\Services<*miniport name*>\Parameters
* Value:
  * Default: 0
  * Units: milliseconds
* Description: If this registry value is > 0, StorPort will hold incoming I/O requests in the queue when any I/O request sent to miniport driver has not been completed in the period of time specified.
* Applies: Starting with Windows 8.

## Device Enumeration Entries

### Name: TotalSenseDataBytes

* Type: REG_DWORD
* Path:
  * Adapter scope: HKLM\System\CurrentControlSet\Enum<*instance path*>\Device Parameters\StorPort
* Value:
  * Default: 255
  * Minimum: 18
  * Maximum: 255
  * Units: bytes
* Description: Indicates the **Sense Data** size that the miniport driver returns to StorPort.
* Applies: Starting with Windows Server 2003.

### Name: QueueFullWaitIoPercentage

* Type: REG_DWORD
* Path:
  * Logical unit scope: HKLM\CurrentControlSet\Enum\SCSI<*HardwareId*><*InstanceId*>\Device Parameters\StorPort
* Value:
  * Default: 25
  * Maximum: 100
  * Units: Percentage of queue depth
* Description: When the miniport reports device-busy by setting **SCSISTAT_QUEUE_FULL** in **ScsiStatus** of a **SRB**, StorPort pauses the logical unit queue and waits until a certain amount I/O requests are completed by the miniport before sending any further requests. The amount of I/O requests StorPort waits on is calculated using this registry value relative to the count of I/O requests currently sent to the miniport.
* Applies: Starting with Windows Server 2003.

### Name: BusyPauseTime

* Type: REG_DWORD
* Path:
  * Logical unit scope: HKLM\CurrentControlSet\Enum\SCSI<*HardwareId*><*InstanceId*>\Device Parameters\StorPort
* Value:
  * Default: 250
  * Units: milliseconds
* Description: When the miniport reports device-busy by setting **SRB_STATUS_BUSY** in the **SrbStatus** of a **SRB**, StorPort pauses the unit queue and waits for the specified amount time before starting sending I/O requests again.
* Applies: Starting with Windows Server 2003.

### Name: BusyRetryCount

* Type: REG_DWORD
* Path:
  * Logical unit scope: HKLM\CurrentControlSet\Enum\SCSI<*HardwareId*><*InstanceId*>\Device Parameters\StorPort
* Value:
  * Default: 20
* Description: The retry for StorPort to reissue an **Srb** when the miniport reports device busy or link down.
* Applies: Starting with Windows Server 2003.

### Name: EnableIdlePowerManagement

* Type: REG_DWORD
* Path:
  * Adapter scope: HKLM\System\CurrentControlSet\Enum<*instance path*>\Device Parameters\StorPort
* Value:
  * Default: 0, disabled
* Description: If this registry value is > 0, then idle power management is enabled. The idle power management is for logical units connected to the adapter.
* Applies: Starting with Windows 7.

### Name: DisableIdlePowerManagement

* Type: REG_DWORD
* Path:
  * Logical unit scope: HKLM\CurrentControlSet\Enum\SCSI<*HardwareId*><*InstanceId*>\Device Parameters\StorPort
* Value:
  * Default: 0, enabled
* Description: If this registry value is > 0, then idle power management is disabled for this logical unit.
* Applies: Starting with Windows 8.

### Name: MinimumIdleTimeoutInMS

* Type: REG_DWORD
* Path:
  * Logical unit scope: HKLM\CurrentControlSet\Enum\SCSI<*HardwareId*><*InstanceId*>\Device Parameters\StorPort
* Value:
  * Default: MAXULONG, indicating unset. If the miniport provides no timeout value, the actual default value is 5 \* 60 \* 1000, which is 5 minutes.
  * Units: milliseconds
* Description: This value specifies the minimum amount of time the power framework must wait to power down a logical unit once it is at idle.
* Applies: Starting with Windows 8.

### Name: DisableRuntimePowerManagement

* Type: REG_DWORD
* Path</td>
  * Adapter scope: HKLM\System\CurrentControlSet\Enum<*instance path*>\Device Parameters\StorPort
* Value:
  * Default: 0, enabled
* Description: If the value > 0, then runtime power management for adapter is disabled. This disables runtime power management for specific adapter. NOTE: Runtime power management for devices attached to this adapter is not affected.
* Applies: Starting with Windows 8.

### Name: IdleTimeoutInMS

* Type: REG_DWORD
* Path</td>
  * Adapter scope: HKLM\System\CurrentControlSet\Enum<*instance path*>\Device Parameters\StorPort
* Value:
  * Default: 60
  * Units: seconds
* Description: Specifies the time that runtime power framework needs to wait before powering down an idle adapter.
* Applies: Starting with Windows 8.

### Name: DisableD3Cold

* Type: REG_DWORD
* Path</td>
  * Adapter scope: HKLM\System\CurrentControlSet\Enum<*instance path*>\Device Parameters\StorPort
* Value:
  * Default: enabled (when D3Cold is supported)
* Description: If the value > 0, then D3Cold support for the adapter is disabled.
* Applies: Starting with Windows 8.
