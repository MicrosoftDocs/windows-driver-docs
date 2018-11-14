---
title: Hyper-V Extensible Switch Save Operations
description: Hyper-V Extensible Switch Save Operations
ms.assetid: 7148B094-2551-4035-A6BE-141DD01BEA14
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# Hyper-V Extensible Switch Save Operations


When a Hyper-V child partition is stopped, saved, or live migrated, the run-time state of the partition is saved. During the save operation, a Hyper-V extensible switch extension can save run-time data about an extensible switch network adapter (NIC).

When a save operation is being performed on a Hyper-V child partition, the extensible switch interface notifies the extension about the operation. The extension is notified through the following object identifier (OID) requests:

<a href="" id="oid-switch-nic-save"></a>[OID\_SWITCH\_NIC\_SAVE](https://msdn.microsoft.com/library/windows/hardware/hh598268)  
The extensible switch interface signals the protocol edge of the extensible switch to issue this OID during the save operation for an extensible switch NIC. When it handles this OID request, the extension returns run-time data for the NIC. After the run-time data is saved, it is restored through OID set requests of [OID\_SWITCH\_NIC\_RESTORE](https://msdn.microsoft.com/library/windows/hardware/hh598267).

When it receives the [OID\_SWITCH\_NIC\_SAVE](https://msdn.microsoft.com/library/windows/hardware/hh598268) method request, the extension can do one of the following:

-   If the extension has run-time data to save, it initializes an [**NDIS\_SWITCH\_NIC\_SAVE\_STATE**](https://msdn.microsoft.com/library/windows/hardware/hh598216) structure and sets the various members, such as the **ExtensionId** member, to identify itself and the data that it is saving. The extension also saves the data within the **NDIS\_SWITCH\_NIC\_SAVE\_STATE** structure starting SaveDataOffset bytes from the start of the structure, and then completes the OID method request with NDIS\_STATUS\_SUCCESS.

-   If the [**NDIS\_SWITCH\_NIC\_SAVE\_STATE**](https://msdn.microsoft.com/library/windows/hardware/hh598216) structure does not provide a sufficient buffer size, enumerated in the NDIS\_OBJECT\_HEADER **Size** member to hold the run-time state, the extension sets the method structure's *BytesNeeded* field to NDIS\_SIZEOF\_NDIS\_SWITCH\_NIC\_SAVE\_STATE\_REVISION\_1 plus the amount of buffer necessary to hold the save data, and completes the OID with NDIS\_STATUS\_BUFFER\_TOO\_SHORT. The OID will be reissued with the required size.
-   If the extension does not have run-time data to save, it must call [**NdisFOidRequest**](https://msdn.microsoft.com/library/windows/hardware/ff561830). This forwards the OID method request to underlying extensions in the extensible switch driver stack. For more information about this procedure, see [Filtering OID Requests in an NDIS Filter Driver](filtering-oid-requests-in-an-ndis-filter-driver.md).

For more information about this OID request, see [Handling the OID\_SWITCH\_NIC\_SAVE Request](handling-the-oid-switch-nic-save-request.md).

<a href="" id="oid-switch-nic-save-complete"></a>[OID\_SWITCH\_NIC\_SAVE\_COMPLETE](https://msdn.microsoft.com/library/windows/hardware/hh598268)  
The extensible switch interface signals the protocol edge of the extensible switch to issue this OID at the completion of the save operation of run-time data for an extensible switch NIC.

This OID request notifies the extension that the save operation has completed only for a specified extensible switch NIC.

For more information about this OID request, see [Handling the OID\_SWITCH\_NIC\_SAVE\_COMPLETE Request](handling-the-oid-switch-nic-save-complete-request.md).

During the save operation for run-time data, the protocol edge of the extensible switch issues OID requests of [OID\_SWITCH\_NIC\_SAVE](https://msdn.microsoft.com/library/windows/hardware/hh598268) and OID\_SWITCH\_NIC\_SAVE\_COMPLETE for the network interface of a Hyper-V child partition is connected. If multiple Hyper-V child partitions are stopped or live migrated, the protocol edge issues separate sets of OID\_SWITCH\_NIC\_SAVE and OID\_SWITCH\_NIC\_SAVE\_COMPLETE requests for each network interface connection.

**Note**  The protocol edge of the extensible switch will not interleave save operations for run-time data for the same NIC. The protocol edge will start a run-time data save operation for a NIC only after a previous save operation has completed on the same NIC. However, the protocol edge may start a save operation for a NIC while another save operation is in progress for another NIC. Because of this, we highly recommend that extensions perform save operations in a non-interleaved fashion. For example, extensions should not assume that a new save operation cannot start on another NIC before an ongoing save operation has completed for a different NIC.

 

 

 





