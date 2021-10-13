---
title: How the Port Driver Processes WMI Requests
description: How the Port Driver Processes WMI Requests
keywords:
- WMI SRBs WDK storage , WMI request processing
- callback routines WDK WMI SRBs
- WMI IRPs WDK storage
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# How the Port Driver Processes WMI Requests


## <span id="ddk_how_the_port_driver_processes_wmi_requests_kg"></span><span id="DDK_HOW_THE_PORT_DRIVER_PROCESSES_WMI_REQUESTS_KG"></span>


Windows notifies a storage port driver of a WMI request by sending a I/O request packet (IRP) of type [**IRP\_MJ\_SYSTEM\_CONTROL**](../kernel/irp-mj-system-control.md), as described in [Windows Management Instrumentation](../kernel/implementing-wmi.md). A system control IRP can contain any of the minor IRP numbers that represent WMI operations. For more information, see [WMI Minor IRPs](../kernel/wmi-minor-irps.md).

To use the [Using the SCSI Port WMI Library](using-the-scsi-port-wmi-library.md) to process WMI SRBs, your SCSI miniport driver must provide a series of callback routines that correspond to the WMI minor IRP numbers. The following table illustrates the relationship between the miniport driver callback routines and their corresponding WMI minor IRP numbers.

<table>
<colgroup>
<col width="50%" />
<col width="50%" />
</colgroup>
<thead>
<tr class="header">
<th align="left">WMI IRP Minor Number</th>
<th align="left">Miniport Driver Callback Routine</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td align="left"><p><a href="/windows-hardware/drivers/kernel/irp-mn-reginfo" data-raw-source="[&lt;strong&gt;IRP_MN_REGINFO&lt;/strong&gt;](../kernel/irp-mn-reginfo.md)"><strong>IRP_MN_REGINFO</strong></a></p></td>
<td align="left"><p><a href="/windows-hardware/drivers/ddi/scsiwmi/nc-scsiwmi-pscsiwmi_query_reginfo" data-raw-source="[&lt;strong&gt;HwScsiWmiQueryReginfo&lt;/strong&gt;](/windows-hardware/drivers/ddi/scsiwmi/nc-scsiwmi-pscsiwmi_query_reginfo)"><strong>HwScsiWmiQueryReginfo</strong></a></p></td>
</tr>
<tr class="even">
<td align="left"><p><a href="/windows-hardware/drivers/kernel/irp-mn-query-all-data" data-raw-source="[&lt;strong&gt;IRP_MN_QUERY_ALL_DATA&lt;/strong&gt;](../kernel/irp-mn-query-all-data.md)"><strong>IRP_MN_QUERY_ALL_DATA</strong></a></p></td>
<td align="left"><p><a href="/windows-hardware/drivers/ddi/scsiwmi/nc-scsiwmi-pscsiwmi_query_datablock" data-raw-source="[&lt;strong&gt;HwScsiWmiQueryDataBlock&lt;/strong&gt;](/windows-hardware/drivers/ddi/scsiwmi/nc-scsiwmi-pscsiwmi_query_datablock)"><strong>HwScsiWmiQueryDataBlock</strong></a></p></td>
</tr>
<tr class="odd">
<td align="left"><p><a href="/windows-hardware/drivers/kernel/irp-mn-query-single-instance" data-raw-source="[&lt;strong&gt;IRP_MN_QUERY_SINGLE_INSTANCE&lt;/strong&gt;](../kernel/irp-mn-query-single-instance.md)"><strong>IRP_MN_QUERY_SINGLE_INSTANCE</strong></a></p></td>
<td align="left"><p><a href="/windows-hardware/drivers/ddi/scsiwmi/nc-scsiwmi-pscsiwmi_query_datablock" data-raw-source="[&lt;strong&gt;HwScsiWmiQueryDataBlock&lt;/strong&gt;](/windows-hardware/drivers/ddi/scsiwmi/nc-scsiwmi-pscsiwmi_query_datablock)"><strong>HwScsiWmiQueryDataBlock</strong></a></p></td>
</tr>
<tr class="even">
<td align="left"><p><a href="/windows-hardware/drivers/kernel/irp-mn-change-single-instance" data-raw-source="[&lt;strong&gt;IRP_MN_CHANGE_SINGLE_INSTANCE&lt;/strong&gt;](../kernel/irp-mn-change-single-instance.md)"><strong>IRP_MN_CHANGE_SINGLE_INSTANCE</strong></a></p></td>
<td align="left"><p><em>HwScsiWmiSetDataBlock</em></p></td>
</tr>
<tr class="odd">
<td align="left"><p><a href="/windows-hardware/drivers/kernel/irp-mn-change-single-item" data-raw-source="[&lt;strong&gt;IRP_MN_CHANGE_SINGLE_ITEM&lt;/strong&gt;](../kernel/irp-mn-change-single-item.md)"><strong>IRP_MN_CHANGE_SINGLE_ITEM</strong></a></p></td>
<td align="left"><p><a href="/windows-hardware/drivers/ddi/scsiwmi/nc-scsiwmi-pscsiwmi_set_dataitem" data-raw-source="[&lt;strong&gt;HwScsiWmiSetDataItem&lt;/strong&gt;](/windows-hardware/drivers/ddi/scsiwmi/nc-scsiwmi-pscsiwmi_set_dataitem)"><strong>HwScsiWmiSetDataItem</strong></a></p></td>
</tr>
<tr class="even">
<td align="left"><p><a href="/windows-hardware/drivers/kernel/irp-mn-execute-method" data-raw-source="[&lt;strong&gt;IRP_MN_EXECUTE_METHOD&lt;/strong&gt;](../kernel/irp-mn-execute-method.md)"><strong>IRP_MN_EXECUTE_METHOD</strong></a></p></td>
<td align="left"><p><a href="/windows-hardware/drivers/ddi/scsiwmi/nc-scsiwmi-pscsiwmi_execute_method" data-raw-source="[&lt;strong&gt;HwScsiWmiExecuteMethod&lt;/strong&gt;](/windows-hardware/drivers/ddi/scsiwmi/nc-scsiwmi-pscsiwmi_execute_method)"><strong>HwScsiWmiExecuteMethod</strong></a></p></td>
</tr>
<tr class="odd">
<td align="left"><p><a href="/windows-hardware/drivers/kernel/irp-mn-enable-events" data-raw-source="[&lt;strong&gt;IRP_MN_ENABLE_EVENTS&lt;/strong&gt;](../kernel/irp-mn-enable-events.md)"><strong>IRP_MN_ENABLE_EVENTS</strong></a></p></td>
<td align="left"><p><a href="/windows-hardware/drivers/ddi/scsiwmi/nc-scsiwmi-pscsiwmi_function_control" data-raw-source="[&lt;strong&gt;HwScsiWmiFunctionControl&lt;/strong&gt;](/windows-hardware/drivers/ddi/scsiwmi/nc-scsiwmi-pscsiwmi_function_control)"><strong>HwScsiWmiFunctionControl</strong></a></p></td>
</tr>
<tr class="even">
<td align="left"><p><a href="/windows-hardware/drivers/kernel/irp-mn-disable-events" data-raw-source="[&lt;strong&gt;IRP_MN_DISABLE_EVENTS&lt;/strong&gt;](../kernel/irp-mn-disable-events.md)"><strong>IRP_MN_DISABLE_EVENTS</strong></a></p></td>
<td align="left"><p><em>HwScsiWmiFunctionControl</em></p></td>
</tr>
<tr class="odd">
<td align="left"><p><a href="/windows-hardware/drivers/kernel/irp-mn-enable-collection" data-raw-source="[&lt;strong&gt;IRP_MN_ENABLE_COLLECTION&lt;/strong&gt;](../kernel/irp-mn-enable-collection.md)"><strong>IRP_MN_ENABLE_COLLECTION</strong></a></p></td>
<td align="left"><p><em>HwScsiWmiFunctionControl</em></p></td>
</tr>
<tr class="even">
<td align="left"><p><a href="/windows-hardware/drivers/kernel/irp-mn-disable-collection" data-raw-source="[&lt;strong&gt;IRP_MN_DISABLE_COLLECTION&lt;/strong&gt;](../kernel/irp-mn-disable-collection.md)"><strong>IRP_MN_DISABLE_COLLECTION</strong></a></p></td>
<td align="left"><p><em>HwScsiWmiFunctionControl</em></p></td>
</tr>
</tbody>
</table>

 

Each miniport driver callback routine should provide the functionality associated with the corresponding WMI minor IRP number or numbers. Some routines, such as *HwScsiWmiFunctionControl*, must be able to provide functionality that corresponds to several WMI minor IRP numbers.

Your miniport driver will call the SCSI Port WMI library dispatch routine, [**ScsiPortWmiDispatchFunction**](/windows-hardware/drivers/ddi/scsiwmi/nf-scsiwmi-scsiportwmidispatchfunction), and then the dispatch routine will call the appropriate miniport driver callback routine. The port driver transfers the WMI minor IRP number to the SRB so that the dispatch routine can consult the SRB to determine which callback routine to call.

The following diagram illustrates the changes that a WMI request undergoes from the moment that a storage port driver receives it until the storage miniport driver passes it to the SCSI Port WMI library dispatch routine.

![how the storage stack handles a wmi irp .](images/scsiwmilib.png)

1.  The following steps explain how the storage stack repackages a WMI IRP as an SRB:

2.  Windows notifies a storage port driver of a WMI request by sending an IRP of type [**IRP\_MJ\_SYSTEM\_CONTROL**](../kernel/irp-mj-system-control.md).

3.  The port driver repackages the WMI IRP as a WMI SRB of type [**SCSIWMI\_REQUEST\_CONTEXT**](/windows-hardware/drivers/ddi/scsiwmi/ns-scsiwmi-scsiwmi_request_context) and assigns a value of SRB\_FUNCTION\_WMI to the SRB's **Function** member. The port driver transfers the minor WMI IRP number to the SRB **WMISubFunction** member. and arranges for the I/O manager to call the miniport driver's start I/O routine [**HwScsiStartIo**](/previous-versions/windows/hardware/drivers/ff557323(v=vs.85)) by means of a call to [**IoStartPacket**](/windows-hardware/drivers/ddi/ntifs/nf-ntifs-iostartpacket).

4.  The miniport driver calls the SCSI Port WMI library dispatch routine to process the SRB. For more information, see [Using the SCSI Port WMI Library](using-the-scsi-port-wmi-library.md).

