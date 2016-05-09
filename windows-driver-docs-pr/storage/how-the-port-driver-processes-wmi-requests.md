---
title: How the Port Driver Processes WMI Requests
author: windows-driver-content
description: How the Port Driver Processes WMI Requests
ms.assetid: 0b56d382-3c4b-4192-be49-3bad50b0a0ed
keywords: ["WMI SRBs WDK storage , WMI request processing", "callback routines WDK WMI SRBs", "WMI IRPs WDK storage"]
---

# How the Port Driver Processes WMI Requests


## <span id="ddk_how_the_port_driver_processes_wmi_requests_kg"></span><span id="DDK_HOW_THE_PORT_DRIVER_PROCESSES_WMI_REQUESTS_KG"></span>


Windows notifies a storage port driver of a WMI request by sending a I/O request packet (IRP) of type [**IRP\_MJ\_SYSTEM\_CONTROL**](https://msdn.microsoft.com/library/windows/hardware/ff550813), as described in [Windows Management Instrumentation](https://msdn.microsoft.com/library/windows/hardware/ff547139). A system control IRP can contain any of the minor IRP numbers that represent WMI operations. For more information, see [WMI Minor IRPs](https://msdn.microsoft.com/library/windows/hardware/ff566361).

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
<td align="left"><p>[<strong>IRP_MN_REGINFO</strong>](https://msdn.microsoft.com/library/windows/hardware/ff551731)</p></td>
<td align="left"><p>[<strong>HwScsiWmiQueryReginfo</strong>](https://msdn.microsoft.com/library/windows/hardware/ff557344)</p></td>
</tr>
<tr class="even">
<td align="left"><p>[<strong>IRP_MN_QUERY_ALL_DATA</strong>](https://msdn.microsoft.com/library/windows/hardware/ff551650)</p></td>
<td align="left"><p>[<strong>HwScsiWmiQueryDataBlock</strong>](https://msdn.microsoft.com/library/windows/hardware/ff557340)</p></td>
</tr>
<tr class="odd">
<td align="left"><p>[<strong>IRP_MN_QUERY_SINGLE_INSTANCE</strong>](https://msdn.microsoft.com/library/windows/hardware/ff551718)</p></td>
<td align="left"><p>[<strong>HwScsiWmiQueryDataBlock</strong>](https://msdn.microsoft.com/library/windows/hardware/ff557340)</p></td>
</tr>
<tr class="even">
<td align="left"><p>[<strong>IRP_MN_CHANGE_SINGLE_INSTANCE</strong>](https://msdn.microsoft.com/library/windows/hardware/ff550831)</p></td>
<td align="left"><p><em>HwScsiWmiSetDataBlock</em></p></td>
</tr>
<tr class="odd">
<td align="left"><p>[<strong>IRP_MN_CHANGE_SINGLE_ITEM</strong>](https://msdn.microsoft.com/library/windows/hardware/ff550836)</p></td>
<td align="left"><p>[<strong>HwScsiWmiSetDataItem</strong>](https://msdn.microsoft.com/library/windows/hardware/ff557357)</p></td>
</tr>
<tr class="even">
<td align="left"><p>[<strong>IRP_MN_EXECUTE_METHOD</strong>](https://msdn.microsoft.com/library/windows/hardware/ff550868)</p></td>
<td align="left"><p>[<strong>HwScsiWmiExecuteMethod</strong>](https://msdn.microsoft.com/library/windows/hardware/ff557332)</p></td>
</tr>
<tr class="odd">
<td align="left"><p>[<strong>IRP_MN_ENABLE_EVENTS</strong>](https://msdn.microsoft.com/library/windows/hardware/ff550859)</p></td>
<td align="left"><p>[<strong>HwScsiWmiFunctionControl</strong>](https://msdn.microsoft.com/library/windows/hardware/ff557338)</p></td>
</tr>
<tr class="even">
<td align="left"><p>[<strong>IRP_MN_DISABLE_EVENTS</strong>](https://msdn.microsoft.com/library/windows/hardware/ff550851)</p></td>
<td align="left"><p><em>HwScsiWmiFunctionControl</em></p></td>
</tr>
<tr class="odd">
<td align="left"><p>[<strong>IRP_MN_ENABLE_COLLECTION</strong>](https://msdn.microsoft.com/library/windows/hardware/ff550857)</p></td>
<td align="left"><p><em>HwScsiWmiFunctionControl</em></p></td>
</tr>
<tr class="even">
<td align="left"><p>[<strong>IRP_MN_DISABLE_COLLECTION</strong>](https://msdn.microsoft.com/library/windows/hardware/ff550848)</p></td>
<td align="left"><p><em>HwScsiWmiFunctionControl</em></p></td>
</tr>
</tbody>
</table>

 

Each miniport driver callback routine should provide the functionality associated with the corresponding WMI minor IRP number or numbers. Some routines, such as *HwScsiWmiFunctionControl*, must be able to provide functionality that corresponds to several WMI minor IRP numbers.

Your miniport driver will call the SCSI Port WMI library dispatch routine, [**ScsiPortWmiDispatchFunction**](https://msdn.microsoft.com/library/windows/hardware/ff564766), and then the dispatch routine will call the appropriate miniport driver callback routine. The port driver transfers the WMI minor IRP number to the SRB so that the dispatch routine can consult the SRB to determine which callback routine to call.

The following diagram illustrates the changes that a WMI request undergoes from the moment that a storage port driver receives it until the storage miniport driver passes it to the SCSI Port WMI library dispatch routine.

![how the storage stack handles a wmi irp ](images/scsiwmilib.png)

1.  The following steps explain how the storage stack repackages a WMI IRP as an SRB:

2.  Windows notifies a storage port driver of a WMI request by sending an IRP of type [**IRP\_MJ\_SYSTEM\_CONTROL**](https://msdn.microsoft.com/library/windows/hardware/ff550813).

3.  The port driver repackages the WMI IRP as a WMI SRB of type [**SCSIWMI\_REQUEST\_CONTEXT**](https://msdn.microsoft.com/library/windows/hardware/ff564946) and assigns a value of SRB\_FUNCTION\_WMI to the SRB's **Function** member. The port driver transfers the minor WMI IRP number to the SRB **WMISubFunction** member. and arranges for the I/O manager to call the miniport driver's start I/O routine [**HwScsiStartIo**](https://msdn.microsoft.com/library/windows/hardware/ff557323) by means of a call to [**IoStartPacket**](https://msdn.microsoft.com/library/windows/hardware/ff550370).

4.  The miniport driver calls the SCSI Port WMI library dispatch routine to process the SRB. For more information, see [Using the SCSI Port WMI Library](using-the-scsi-port-wmi-library.md).

 

 


--------------------
[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20[storage\storage]:%20How%20the%20Port%20Driver%20Processes%20WMI%20Requests%20%20RELEASE:%20%285/9/2016%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")


