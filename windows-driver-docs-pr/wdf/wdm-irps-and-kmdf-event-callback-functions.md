---
title: WDM IRPs and WDF Event Callback Functions
description: WDM IRPs and WDF Event Callback Functions
ms.date: 04/20/2017
ms.localizationpriority: medium
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
<td align="left"><a href="/windows-hardware/drivers/kernel/irp-mj-cleanup" data-raw-source="[&lt;strong&gt;IRP_MJ_CLEANUP&lt;/strong&gt;](../kernel/irp-mj-cleanup.md)"><strong>IRP_MJ_CLEANUP</strong></a></td>
<td align="left"><a href="/windows-hardware/drivers/ddi/wdfdevice/nc-wdfdevice-evt_wdf_file_cleanup" data-raw-source="[&lt;em&gt;EvtFileCleanup&lt;/em&gt;](/windows-hardware/drivers/ddi/wdfdevice/nc-wdfdevice-evt_wdf_file_cleanup)"><em>EvtFileCleanup</em></a></td>
</tr>
<tr class="even">
<td align="left"><a href="/windows-hardware/drivers/kernel/irp-mj-close" data-raw-source="[&lt;strong&gt;IRP_MJ_CLOSE&lt;/strong&gt;](../kernel/irp-mj-close.md)"><strong>IRP_MJ_CLOSE</strong></a></td>
<td align="left"><a href="/windows-hardware/drivers/ddi/wdfdevice/nc-wdfdevice-evt_wdf_file_close" data-raw-source="[&lt;em&gt;EvtFileClose&lt;/em&gt;](/windows-hardware/drivers/ddi/wdfdevice/nc-wdfdevice-evt_wdf_file_close)"><em>EvtFileClose</em></a></td>
</tr>
<tr class="odd">
<td align="left"><a href="/windows-hardware/drivers/kernel/irp-mj-create" data-raw-source="[&lt;strong&gt;IRP_MJ_CREATE&lt;/strong&gt;](../kernel/irp-mj-create.md)"><strong>IRP_MJ_CREATE</strong></a></td>
<td align="left"><a href="/windows-hardware/drivers/ddi/wdfdevice/nc-wdfdevice-evt_wdf_device_file_create" data-raw-source="[&lt;em&gt;EvtDeviceFileCreate&lt;/em&gt;](/windows-hardware/drivers/ddi/wdfdevice/nc-wdfdevice-evt_wdf_device_file_create)"><em>EvtDeviceFileCreate</em></a> or <a href="/windows-hardware/drivers/ddi/wdfio/nc-wdfio-evt_wdf_io_queue_io_default" data-raw-source="[&lt;em&gt;EvtIoDefault&lt;/em&gt;](/windows-hardware/drivers/ddi/wdfio/nc-wdfio-evt_wdf_io_queue_io_default)"><em>EvtIoDefault</em></a></td>
</tr>
<tr class="even">
<td align="left">IRP_MJ_CREATE_MAILSLOT</td>
<td align="left">No direct support; implement <a href="/windows-hardware/drivers/ddi/wdfdevice/nc-wdfdevice-evt_wdfdevice_wdm_irp_preprocess" data-raw-source="[&lt;em&gt;EvtDeviceWdmIrpPreprocess (KMDF only)&lt;/em&gt;](/windows-hardware/drivers/ddi/wdfdevice/nc-wdfdevice-evt_wdfdevice_wdm_irp_preprocess)"><em>EvtDeviceWdmIrpPreprocess (KMDF only)</em></a></td>
</tr>
<tr class="odd">
<td align="left">IRP_MJ_DEVICE_CHANGE</td>
<td align="left">No direct support; implement <a href="/windows-hardware/drivers/ddi/wdfdevice/nc-wdfdevice-evt_wdfdevice_wdm_irp_preprocess" data-raw-source="[&lt;em&gt;EvtDeviceWdmIrpPreprocess (KMDF only)&lt;/em&gt;](/windows-hardware/drivers/ddi/wdfdevice/nc-wdfdevice-evt_wdfdevice_wdm_irp_preprocess)"><em>EvtDeviceWdmIrpPreprocess (KMDF only)</em></a></td>
</tr>
<tr class="even">
<td align="left"><a href="/windows-hardware/drivers/kernel/irp-mj-device-control" data-raw-source="[&lt;strong&gt;IRP_MJ_DEVICE_CONTROL&lt;/strong&gt;](../kernel/irp-mj-device-control.md)"><strong>IRP_MJ_DEVICE_CONTROL</strong></a></td>
<td align="left"><a href="/windows-hardware/drivers/ddi/wdfio/nc-wdfio-evt_wdf_io_queue_io_device_control" data-raw-source="[&lt;em&gt;EvtIoDeviceControl&lt;/em&gt;](/windows-hardware/drivers/ddi/wdfio/nc-wdfio-evt_wdf_io_queue_io_device_control)"><em>EvtIoDeviceControl</em></a> or <a href="/windows-hardware/drivers/ddi/wdfio/nc-wdfio-evt_wdf_io_queue_io_default" data-raw-source="[&lt;em&gt;EvtIoDefault&lt;/em&gt;](/windows-hardware/drivers/ddi/wdfio/nc-wdfio-evt_wdf_io_queue_io_default)"><em>EvtIoDefault</em></a></td>
</tr>
<tr class="odd">
<td align="left"><a href="/windows-hardware/drivers/ifs/irp-mj-directory-control" data-raw-source="[&lt;strong&gt;IRP_MJ_DIRECTORY_CONTROL&lt;/strong&gt;](../ifs/irp-mj-directory-control.md)"><strong>IRP_MJ_DIRECTORY_CONTROL</strong></a></td>
<td align="left">No direct support; implement <a href="/windows-hardware/drivers/ddi/wdfdevice/nc-wdfdevice-evt_wdfdevice_wdm_irp_preprocess" data-raw-source="[&lt;em&gt;EvtDeviceWdmIrpPreprocess (KMDF only)&lt;/em&gt;](/windows-hardware/drivers/ddi/wdfdevice/nc-wdfdevice-evt_wdfdevice_wdm_irp_preprocess)"><em>EvtDeviceWdmIrpPreprocess (KMDF only)</em></a></td>
</tr>
<tr class="even">
<td align="left"><a href="/windows-hardware/drivers/kernel/irp-mj-file-system-control" data-raw-source="[&lt;strong&gt;IRP_MJ_FILE_SYSTEM_CONTROL&lt;/strong&gt;](../kernel/irp-mj-file-system-control.md)"><strong>IRP_MJ_FILE_SYSTEM_CONTROL</strong></a></td>
<td align="left">No direct support; implement <a href="/windows-hardware/drivers/ddi/wdfdevice/nc-wdfdevice-evt_wdfdevice_wdm_irp_preprocess" data-raw-source="[&lt;em&gt;EvtDeviceWdmIrpPreprocess (KMDF only)&lt;/em&gt;](/windows-hardware/drivers/ddi/wdfdevice/nc-wdfdevice-evt_wdfdevice_wdm_irp_preprocess)"><em>EvtDeviceWdmIrpPreprocess (KMDF only)</em></a></td>
</tr>
<tr class="odd">
<td align="left"><a href="/windows-hardware/drivers/kernel/irp-mj-flush-buffers" data-raw-source="[&lt;strong&gt;IRP_MJ_FLUSH_BUFFERS&lt;/strong&gt;](../kernel/irp-mj-flush-buffers.md)"><strong>IRP_MJ_FLUSH_BUFFERS</strong></a></td>
<td align="left">No direct support; implement <a href="/windows-hardware/drivers/ddi/wdfdevice/nc-wdfdevice-evt_wdfdevice_wdm_irp_preprocess" data-raw-source="[&lt;em&gt;EvtDeviceWdmIrpPreprocess (KMDF only)&lt;/em&gt;](/windows-hardware/drivers/ddi/wdfdevice/nc-wdfdevice-evt_wdfdevice_wdm_irp_preprocess)"><em>EvtDeviceWdmIrpPreprocess (KMDF only)</em></a></td>
</tr>
<tr class="even">
<td align="left"><a href="/windows-hardware/drivers/kernel/irp-mj-internal-device-control" data-raw-source="[&lt;strong&gt;IRP_MJ_INTERNAL_DEVICE_CONTROL&lt;/strong&gt;](../kernel/irp-mj-internal-device-control.md)"><strong>IRP_MJ_INTERNAL_DEVICE_CONTROL</strong></a></td>
<td align="left"><a href="/windows-hardware/drivers/ddi/wdfio/nc-wdfio-evt_wdf_io_queue_io_internal_device_control" data-raw-source="[&lt;em&gt;EvtIoInternalDeviceControl&lt;/em&gt;](/windows-hardware/drivers/ddi/wdfio/nc-wdfio-evt_wdf_io_queue_io_internal_device_control)"><em>EvtIoInternalDeviceControl</em></a> or <a href="/windows-hardware/drivers/ddi/wdfio/nc-wdfio-evt_wdf_io_queue_io_default" data-raw-source="[&lt;em&gt;EvtIoDefault&lt;/em&gt;](/windows-hardware/drivers/ddi/wdfio/nc-wdfio-evt_wdf_io_queue_io_default)"><em>EvtIoDefault</em></a></td>
</tr>
<tr class="odd">
<td align="left"><a href="/windows-hardware/drivers/ifs/irp-mj-lock-control" data-raw-source="[&lt;strong&gt;IRP_MJ_LOCK_CONTROL&lt;/strong&gt;](../ifs/irp-mj-lock-control.md)"><strong>IRP_MJ_LOCK_CONTROL</strong></a></td>
<td align="left">No direct support; implement <a href="/windows-hardware/drivers/ddi/wdfdevice/nc-wdfdevice-evt_wdfdevice_wdm_irp_preprocess" data-raw-source="[&lt;em&gt;EvtDeviceWdmIrpPreprocess (KMDF only)&lt;/em&gt;](/windows-hardware/drivers/ddi/wdfdevice/nc-wdfdevice-evt_wdfdevice_wdm_irp_preprocess)"><em>EvtDeviceWdmIrpPreprocess (KMDF only)</em></a></td>
</tr>
<tr class="even">
<td align="left"><a href="/windows-hardware/drivers/kernel/irp-mj-pnp" data-raw-source="[&lt;strong&gt;IRP_MJ_PNP&lt;/strong&gt;](../kernel/irp-mj-pnp.md)"><strong>IRP_MJ_PNP</strong></a></td>
<td align="left">Many; see <a href="#kmdf-callbacks-for-irp_mj_pnp" data-raw-source="[KMDF Callbacks for IRP_MJ_PNP](#kmdf-callbacks-for-irp_mj_pnp)">KMDF Callbacks for IRP_MJ_PNP</a>.</td>
</tr>
<tr class="odd">
<td align="left"><a href="/windows-hardware/drivers/kernel/irp-mj-power" data-raw-source="[&lt;strong&gt;IRP_MJ_POWER&lt;/strong&gt;](../kernel/irp-mj-power.md)"><strong>IRP_MJ_POWER</strong></a></td>
<td align="left">Many; see <a href="#kmdf-callbacks-for-irp_mj_power" data-raw-source="[KMDF Callbacks for IRP_MJ_POWER](#kmdf-callbacks-for-irp_mj_power)">KMDF Callbacks for IRP_MJ_POWER</a>.</td>
</tr>
<tr class="even">
<td align="left"><a href="/windows-hardware/drivers/ifs/irp-mj-query-ea" data-raw-source="[&lt;strong&gt;IRP_MJ_QUERY_EA&lt;/strong&gt;](../ifs/irp-mj-query-ea.md)"><strong>IRP_MJ_QUERY_EA</strong></a></td>
<td align="left">No direct support; implement <a href="/windows-hardware/drivers/ddi/wdfdevice/nc-wdfdevice-evt_wdfdevice_wdm_irp_preprocess" data-raw-source="[&lt;em&gt;EvtDeviceWdmIrpPreprocess (KMDF only)&lt;/em&gt;](/windows-hardware/drivers/ddi/wdfdevice/nc-wdfdevice-evt_wdfdevice_wdm_irp_preprocess)"><em>EvtDeviceWdmIrpPreprocess (KMDF only)</em></a></td>
</tr>
<tr class="odd">
<td align="left"><a href="/windows-hardware/drivers/kernel/irp-mj-query-information" data-raw-source="[&lt;strong&gt;IRP_MJ_QUERY_INFORMATION&lt;/strong&gt;](../kernel/irp-mj-query-information.md)"><strong>IRP_MJ_QUERY_INFORMATION</strong></a></td>
<td align="left">No direct support; implement <a href="/windows-hardware/drivers/ddi/wdfdevice/nc-wdfdevice-evt_wdfdevice_wdm_irp_preprocess" data-raw-source="[&lt;em&gt;EvtDeviceWdmIrpPreprocess (KMDF only)&lt;/em&gt;](/windows-hardware/drivers/ddi/wdfdevice/nc-wdfdevice-evt_wdfdevice_wdm_irp_preprocess)"><em>EvtDeviceWdmIrpPreprocess (KMDF only)</em></a></td>
</tr>
<tr class="even">
<td align="left"><a href="/windows-hardware/drivers/ifs/irp-mj-query-quota" data-raw-source="[&lt;strong&gt;IRP_MJ_QUERY_QUOTA&lt;/strong&gt;](../ifs/irp-mj-query-quota.md)"><strong>IRP_MJ_QUERY_QUOTA</strong></a></td>
<td align="left">No direct support; implement <a href="/windows-hardware/drivers/ddi/wdfdevice/nc-wdfdevice-evt_wdfdevice_wdm_irp_preprocess" data-raw-source="[&lt;em&gt;EvtDeviceWdmIrpPreprocess (KMDF only)&lt;/em&gt;](/windows-hardware/drivers/ddi/wdfdevice/nc-wdfdevice-evt_wdfdevice_wdm_irp_preprocess)"><em>EvtDeviceWdmIrpPreprocess (KMDF only)</em></a></td>
</tr>
<tr class="odd">
<td align="left"><a href="/windows-hardware/drivers/ifs/irp-mj-query-security" data-raw-source="[&lt;strong&gt;IRP_MJ_QUERY_SECURITY&lt;/strong&gt;](../ifs/irp-mj-query-security.md)"><strong>IRP_MJ_QUERY_SECURITY</strong></a></td>
<td align="left">No direct support; implement <a href="/windows-hardware/drivers/ddi/wdfdevice/nc-wdfdevice-evt_wdfdevice_wdm_irp_preprocess" data-raw-source="[&lt;em&gt;EvtDeviceWdmIrpPreprocess (KMDF only)&lt;/em&gt;](/windows-hardware/drivers/ddi/wdfdevice/nc-wdfdevice-evt_wdfdevice_wdm_irp_preprocess)"><em>EvtDeviceWdmIrpPreprocess (KMDF only)</em></a></td>
</tr>
<tr class="even">
<td align="left"><a href="/windows-hardware/drivers/ifs/irp-mj-query-volume-information" data-raw-source="[&lt;strong&gt;IRP_MJ_QUERY_VOLUME_INFORMATION&lt;/strong&gt;](../ifs/irp-mj-query-volume-information.md)"><strong>IRP_MJ_QUERY_VOLUME_INFORMATION</strong></a></td>
<td align="left">No direct support; implement <a href="/windows-hardware/drivers/ddi/wdfdevice/nc-wdfdevice-evt_wdfdevice_wdm_irp_preprocess" data-raw-source="[&lt;em&gt;EvtDeviceWdmIrpPreprocess (KMDF only)&lt;/em&gt;](/windows-hardware/drivers/ddi/wdfdevice/nc-wdfdevice-evt_wdfdevice_wdm_irp_preprocess)"><em>EvtDeviceWdmIrpPreprocess (KMDF only)</em></a></td>
</tr>
<tr class="odd">
<td align="left"><a href="/windows-hardware/drivers/kernel/irp-mj-read" data-raw-source="[&lt;strong&gt;IRP_MJ_READ&lt;/strong&gt;](../kernel/irp-mj-read.md)"><strong>IRP_MJ_READ</strong></a></td>
<td align="left"><a href="/windows-hardware/drivers/ddi/wdfio/nc-wdfio-evt_wdf_io_queue_io_read" data-raw-source="[&lt;em&gt;EvtIoRead&lt;/em&gt;](/windows-hardware/drivers/ddi/wdfio/nc-wdfio-evt_wdf_io_queue_io_read)"><em>EvtIoRead</em></a> or <a href="/windows-hardware/drivers/ddi/wdfio/nc-wdfio-evt_wdf_io_queue_io_default" data-raw-source="[&lt;em&gt;EvtIoDefault&lt;/em&gt;](/windows-hardware/drivers/ddi/wdfio/nc-wdfio-evt_wdf_io_queue_io_default)"><em>EvtIoDefault</em></a></td>
</tr>
<tr class="even">
<td align="left"><a href="/windows-hardware/drivers/ifs/irp-mj-set-ea" data-raw-source="[&lt;strong&gt;IRP_MJ_SET_EA&lt;/strong&gt;](../ifs/irp-mj-set-ea.md)"><strong>IRP_MJ_SET_EA</strong></a></td>
<td align="left">No direct support; implement <a href="/windows-hardware/drivers/ddi/wdfdevice/nc-wdfdevice-evt_wdfdevice_wdm_irp_preprocess" data-raw-source="[&lt;em&gt;EvtDeviceWdmIrpPreprocess (KMDF only)&lt;/em&gt;](/windows-hardware/drivers/ddi/wdfdevice/nc-wdfdevice-evt_wdfdevice_wdm_irp_preprocess)"><em>EvtDeviceWdmIrpPreprocess (KMDF only)</em></a></td>
</tr>
<tr class="odd">
<td align="left"><a href="/windows-hardware/drivers/kernel/irp-mj-set-information" data-raw-source="[&lt;strong&gt;IRP_MJ_SET_INFORMATION&lt;/strong&gt;](../kernel/irp-mj-set-information.md)"><strong>IRP_MJ_SET_INFORMATION</strong></a></td>
<td align="left">No direct support; implement <a href="/windows-hardware/drivers/ddi/wdfdevice/nc-wdfdevice-evt_wdfdevice_wdm_irp_preprocess" data-raw-source="[&lt;em&gt;EvtDeviceWdmIrpPreprocess (KMDF only)&lt;/em&gt;](/windows-hardware/drivers/ddi/wdfdevice/nc-wdfdevice-evt_wdfdevice_wdm_irp_preprocess)"><em>EvtDeviceWdmIrpPreprocess (KMDF only)</em></a></td>
</tr>
<tr class="even">
<td align="left"><a href="/windows-hardware/drivers/ifs/irp-mj-set-quota" data-raw-source="[&lt;strong&gt;IRP_MJ_SET_QUOTA&lt;/strong&gt;](../ifs/irp-mj-set-quota.md)"><strong>IRP_MJ_SET_QUOTA</strong></a></td>
<td align="left">No direct support; implement <a href="/windows-hardware/drivers/ddi/wdfdevice/nc-wdfdevice-evt_wdfdevice_wdm_irp_preprocess" data-raw-source="[&lt;em&gt;EvtDeviceWdmIrpPreprocess (KMDF only)&lt;/em&gt;](/windows-hardware/drivers/ddi/wdfdevice/nc-wdfdevice-evt_wdfdevice_wdm_irp_preprocess)"><em>EvtDeviceWdmIrpPreprocess (KMDF only)</em></a></td>
</tr>
<tr class="odd">
<td align="left"><a href="/windows-hardware/drivers/ifs/irp-mj-set-security" data-raw-source="[&lt;strong&gt;IRP_MJ_SET_SECURITY&lt;/strong&gt;](../ifs/irp-mj-set-security.md)"><strong>IRP_MJ_SET_SECURITY</strong></a></td>
<td align="left">No direct support; implement <a href="/windows-hardware/drivers/ddi/wdfdevice/nc-wdfdevice-evt_wdfdevice_wdm_irp_preprocess" data-raw-source="[&lt;em&gt;EvtDeviceWdmIrpPreprocess (KMDF only)&lt;/em&gt;](/windows-hardware/drivers/ddi/wdfdevice/nc-wdfdevice-evt_wdfdevice_wdm_irp_preprocess)"><em>EvtDeviceWdmIrpPreprocess (KMDF only)</em></a></td>
</tr>
<tr class="even">
<td align="left"><a href="/windows-hardware/drivers/ifs/irp-mj-set-volume-information" data-raw-source="[&lt;strong&gt;IRP_MJ_SET_VOLUME_INFORMATION&lt;/strong&gt;](../ifs/irp-mj-set-volume-information.md)"><strong>IRP_MJ_SET_VOLUME_INFORMATION</strong></a></td>
<td align="left">No direct support; implement <a href="/windows-hardware/drivers/ddi/wdfdevice/nc-wdfdevice-evt_wdfdevice_wdm_irp_preprocess" data-raw-source="[&lt;em&gt;EvtDeviceWdmIrpPreprocess (KMDF only)&lt;/em&gt;](/windows-hardware/drivers/ddi/wdfdevice/nc-wdfdevice-evt_wdfdevice_wdm_irp_preprocess)"><em>EvtDeviceWdmIrpPreprocess (KMDF only)</em></a></td>
</tr>
<tr class="odd">
<td align="left"><a href="/windows-hardware/drivers/kernel/irp-mj-shutdown" data-raw-source="[&lt;strong&gt;IRP_MJ_SHUTDOWN&lt;/strong&gt;](../kernel/irp-mj-shutdown.md)"><strong>IRP_MJ_SHUTDOWN</strong></a></td>
<td align="left"><p>For control device objects, implement <a href="/windows-hardware/drivers/ddi/wdfcontrol/nc-wdfcontrol-evt_wdf_device_shutdown_notification" data-raw-source="[&lt;em&gt;EvtDeviceShutdownNotification (KMDF only)&lt;/em&gt;](/windows-hardware/drivers/ddi/wdfcontrol/nc-wdfcontrol-evt_wdf_device_shutdown_notification)"><em>EvtDeviceShutdownNotification (KMDF only)</em></a></p>
<p>For all Plug and Play device objects: Not supported; implement <a href="/windows-hardware/drivers/ddi/wdfdevice/nc-wdfdevice-evt_wdfdevice_wdm_irp_preprocess" data-raw-source="[&lt;em&gt;EvtDeviceWdmIrpPreprocess (KMDF only)&lt;/em&gt;](/windows-hardware/drivers/ddi/wdfdevice/nc-wdfdevice-evt_wdfdevice_wdm_irp_preprocess)"><em>EvtDeviceWdmIrpPreprocess (KMDF only)</em></a>.</p></td>
</tr>
<tr class="even">
<td align="left"><a href="/windows-hardware/drivers/kernel/irp-mj-system-control" data-raw-source="[&lt;strong&gt;IRP_MJ_SYSTEM_CONTROL&lt;/strong&gt;](../kernel/irp-mj-system-control.md)"><strong>IRP_MJ_SYSTEM_CONTROL</strong></a></td>
<td align="left">Create WDFWMIPROVIDER and WDFWMIINSTANCE objects and implement <strong>EvtWmiXxx (KMDF only)</strong> callbacks.</td>
</tr>
<tr class="odd">
<td align="left"><a href="/windows-hardware/drivers/kernel/irp-mj-write" data-raw-source="[&lt;strong&gt;IRP_MJ_WRITE&lt;/strong&gt;](../kernel/irp-mj-write.md)"><strong>IRP_MJ_WRITE</strong></a></td>
<td align="left"><a href="/windows-hardware/drivers/ddi/wdfio/nc-wdfio-evt_wdf_io_queue_io_write" data-raw-source="[&lt;em&gt;EvtIoWrite&lt;/em&gt;](/windows-hardware/drivers/ddi/wdfio/nc-wdfio-evt_wdf_io_queue_io_write)"><em>EvtIoWrite</em></a> or <a href="/windows-hardware/drivers/ddi/wdfio/nc-wdfio-evt_wdf_io_queue_io_default" data-raw-source="[&lt;em&gt;EvtIoDefault&lt;/em&gt;](/windows-hardware/drivers/ddi/wdfio/nc-wdfio-evt_wdf_io_queue_io_default)"><em>EvtIoDefault</em></a></td>
</tr>
</tbody>
</table>

 

## KMDF Callbacks for IRP\_MJ\_PNP


The following table lists, in order of execution, the KMDF callbacks that correspond to the minor IRP codes for [**IRP\_MJ\_PNP**](../kernel/irp-mj-pnp.md). The arrows indicate whether a WDM FDO handles the IRP as it travels up or down the stack.

**Note**   In a KMDF driver, Plug and Play and power management are integrated operations and the driver does not receive the individual minor [**IRP\_MJ\_PNP**](../kernel/irp-mj-pnp.md) or [**IRP\_MJ\_POWER**](../kernel/irp-mj-power.md) requests. Instead, the framework calls a core set of callbacks at power up and a corresponding set at power down, and calls additional callbacks before and after this core set as appropriate for each individual Plug and Play request. For comprehensive diagrams that show the power-up and power-down sequences, see [Porting PnP and Power Management Functionality](porting-pnp-and-power-management-functionality.md).

 

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
<td align="left">↓<a href="/windows-hardware/drivers/kernel/irp-mn-cancel-remove-device" data-raw-source="[&lt;strong&gt;IRP_MN_CANCEL_REMOVE_DEVICE&lt;/strong&gt;](../kernel/irp-mn-cancel-remove-device.md)"><strong>IRP_MN_CANCEL_REMOVE_DEVICE</strong></a></td>
<td align="left">None</td>
</tr>
<tr class="even">
<td align="left">↓<a href="/windows-hardware/drivers/kernel/irp-mn-cancel-stop-device" data-raw-source="[&lt;strong&gt;IRP_MN_CANCEL_STOP_DEVICE&lt;/strong&gt;](../kernel/irp-mn-cancel-stop-device.md)"><strong>IRP_MN_CANCEL_STOP_DEVICE</strong></a></td>
<td align="left">None</td>
</tr>
<tr class="odd">
<td align="left">↑<a href="/windows-hardware/drivers/kernel/irp-mn-device-usage-notification" data-raw-source="[&lt;strong&gt;IRP_MN_DEVICE_USAGE_NOTIFICATION&lt;/strong&gt;](../kernel/irp-mn-device-usage-notification.md)"><strong>IRP_MN_DEVICE_USAGE_NOTIFICATION</strong></a></td>
<td align="left"><a href="/windows-hardware/drivers/ddi/wdfdevice/nc-wdfdevice-evt_wdf_device_usage_notification" data-raw-source="[&lt;em&gt;EvtDeviceUsageNotification&lt;/em&gt;](/windows-hardware/drivers/ddi/wdfdevice/nc-wdfdevice-evt_wdf_device_usage_notification)"><em>EvtDeviceUsageNotification</em></a></td>
</tr>
<tr class="even">
<td align="left">↓<a href="/windows-hardware/drivers/kernel/irp-mn-eject" data-raw-source="[&lt;strong&gt;IRP_MN_EJECT&lt;/strong&gt;](../kernel/irp-mn-eject.md)"><strong>IRP_MN_EJECT</strong></a></td>
<td align="left"><a href="/windows-hardware/drivers/ddi/wdfpdo/nc-wdfpdo-evt_wdf_device_eject" data-raw-source="[&lt;em&gt;EvtDeviceEject (KMDF only)&lt;/em&gt;](/windows-hardware/drivers/ddi/wdfpdo/nc-wdfpdo-evt_wdf_device_eject)"><em>EvtDeviceEject (KMDF only)</em></a></td>
</tr>
<tr class="odd">
<td align="left">↓<a href="/windows-hardware/drivers/kernel/irp-mn-filter-resource-requirements" data-raw-source="[&lt;strong&gt;IRP_MN_FILTER_RESOURCE_REQUIREMENTS&lt;/strong&gt;](../kernel/irp-mn-filter-resource-requirements.md)"><strong>IRP_MN_FILTER_RESOURCE_REQUIREMENTS</strong></a></td>
<td align="left"><a href="/windows-hardware/drivers/ddi/wdffdo/nc-wdffdo-evt_wdf_device_filter_resource_requirements" data-raw-source="[&lt;em&gt;EvtDeviceFilterRemoveResourceRequirements (KMDF only)&lt;/em&gt;](/windows-hardware/drivers/ddi/wdffdo/nc-wdffdo-evt_wdf_device_filter_resource_requirements)"><em>EvtDeviceFilterRemoveResourceRequirements (KMDF only)</em></a></td>
</tr>
<tr class="even">
<td align="left">↑<a href="/windows-hardware/drivers/kernel/irp-mn-filter-resource-requirements" data-raw-source="[&lt;strong&gt;IRP_MN_FILTER_RESOURCE_REQUIREMENTS&lt;/strong&gt;](../kernel/irp-mn-filter-resource-requirements.md)"><strong>IRP_MN_FILTER_RESOURCE_REQUIREMENTS</strong></a></td>
<td align="left"><a href="/windows-hardware/drivers/ddi/wdffdo/nc-wdffdo-evt_wdf_device_filter_resource_requirements" data-raw-source="[&lt;em&gt;EvtDeviceFilterAddResourceRequirements (KMDF only)&lt;/em&gt;](/windows-hardware/drivers/ddi/wdffdo/nc-wdffdo-evt_wdf_device_filter_resource_requirements)"><em>EvtDeviceFilterAddResourceRequirements (KMDF only)</em></a></td>
</tr>
<tr class="odd">
<td align="left"><a href="/windows-hardware/drivers/kernel/irp-mn-query-bus-information" data-raw-source="[&lt;strong&gt;IRP_MN_QUERY_BUS_INFORMATION&lt;/strong&gt;](../kernel/irp-mn-query-bus-information.md)"><strong>IRP_MN_QUERY_BUS_INFORMATION</strong></a></td>
<td align="left">None. The KMDF driver calls <strong>WdfDeviceInitXxx</strong> methods to set device properties during initialization so that the framework can respond to this query on its own without notifying the driver.</td>
</tr>
<tr class="even">
<td align="left"><a href="/windows-hardware/drivers/kernel/irp-mn-query-capabilities" data-raw-source="[&lt;strong&gt;IRP_MN_QUERY_CAPABILITIES&lt;/strong&gt;](../kernel/irp-mn-query-capabilities.md)"><strong>IRP_MN_QUERY_CAPABILITIES</strong></a></td>
<td align="left">None. The KMDF driver calls <strong>WdfDeviceInitXxx</strong> methods to set device properties during initialization so that the framework can respond to this query on its own without notifying the driver.</td>
</tr>
<tr class="odd">
<td align="left">↓<a href="/windows-hardware/drivers/kernel/irp-mn-query-device-relations" data-raw-source="[&lt;strong&gt;IRP_MN_QUERY_DEVICE_RELATIONS&lt;/strong&gt;](../kernel/irp-mn-query-device-relations.md)"><strong>IRP_MN_QUERY_DEVICE_RELATIONS</strong></a> (bus, removal, and ejection relations)</td>
<td align="left"><a href="/windows-hardware/drivers/ddi/wdfdevice/nc-wdfdevice-evt_wdf_device_relations_query" data-raw-source="[&lt;em&gt;EvtDeviceRelationsQuery&lt;/em&gt;](/windows-hardware/drivers/ddi/wdfdevice/nc-wdfdevice-evt_wdf_device_relations_query)"><em>EvtDeviceRelationsQuery</em></a></td>
</tr>
<tr class="even">
<td align="left"><a href="/windows-hardware/drivers/kernel/irp-mn-query-device-text" data-raw-source="[&lt;strong&gt;IRP_MN_QUERY_DEVICE_TEXT&lt;/strong&gt;](../kernel/irp-mn-query-device-text.md)"><strong>IRP_MN_QUERY_DEVICE_TEXT</strong></a></td>
<td align="left">None. The KMDF driver calls <strong>WdfDeviceInitXxx</strong> methods to set device properties during initialization so that the framework can respond to this query on its own without notifying the driver.</td>
</tr>
<tr class="odd">
<td align="left"><a href="/windows-hardware/drivers/kernel/irp-mn-query-id" data-raw-source="[&lt;strong&gt;IRP_MN_QUERY_ID&lt;/strong&gt;](../kernel/irp-mn-query-id.md)"><strong>IRP_MN_QUERY_ID</strong></a></td>
<td align="left">None. The KMDF driver calls <strong>WdfDeviceInitXxx</strong> methods to set device properties during initialization so that the framework can respond to this query on its own without notifying the driver.</td>
</tr>
<tr class="even">
<td align="left">↓<a href="/windows-hardware/drivers/kernel/irp-mn-query-interface" data-raw-source="[&lt;strong&gt;IRP_MN_QUERY_INTERFACE&lt;/strong&gt;](../kernel/irp-mn-query-interface.md)"><strong>IRP_MN_QUERY_INTERFACE</strong></a></td>
<td align="left"><a href="/windows-hardware/drivers/ddi/wdfqueryinterface/nc-wdfqueryinterface-evt_wdf_device_process_query_interface_request" data-raw-source="[&lt;em&gt;EvtDeviceProcessQueryInterfaceRequest (KMDF only)&lt;/em&gt;](/windows-hardware/drivers/ddi/wdfqueryinterface/nc-wdfqueryinterface-evt_wdf_device_process_query_interface_request)"><em>EvtDeviceProcessQueryInterfaceRequest (KMDF only)</em></a></td>
</tr>
<tr class="odd">
<td align="left"><a href="/windows-hardware/drivers/kernel/irp-mn-query-pnp-device-state" data-raw-source="[&lt;strong&gt;IRP_MN_QUERY_PNP_DEVICE_STATE&lt;/strong&gt;](../kernel/irp-mn-query-pnp-device-state.md)"><strong>IRP_MN_QUERY_PNP_DEVICE_STATE</strong></a></td>
<td align="left">None. The KMDF driver calls <strong>WdfDeviceInitXxx</strong> methods to set device properties during initialization so that the framework can respond to this query on its own without notifying the driver.</td>
</tr>
<tr class="even">
<td align="left">↓<a href="/windows-hardware/drivers/kernel/irp-mn-query-remove-device" data-raw-source="[&lt;strong&gt;IRP_MN_QUERY_REMOVE_DEVICE&lt;/strong&gt;](../kernel/irp-mn-query-remove-device.md)"><strong>IRP_MN_QUERY_REMOVE_DEVICE</strong></a></td>
<td align="left"><a href="/windows-hardware/drivers/ddi/wdfdevice/nc-wdfdevice-evt_wdf_device_query_remove" data-raw-source="[&lt;em&gt;EvtDeviceQueryRemove&lt;/em&gt;](/windows-hardware/drivers/ddi/wdfdevice/nc-wdfdevice-evt_wdf_device_query_remove)"><em>EvtDeviceQueryRemove</em></a></td>
</tr>
<tr class="odd">
<td align="left">↓<a href="/windows-hardware/drivers/kernel/irp-mn-query-resource-requirements" data-raw-source="[&lt;strong&gt;IRP_MN_QUERY_RESOURCE_REQUIREMENTS&lt;/strong&gt;](../kernel/irp-mn-query-resource-requirements.md)"><strong>IRP_MN_QUERY_RESOURCE_REQUIREMENTS</strong></a></td>
<td align="left"><a href="/windows-hardware/drivers/ddi/wdfpdo/nc-wdfpdo-evt_wdf_device_resource_requirements_query" data-raw-source="[&lt;em&gt;EvtDeviceResourceRequirementsQuery (KMDF only)&lt;/em&gt;](/windows-hardware/drivers/ddi/wdfpdo/nc-wdfpdo-evt_wdf_device_resource_requirements_query)"><em>EvtDeviceResourceRequirementsQuery (KMDF only)</em></a></td>
</tr>
<tr class="even">
<td align="left">↓<a href="/windows-hardware/drivers/kernel/irp-mn-query-resources" data-raw-source="[&lt;strong&gt;IRP_MN_QUERY_RESOURCES&lt;/strong&gt;](../kernel/irp-mn-query-resources.md)"><strong>IRP_MN_QUERY_RESOURCES</strong></a></td>
<td align="left"><a href="/windows-hardware/drivers/ddi/wdfpdo/nc-wdfpdo-evt_wdf_device_resources_query" data-raw-source="[&lt;em&gt;EvtDeviceResourcesQuery (KMDF only)&lt;/em&gt;](/windows-hardware/drivers/ddi/wdfpdo/nc-wdfpdo-evt_wdf_device_resources_query)"><em>EvtDeviceResourcesQuery (KMDF only)</em></a></td>
</tr>
<tr class="odd">
<td align="left">↓<a href="/windows-hardware/drivers/kernel/irp-mn-query-stop-device" data-raw-source="[&lt;strong&gt;IRP_MN_QUERY_STOP_DEVICE&lt;/strong&gt;](../kernel/irp-mn-query-stop-device.md)"><strong>IRP_MN_QUERY_STOP_DEVICE</strong></a></td>
<td align="left"><a href="/windows-hardware/drivers/ddi/wdfdevice/nc-wdfdevice-evt_wdf_device_query_stop" data-raw-source="[&lt;em&gt;EvtDeviceQueryStop&lt;/em&gt;](/windows-hardware/drivers/ddi/wdfdevice/nc-wdfdevice-evt_wdf_device_query_stop)"><em>EvtDeviceQueryStop</em></a></td>
</tr>
<tr class="even">
<td align="left"><a href="/windows-hardware/drivers/kernel/irp-mn-read-config" data-raw-source="[&lt;strong&gt;IRP_MN_READ_CONFIG&lt;/strong&gt;](../kernel/irp-mn-read-config.md)"><strong>IRP_MN_READ_CONFIG</strong></a></td>
<td align="left">None. The KMDF driver calls <strong>WdfDeviceInitXxx</strong> methods to set device properties during initialization so that the framework can respond to this query on its own without notifying the driver.</td>
</tr>
<tr class="odd">
<td align="left">↓<a href="/windows-hardware/drivers/kernel/irp-mn-remove-device" data-raw-source="[&lt;strong&gt;IRP_MN_REMOVE_DEVICE&lt;/strong&gt;](../kernel/irp-mn-remove-device.md)"><strong>IRP_MN_REMOVE_DEVICE</strong></a></td>
<td align="left"><p>After <a href="/windows-hardware/drivers/kernel/irp-mn-query-remove-device" data-raw-source="[&lt;strong&gt;IRP_MN_QUERY_REMOVE_DEVICE&lt;/strong&gt;](../kernel/irp-mn-query-remove-device.md)"><strong>IRP_MN_QUERY_REMOVE_DEVICE</strong></a>:</p>
<a href="/windows-hardware/drivers/ddi/wdfdevice/nc-wdfdevice-evt_wdf_device_self_managed_io_suspend" data-raw-source="[&lt;em&gt;EvtDeviceSelfManagedIoSuspend&lt;/em&gt;](/windows-hardware/drivers/ddi/wdfdevice/nc-wdfdevice-evt_wdf_device_self_managed_io_suspend)"><em>EvtDeviceSelfManagedIoSuspend</em></a>
<a href="/windows-hardware/drivers/ddi/wdfio/nc-wdfio-evt_wdf_io_queue_io_stop" data-raw-source="[&lt;em&gt;EvtIoStop&lt;/em&gt;](/windows-hardware/drivers/ddi/wdfio/nc-wdfio-evt_wdf_io_queue_io_stop)"><em>EvtIoStop</em></a> (<strong>WdfRequestStopActionSuspend</strong> flag)
<a href="/windows-hardware/drivers/ddi/wdfdmaenabler/nc-wdfdmaenabler-evt_wdf_dma_enabler_selfmanaged_io_stop" data-raw-source="[&lt;em&gt;EvtDmaEnablerSelfManagedIoStop (KMDF only)&lt;/em&gt;](/windows-hardware/drivers/ddi/wdfdmaenabler/nc-wdfdmaenabler-evt_wdf_dma_enabler_selfmanaged_io_stop)"><em>EvtDmaEnablerSelfManagedIoStop (KMDF only)</em></a>
<a href="/windows-hardware/drivers/ddi/wdfdmaenabler/nc-wdfdmaenabler-evt_wdf_dma_enabler_disable" data-raw-source="[&lt;em&gt;EvtDmaEnablerDisable (KMDF only)&lt;/em&gt;](/windows-hardware/drivers/ddi/wdfdmaenabler/nc-wdfdmaenabler-evt_wdf_dma_enabler_disable)"><em>EvtDmaEnablerDisable (KMDF only)</em></a>
<a href="/windows-hardware/drivers/ddi/wdfdmaenabler/nc-wdfdmaenabler-evt_wdf_dma_enabler_flush" data-raw-source="[&lt;em&gt;EvtDmaEnablerFlush (KMDF only)&lt;/em&gt;](/windows-hardware/drivers/ddi/wdfdmaenabler/nc-wdfdmaenabler-evt_wdf_dma_enabler_flush)"><em>EvtDmaEnablerFlush (KMDF only)</em></a>
<a href="/windows-hardware/drivers/ddi/wdfdevice/nc-wdfdevice-evt_wdf_device_d0_exit_pre_interrupts_disabled" data-raw-source="[&lt;em&gt;EvtDeviceD0ExitPreInterruptsDisabled&lt;/em&gt;](/windows-hardware/drivers/ddi/wdfdevice/nc-wdfdevice-evt_wdf_device_d0_exit_pre_interrupts_disabled)"><em>EvtDeviceD0ExitPreInterruptsDisabled</em></a>
<a href="/windows-hardware/drivers/ddi/wdfinterrupt/nc-wdfinterrupt-evt_wdf_interrupt_disable" data-raw-source="[&lt;em&gt;EvtInterruptDisable&lt;/em&gt;](/windows-hardware/drivers/ddi/wdfinterrupt/nc-wdfinterrupt-evt_wdf_interrupt_disable)"><em>EvtInterruptDisable</em></a>
<a href="/windows-hardware/drivers/ddi/wdfdevice/nc-wdfdevice-evt_wdf_device_d0_exit" data-raw-source="[&lt;em&gt;EvtDeviceD0Exit&lt;/em&gt;](/windows-hardware/drivers/ddi/wdfdevice/nc-wdfdevice-evt_wdf_device_d0_exit)"><em>EvtDeviceD0Exit</em></a> (<strong>WdfPowerDeviceD3Final</strong> state)
<a href="/windows-hardware/drivers/ddi/wdfdevice/nc-wdfdevice-evt_wdf_device_release_hardware" data-raw-source="[&lt;em&gt;EvtDeviceReleaseHardware&lt;/em&gt;](/windows-hardware/drivers/ddi/wdfdevice/nc-wdfdevice-evt_wdf_device_release_hardware)"><em>EvtDeviceReleaseHardware</em></a>
<a href="/windows-hardware/drivers/ddi/wdfio/nc-wdfio-evt_wdf_io_queue_io_stop" data-raw-source="[&lt;em&gt;EvtIoStop&lt;/em&gt;](/windows-hardware/drivers/ddi/wdfio/nc-wdfio-evt_wdf_io_queue_io_stop)"><em>EvtIoStop</em></a> (<strong>WdfRequestStopActionPurge</strong> flag) for power-managed queues
<a href="/windows-hardware/drivers/ddi/wdfdevice/nc-wdfdevice-evt_wdf_device_self_managed_io_flush" data-raw-source="[&lt;em&gt;EvtDeviceSelfManagedIoFlush&lt;/em&gt;](/windows-hardware/drivers/ddi/wdfdevice/nc-wdfdevice-evt_wdf_device_self_managed_io_flush)"><em>EvtDeviceSelfManagedIoFlush</em></a>
<a href="/windows-hardware/drivers/ddi/wdfio/nc-wdfio-evt_wdf_io_queue_io_stop" data-raw-source="[&lt;em&gt;EvtIoStop&lt;/em&gt;](/windows-hardware/drivers/ddi/wdfio/nc-wdfio-evt_wdf_io_queue_io_stop)"><em>EvtIoStop</em></a> (<strong>WdfRequestStopActionPurge</strong> flag) for non-power-managed queues
<a href="/windows-hardware/drivers/ddi/wdfdevice/nc-wdfdevice-evt_wdf_device_self_managed_io_cleanup" data-raw-source="[&lt;em&gt;EvtDeviceSelfManagedIoCleanup&lt;/em&gt;](/windows-hardware/drivers/ddi/wdfdevice/nc-wdfdevice-evt_wdf_device_self_managed_io_cleanup)"><em>EvtDeviceSelfManagedIoCleanup</em></a>
<a href="/windows-hardware/drivers/ddi/wdfobject/nc-wdfobject-evt_wdf_object_context_cleanup" data-raw-source="[&lt;em&gt;EvtCleanupCallback&lt;/em&gt;](/windows-hardware/drivers/ddi/wdfobject/nc-wdfobject-evt_wdf_object_context_cleanup)"><em>EvtCleanupCallback</em></a> for WDFDEVICE
<a href="/windows-hardware/drivers/ddi/wdfobject/nc-wdfobject-evt_wdf_object_context_destroy" data-raw-source="[&lt;em&gt;EvtDestroyCallback&lt;/em&gt;](/windows-hardware/drivers/ddi/wdfobject/nc-wdfobject-evt_wdf_object_context_destroy)"><em>EvtDestroyCallback</em></a> for WDFDEVICE
<p>After <a href="/windows-hardware/drivers/kernel/irp-mn-surprise-removal" data-raw-source="[&lt;strong&gt;IRP_MN_SURPRISE_REMOVAL&lt;/strong&gt;](../kernel/irp-mn-surprise-removal.md)"><strong>IRP_MN_SURPRISE_REMOVAL</strong></a>:</p>
<a href="/windows-hardware/drivers/ddi/wdfio/nc-wdfio-evt_wdf_io_queue_io_stop" data-raw-source="[&lt;em&gt;EvtIoStop&lt;/em&gt;](/windows-hardware/drivers/ddi/wdfio/nc-wdfio-evt_wdf_io_queue_io_stop)"><em>EvtIoStop</em></a> (<strong>WdfRequestStopActionPurge</strong> flag) for non-power-managed queues
<a href="/windows-hardware/drivers/ddi/wdfdevice/nc-wdfdevice-evt_wdf_device_self_managed_io_cleanup" data-raw-source="[&lt;em&gt;EvtDeviceSelfManagedIoCleanup&lt;/em&gt;](/windows-hardware/drivers/ddi/wdfdevice/nc-wdfdevice-evt_wdf_device_self_managed_io_cleanup)"><em>EvtDeviceSelfManagedIoCleanup</em></a>
<a href="/windows-hardware/drivers/ddi/wdfobject/nc-wdfobject-evt_wdf_object_context_cleanup" data-raw-source="[&lt;em&gt;EvtCleanupCallback&lt;/em&gt;](/windows-hardware/drivers/ddi/wdfobject/nc-wdfobject-evt_wdf_object_context_cleanup)"><em>EvtCleanupCallback</em></a> for WDFDEVICE
<a href="/windows-hardware/drivers/ddi/wdfobject/nc-wdfobject-evt_wdf_object_context_destroy" data-raw-source="[&lt;em&gt;EvtDestroyCallback&lt;/em&gt;](/windows-hardware/drivers/ddi/wdfobject/nc-wdfobject-evt_wdf_object_context_destroy)"><em>EvtDestroyCallback</em></a> for WDFDEVICE</td>
</tr>
<tr class="even">
<td align="left">↓<a href="/windows-hardware/drivers/kernel/irp-mn-set-lock" data-raw-source="[&lt;strong&gt;IRP_MN_SET_LOCK&lt;/strong&gt;](../kernel/irp-mn-set-lock.md)"><strong>IRP_MN_SET_LOCK</strong></a></td>
<td align="left"><a href="/windows-hardware/drivers/ddi/wdfpdo/nc-wdfpdo-evt_wdf_device_set_lock" data-raw-source="[&lt;em&gt;EvtDeviceSetLock (KMDF only)&lt;/em&gt;](/windows-hardware/drivers/ddi/wdfpdo/nc-wdfpdo-evt_wdf_device_set_lock)"><em>EvtDeviceSetLock (KMDF only)</em></a></td>
</tr>
<tr class="odd">
<td align="left">↑<a href="/windows-hardware/drivers/kernel/irp-mn-start-device" data-raw-source="[&lt;strong&gt;IRP_MN_START_DEVICE&lt;/strong&gt;](../kernel/irp-mn-start-device.md)"><strong>IRP_MN_START_DEVICE</strong></a></td>
<td align="left"><p>After enumeration:</p>
<a href="/windows-hardware/drivers/ddi/wdffdo/nc-wdffdo-evt_wdf_device_remove_added_resources" data-raw-source="[&lt;em&gt;EvtDeviceRemoveAddedResources (KMDF only)&lt;/em&gt;](/windows-hardware/drivers/ddi/wdffdo/nc-wdffdo-evt_wdf_device_remove_added_resources)"><em>EvtDeviceRemoveAddedResources (KMDF only)</em></a>
<a href="/windows-hardware/drivers/ddi/wdfdevice/nc-wdfdevice-evt_wdf_device_prepare_hardware" data-raw-source="[&lt;em&gt;EvtDevicePrepareHardware&lt;/em&gt;](/windows-hardware/drivers/ddi/wdfdevice/nc-wdfdevice-evt_wdf_device_prepare_hardware)"><em>EvtDevicePrepareHardware</em></a>
<a href="/windows-hardware/drivers/ddi/wdfdevice/nc-wdfdevice-evt_wdf_device_d0_entry" data-raw-source="[&lt;em&gt;EvtDeviceD0Entry&lt;/em&gt;](/windows-hardware/drivers/ddi/wdfdevice/nc-wdfdevice-evt_wdf_device_d0_entry)"><em>EvtDeviceD0Entry</em></a>
<a href="/windows-hardware/drivers/ddi/wdfinterrupt/nc-wdfinterrupt-evt_wdf_interrupt_enable" data-raw-source="[&lt;em&gt;EvtInterruptEnable&lt;/em&gt;](/windows-hardware/drivers/ddi/wdfinterrupt/nc-wdfinterrupt-evt_wdf_interrupt_enable)"><em>EvtInterruptEnable</em></a>
<a href="/windows-hardware/drivers/ddi/wdfdevice/nc-wdfdevice-evt_wdf_device_d0_entry_post_interrupts_enabled" data-raw-source="[&lt;em&gt;EvtDeviceD0EntryPostInterruptsEnabled&lt;/em&gt;](/windows-hardware/drivers/ddi/wdfdevice/nc-wdfdevice-evt_wdf_device_d0_entry_post_interrupts_enabled)"><em>EvtDeviceD0EntryPostInterruptsEnabled</em></a>
<a href="/windows-hardware/drivers/ddi/wdfdmaenabler/nc-wdfdmaenabler-evt_wdf_dma_enabler_fill" data-raw-source="[&lt;em&gt;EvtDmaEnablerFill (KMDF only)&lt;/em&gt;](/windows-hardware/drivers/ddi/wdfdmaenabler/nc-wdfdmaenabler-evt_wdf_dma_enabler_fill)"><em>EvtDmaEnablerFill (KMDF only)</em></a>
<a href="/windows-hardware/drivers/ddi/wdfdmaenabler/nc-wdfdmaenabler-evt_wdf_dma_enabler_enable" data-raw-source="[&lt;em&gt;EvtDmaEnablerEnable (KMDF only)&lt;/em&gt;](/windows-hardware/drivers/ddi/wdfdmaenabler/nc-wdfdmaenabler-evt_wdf_dma_enabler_enable)"><em>EvtDmaEnablerEnable (KMDF only)</em></a>
<a href="/windows-hardware/drivers/ddi/wdfdmaenabler/nc-wdfdmaenabler-evt_wdf_dma_enabler_selfmanaged_io_start" data-raw-source="[&lt;em&gt;EvtDmaEnablerSelfManagedIoStart (KMDF only)&lt;/em&gt;](/windows-hardware/drivers/ddi/wdfdmaenabler/nc-wdfdmaenabler-evt_wdf_dma_enabler_selfmanaged_io_start)"><em>EvtDmaEnablerSelfManagedIoStart (KMDF only)</em></a>
<a href="/windows-hardware/drivers/ddi/wdfdevice/nc-wdfdevice-evt_wdf_device_self_managed_io_init" data-raw-source="[&lt;em&gt;EvtDeviceSelfManagedIoInit&lt;/em&gt;](/windows-hardware/drivers/ddi/wdfdevice/nc-wdfdevice-evt_wdf_device_self_managed_io_init)"><em>EvtDeviceSelfManagedIoInit</em></a>
<p>After <a href="/windows-hardware/drivers/kernel/irp-mn-stop-device" data-raw-source="[&lt;strong&gt;IRP_MN_STOP_DEVICE&lt;/strong&gt;](../kernel/irp-mn-stop-device.md)"><strong>IRP_MN_STOP_DEVICE</strong></a>:</p>
<a href="/windows-hardware/drivers/ddi/wdffdo/nc-wdffdo-evt_wdf_device_remove_added_resources" data-raw-source="[&lt;em&gt;EvtDeviceRemoveAddedResources (KMDF only)&lt;/em&gt;](/windows-hardware/drivers/ddi/wdffdo/nc-wdffdo-evt_wdf_device_remove_added_resources)"><em>EvtDeviceRemoveAddedResources (KMDF only)</em></a>
<a href="/windows-hardware/drivers/ddi/wdfdevice/nc-wdfdevice-evt_wdf_device_prepare_hardware" data-raw-source="[&lt;em&gt;EvtDevicePrepareHardware&lt;/em&gt;](/windows-hardware/drivers/ddi/wdfdevice/nc-wdfdevice-evt_wdf_device_prepare_hardware)"><em>EvtDevicePrepareHardware</em></a>
<a href="/windows-hardware/drivers/ddi/wdfdevice/nc-wdfdevice-evt_wdf_device_d0_entry" data-raw-source="[&lt;em&gt;EvtDeviceD0Entry&lt;/em&gt;](/windows-hardware/drivers/ddi/wdfdevice/nc-wdfdevice-evt_wdf_device_d0_entry)"><em>EvtDeviceD0Entry</em></a>
<a href="/windows-hardware/drivers/ddi/wdfinterrupt/nc-wdfinterrupt-evt_wdf_interrupt_enable" data-raw-source="[&lt;em&gt;EvtInterruptEnable&lt;/em&gt;](/windows-hardware/drivers/ddi/wdfinterrupt/nc-wdfinterrupt-evt_wdf_interrupt_enable)"><em>EvtInterruptEnable</em></a>
<a href="/windows-hardware/drivers/ddi/wdfdevice/nc-wdfdevice-evt_wdf_device_d0_entry_post_interrupts_enabled" data-raw-source="[&lt;em&gt;EvtDeviceD0EntryPostInterruptsEnabled&lt;/em&gt;](/windows-hardware/drivers/ddi/wdfdevice/nc-wdfdevice-evt_wdf_device_d0_entry_post_interrupts_enabled)"><em>EvtDeviceD0EntryPostInterruptsEnabled</em></a>
<a href="/windows-hardware/drivers/ddi/wdfdmaenabler/nc-wdfdmaenabler-evt_wdf_dma_enabler_fill" data-raw-source="[&lt;em&gt;EvtDmaEnablerFill (KMDF only)&lt;/em&gt;](/windows-hardware/drivers/ddi/wdfdmaenabler/nc-wdfdmaenabler-evt_wdf_dma_enabler_fill)"><em>EvtDmaEnablerFill (KMDF only)</em></a>
<a href="/windows-hardware/drivers/ddi/wdfdmaenabler/nc-wdfdmaenabler-evt_wdf_dma_enabler_enable" data-raw-source="[&lt;em&gt;EvtDmaEnablerEnable (KMDF only)&lt;/em&gt;](/windows-hardware/drivers/ddi/wdfdmaenabler/nc-wdfdmaenabler-evt_wdf_dma_enabler_enable)"><em>EvtDmaEnablerEnable (KMDF only)</em></a>
<a href="/windows-hardware/drivers/ddi/wdfdmaenabler/nc-wdfdmaenabler-evt_wdf_dma_enabler_selfmanaged_io_start" data-raw-source="[&lt;em&gt;EvtDmaEnablerSelfManagedIoStart (KMDF only)&lt;/em&gt;](/windows-hardware/drivers/ddi/wdfdmaenabler/nc-wdfdmaenabler-evt_wdf_dma_enabler_selfmanaged_io_start)"><em>EvtDmaEnablerSelfManagedIoStart (KMDF only)</em></a>
<a href="/windows-hardware/drivers/ddi/wdfio/nc-wdfio-evt_wdf_io_queue_io_resume" data-raw-source="[&lt;em&gt;EvtIoResume&lt;/em&gt;](/windows-hardware/drivers/ddi/wdfio/nc-wdfio-evt_wdf_io_queue_io_resume)"><em>EvtIoResume</em></a>
<a href="/windows-hardware/drivers/ddi/wdfdevice/nc-wdfdevice-evt_wdf_device_self_managed_io_restart" data-raw-source="[&lt;em&gt;EvtDeviceSelfManagedIoRestart&lt;/em&gt;](/windows-hardware/drivers/ddi/wdfdevice/nc-wdfdevice-evt_wdf_device_self_managed_io_restart)"><em>EvtDeviceSelfManagedIoRestart</em></a></td>
</tr>
<tr class="even">
<td align="left">↓<a href="/windows-hardware/drivers/kernel/irp-mn-stop-device" data-raw-source="[&lt;strong&gt;IRP_MN_STOP_DEVICE&lt;/strong&gt;](../kernel/irp-mn-stop-device.md)"><strong>IRP_MN_STOP_DEVICE</strong></a></td>
<td align="left"><a href="/windows-hardware/drivers/ddi/wdfdevice/nc-wdfdevice-evt_wdf_device_self_managed_io_suspend" data-raw-source="[&lt;em&gt;EvtDeviceSelfManagedIoSuspend&lt;/em&gt;](/windows-hardware/drivers/ddi/wdfdevice/nc-wdfdevice-evt_wdf_device_self_managed_io_suspend)"><em>EvtDeviceSelfManagedIoSuspend</em></a>
<a href="/windows-hardware/drivers/ddi/wdfio/nc-wdfio-evt_wdf_io_queue_io_stop" data-raw-source="[&lt;em&gt;EvtIoStop&lt;/em&gt;](/windows-hardware/drivers/ddi/wdfio/nc-wdfio-evt_wdf_io_queue_io_stop)"><em>EvtIoStop</em></a> (<strong>WdfRequestStopActionSuspend</strong> flag)
<a href="/windows-hardware/drivers/ddi/wdfdmaenabler/nc-wdfdmaenabler-evt_wdf_dma_enabler_selfmanaged_io_stop" data-raw-source="[&lt;em&gt;EvtDmaEnablerSelfManagedIoStop (KMDF only)&lt;/em&gt;](/windows-hardware/drivers/ddi/wdfdmaenabler/nc-wdfdmaenabler-evt_wdf_dma_enabler_selfmanaged_io_stop)"><em>EvtDmaEnablerSelfManagedIoStop (KMDF only)</em></a>
<a href="/windows-hardware/drivers/ddi/wdfdmaenabler/nc-wdfdmaenabler-evt_wdf_dma_enabler_disable" data-raw-source="[&lt;em&gt;EvtDmaEnablerDisable (KMDF only)&lt;/em&gt;](/windows-hardware/drivers/ddi/wdfdmaenabler/nc-wdfdmaenabler-evt_wdf_dma_enabler_disable)"><em>EvtDmaEnablerDisable (KMDF only)</em></a>
<a href="/windows-hardware/drivers/ddi/wdfdmaenabler/nc-wdfdmaenabler-evt_wdf_dma_enabler_flush" data-raw-source="[&lt;em&gt;EvtDmaEnablerFlush (KMDF only)&lt;/em&gt;](/windows-hardware/drivers/ddi/wdfdmaenabler/nc-wdfdmaenabler-evt_wdf_dma_enabler_flush)"><em>EvtDmaEnablerFlush (KMDF only)</em></a>
<a href="/windows-hardware/drivers/ddi/wdfdevice/nc-wdfdevice-evt_wdf_device_d0_exit_pre_interrupts_disabled" data-raw-source="[&lt;em&gt;EvtDeviceD0ExitPreInterruptsDisabled&lt;/em&gt;](/windows-hardware/drivers/ddi/wdfdevice/nc-wdfdevice-evt_wdf_device_d0_exit_pre_interrupts_disabled)"><em>EvtDeviceD0ExitPreInterruptsDisabled</em></a>
<a href="/windows-hardware/drivers/ddi/wdfinterrupt/nc-wdfinterrupt-evt_wdf_interrupt_disable" data-raw-source="[&lt;em&gt;EvtInterruptDisable&lt;/em&gt;](/windows-hardware/drivers/ddi/wdfinterrupt/nc-wdfinterrupt-evt_wdf_interrupt_disable)"><em>EvtInterruptDisable</em></a>
<a href="/windows-hardware/drivers/ddi/wdfdevice/nc-wdfdevice-evt_wdf_device_d0_exit" data-raw-source="[&lt;em&gt;EvtDeviceD0Exit&lt;/em&gt;](/windows-hardware/drivers/ddi/wdfdevice/nc-wdfdevice-evt_wdf_device_d0_exit)"><em>EvtDeviceD0Exit</em></a> (<strong>WdfPowerDeviceD3Final</strong> state)
<a href="/windows-hardware/drivers/ddi/wdfdevice/nc-wdfdevice-evt_wdf_device_release_hardware" data-raw-source="[&lt;em&gt;EvtDeviceReleaseHardware&lt;/em&gt;](/windows-hardware/drivers/ddi/wdfdevice/nc-wdfdevice-evt_wdf_device_release_hardware)"><em>EvtDeviceReleaseHardware</em></a></td>
</tr>
<tr class="odd">
<td align="left">↓<a href="/windows-hardware/drivers/kernel/irp-mn-surprise-removal" data-raw-source="[&lt;strong&gt;IRP_MN_SURPRISE_REMOVAL&lt;/strong&gt;](../kernel/irp-mn-surprise-removal.md)"><strong>IRP_MN_SURPRISE_REMOVAL</strong></a></td>
<td align="left"><a href="/windows-hardware/drivers/ddi/wdfdevice/nc-wdfdevice-evt_wdf_device_surprise_removal" data-raw-source="[&lt;em&gt;EvtDeviceSurpriseRemoval&lt;/em&gt;](/windows-hardware/drivers/ddi/wdfdevice/nc-wdfdevice-evt_wdf_device_surprise_removal)"><em>EvtDeviceSurpriseRemoval</em></a>
<a href="/windows-hardware/drivers/ddi/wdfdevice/nc-wdfdevice-evt_wdf_device_self_managed_io_suspend" data-raw-source="[&lt;em&gt;EvtDeviceSelfManagedIoSuspend&lt;/em&gt;](/windows-hardware/drivers/ddi/wdfdevice/nc-wdfdevice-evt_wdf_device_self_managed_io_suspend)"><em>EvtDeviceSelfManagedIoSuspend</em></a>
<a href="/windows-hardware/drivers/ddi/wdfio/nc-wdfio-evt_wdf_io_queue_io_stop" data-raw-source="[&lt;em&gt;EvtIoStop&lt;/em&gt;](/windows-hardware/drivers/ddi/wdfio/nc-wdfio-evt_wdf_io_queue_io_stop)"><em>EvtIoStop</em></a> (<strong>WdfRequestStopActionSuspend</strong> flag)
<a href="/windows-hardware/drivers/ddi/wdfdmaenabler/nc-wdfdmaenabler-evt_wdf_dma_enabler_selfmanaged_io_stop" data-raw-source="[&lt;em&gt;EvtDmaEnablerSelfManagedIoStop (KMDF only)&lt;/em&gt;](/windows-hardware/drivers/ddi/wdfdmaenabler/nc-wdfdmaenabler-evt_wdf_dma_enabler_selfmanaged_io_stop)"><em>EvtDmaEnablerSelfManagedIoStop (KMDF only)</em></a>
<a href="/windows-hardware/drivers/ddi/wdfdmaenabler/nc-wdfdmaenabler-evt_wdf_dma_enabler_disable" data-raw-source="[&lt;em&gt;EvtDmaEnablerDisable (KMDF only)&lt;/em&gt;](/windows-hardware/drivers/ddi/wdfdmaenabler/nc-wdfdmaenabler-evt_wdf_dma_enabler_disable)"><em>EvtDmaEnablerDisable (KMDF only)</em></a>
<a href="/windows-hardware/drivers/ddi/wdfdmaenabler/nc-wdfdmaenabler-evt_wdf_dma_enabler_flush" data-raw-source="[&lt;em&gt;EvtDmaEnablerFlush (KMDF only)&lt;/em&gt;](/windows-hardware/drivers/ddi/wdfdmaenabler/nc-wdfdmaenabler-evt_wdf_dma_enabler_flush)"><em>EvtDmaEnablerFlush (KMDF only)</em></a>
<a href="/windows-hardware/drivers/ddi/wdfdevice/nc-wdfdevice-evt_wdf_device_d0_exit_pre_interrupts_disabled" data-raw-source="[&lt;em&gt;EvtDeviceD0ExitPreInterruptsDisabled&lt;/em&gt;](/windows-hardware/drivers/ddi/wdfdevice/nc-wdfdevice-evt_wdf_device_d0_exit_pre_interrupts_disabled)"><em>EvtDeviceD0ExitPreInterruptsDisabled</em></a>
<a href="/windows-hardware/drivers/ddi/wdfinterrupt/nc-wdfinterrupt-evt_wdf_interrupt_disable" data-raw-source="[&lt;em&gt;EvtInterruptDisable&lt;/em&gt;](/windows-hardware/drivers/ddi/wdfinterrupt/nc-wdfinterrupt-evt_wdf_interrupt_disable)"><em>EvtInterruptDisable</em></a>
<a href="/windows-hardware/drivers/ddi/wdfdevice/nc-wdfdevice-evt_wdf_device_d0_exit" data-raw-source="[&lt;em&gt;EvtDeviceD0Exit&lt;/em&gt;](/windows-hardware/drivers/ddi/wdfdevice/nc-wdfdevice-evt_wdf_device_d0_exit)"><em>EvtDeviceD0Exit</em></a> (<strong>WdfPowerDeviceD3Final</strong> state)
<a href="/windows-hardware/drivers/ddi/wdfdevice/nc-wdfdevice-evt_wdf_device_release_hardware" data-raw-source="[&lt;em&gt;EvtDeviceReleaseHardware&lt;/em&gt;](/windows-hardware/drivers/ddi/wdfdevice/nc-wdfdevice-evt_wdf_device_release_hardware)"><em>EvtDeviceReleaseHardware</em></a>
<a href="/windows-hardware/drivers/ddi/wdfio/nc-wdfio-evt_wdf_io_queue_io_stop" data-raw-source="[&lt;em&gt;EvtIoStop&lt;/em&gt;](/windows-hardware/drivers/ddi/wdfio/nc-wdfio-evt_wdf_io_queue_io_stop)"><em>EvtIoStop</em></a> (<strong>WdfRequestStopActionPurge</strong> flag) for power-managed queues
<a href="/windows-hardware/drivers/ddi/wdfdevice/nc-wdfdevice-evt_wdf_device_self_managed_io_flush" data-raw-source="[&lt;em&gt;EvtDeviceSelfManagedIoFlush&lt;/em&gt;](/windows-hardware/drivers/ddi/wdfdevice/nc-wdfdevice-evt_wdf_device_self_managed_io_flush)"><em>EvtDeviceSelfManagedIoFlush</em></a></td>
</tr>
<tr class="even">
<td align="left"><a href="/windows-hardware/drivers/kernel/irp-mn-write-config" data-raw-source="[&lt;strong&gt;IRP_MN_WRITE_CONFIG&lt;/strong&gt;](../kernel/irp-mn-write-config.md)"><strong>IRP_MN_WRITE_CONFIG</strong></a></td>
<td align="left">None. The KMDF driver calls <strong>WdfDeviceInitXxx</strong> methods to set device properties during initialization so that the framework can respond to this query on its own without notifying the driver.</td>
</tr>
</tbody>
</table>

 

## KMDF Callbacks for IRP\_MJ\_POWER


The following table lists, in order of execution, the KMDF callbacks that correspond to the minor IRP codes for [**IRP\_MJ\_POWER**](../kernel/irp-mj-power.md). The arrows indicate whether a WDM FDO handles the IRP as it travels up or down the stack.

**Note**   Note: In a KMDF driver, Plug and Play and power management are integrated operations and the driver does not receive the individual minor [**IRP\_MJ\_PNP**](../kernel/irp-mj-pnp.md) or [**IRP\_MJ\_POWER**](../kernel/irp-mj-power.md) requests. Instead, the framework calls a core set of callbacks at power up and a corresponding set at power down, and calls additional callbacks before and after this core set as appropriate for each individual Plug and Play request. For comprehensive diagrams that show the power-up and power-down sequences, see [Porting PnP and Power Management Functionality](porting-pnp-and-power-management-functionality.md).

 

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
<td align="left">↓<a href="/windows-hardware/drivers/kernel/irp-mn-set-power" data-raw-source="[&lt;strong&gt;IRP_MN_SET_POWER&lt;/strong&gt;](../kernel/irp-mn-set-power.md)"><strong>IRP_MN_SET_POWER</strong></a> for D1, D2, or D3 (power down)</td>
<td align="left"><a href="/windows-hardware/drivers/ddi/wdfdevice/nc-wdfdevice-evt_wdf_device_self_managed_io_suspend" data-raw-source="[&lt;em&gt;EvtDeviceSelfManagedIoSuspend&lt;/em&gt;](/windows-hardware/drivers/ddi/wdfdevice/nc-wdfdevice-evt_wdf_device_self_managed_io_suspend)"><em>EvtDeviceSelfManagedIoSuspend</em></a>
<a href="/windows-hardware/drivers/ddi/wdfio/nc-wdfio-evt_wdf_io_queue_io_stop" data-raw-source="[&lt;em&gt;EvtIoStop&lt;/em&gt;](/windows-hardware/drivers/ddi/wdfio/nc-wdfio-evt_wdf_io_queue_io_stop)"><em>EvtIoStop</em></a> (<strong>WdfRequestStopActionSuspend</strong> flag)
<a href="/windows-hardware/drivers/ddi/wdfdevice/nc-wdfdevice-evt_wdf_device_arm_wake_from_s0" data-raw-source="[&lt;em&gt;EvtDeviceArmWakeFromS0&lt;/em&gt;](/windows-hardware/drivers/ddi/wdfdevice/nc-wdfdevice-evt_wdf_device_arm_wake_from_s0)"><em>EvtDeviceArmWakeFromS0</em></a> or <a href="/windows-hardware/drivers/ddi/wdfdevice/nc-wdfdevice-evt_wdf_device_arm_wake_from_sx" data-raw-source="[&lt;em&gt;EvtDeviceArmWakeFromSx&lt;/em&gt;](/windows-hardware/drivers/ddi/wdfdevice/nc-wdfdevice-evt_wdf_device_arm_wake_from_sx)"><em>EvtDeviceArmWakeFromSx</em></a>
<a href="/windows-hardware/drivers/ddi/wdfdmaenabler/nc-wdfdmaenabler-evt_wdf_dma_enabler_selfmanaged_io_stop" data-raw-source="[&lt;em&gt;EvtDmaEnablerSelfManagedIoStop (KMDF only)&lt;/em&gt;](/windows-hardware/drivers/ddi/wdfdmaenabler/nc-wdfdmaenabler-evt_wdf_dma_enabler_selfmanaged_io_stop)"><em>EvtDmaEnablerSelfManagedIoStop (KMDF only)</em></a>
<a href="/windows-hardware/drivers/ddi/wdfdmaenabler/nc-wdfdmaenabler-evt_wdf_dma_enabler_disable" data-raw-source="[&lt;em&gt;EvtDmaEnablerDisable (KMDF only)&lt;/em&gt;](/windows-hardware/drivers/ddi/wdfdmaenabler/nc-wdfdmaenabler-evt_wdf_dma_enabler_disable)"><em>EvtDmaEnablerDisable (KMDF only)</em></a>
<a href="/windows-hardware/drivers/ddi/wdfdmaenabler/nc-wdfdmaenabler-evt_wdf_dma_enabler_flush" data-raw-source="[&lt;em&gt;EvtDmaEnablerFlush (KMDF only)&lt;/em&gt;](/windows-hardware/drivers/ddi/wdfdmaenabler/nc-wdfdmaenabler-evt_wdf_dma_enabler_flush)"><em>EvtDmaEnablerFlush (KMDF only)</em></a>
<a href="/windows-hardware/drivers/ddi/wdfdevice/nc-wdfdevice-evt_wdf_device_d0_exit_pre_interrupts_disabled" data-raw-source="[&lt;em&gt;EvtDeviceD0ExitPreInterruptsDisabled&lt;/em&gt;](/windows-hardware/drivers/ddi/wdfdevice/nc-wdfdevice-evt_wdf_device_d0_exit_pre_interrupts_disabled)"><em>EvtDeviceD0ExitPreInterruptsDisabled</em></a>
<a href="/windows-hardware/drivers/ddi/wdfinterrupt/nc-wdfinterrupt-evt_wdf_interrupt_disable" data-raw-source="[&lt;em&gt;EvtInterruptDisable&lt;/em&gt;](/windows-hardware/drivers/ddi/wdfinterrupt/nc-wdfinterrupt-evt_wdf_interrupt_disable)"><em>EvtInterruptDisable</em></a>
<a href="/windows-hardware/drivers/ddi/wdfdevice/nc-wdfdevice-evt_wdf_device_d0_exit" data-raw-source="[&lt;em&gt;EvtDeviceD0Exit&lt;/em&gt;](/windows-hardware/drivers/ddi/wdfdevice/nc-wdfdevice-evt_wdf_device_d0_exit)"><em>EvtDeviceD0Exit</em></a></td>
</tr>
<tr class="even">
<td align="left">↑<a href="/windows-hardware/drivers/kernel/irp-mn-set-power" data-raw-source="[&lt;strong&gt;IRP_MN_SET_POWER&lt;/strong&gt;](../kernel/irp-mn-set-power.md)"><strong>IRP_MN_SET_POWER</strong></a> for D0 (power up)</td>
<td align="left"><a href="/windows-hardware/drivers/ddi/wdfdevice/nc-wdfdevice-evt_wdf_device_d0_entry" data-raw-source="[&lt;em&gt;EvtDeviceD0Entry&lt;/em&gt;](/windows-hardware/drivers/ddi/wdfdevice/nc-wdfdevice-evt_wdf_device_d0_entry)"><em>EvtDeviceD0Entry</em></a>
<a href="/windows-hardware/drivers/ddi/wdfinterrupt/nc-wdfinterrupt-evt_wdf_interrupt_enable" data-raw-source="[&lt;em&gt;EvtInterruptEnable&lt;/em&gt;](/windows-hardware/drivers/ddi/wdfinterrupt/nc-wdfinterrupt-evt_wdf_interrupt_enable)"><em>EvtInterruptEnable</em></a>
<a href="/windows-hardware/drivers/ddi/wdfdevice/nc-wdfdevice-evt_wdf_device_d0_entry_post_interrupts_enabled" data-raw-source="[&lt;em&gt;EvtDeviceD0EntryPostInterruptsEnabled&lt;/em&gt;](/windows-hardware/drivers/ddi/wdfdevice/nc-wdfdevice-evt_wdf_device_d0_entry_post_interrupts_enabled)"><em>EvtDeviceD0EntryPostInterruptsEnabled</em></a>
<a href="/windows-hardware/drivers/ddi/wdfdmaenabler/nc-wdfdmaenabler-evt_wdf_dma_enabler_fill" data-raw-source="[&lt;em&gt;EvtDmaEnablerFill (KMDF only)&lt;/em&gt;](/windows-hardware/drivers/ddi/wdfdmaenabler/nc-wdfdmaenabler-evt_wdf_dma_enabler_fill)"><em>EvtDmaEnablerFill (KMDF only)</em></a>
<a href="/windows-hardware/drivers/ddi/wdfdmaenabler/nc-wdfdmaenabler-evt_wdf_dma_enabler_enable" data-raw-source="[&lt;em&gt;EvtDmaEnablerEnable (KMDF only)&lt;/em&gt;](/windows-hardware/drivers/ddi/wdfdmaenabler/nc-wdfdmaenabler-evt_wdf_dma_enabler_enable)"><em>EvtDmaEnablerEnable (KMDF only)</em></a>
<a href="/windows-hardware/drivers/ddi/wdfdmaenabler/nc-wdfdmaenabler-evt_wdf_dma_enabler_selfmanaged_io_start" data-raw-source="[&lt;em&gt;EvtDmaEnablerSelfManagedIoStart (KMDF only)&lt;/em&gt;](/windows-hardware/drivers/ddi/wdfdmaenabler/nc-wdfdmaenabler-evt_wdf_dma_enabler_selfmanaged_io_start)"><em>EvtDmaEnablerSelfManagedIoStart (KMDF only)</em></a>
<a href="/windows-hardware/drivers/ddi/wdfio/nc-wdfio-evt_wdf_io_queue_io_resume" data-raw-source="[&lt;em&gt;EvtIoResume&lt;/em&gt;](/windows-hardware/drivers/ddi/wdfio/nc-wdfio-evt_wdf_io_queue_io_resume)"><em>EvtIoResume</em></a>
<a href="/windows-hardware/drivers/ddi/wdfdevice/nc-wdfdevice-evt_wdf_device_self_managed_io_restart" data-raw-source="[&lt;em&gt;EvtDeviceSelfManagedIoRestart&lt;/em&gt;](/windows-hardware/drivers/ddi/wdfdevice/nc-wdfdevice-evt_wdf_device_self_managed_io_restart)"><em>EvtDeviceSelfManagedIoRestart</em></a></td>
</tr>
<tr class="odd">
<td align="left">↓<a href="/windows-hardware/drivers/kernel/irp-mn-set-power" data-raw-source="[&lt;strong&gt;IRP_MN_SET_POWER&lt;/strong&gt;](../kernel/irp-mn-set-power.md)"><strong>IRP_MN_SET_POWER</strong></a> for Sx</td>
<td align="left">None</td>
</tr>
<tr class="even">
<td align="left">↑<a href="/windows-hardware/drivers/kernel/irp-mn-set-power" data-raw-source="[&lt;strong&gt;IRP_MN_SET_POWER&lt;/strong&gt;](../kernel/irp-mn-set-power.md)"><strong>IRP_MN_SET_POWER</strong></a> for Sx</td>
<td align="left">None</td>
</tr>
<tr class="odd">
<td align="left"><a href="/windows-hardware/drivers/kernel/irp-mn-power-sequence" data-raw-source="[&lt;strong&gt;IRP_MN_POWER_SEQUENCE&lt;/strong&gt;](../kernel/irp-mn-power-sequence.md)"><strong>IRP_MN_POWER_SEQUENCE</strong></a></td>
<td align="left">None</td>
</tr>
<tr class="even">
<td align="left">↓<a href="/windows-hardware/drivers/kernel/irp-mn-wait-wake" data-raw-source="[&lt;strong&gt;IRP_MN_WAIT_WAKE&lt;/strong&gt;](../kernel/irp-mn-wait-wake.md)"><strong>IRP_MN_WAIT_WAKE</strong></a></td>
<td align="left"><a href="/windows-hardware/drivers/ddi/wdfpdo/nc-wdfpdo-evt_wdf_device_enable_wake_at_bus" data-raw-source="[&lt;em&gt;EvtDeviceEnableWakeAtBus (KMDF only)&lt;/em&gt;](/windows-hardware/drivers/ddi/wdfpdo/nc-wdfpdo-evt_wdf_device_enable_wake_at_bus)"><em>EvtDeviceEnableWakeAtBus (KMDF only)</em></a></td>
</tr>
<tr class="odd">
<td align="left">↑<a href="/windows-hardware/drivers/kernel/irp-mn-wait-wake" data-raw-source="[&lt;strong&gt;IRP_MN_WAIT_WAKE&lt;/strong&gt;](../kernel/irp-mn-wait-wake.md)"><strong>IRP_MN_WAIT_WAKE</strong></a></td>
<td align="left"><a href="/windows-hardware/drivers/ddi/wdfpdo/nc-wdfpdo-evt_wdf_device_disable_wake_at_bus" data-raw-source="[&lt;em&gt;EvtDeviceDisableWakeAtBus (KMDF only)&lt;/em&gt;](/windows-hardware/drivers/ddi/wdfpdo/nc-wdfpdo-evt_wdf_device_disable_wake_at_bus)"><em>EvtDeviceDisableWakeAtBus (KMDF only)</em></a></td>
</tr>
</tbody>
</table>

 

