---
title: Hyper-V Extensible Switch Restore Operations
description: Hyper-V Extensible Switch Restore Operations
ms.assetid: 283D9E43-79F2-47B1-8D29-39A8E7CBE2C7
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# Hyper-V Extensible Switch Restore Operations


When a Hyper-V child partition is restarted after it was stopped or live migrated, the run-time state of the partition is restored. During the restore operation, a Hyper-V extensible switch extension driver can restore run-time data about an extensible switch network adapter (NIC).

When a restore operation is being performed on a Hyper-V child partition, the extensible switch interface signals the protocol edge of the extensible switch to issue an OID set request of [OID\_SWITCH\_NIC\_RESTORE](https://msdn.microsoft.com/library/windows/hardware/hh598268). The **InformationBuffer** member of the [**NDIS\_OID\_REQUEST**](https://msdn.microsoft.com/library/windows/hardware/ff566710) structure for the OID\_SWITCH\_NIC\_RESTORE request contains a pointer to an [**NDIS\_SWITCH\_NIC\_SAVE\_STATE**](https://msdn.microsoft.com/library/windows/hardware/hh598216) structure.

When it handles this OID request, the extension restores the run-time data for the network adapter. This run-time data was previously saved through OID requests of [OID\_SWITCH\_NIC\_SAVE](https://msdn.microsoft.com/library/windows/hardware/hh598268) and OID\_SWITCH\_NIC\_SAVE\_COMPLETE.

When it receives the [OID\_SWITCH\_NIC\_RESTORE](https://msdn.microsoft.com/library/windows/hardware/hh598267) request, the extensible switch extension must first determine whether it owns the run-time data. The driver does this by comparing the value of the **ExtensionId** member of the [**NDIS\_SWITCH\_NIC\_SAVE\_STATE**](https://msdn.microsoft.com/library/windows/hardware/hh598216) structure to the GUID value that the driver uses to identify itself.

If the extension owns the run-time data, it restores this data in the following way:

1.  The extension copies the run-time data in the **SaveData** member to driver-allocated storage.

    **Note**  The value of the **PortId** member of the [**NDIS\_SWITCH\_NIC\_SAVE\_STATE**](https://msdn.microsoft.com/library/windows/hardware/hh598216) structure may be different from the **PortId** value at the time that the run-time data was saved. This can occur if run-time data was saved during a Live Migration from one host to another. However, the configuration of the extensible switch NIC is retained during the Live Migration. This enables the extension to restore the run-time data to the extensible switch NIC by using the new **PortId** value.

     

2.  The extension completes the OID set request with NDIS\_STATUS\_SUCCESS.

If the extension does not own the run-time data, it must call [**NdisFOidRequest**](https://msdn.microsoft.com/library/windows/hardware/ff561830). This forwards the OID method request to underlying extensions in the extensible switch driver stack. For more information about this procedure, see [Filtering OID Requests in an NDIS Filter Driver](filtering-oid-requests-in-an-ndis-filter-driver.md).

<a href="" id="oid-switch-nic-restore-complete"></a>[OID\_SWITCH\_NIC\_RESTORE\_COMPLETE](https://msdn.microsoft.com/library/windows/hardware/hh846215)  
The extensible switch interface signals the protocol edge of the extensible switch to issue this OID at the completion of the restore operation of run-time data for an extensible switch NIC.

This OID request notifies the extension that the restore operation has completed only for a specified extensible switch NIC.

For more information about this OID request, see [OID\_SWITCH\_NIC\_RESTORE\_COMPLETE](https://msdn.microsoft.com/library/windows/hardware/hh846215).

During the restore operation for run-time data, the protocol edge of the extensible switch issues OID requests of [OID\_SWITCH\_NIC\_RESTORE](https://msdn.microsoft.com/library/windows/hardware/hh598267) and [OID\_SWITCH\_NIC\_RESTORE\_COMPLETE](https://msdn.microsoft.com/library/windows/hardware/hh846215) for the network interface of a Hyper-V child partition is connected. If multiple Hyper-V child partitions are restored, the protocol edge issues separate sets of OID\_SWITCH\_NIC\_RESTORE and OID\_SWITCH\_NIC\_RESTORE\_COMPLETE requests for each network interface connection.

**Note**  The protocol edge of the extensible switch will not interleave restore operations for run-time data for the same NIC. The protocol edge will start a run-time data restore operation for a NIC only after a previous restore operation has completed on the same NIC. However, the protocol edge may start a restore operation for a NIC while another restore operation is in progress for another NIC. Because of this, we highly recommend that extensions perform restore operations in a non-interleaved fashion. For example, extensions should not assume that a new restore operation cannot start on another NIC before an ongoing restore operation has completed for a different NIC.

 

For more information about this OID request, see [Restoring Hyper-V Extensible Switch Run-Time Data](restoring-hyper-v-extensible-switch-run-time-data.md).

 

 





