---
title: WDM IRPs and WDF Event Callback Functions
author: windows-driver-content
description: WDM IRPs and WDF Event Callback Functions
ms.assetid: 9B9A01FD-AA15-4C30-B19D-2F6451014EAD
---

# WDM IRPs and WDF Event Callback Functions


Kernel-Mode Driver Framework (KMDF) and User-Mode Driver Framework (UMDF) support a subset of Windows IRPs. The following table lists the major WDM IRP types and the corresponding framework event callback functions. Unless otherwise specified, the callbacks apply to both KMDF and UMDF.

<table>
<colgroup>
<col width="50%" />
<col width="50%" />
</colgroup>
<thead>
<tr class="header">
<th align="left">Major IRP code</th>
<th align="left">WDF event callback function</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td align="left">[<strong>IRP_MJ_CLEANUP</strong>](https://msdn.microsoft.com/library/windows/hardware/ff550718)</td>
<td align="left">[<em>EvtFileCleanup</em>](https://msdn.microsoft.com/library/windows/hardware/ff541700)</td>
</tr>
<tr class="even">
<td align="left">[<strong>IRP_MJ_CLOSE</strong>](https://msdn.microsoft.com/library/windows/hardware/ff550720)</td>
<td align="left">[<em>EvtFileClose</em>](https://msdn.microsoft.com/library/windows/hardware/ff541702)</td>
</tr>
<tr class="odd">
<td align="left">[<strong>IRP_MJ_CREATE</strong>](https://msdn.microsoft.com/library/windows/hardware/ff550729)</td>
<td align="left">[<em>EvtDeviceFileCreate</em>](https://msdn.microsoft.com/library/windows/hardware/ff540868) or [<em>EvtIoDefault</em>](https://msdn.microsoft.com/library/windows/hardware/ff541757)</td>
</tr>
<tr class="even">
<td align="left">IRP_MJ_CREATE_MAILSLOT</td>
<td align="left">No direct support; implement [<em>EvtDeviceWdmIrpPreprocess (KMDF only)</em>](https://msdn.microsoft.com/library/windows/hardware/ff540925)</td>
</tr>
<tr class="odd">
<td align="left">IRP_MJ_DEVICE_CHANGE</td>
<td align="left">No direct support; implement [<em>EvtDeviceWdmIrpPreprocess (KMDF only)</em>](https://msdn.microsoft.com/library/windows/hardware/ff540925)</td>
</tr>
<tr class="even">
<td align="left">[<strong>IRP_MJ_DEVICE_CONTROL</strong>](https://msdn.microsoft.com/library/windows/hardware/ff550744)</td>
<td align="left">[<em>EvtIoDeviceControl</em>](https://msdn.microsoft.com/library/windows/hardware/ff541758) or [<em>EvtIoDefault</em>](https://msdn.microsoft.com/library/windows/hardware/ff541757)</td>
</tr>
<tr class="odd">
<td align="left">[<strong>IRP_MJ_DIRECTORY_CONTROL</strong>](https://msdn.microsoft.com/library/windows/hardware/ff548658)</td>
<td align="left">No direct support; implement [<em>EvtDeviceWdmIrpPreprocess (KMDF only)</em>](https://msdn.microsoft.com/library/windows/hardware/ff540925)</td>
</tr>
<tr class="even">
<td align="left">[<strong>IRP_MJ_FILE_SYSTEM_CONTROL</strong>](https://msdn.microsoft.com/library/windows/hardware/ff550751)</td>
<td align="left">No direct support; implement [<em>EvtDeviceWdmIrpPreprocess (KMDF only)</em>](https://msdn.microsoft.com/library/windows/hardware/ff540925)</td>
</tr>
<tr class="odd">
<td align="left">[<strong>IRP_MJ_FLUSH_BUFFERS</strong>](https://msdn.microsoft.com/library/windows/hardware/ff550760)</td>
<td align="left">No direct support; implement [<em>EvtDeviceWdmIrpPreprocess (KMDF only)</em>](https://msdn.microsoft.com/library/windows/hardware/ff540925)</td>
</tr>
<tr class="even">
<td align="left">[<strong>IRP_MJ_INTERNAL_DEVICE_CONTROL</strong>](https://msdn.microsoft.com/library/windows/hardware/ff550766)</td>
<td align="left">[<em>EvtIoInternalDeviceControl</em>](https://msdn.microsoft.com/library/windows/hardware/ff541768) or [<em>EvtIoDefault</em>](https://msdn.microsoft.com/library/windows/hardware/ff541757)</td>
</tr>
<tr class="odd">
<td align="left">[<strong>IRP_MJ_LOCK_CONTROL</strong>](https://msdn.microsoft.com/library/windows/hardware/ff549251)</td>
<td align="left">No direct support; implement [<em>EvtDeviceWdmIrpPreprocess (KMDF only)</em>](https://msdn.microsoft.com/library/windows/hardware/ff540925)</td>
</tr>
<tr class="even">
<td align="left">[<strong>IRP_MJ_PNP</strong>](https://msdn.microsoft.com/library/windows/hardware/ff550772)</td>
<td align="left">Many; see [KMDF Callbacks for IRP_MJ_PNP](#pnp).</td>
</tr>
<tr class="odd">
<td align="left">[<strong>IRP_MJ_POWER</strong>](https://msdn.microsoft.com/library/windows/hardware/ff550784)</td>
<td align="left">Many; see [KMDF Callbacks for IRP_MJ_POWER](#power).</td>
</tr>
<tr class="even">
<td align="left">[<strong>IRP_MJ_QUERY_EA</strong>](https://msdn.microsoft.com/library/windows/hardware/ff549279)</td>
<td align="left">No direct support; implement [<em>EvtDeviceWdmIrpPreprocess (KMDF only)</em>](https://msdn.microsoft.com/library/windows/hardware/ff540925)</td>
</tr>
<tr class="odd">
<td align="left">[<strong>IRP_MJ_QUERY_INFORMATION</strong>](https://msdn.microsoft.com/library/windows/hardware/ff550788)</td>
<td align="left">No direct support; implement [<em>EvtDeviceWdmIrpPreprocess (KMDF only)</em>](https://msdn.microsoft.com/library/windows/hardware/ff540925)</td>
</tr>
<tr class="even">
<td align="left">[<strong>IRP_MJ_QUERY_QUOTA</strong>](https://msdn.microsoft.com/library/windows/hardware/ff549293)</td>
<td align="left">No direct support; implement [<em>EvtDeviceWdmIrpPreprocess (KMDF only)</em>](https://msdn.microsoft.com/library/windows/hardware/ff540925)</td>
</tr>
<tr class="odd">
<td align="left">[<strong>IRP_MJ_QUERY_SECURITY</strong>](https://msdn.microsoft.com/library/windows/hardware/ff549298)</td>
<td align="left">No direct support; implement [<em>EvtDeviceWdmIrpPreprocess (KMDF only)</em>](https://msdn.microsoft.com/library/windows/hardware/ff540925)</td>
</tr>
<tr class="even">
<td align="left">[<strong>IRP_MJ_QUERY_VOLUME_INFORMATION</strong>](https://msdn.microsoft.com/library/windows/hardware/ff549318)</td>
<td align="left">No direct support; implement [<em>EvtDeviceWdmIrpPreprocess (KMDF only)</em>](https://msdn.microsoft.com/library/windows/hardware/ff540925)</td>
</tr>
<tr class="odd">
<td align="left">[<strong>IRP_MJ_READ</strong>](https://msdn.microsoft.com/library/windows/hardware/ff550794)</td>
<td align="left">[<em>EvtIoRead</em>](https://msdn.microsoft.com/library/windows/hardware/ff541776) or [<em>EvtIoDefault</em>](https://msdn.microsoft.com/library/windows/hardware/ff541757)</td>
</tr>
<tr class="even">
<td align="left">[<strong>IRP_MJ_SET_EA</strong>](https://msdn.microsoft.com/library/windows/hardware/ff549346)</td>
<td align="left">No direct support; implement [<em>EvtDeviceWdmIrpPreprocess (KMDF only)</em>](https://msdn.microsoft.com/library/windows/hardware/ff540925)</td>
</tr>
<tr class="odd">
<td align="left">[<strong>IRP_MJ_SET_INFORMATION</strong>](https://msdn.microsoft.com/library/windows/hardware/ff550799)</td>
<td align="left">No direct support; implement [<em>EvtDeviceWdmIrpPreprocess (KMDF only)</em>](https://msdn.microsoft.com/library/windows/hardware/ff540925)</td>
</tr>
<tr class="even">
<td align="left">[<strong>IRP_MJ_SET_QUOTA</strong>](https://msdn.microsoft.com/library/windows/hardware/ff549401)</td>
<td align="left">No direct support; implement [<em>EvtDeviceWdmIrpPreprocess (KMDF only)</em>](https://msdn.microsoft.com/library/windows/hardware/ff540925)</td>
</tr>
<tr class="odd">
<td align="left">[<strong>IRP_MJ_SET_SECURITY</strong>](https://msdn.microsoft.com/library/windows/hardware/ff549407)</td>
<td align="left">No direct support; implement [<em>EvtDeviceWdmIrpPreprocess (KMDF only)</em>](https://msdn.microsoft.com/library/windows/hardware/ff540925)</td>
</tr>
<tr class="even">
<td align="left">[<strong>IRP_MJ_SET_VOLUME_INFORMATION</strong>](https://msdn.microsoft.com/library/windows/hardware/ff549415)</td>
<td align="left">No direct support; implement [<em>EvtDeviceWdmIrpPreprocess (KMDF only)</em>](https://msdn.microsoft.com/library/windows/hardware/ff540925)</td>
</tr>
<tr class="odd">
<td align="left">[<strong>IRP_MJ_SHUTDOWN</strong>](https://msdn.microsoft.com/library/windows/hardware/ff550807)</td>
<td align="left"><p>For control device objects, implement [<em>EvtDeviceShutdownNotification (KMDF only)</em>](https://msdn.microsoft.com/library/windows/hardware/ff540911)</p>
<p>For all Plug and Play device objects: Not supported; implement [<em>EvtDeviceWdmIrpPreprocess (KMDF only)</em>](https://msdn.microsoft.com/library/windows/hardware/ff540925).</p></td>
</tr>
<tr class="even">
<td align="left">[<strong>IRP_MJ_SYSTEM_CONTROL</strong>](https://msdn.microsoft.com/library/windows/hardware/ff550813)</td>
<td align="left">Create WDFWMIPROVIDER and WDFWMIINSTANCE objects and implement <strong>EvtWmiXxx (KMDF only)</strong> callbacks.</td>
</tr>
<tr class="odd">
<td align="left">[<strong>IRP_MJ_WRITE</strong>](https://msdn.microsoft.com/library/windows/hardware/ff550819)</td>
<td align="left">[<em>EvtIoWrite</em>](https://msdn.microsoft.com/library/windows/hardware/ff541813) or [<em>EvtIoDefault</em>](https://msdn.microsoft.com/library/windows/hardware/ff541757)</td>
</tr>
</tbody>
</table>

 

## <a href="" id="pnp"></a>KMDF Callbacks for IRP\_MJ\_PNP


The following table lists, in order of execution, the KMDF callbacks that correspond to the minor IRP codes for [**IRP\_MJ\_PNP**](https://msdn.microsoft.com/library/windows/hardware/ff550772). The arrows indicate whether a WDM FDO handles the IRP as it travels up or down the stack.

**Note**   In a KMDF driver, Plug and Play and power management are integrated operations and the driver does not receive the individual minor [**IRP\_MJ\_PNP**](https://msdn.microsoft.com/library/windows/hardware/ff550772) or [**IRP\_MJ\_POWER**](https://msdn.microsoft.com/library/windows/hardware/ff550784) requests. Instead, the framework calls a core set of callbacks at power up and a corresponding set at power down, and calls additional callbacks before and after this core set as appropriate for each individual Plug and Play request. For comprehensive diagrams that show the power-up and power-down sequences, see [Porting PnP and Power Management Functionality](porting-pnp-and-power-management-functionality.md).

 

<table>
<colgroup>
<col width="50%" />
<col width="50%" />
</colgroup>
<thead>
<tr class="header">
<th align="left">IRP_MJ_PNP minor code</th>
<th align="left">KMDF callbacks</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td align="left">↓[<strong>IRP_MN_CANCEL_REMOVE_DEVICE</strong>](https://msdn.microsoft.com/library/windows/hardware/ff550823)</td>
<td align="left">None</td>
</tr>
<tr class="even">
<td align="left">↓[<strong>IRP_MN_CANCEL_STOP_DEVICE</strong>](https://msdn.microsoft.com/library/windows/hardware/ff550826)</td>
<td align="left">None</td>
</tr>
<tr class="odd">
<td align="left">↑[<strong>IRP_MN_DEVICE_USAGE_NOTIFICATION</strong>](https://msdn.microsoft.com/library/windows/hardware/ff550841)</td>
<td align="left">[<em>EvtDeviceUsageNotification</em>](https://msdn.microsoft.com/library/windows/hardware/ff540915)</td>
</tr>
<tr class="even">
<td align="left">↓[<strong>IRP_MN_EJECT</strong>](https://msdn.microsoft.com/library/windows/hardware/ff550853)</td>
<td align="left">[<em>EvtDeviceEject (KMDF only)</em>](https://msdn.microsoft.com/library/windows/hardware/ff540863)</td>
</tr>
<tr class="odd">
<td align="left">↓[<strong>IRP_MN_FILTER_RESOURCE_REQUIREMENTS</strong>](https://msdn.microsoft.com/library/windows/hardware/ff550874)</td>
<td align="left">[<em>EvtDeviceFilterRemoveResourceRequirements (KMDF only)</em>](https://msdn.microsoft.com/library/windows/hardware/ff540872)</td>
</tr>
<tr class="even">
<td align="left">↑[<strong>IRP_MN_FILTER_RESOURCE_REQUIREMENTS</strong>](https://msdn.microsoft.com/library/windows/hardware/ff550874)</td>
<td align="left">[<em>EvtDeviceFilterAddResourceRequirements (KMDF only)</em>](https://msdn.microsoft.com/library/windows/hardware/ff540870)</td>
</tr>
<tr class="odd">
<td align="left">[<strong>IRP_MN_QUERY_BUS_INFORMATION</strong>](https://msdn.microsoft.com/library/windows/hardware/ff551654)</td>
<td align="left">None. The KMDF driver calls <strong>WdfDeviceInitXxx</strong> methods to set device properties during initialization so that the framework can respond to this query on its own without notifying the driver.</td>
</tr>
<tr class="even">
<td align="left">[<strong>IRP_MN_QUERY_CAPABILITIES</strong>](https://msdn.microsoft.com/library/windows/hardware/ff551664)</td>
<td align="left">None. The KMDF driver calls <strong>WdfDeviceInitXxx</strong> methods to set device properties during initialization so that the framework can respond to this query on its own without notifying the driver.</td>
</tr>
<tr class="odd">
<td align="left">↓[<strong>IRP_MN_QUERY_DEVICE_RELATIONS</strong>](https://msdn.microsoft.com/library/windows/hardware/ff551670) (bus, removal, and ejection relations)</td>
<td align="left">[<em>EvtDeviceRelationsQuery</em>](https://msdn.microsoft.com/library/windows/hardware/ff540886)</td>
</tr>
<tr class="even">
<td align="left">[<strong>IRP_MN_QUERY_DEVICE_TEXT</strong>](https://msdn.microsoft.com/library/windows/hardware/ff551674)</td>
<td align="left">None. The KMDF driver calls <strong>WdfDeviceInitXxx</strong> methods to set device properties during initialization so that the framework can respond to this query on its own without notifying the driver.</td>
</tr>
<tr class="odd">
<td align="left">[<strong>IRP_MN_QUERY_ID</strong>](https://msdn.microsoft.com/library/windows/hardware/ff551679)</td>
<td align="left">None. The KMDF driver calls <strong>WdfDeviceInitXxx</strong> methods to set device properties during initialization so that the framework can respond to this query on its own without notifying the driver.</td>
</tr>
<tr class="even">
<td align="left">↓[<strong>IRP_MN_QUERY_INTERFACE</strong>](https://msdn.microsoft.com/library/windows/hardware/ff551687)</td>
<td align="left">[<em>EvtDeviceProcessQueryInterfaceRequest (KMDF only)</em>](https://msdn.microsoft.com/library/windows/hardware/ff540882)</td>
</tr>
<tr class="odd">
<td align="left">[<strong>IRP_MN_QUERY_PNP_DEVICE_STATE</strong>](https://msdn.microsoft.com/library/windows/hardware/ff551698)</td>
<td align="left">None. The KMDF driver calls <strong>WdfDeviceInitXxx</strong> methods to set device properties during initialization so that the framework can respond to this query on its own without notifying the driver.</td>
</tr>
<tr class="even">
<td align="left">↓[<strong>IRP_MN_QUERY_REMOVE_DEVICE</strong>](https://msdn.microsoft.com/library/windows/hardware/ff551705)</td>
<td align="left">[<em>EvtDeviceQueryRemove</em>](https://msdn.microsoft.com/library/windows/hardware/ff540883)</td>
</tr>
<tr class="odd">
<td align="left">↓[<strong>IRP_MN_QUERY_RESOURCE_REQUIREMENTS</strong>](https://msdn.microsoft.com/library/windows/hardware/ff551715)</td>
<td align="left">[<em>EvtDeviceResourceRequirementsQuery (KMDF only)</em>](https://msdn.microsoft.com/library/windows/hardware/ff540894)</td>
</tr>
<tr class="even">
<td align="left">↓[<strong>IRP_MN_QUERY_RESOURCES</strong>](https://msdn.microsoft.com/library/windows/hardware/ff551710)</td>
<td align="left">[<em>EvtDeviceResourcesQuery (KMDF only)</em>](https://msdn.microsoft.com/library/windows/hardware/ff540895)</td>
</tr>
<tr class="odd">
<td align="left">↓[<strong>IRP_MN_QUERY_STOP_DEVICE</strong>](https://msdn.microsoft.com/library/windows/hardware/ff551725)</td>
<td align="left">[<em>EvtDeviceQueryStop</em>](https://msdn.microsoft.com/library/windows/hardware/ff540885)</td>
</tr>
<tr class="even">
<td align="left">[<strong>IRP_MN_READ_CONFIG</strong>](https://msdn.microsoft.com/library/windows/hardware/ff551727)</td>
<td align="left">None. The KMDF driver calls <strong>WdfDeviceInitXxx</strong> methods to set device properties during initialization so that the framework can respond to this query on its own without notifying the driver.</td>
</tr>
<tr class="odd">
<td align="left">↓[<strong>IRP_MN_REMOVE_DEVICE</strong>](https://msdn.microsoft.com/library/windows/hardware/ff551738)</td>
<td align="left"><p>After [<strong>IRP_MN_QUERY_REMOVE_DEVICE</strong>](https://msdn.microsoft.com/library/windows/hardware/ff551705):</p>
[<em>EvtDeviceSelfManagedIoSuspend</em>](https://msdn.microsoft.com/library/windows/hardware/ff540907)
[<em>EvtIoStop</em>](https://msdn.microsoft.com/library/windows/hardware/ff541788) (<strong>WdfRequestStopActionSuspend</strong> flag)
[<em>EvtDmaEnablerSelfManagedIoStop (KMDF only)</em>](https://msdn.microsoft.com/library/windows/hardware/ff541677)
[<em>EvtDmaEnablerDisable (KMDF only)</em>](https://msdn.microsoft.com/library/windows/hardware/ff540927)
[<em>EvtDmaEnablerFlush (KMDF only)</em>](https://msdn.microsoft.com/library/windows/hardware/ff541655)
[<em>EvtDeviceD0ExitPreInterruptsDisabled</em>](https://msdn.microsoft.com/library/windows/hardware/ff540856)
[<em>EvtInterruptDisable</em>](https://msdn.microsoft.com/library/windows/hardware/ff541714)
[<em>EvtDeviceD0Exit</em>](https://msdn.microsoft.com/library/windows/hardware/ff540855) (<strong>WdfPowerDeviceD3Final</strong> state)
[<em>EvtDeviceReleaseHardware</em>](https://msdn.microsoft.com/library/windows/hardware/ff540890)
[<em>EvtIoStop</em>](https://msdn.microsoft.com/library/windows/hardware/ff541788) (<strong>WdfRequestStopActionPurge</strong> flag) for power-managed queues
[<em>EvtDeviceSelfManagedIoFlush</em>](https://msdn.microsoft.com/library/windows/hardware/ff540901)
[<em>EvtIoStop</em>](https://msdn.microsoft.com/library/windows/hardware/ff541788) (<strong>WdfRequestStopActionPurge</strong> flag) for non-power-managed queues
[<em>EvtDeviceSelfManagedIoCleanup</em>](https://msdn.microsoft.com/library/windows/hardware/ff540898)
[<em>EvtCleanupCallback</em>](https://msdn.microsoft.com/library/windows/hardware/ff540840) for WDFDEVICE
[<em>EvtDestroyCallback</em>](https://msdn.microsoft.com/library/windows/hardware/ff540841) for WDFDEVICE
<p>After [<strong>IRP_MN_SURPRISE_REMOVAL</strong>](https://msdn.microsoft.com/library/windows/hardware/ff551760):</p>
[<em>EvtIoStop</em>](https://msdn.microsoft.com/library/windows/hardware/ff541788) (<strong>WdfRequestStopActionPurge</strong> flag) for non-power-managed queues
[<em>EvtDeviceSelfManagedIoCleanup</em>](https://msdn.microsoft.com/library/windows/hardware/ff540898)
[<em>EvtCleanupCallback</em>](https://msdn.microsoft.com/library/windows/hardware/ff540840) for WDFDEVICE
[<em>EvtDestroyCallback</em>](https://msdn.microsoft.com/library/windows/hardware/ff540841) for WDFDEVICE</td>
</tr>
<tr class="even">
<td align="left">↓[<strong>IRP_MN_SET_LOCK</strong>](https://msdn.microsoft.com/library/windows/hardware/ff551742)</td>
<td align="left">[<em>EvtDeviceSetLock (KMDF only)</em>](https://msdn.microsoft.com/library/windows/hardware/ff540909)</td>
</tr>
<tr class="odd">
<td align="left">↑[<strong>IRP_MN_START_DEVICE</strong>](https://msdn.microsoft.com/library/windows/hardware/ff551749)</td>
<td align="left"><p>After enumeration:</p>
[<em>EvtDeviceRemoveAddedResources (KMDF only)</em>](https://msdn.microsoft.com/library/windows/hardware/ff540892)
[<em>EvtDevicePrepareHardware</em>](https://msdn.microsoft.com/library/windows/hardware/ff540880)
[<em>EvtDeviceD0Entry</em>](https://msdn.microsoft.com/library/windows/hardware/ff540848)
[<em>EvtInterruptEnable</em>](https://msdn.microsoft.com/library/windows/hardware/ff541730)
[<em>EvtDeviceD0EntryPostInterruptsEnabled</em>](https://msdn.microsoft.com/library/windows/hardware/ff540853)
[<em>EvtDmaEnablerFill (KMDF only)</em>](https://msdn.microsoft.com/library/windows/hardware/ff540932)
[<em>EvtDmaEnablerEnable (KMDF only)</em>](https://msdn.microsoft.com/library/windows/hardware/ff540929)
[<em>EvtDmaEnablerSelfManagedIoStart (KMDF only)</em>](https://msdn.microsoft.com/library/windows/hardware/ff541663)
[<em>EvtDeviceSelfManagedIoInit</em>](https://msdn.microsoft.com/library/windows/hardware/ff540902)
<p>After [<strong>IRP_MN_STOP_DEVICE</strong>](https://msdn.microsoft.com/library/windows/hardware/ff551755):</p>
[<em>EvtDeviceRemoveAddedResources (KMDF only)</em>](https://msdn.microsoft.com/library/windows/hardware/ff540892)
[<em>EvtDevicePrepareHardware</em>](https://msdn.microsoft.com/library/windows/hardware/ff540880)
[<em>EvtDeviceD0Entry</em>](https://msdn.microsoft.com/library/windows/hardware/ff540848)
[<em>EvtInterruptEnable</em>](https://msdn.microsoft.com/library/windows/hardware/ff541730)
[<em>EvtDeviceD0EntryPostInterruptsEnabled</em>](https://msdn.microsoft.com/library/windows/hardware/ff540853)
[<em>EvtDmaEnablerFill (KMDF only)</em>](https://msdn.microsoft.com/library/windows/hardware/ff540932)
[<em>EvtDmaEnablerEnable (KMDF only)</em>](https://msdn.microsoft.com/library/windows/hardware/ff540929)
[<em>EvtDmaEnablerSelfManagedIoStart (KMDF only)</em>](https://msdn.microsoft.com/library/windows/hardware/ff541663)
[<em>EvtIoResume</em>](https://msdn.microsoft.com/library/windows/hardware/ff541779)
[<em>EvtDeviceSelfManagedIoRestart</em>](https://msdn.microsoft.com/library/windows/hardware/ff540905)</td>
</tr>
<tr class="even">
<td align="left">↓[<strong>IRP_MN_STOP_DEVICE</strong>](https://msdn.microsoft.com/library/windows/hardware/ff551755)</td>
<td align="left">[<em>EvtDeviceSelfManagedIoSuspend</em>](https://msdn.microsoft.com/library/windows/hardware/ff540907)
[<em>EvtIoStop</em>](https://msdn.microsoft.com/library/windows/hardware/ff541788) (<strong>WdfRequestStopActionSuspend</strong> flag)
[<em>EvtDmaEnablerSelfManagedIoStop (KMDF only)</em>](https://msdn.microsoft.com/library/windows/hardware/ff541677)
[<em>EvtDmaEnablerDisable (KMDF only)</em>](https://msdn.microsoft.com/library/windows/hardware/ff540927)
[<em>EvtDmaEnablerFlush (KMDF only)</em>](https://msdn.microsoft.com/library/windows/hardware/ff541655)
[<em>EvtDeviceD0ExitPreInterruptsDisabled</em>](https://msdn.microsoft.com/library/windows/hardware/ff540856)
[<em>EvtInterruptDisable</em>](https://msdn.microsoft.com/library/windows/hardware/ff541714)
[<em>EvtDeviceD0Exit</em>](https://msdn.microsoft.com/library/windows/hardware/ff540855) (<strong>WdfPowerDeviceD3Final</strong> state)
[<em>EvtDeviceReleaseHardware</em>](https://msdn.microsoft.com/library/windows/hardware/ff540890)</td>
</tr>
<tr class="odd">
<td align="left">↓[<strong>IRP_MN_SURPRISE_REMOVAL</strong>](https://msdn.microsoft.com/library/windows/hardware/ff551760)</td>
<td align="left">[<em>EvtDeviceSurpriseRemoval</em>](https://msdn.microsoft.com/library/windows/hardware/ff540913)
[<em>EvtDeviceSelfManagedIoSuspend</em>](https://msdn.microsoft.com/library/windows/hardware/ff540907)
[<em>EvtIoStop</em>](https://msdn.microsoft.com/library/windows/hardware/ff541788) (<strong>WdfRequestStopActionSuspend</strong> flag)
[<em>EvtDmaEnablerSelfManagedIoStop (KMDF only)</em>](https://msdn.microsoft.com/library/windows/hardware/ff541677)
[<em>EvtDmaEnablerDisable (KMDF only)</em>](https://msdn.microsoft.com/library/windows/hardware/ff540927)
[<em>EvtDmaEnablerFlush (KMDF only)</em>](https://msdn.microsoft.com/library/windows/hardware/ff541655)
[<em>EvtDeviceD0ExitPreInterruptsDisabled</em>](https://msdn.microsoft.com/library/windows/hardware/ff540856)
[<em>EvtInterruptDisable</em>](https://msdn.microsoft.com/library/windows/hardware/ff541714)
[<em>EvtDeviceD0Exit</em>](https://msdn.microsoft.com/library/windows/hardware/ff540855) (<strong>WdfPowerDeviceD3Final</strong> state)
[<em>EvtDeviceReleaseHardware</em>](https://msdn.microsoft.com/library/windows/hardware/ff540890)
[<em>EvtIoStop</em>](https://msdn.microsoft.com/library/windows/hardware/ff541788) (<strong>WdfRequestStopActionPurge</strong> flag) for power-managed queues
[<em>EvtDeviceSelfManagedIoFlush</em>](https://msdn.microsoft.com/library/windows/hardware/ff540901)</td>
</tr>
<tr class="even">
<td align="left">[<strong>IRP_MN_WRITE_CONFIG</strong>](https://msdn.microsoft.com/library/windows/hardware/ff551769)</td>
<td align="left">None. The KMDF driver calls <strong>WdfDeviceInitXxx</strong> methods to set device properties during initialization so that the framework can respond to this query on its own without notifying the driver.</td>
</tr>
</tbody>
</table>

 

## <a href="" id="power"></a>KMDF Callbacks for IRP\_MJ\_POWER


The following table lists, in order of execution, the KMDF callbacks that correspond to the minor IRP codes for [**IRP\_MJ\_POWER**](https://msdn.microsoft.com/library/windows/hardware/ff550784). The arrows indicate whether a WDM FDO handles the IRP as it travels up or down the stack.

**Note**   Note: In a KMDF driver, Plug and Play and power management are integrated operations and the driver does not receive the individual minor [**IRP\_MJ\_PNP**](https://msdn.microsoft.com/library/windows/hardware/ff550772) or [**IRP\_MJ\_POWER**](https://msdn.microsoft.com/library/windows/hardware/ff550784) requests. Instead, the framework calls a core set of callbacks at power up and a corresponding set at power down, and calls additional callbacks before and after this core set as appropriate for each individual Plug and Play request. For comprehensive diagrams that show the power-up and power-down sequences, see [Porting PnP and Power Management Functionality](porting-pnp-and-power-management-functionality.md).

 

<table>
<colgroup>
<col width="50%" />
<col width="50%" />
</colgroup>
<thead>
<tr class="header">
<th align="left">IRP_MJ_POWER minor code</th>
<th align="left">Framework callbacks</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td align="left">↓[<strong>IRP_MN_SET_POWER</strong>](https://msdn.microsoft.com/library/windows/hardware/ff551744) for D1, D2, or D3 (power down)</td>
<td align="left">[<em>EvtDeviceSelfManagedIoSuspend</em>](https://msdn.microsoft.com/library/windows/hardware/ff540907)
[<em>EvtIoStop</em>](https://msdn.microsoft.com/library/windows/hardware/ff541788) (<strong>WdfRequestStopActionSuspend</strong> flag)
[<em>EvtDeviceArmWakeFromS0</em>](https://msdn.microsoft.com/library/windows/hardware/ff540843) or [<em>EvtDeviceArmWakeFromSx</em>](https://msdn.microsoft.com/library/windows/hardware/ff540844)
[<em>EvtDmaEnablerSelfManagedIoStop (KMDF only)</em>](https://msdn.microsoft.com/library/windows/hardware/ff541677)
[<em>EvtDmaEnablerDisable (KMDF only)</em>](https://msdn.microsoft.com/library/windows/hardware/ff540927)
[<em>EvtDmaEnablerFlush (KMDF only)</em>](https://msdn.microsoft.com/library/windows/hardware/ff541655)
[<em>EvtDeviceD0ExitPreInterruptsDisabled</em>](https://msdn.microsoft.com/library/windows/hardware/ff540856)
[<em>EvtInterruptDisable</em>](https://msdn.microsoft.com/library/windows/hardware/ff541714)
[<em>EvtDeviceD0Exit</em>](https://msdn.microsoft.com/library/windows/hardware/ff540855)</td>
</tr>
<tr class="even">
<td align="left">↑[<strong>IRP_MN_SET_POWER</strong>](https://msdn.microsoft.com/library/windows/hardware/ff551744) for D0 (power up)</td>
<td align="left">[<em>EvtDeviceD0Entry</em>](https://msdn.microsoft.com/library/windows/hardware/ff540848)
[<em>EvtInterruptEnable</em>](https://msdn.microsoft.com/library/windows/hardware/ff541730)
[<em>EvtDeviceD0EntryPostInterruptsEnabled</em>](https://msdn.microsoft.com/library/windows/hardware/ff540853)
[<em>EvtDmaEnablerFill (KMDF only)</em>](https://msdn.microsoft.com/library/windows/hardware/ff540932)
[<em>EvtDmaEnablerEnable (KMDF only)</em>](https://msdn.microsoft.com/library/windows/hardware/ff540929)
[<em>EvtDmaEnablerSelfManagedIoStart (KMDF only)</em>](https://msdn.microsoft.com/library/windows/hardware/ff541663)
[<em>EvtIoResume</em>](https://msdn.microsoft.com/library/windows/hardware/ff541779)
[<em>EvtDeviceSelfManagedIoRestart</em>](https://msdn.microsoft.com/library/windows/hardware/ff540905)</td>
</tr>
<tr class="odd">
<td align="left">↓[<strong>IRP_MN_SET_POWER</strong>](https://msdn.microsoft.com/library/windows/hardware/ff551744) for Sx</td>
<td align="left">None</td>
</tr>
<tr class="even">
<td align="left">↑[<strong>IRP_MN_SET_POWER</strong>](https://msdn.microsoft.com/library/windows/hardware/ff551744) for Sx</td>
<td align="left">None</td>
</tr>
<tr class="odd">
<td align="left">[<strong>IRP_MN_POWER_SEQUENCE</strong>](https://msdn.microsoft.com/library/windows/hardware/ff551644)</td>
<td align="left">None</td>
</tr>
<tr class="even">
<td align="left">↓[<strong>IRP_MN_WAIT_WAKE</strong>](https://msdn.microsoft.com/library/windows/hardware/ff551766)</td>
<td align="left">[<em>EvtDeviceEnableWakeAtBus (KMDF only)</em>](https://msdn.microsoft.com/library/windows/hardware/ff540866)</td>
</tr>
<tr class="odd">
<td align="left">↑[<strong>IRP_MN_WAIT_WAKE</strong>](https://msdn.microsoft.com/library/windows/hardware/ff551766)</td>
<td align="left">[<em>EvtDeviceDisableWakeAtBus (KMDF only)</em>](https://msdn.microsoft.com/library/windows/hardware/ff540858)</td>
</tr>
</tbody>
</table>

 

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bwdf\wdf%5D:%20WDM%20IRPs%20and%20WDF%20Event%20Callback%20Functions%20%20RELEASE:%20%284/5/2016%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")




