---
title: Registry Entries for StorPort Miniport Drivers
description: StorPort defines a set of registry entries to configure the behavior of StorPort and miniport operations.
ms.assetid: 543EC6A4-113C-4525-8063-28854B50760E
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# Registry Entries for StorPort Miniport Drivers


StorPort defines a set of registry entries to configure the behavior of StorPort and miniport operations. Values are set in the scope of the miniport driver or per instance.

## <span id="Service_Entries"></span><span id="service_entries"></span><span id="SERVICE_ENTRIES"></span>Service Entries


Registry entries for the miniport are keyed by the *\\Parameters* subkey and the *\\Parameters\\Device* subkey of the miniport's services key. For individual adapter entries, the subkey is extended to include the adapter index, such as *\\Parameters\\Device1*.

<table>
<colgroup>
<col width="50%" />
<col width="50%" />
</colgroup>
<tbody>
<tr class="odd">
<td align="left">Name</td>
<td align="left"><strong>DriverParameter</strong></td>
</tr>
<tr class="even">
<td align="left">Type</td>
<td align="left">Any</td>
</tr>
<tr class="odd">
<td align="left">Path</td>
<td align="left"><p>Miniport scope:</p>
<p>HKLM\System\CurrentControlSet\Services&amp;lt;miniport name&gt;\Parameters\Device</p>
<p>Adapter scope:</p>
<p>HKLM\System\CurrentControlSet\Services&amp;lt;miniport name&gt;\Parameters\Device&lt;adapter#&gt;</p></td>
</tr>
<tr class="even">
<td align="left">Value</td>
<td align="left"><p>Any miniport specific data.</p></td>
</tr>
<tr class="odd">
<td align="left">Description</td>
<td align="left"><p>Storport retrieves this registry data, and passes the buffer to the miniport as <em>Parameter</em> when it calls the miniport’s <a href="https://msdn.microsoft.com/library/windows/hardware/ff557390" data-raw-source="[&lt;strong&gt;HwStorFindAdapter&lt;/strong&gt;](https://msdn.microsoft.com/library/windows/hardware/ff557390)"><strong>HwStorFindAdapter</strong></a> routine.</p></td>
</tr>
<tr class="even">
<td align="left">Applies</td>
<td align="left"><p>Starting with Windows Server 2003.</p></td>
</tr>
</tbody>
</table>

 

<table>
<colgroup>
<col width="50%" />
<col width="50%" />
</colgroup>
<tbody>
<tr class="odd">
<td align="left">Name</td>
<td align="left"><strong>LinkDownTimeoutValue</strong></td>
</tr>
<tr class="even">
<td align="left">Type</td>
<td align="left">REG_DWORD</td>
</tr>
<tr class="odd">
<td align="left">Path</td>
<td align="left"><p>Miniport scope:</p>
<p>HKLM\System\CurrentControlSet\Services&amp;lt;miniport name&gt;\Parameters\Device</p>
<p>Adapter scope:</p>
<p>HKLM\System\CurrentControlSet\Services&amp;lt;miniport name&gt;\Parameters\Device&lt;adapter#&gt;</p></td>
</tr>
<tr class="even">
<td align="left">Value</td>
<td align="left"><p>Default: 30</p>
<p>Maximum: 600</p>
<p>Units: seconds</p></td>
</tr>
<tr class="odd">
<td align="left">Description</td>
<td align="left"><p>This value is used by miniport driver to inform Storport, after the link goes down, how long StorPort should wait before restarting I/O to the miniport driver.</p></td>
</tr>
<tr class="even">
<td align="left">Applies</td>
<td align="left"><p>Starting with Windows Server 2003.</p></td>
</tr>
</tbody>
</table>

 

<table>
<colgroup>
<col width="50%" />
<col width="50%" />
</colgroup>
<tbody>
<tr class="odd">
<td align="left">Name</td>
<td align="left"><strong>MaximumLogicalUnit</strong></td>
</tr>
<tr class="even">
<td align="left">Type</td>
<td align="left">REG_DWORD</td>
</tr>
<tr class="odd">
<td align="left">Path</td>
<td align="left"><p>Miniport scope:</p>
<p>HKLM\System\CurrentControlSet\Services&amp;lt;miniport name&gt;\Parameters\Device</p>
<p>Adapter scope:</p>
<p>HKLM\System\CurrentControlSet\Services&amp;lt;miniport name&gt;\Parameters\Device&lt;adapter#&gt;</p></td>
</tr>
<tr class="even">
<td align="left">Value</td>
<td align="left"><p>Default: 255</p>
<p>Maximum: 8 when set in the registry</p></td>
</tr>
<tr class="odd">
<td align="left">Description</td>
<td align="left"><p>This value sets the maximum number of logical units (LUN) for a target device.</p></td>
</tr>
<tr class="even">
<td align="left">Applies</td>
<td align="left"><p>Starting with Windows Server 2003.</p></td>
</tr>
</tbody>
</table>

 

<table>
<colgroup>
<col width="50%" />
<col width="50%" />
</colgroup>
<tbody>
<tr class="odd">
<td align="left">Name</td>
<td align="left"><strong>MaximumUCXAddress</strong></td>
</tr>
<tr class="even">
<td align="left">Type</td>
<td align="left">REG_BINARY</td>
</tr>
<tr class="odd">
<td align="left">Path</td>
<td align="left"><p>Miniport scope:</p>
<p>HKLM\System\CurrentControlSet\Services&amp;lt;miniport name&gt;\Parameters\Device</p>
<p>Adapter scope:</p>
<p>HKLM\System\CurrentControlSet\Services&amp;lt;miniport name&gt;\Parameters\Device&lt;adapter#&gt;</p></td>
</tr>
<tr class="even">
<td align="left">Value</td>
<td align="left"><p>Default: 0xffffffff</p>
<p>When 0, StorPort uses the default value</p></td>
</tr>
<tr class="odd">
<td align="left">Description</td>
<td align="left"><p>This value sets the maximum address value of an uncached extension.</p></td>
</tr>
<tr class="even">
<td align="left">Applies</td>
<td align="left"><p>Starting with Windows Server 2003.</p></td>
</tr>
</tbody>
</table>

 

<table>
<colgroup>
<col width="50%" />
<col width="50%" />
</colgroup>
<tbody>
<tr class="odd">
<td align="left">Name</td>
<td align="left"><strong>MinimumUCXAddress</strong></td>
</tr>
<tr class="even">
<td align="left">Type</td>
<td align="left">REG_BINARY</td>
</tr>
<tr class="odd">
<td align="left">Path</td>
<td align="left"><p>Miniport scope:</p>
<p>HKLM\System\CurrentControlSet\Services&amp;lt;miniport name&gt;\Parameters\Device</p>
<p>Adapter scope:</p>
<p>HKLM\System\CurrentControlSet\Services&amp;lt;miniport name&gt;\Parameters\Device&lt;adapter#&gt;</p></td>
</tr>
<tr class="even">
<td align="left">Value</td>
<td align="left"><p>Default: 0x00000000</p>
<p>When MinimumUCXAddress &gt;= MaximumUCXAddress - PAGE_SIZE, StorPort uses the default value.</p></td>
</tr>
<tr class="odd">
<td align="left">Description</td>
<td align="left"><p>This value sets the minimum address value of an uncached extension.</p></td>
</tr>
<tr class="even">
<td align="left">Applies</td>
<td align="left"><p>Starting with Windows Server 2003.</p></td>
</tr>
</tbody>
</table>

 

<table>
<colgroup>
<col width="50%" />
<col width="50%" />
</colgroup>
<tbody>
<tr class="odd">
<td align="left">Name</td>
<td align="left"><strong>UncachedExtAlignment</strong></td>
</tr>
<tr class="even">
<td align="left">Type</td>
<td align="left">REG_DWORD</td>
</tr>
<tr class="odd">
<td align="left">Path</td>
<td align="left"><p>Miniport scope:</p>
<p>HKLM\System\CurrentControlSet\Services&amp;lt;miniport name&gt;\Parameters\Device</p>
<p>Adapter scope:</p>
<p>HKLM\System\CurrentControlSet\Services&amp;lt;miniport name&gt;\Parameters\Device&lt;adapter#&gt;</p></td>
</tr>
<tr class="even">
<td align="left">Value</td>
<td align="left"><p>Default: 0</p>
<p>Minimum: 3</p>
<p>Maximum: 16</p></td>
</tr>
<tr class="odd">
<td align="left">Description</td>
<td align="left"><p>StorPort uses this value to calculate a base 2 exponent (e.g. 1 &lt;&lt; value) to use as an alignment value for the uncached extension buffer allocation.</p></td>
</tr>
<tr class="even">
<td align="left">Applies</td>
<td align="left"><p>Starting with Windows Server 2003.</p></td>
</tr>
</tbody>
</table>

 

<table>
<colgroup>
<col width="50%" />
<col width="50%" />
</colgroup>
<tbody>
<tr class="odd">
<td align="left">Name</td>
<td align="left"><strong>NumberOfRequests</strong></td>
</tr>
<tr class="even">
<td align="left">Type</td>
<td align="left">REG_DWORD</td>
</tr>
<tr class="odd">
<td align="left">Path</td>
<td align="left"><p>Miniport scope:</p>
<p>HKLM\System\CurrentControlSet\Services&amp;lt;miniport name&gt;\Parameters\Device</p>
<p>Adapter scope:</p>
<p>HKLM\System\CurrentControlSet\Services&amp;lt;miniport name&gt;\Parameters\Device&lt;adapter#&gt;</p></td>
</tr>
<tr class="even">
<td align="left">Value</td>
<td align="left"><p>Default: 1000</p>
<p>Minimum: 16</p>
<p>Maximum: 255</p></td>
</tr>
<tr class="odd">
<td align="left">Description</td>
<td align="left"><p>The number or requests that an adapter can process. When set, the range is smaller than the default.</p></td>
</tr>
</tbody>
</table>

 

<table>
<colgroup>
<col width="50%" />
<col width="50%" />
</colgroup>
<tbody>
<tr class="odd">
<td align="left">Name</td>
<td align="left"><strong>BusType</strong></td>
</tr>
<tr class="even">
<td align="left">Type</td>
<td align="left">REG_DWORD</td>
</tr>
<tr class="odd">
<td align="left">Path</td>
<td align="left"><p>Miniport scope:</p>
<p>HKLM\System\CurrentControlSet\Services&amp;lt;miniport name&gt;\Parameters</p></td>
</tr>
<tr class="even">
<td align="left">Value</td>
<td align="left"><p>Default: 6, <strong>BusTypeFiber</strong></p>
<p>Maximum: 0x7f, any value greater is treated as the default.</p></td>
</tr>
<tr class="odd">
<td align="left">Description</td>
<td align="left"><p>This value is used to indicate the bus type for the adapters that the miniport driver manages. The value corresponds to the bus enumeration type: <strong>STORAGE_BUS_TYPE</strong>.</p></td>
</tr>
<tr class="even">
<td align="left">Applies</td>
<td align="left"><p>Starting with Windows Server 2003.</p></td>
</tr>
</tbody>
</table>

 

<table>
<colgroup>
<col width="50%" />
<col width="50%" />
</colgroup>
<tbody>
<tr class="odd">
<td align="left">Name</td>
<td align="left"><strong>IoTimeoutValue</strong></td>
</tr>
<tr class="even">
<td align="left">Type</td>
<td align="left">REG_DWORD</td>
</tr>
<tr class="odd">
<td align="left">Path</td>
<td align="left"><p>Miniport scope:</p>
<p>HKLM\System\CurrentControlSet\Services&amp;lt;miniport name&gt;\Parameters</p></td>
</tr>
<tr class="even">
<td align="left">Value</td>
<td align="left"><p>Minimum: 0</p>
<p>Maximum: 65535</p>
<p>Units: seconds</p></td>
</tr>
<tr class="odd">
<td align="left">Description</td>
<td align="left"><p>Indicates the I/O timeout value for devices managed by the miniport driver. If this registry value doesn’t exist, the system will use the global disk I/O timeout value.</p></td>
</tr>
<tr class="even">
<td align="left">Applies</td>
<td align="left"><p>Starting with Windows 8.</p></td>
</tr>
</tbody>
</table>

 

<table>
<colgroup>
<col width="50%" />
<col width="50%" />
</colgroup>
<tbody>
<tr class="odd">
<td align="left">Name</td>
<td align="left"><strong>IoLatencyCap</strong></td>
</tr>
<tr class="even">
<td align="left">Type</td>
<td align="left">REG_DWORD</td>
</tr>
<tr class="odd">
<td align="left">Path</td>
<td align="left"><p>Miniport scope:</p>
<p>HKLM\System\CurrentControlSet\Services&amp;lt;miniport name&gt;\Parameters</p></td>
</tr>
<tr class="even">
<td align="left">Value</td>
<td align="left"><p>Default: 0</p>
<p>Units: milliseconds</p></td>
</tr>
<tr class="odd">
<td align="left">Description</td>
<td align="left"><p>If this registry value is &gt; 0, StorPort will hold incoming I/O requests in the queue when any I/O request sent to miniport driver has not been completed in the period of time specified.</p></td>
</tr>
<tr class="even">
<td align="left">Applies</td>
<td align="left"><p>Starting with Windows 8.</p></td>
</tr>
</tbody>
</table>

 

## <span id="Device_Enumeration_Entries"></span><span id="device_enumeration_entries"></span><span id="DEVICE_ENUMERATION_ENTRIES"></span>Device Enumeration Entries


<table>
<colgroup>
<col width="50%" />
<col width="50%" />
</colgroup>
<tbody>
<tr class="odd">
<td align="left">Name</td>
<td align="left"><strong>TotalSenseDataBytes</strong></td>
</tr>
<tr class="even">
<td align="left">Type</td>
<td align="left">REG_DWORD</td>
</tr>
<tr class="odd">
<td align="left">Path</td>
<td align="left"><p>Adapter scope:</p>
<p>HKLM\System\CurrentControlSet\Enum&amp;lt;instance path&gt;\Device Parameters\StorPort</p></td>
</tr>
<tr class="even">
<td align="left">Value</td>
<td align="left"><p>Default: 255</p>
<p>Minimum: 18</p>
<p>Maximum: 255</p>
<p>Units: bytes</p></td>
</tr>
<tr class="odd">
<td align="left">Description</td>
<td align="left"><p>Indicates the <em>Sense Data</em> size that the miniport driver returns to StorPort.</p></td>
</tr>
<tr class="even">
<td align="left">Applies</td>
<td align="left"><p>Starting with Windows Server 2003.</p></td>
</tr>
</tbody>
</table>

 

<table>
<colgroup>
<col width="50%" />
<col width="50%" />
</colgroup>
<tbody>
<tr class="odd">
<td align="left">Name</td>
<td align="left"><strong>QueueFullWaitIoPercentage</strong></td>
</tr>
<tr class="even">
<td align="left">Type</td>
<td align="left">REG_DWORD</td>
</tr>
<tr class="odd">
<td align="left">Path</td>
<td align="left"><p>Logical unit scope:</p>
<p>HKLM\CurrentControlSet\Enum\SCSI&amp;lt;HardwareId&gt;&amp;lt;InstanceId&gt;\Device Parameters\StorPort</p></td>
</tr>
<tr class="even">
<td align="left">Value</td>
<td align="left"><p>Default: 25</p>
<p>Maximum: 100</p>
<p>Units: Percentage of queue depth</p></td>
</tr>
<tr class="odd">
<td align="left">Description</td>
<td align="left"><p>When miniport reports device-busy by setting <strong>SCSISTAT_QUEUE_FULL</strong> in <strong>ScsiStatus</strong> of a <strong>SRB</strong>, StorPort pauses the logical unit queue and waits until a certain amount I/O requests are completed by the miniport before sending any further requests. The amount of I/O requests StorPort waits on is calculated using this registry value relative to the count of I/O requests currently sent to the miniport.</p></td>
</tr>
<tr class="even">
<td align="left">Applies</td>
<td align="left"><p>Starting with Windows Server 2003.</p></td>
</tr>
</tbody>
</table>

 

<table>
<colgroup>
<col width="50%" />
<col width="50%" />
</colgroup>
<tbody>
<tr class="odd">
<td align="left">Name</td>
<td align="left"><strong>BusyPauseTime</strong></td>
</tr>
<tr class="even">
<td align="left">Type</td>
<td align="left">REG_DWORD</td>
</tr>
<tr class="odd">
<td align="left">Path</td>
<td align="left"><p>Logical unit scope:</p>
<p>HKLM\CurrentControlSet\Enum\SCSI&amp;lt;HardwareId&gt;&amp;lt;InstanceId&gt;\Device Parameters\StorPort</p></td>
</tr>
<tr class="even">
<td align="left">Value</td>
<td align="left"><p>Default: 250</p>
<p>Units: milliseconds</p></td>
</tr>
<tr class="odd">
<td align="left">Description</td>
<td align="left"><p>When the miniport reports device-busy by setting <strong>SRB_STATUS_BUSY</strong> in the <strong>SrbStatus</strong> of a <strong>SRB</strong>, StorPort pauses the unit queue and waits for the specified amount time before starting sending I/O requests again.</p></td>
</tr>
<tr class="even">
<td align="left">Applies</td>
<td align="left"><p>Starting with Windows Server 2003.</p></td>
</tr>
</tbody>
</table>

 

<table>
<colgroup>
<col width="50%" />
<col width="50%" />
</colgroup>
<tbody>
<tr class="odd">
<td align="left">Name</td>
<td align="left"><strong>BusyPauseTime</strong></td>
</tr>
<tr class="even">
<td align="left">Type</td>
<td align="left">REG_DWORD</td>
</tr>
<tr class="odd">
<td align="left">Path</td>
<td align="left"><p>Logical unit scope:</p>
<p>HKLM\CurrentControlSet\Enum\SCSI&amp;lt;HardwareId&gt;&amp;lt;InstanceId&gt;\Device Parameters\StorPort</p></td>
</tr>
<tr class="even">
<td align="left">Value</td>
<td align="left"><p>Default: 250</p>
<p>Units: milliseconds</p></td>
</tr>
<tr class="odd">
<td align="left">Description</td>
<td align="left"><p>When the miniport reports device-busy by setting <strong>SRB_STATUS_BUSY</strong> in the <strong>SrbStatus</strong> of a <strong>SRB</strong>, StorPort pauses the logical unit queue and waits for the specified amount time before starting sending I/O requests again.</p></td>
</tr>
<tr class="even">
<td align="left">Applies</td>
<td align="left"><p>Starting with Windows Server 2003.</p></td>
</tr>
</tbody>
</table>

 

<table>
<colgroup>
<col width="50%" />
<col width="50%" />
</colgroup>
<tbody>
<tr class="odd">
<td align="left">Name</td>
<td align="left"><strong>BusyRetryCount</strong></td>
</tr>
<tr class="even">
<td align="left">Type</td>
<td align="left">REG_DWORD</td>
</tr>
<tr class="odd">
<td align="left">Path</td>
<td align="left"><p>Logical unit scope:</p>
<p>HKLM\CurrentControlSet\Enum\SCSI&amp;lt;HardwareId&gt;&amp;lt;InstanceId&gt;\Device Parameters\StorPort</p></td>
</tr>
<tr class="even">
<td align="left">Value</td>
<td align="left"><p>Default: 10</p></td>
</tr>
<tr class="odd">
<td align="left">Description</td>
<td align="left"><p>The retry for StorPort to reissue an <strong>Srb</strong> when the miniport reports device busy or link down.</p></td>
</tr>
<tr class="even">
<td align="left">Applies</td>
<td align="left"><p>Starting with Windows Server 2003.</p></td>
</tr>
</tbody>
</table>

 

<table>
<colgroup>
<col width="50%" />
<col width="50%" />
</colgroup>
<tbody>
<tr class="odd">
<td align="left">Name</td>
<td align="left"><strong>EnableIdlePowerManagement</strong></td>
</tr>
<tr class="even">
<td align="left">Type</td>
<td align="left">REG_DWORD</td>
</tr>
<tr class="odd">
<td align="left">Path</td>
<td align="left"><p>Adapter scope:</p>
<p>HKLM\System\CurrentControlSet\Enum&amp;lt;instance path&gt;\Device Parameters\StorPort</p></td>
</tr>
<tr class="even">
<td align="left">Value</td>
<td align="left"><p>Default: 0, disabled</p></td>
</tr>
<tr class="odd">
<td align="left">Description</td>
<td align="left"><p>If this registry value is &gt; 0, then idle power management is enabled. The idle power management is for logical units connected to the adapter.</p></td>
</tr>
<tr class="even">
<td align="left">Applies</td>
<td align="left"><p>Starting with Windows 7.</p></td>
</tr>
</tbody>
</table>

 

<table>
<colgroup>
<col width="50%" />
<col width="50%" />
</colgroup>
<tbody>
<tr class="odd">
<td align="left">Name</td>
<td align="left"><strong>DisableIdlePowerManagement</strong></td>
</tr>
<tr class="even">
<td align="left">Type</td>
<td align="left">REG_DWORD</td>
</tr>
<tr class="odd">
<td align="left">Path</td>
<td align="left"><p>Logical unit scope:</p>
<p>HKLM\CurrentControlSet\Enum\SCSI&amp;lt;HardwareId&gt;&amp;lt;InstanceId&gt;\Device Parameters\StorPort</p></td>
</tr>
<tr class="even">
<td align="left">Value</td>
<td align="left"><p>Default: 0, enabled</p></td>
</tr>
<tr class="odd">
<td align="left">Description</td>
<td align="left"><p>If this registry value is &gt; 0, then idle power management is disabled for this logical unit.</p></td>
</tr>
<tr class="even">
<td align="left">Applies</td>
<td align="left"><p>Starting with Windows 8.</p></td>
</tr>
</tbody>
</table>

 

<table>
<colgroup>
<col width="50%" />
<col width="50%" />
</colgroup>
<tbody>
<tr class="odd">
<td align="left">Name</td>
<td align="left"><strong>MinimumIdleTimeoutInMS</strong></td>
</tr>
<tr class="even">
<td align="left">Type</td>
<td align="left">REG_DWORD</td>
</tr>
<tr class="odd">
<td align="left">Path</td>
<td align="left"><p>Logical unit scope:</p>
<p>HKLM\CurrentControlSet\Enum\SCSI&amp;lt;HardwareId&gt;&amp;lt;InstanceId&gt;\Device Parameters\StorPort</p></td>
</tr>
<tr class="even">
<td align="left">Value</td>
<td align="left"><p>Default: MAXULONG, indicating unset. If the miniport provides no timeout value, the actual default value is 5 minutes, or, 5 * 60 * 1000.</p>
<p>Units: milliseconds</p></td>
</tr>
<tr class="odd">
<td align="left">Description</td>
<td align="left"><p>This value specifies the minimum amount of time the power framework must wait to power down a logical unit once it is at idle.</p></td>
</tr>
<tr class="even">
<td align="left">Applies</td>
<td align="left"><p>Starting with Windows 8.</p></td>
</tr>
</tbody>
</table>

 

<table>
<colgroup>
<col width="50%" />
<col width="50%" />
</colgroup>
<tbody>
<tr class="odd">
<td align="left">Name</td>
<td align="left"><strong>DisableRuntimePowerManagement</strong></td>
</tr>
<tr class="even">
<td align="left">Type</td>
<td align="left">REG_DWORD</td>
</tr>
<tr class="odd">
<td align="left">Path</td>
<td align="left"><p>Adapter scope:</p>
<p>HKLM\System\CurrentControlSet\Enum&amp;lt;instance path&gt;\Device Parameters\StorPort</p></td>
</tr>
<tr class="even">
<td align="left">Value</td>
<td align="left"><p>Default: enabled</p></td>
</tr>
<tr class="odd">
<td align="left">Description</td>
<td align="left"><p>If the value &gt; 0, then runtime power management for adapter is disabled. This disables runtime power management for specific adapter.</p>
<div class="alert">
<strong>Note</strong>  Runtime power management for devices attached to this adapter is not affected.
</div>
<div>
 
</div></td>
</tr>
<tr class="even">
<td align="left">Applies</td>
<td align="left"><p>Starting with Windows 8.</p></td>
</tr>
</tbody>
</table>

 

<table>
<colgroup>
<col width="50%" />
<col width="50%" />
</colgroup>
<tbody>
<tr class="odd">
<td align="left">Name</td>
<td align="left"><strong>IdleTimeoutInMS</strong></td>
</tr>
<tr class="even">
<td align="left">Type</td>
<td align="left">REG_DWORD</td>
</tr>
<tr class="odd">
<td align="left">Path</td>
<td align="left"><p>Adapter scope:</p>
<p>HKLM\System\CurrentControlSet\Enum&amp;lt;instance path&gt;\Device Parameters\StorPort</p></td>
</tr>
<tr class="even">
<td align="left">Value</td>
<td align="left"><p>Default: 60</p>
<p>Units: seconds</p></td>
</tr>
<tr class="odd">
<td align="left">Description</td>
<td align="left"><p>Specifies the time that runtime power framework needs to wait before powering down an idle adapter.</p></td>
</tr>
<tr class="even">
<td align="left">Applies</td>
<td align="left"><p>Starting with Windows 8.</p></td>
</tr>
</tbody>
</table>

 

<table>
<colgroup>
<col width="50%" />
<col width="50%" />
</colgroup>
<tbody>
<tr class="odd">
<td align="left">Name</td>
<td align="left"><strong>DisableD3Cold</strong></td>
</tr>
<tr class="even">
<td align="left">Type</td>
<td align="left">REG_DWORD</td>
</tr>
<tr class="odd">
<td align="left">Path</td>
<td align="left"><p>Adapter scope:</p>
<p>HKLM\System\CurrentControlSet\Enum&amp;lt;instance path&gt;\Device Parameters\StorPort</p></td>
</tr>
<tr class="even">
<td align="left">Value</td>
<td align="left"><p>Default: enabled (when D3Cold is supported)</p></td>
</tr>
<tr class="odd">
<td align="left">Description</td>
<td align="left"><p>If the value &gt; 0, then D3Cold support for the adapter is disabled.</p></td>
</tr>
<tr class="even">
<td align="left">Applies</td>
<td align="left"><p>Starting with Windows 8.</p></td>
</tr>
</tbody>
</table>

 

 

 




