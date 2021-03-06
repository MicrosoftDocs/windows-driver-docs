---
title: Managing Hyper-V Extensible Switch Run-Time Data
description: Managing Hyper-V Extensible Switch Run-Time Data
ms.date: 12/04/2018
ms.localizationpriority: medium
---

# Managing Hyper-V Extensible Switch Run-Time Data

This topic describes save and restore operations for Hyper-V extensible switch extensions. These operations allow an extension to save and restore run-time data for individual extensible switch network adapters(NICs). These operations are performed when a Hyper-V child partition that has a network adapter connection to an extensible switch port is being stopped or started.

## Saving Hyper-V Extensible Switch Run-Time Data

This section describes the operation by which a Hyper-V Extensible Switch extension can save run-time data for individual network adapters (NICs). This operation is performed when a Hyper-V child partition with a network adapter connection to an extensible switch port is being stopped or its state is being saved.

### Handling the OID\_SWITCH\_NIC\_SAVE Request

When a Hyper-V child partition with a network adapter connection to an extensible switch port is stopped or its state is saved, the Hyper-V extensible switch interface is notified. This causes the protocol edge of the extensible switch to issue an object identifier (OID) method request of [OID\_SWITCH\_NIC\_SAVE](./oid-switch-nic-save.md) down the extensible switch driver stack. When an extensible switch extension receives this OID request, it can save its run-time data for the specified network adapter connection that is attached to the child partition.

The **InformationBuffer** member of the [**NDIS\_OID\_REQUEST**](/windows-hardware/drivers/ddi/oidrequest/ns-oidrequest-ndis_oid_request) structure for the [OID\_SWITCH\_NIC\_SAVE](./oid-switch-nic-save.md) request contains a pointer to an [**NDIS\_SWITCH\_NIC\_SAVE\_STATE**](/windows-hardware/drivers/ddi/ntddndis/ns-ntddndis-_ndis_switch_nic_save_state) structure. This structure is allocated by the protocol edge of the extensible switch and initialized in the following way:

-   The **Header** member is initialized to contain the current type, revisionof the [**NDIS\_SWITCH\_NIC\_SAVE\_STATE**](/windows-hardware/drivers/ddi/ntddndis/ns-ntddndis-_ndis_switch_nic_save_state) structure. Size is set to the full buffer size.

-   The **PortId** member contains the unique identifier of the extensible switch port for which the save operation is being performed.

When it receives the [OID\_SWITCH\_NIC\_SAVE](./oid-switch-nic-save.md) method request, the extension does the following:

1.  The extension reads the **PortId** member of the [**NDIS\_SWITCH\_NIC\_SAVE\_STATE**](/windows-hardware/drivers/ddi/ntddndis/ns-ntddndis-_ndis_switch_nic_save_state) structure.

2.  If the extension has run-time data to save for the specified NIC, it saves its data within the [**NDIS\_SWITCH\_NIC\_SAVE\_STATE**](/windows-hardware/drivers/ddi/ntddndis/ns-ntddndis-_ndis_switch_nic_save_state) structure starting with *SaveDataOffset* bytes from the start of the structure. The extension then completes the OID method request with NDIS\_STATUS\_SUCCESS.

3.  If the [**NDIS\_SWITCH\_NIC\_SAVE\_STATE**](/windows-hardware/drivers/ddi/ntddndis/ns-ntddndis-_ndis_switch_nic_save_state) structure does not provide a sufficient buffer to hold the runtime state, the extension the extension sets the method structure’s *BytesNeeded* field to **NDIS\_SIZEOF\_NDIS\_SWITCH\_NIC\_SAVE\_STATE\_REVISION\_1** plus the amount of buffer necessary to hold the save data, and completes the OID with **NDIS\_STATUS\_BUFFER\_TOO\_SHORT**. The OID will be re-issued with the required size.

4.  If the extension does not have run-time data to save for the specified NIC, it must call [**NdisFOidRequest**](/windows-hardware/drivers/ddi/ndis/nf-ndis-ndisfoidrequest). This forwards the OID method request to underlying drivers in the extensible switch driver stack. For more information about this procedure, see [Filtering OID Requests in an NDIS Filter Driver](filtering-oid-requests-in-an-ndis-filter-driver.md).

If the extension has run-time port data to save, it must follow these guidelines when it saves run-time port data within the [**NDIS\_SWITCH\_NIC\_SAVE\_STATE**](/windows-hardware/drivers/ddi/ntddndis/ns-ntddndis-_ndis_switch_nic_save_state) structure:

1.  The extension sets the **ExtensionId** member to the GUID value that uniquely identifies the driver.
2.  The extension sets the **ExtensionFriendlyName** member to the name of the driver.

    **Note**  The NDIS\_SWITCH\_EXTENSION\_FRIENDLYNAME data type is type-defined by the [**IF\_COUNTED\_STRING**](/windows/win32/api/ifdef/ns-ifdef-if_counted_string_lh) structure. A string that is defined by this structure does not have to be null-terminated. However, the length of the string must be set in the **Length** member of this structure. If the string is NULL-terminated, the **Length** member must not include the terminating NULL character.     

3.  If a feature class is associated with the saved run-time data, the extension sets the **FeatureClassId** with the GUID that uniquely identifies the class.

    **Note**  If a feature class is not associated with the saved run-time data, the extension sets the **FeatureClassId** to zero.     

4.  The extension copies the run-time data to the **SaveData** member and sets the **SaveDataSize** member to the size, in bytes, of the run-time data.

**Note**  The extension must not change the **Header** or **PortId** members of the [**NDIS\_SWITCH\_NIC\_SAVE\_STATE**](/windows-hardware/drivers/ddi/ntddndis/ns-ntddndis-_ndis_switch_nic_save_state) structure. 

OID method requests of [OID\_SWITCH\_NIC\_SAVE](./oid-switch-nic-save.md) are ultimately handled by the underlying miniport edge of the extensible switch. Once this OID method request has been forwarded to the miniport driver through the extensible switch driver stack, the miniport driver completes the OID request with NDIS\_STATUS\_SUCCESS. This notifies the protocol edge of the extensible switch that all extensions in the extensible switch driver stack have been queried for run-time port data. The protocol edge of the extensible switch then issues an OID set request of [OID\_SWITCH\_NIC\_SAVE\_COMPLETE](./oid-switch-nic-save-complete.md) to complete the save operation.

### Handling the OID\_SWITCH\_NIC\_SAVE\_COMPLETE Request

When a Hyper-V child partition that has a network adapter connection to an extensible switch port is paused or its state is being saved, the Hyper-V extensible switch interface is notified. This causes the protocol edge of the extensible switch to issue an object identifier (OID) method request of [OID\_SWITCH\_NIC\_SAVE](./oid-switch-nic-save.md) down the extensible switch driver stack.

When every Hyper-V extensible switch extension has saved its run-time data, the protocol edge of the extensible switch notifies underlying extensions that the save operation has completed. The protocol edge does this by issuing an OID set request of [OID\_SWITCH\_NIC\_SAVE\_COMPLETE](./oid-switch-nic-save-complete.md) down the extensible switch driver stack.

**Note**  When a run-time save operation is started for an extensible switch network adapter connection, another save operation for the same network adapter connection will not be performed until the [OID\_SWITCH\_NIC\_SAVE\_COMPLETE](./oid-switch-nic-save-complete.md) request is issued. However, save operations for other network adapter connections could occur during this time. 

The **InformationBuffer** member of the [**NDIS\_OID\_REQUEST**](/windows-hardware/drivers/ddi/oidrequest/ns-oidrequest-ndis_oid_request) structure for the [OID\_SWITCH\_NIC\_SAVE\_COMPLETE](./oid-switch-nic-save-complete.md) request contains a pointer to an [**NDIS\_SWITCH\_NIC\_SAVE\_STATE**](/windows-hardware/drivers/ddi/ntddndis/ns-ntddndis-_ndis_switch_nic_save_state) structure. This structure is allocated by the protocol edge of the extensible switch.

When it receives the OID set request of [OID\_SWITCH\_NIC\_SAVE\_COMPLETE](./oid-switch-nic-save-complete.md), the extension must follow these guidelines:

-   The extension must not modify the [**NDIS\_SWITCH\_NIC\_SAVE\_STATE**](/windows-hardware/drivers/ddi/ntddndis/ns-ntddndis-_ndis_switch_nic_save_state) structure that is associated with the OID request.

-   The extension must call [**NdisFOidRequest**](/windows-hardware/drivers/ddi/ndis/nf-ndis-ndisfoidrequest) to forward this OID request through the extensible switch extension stack. The extension must not fail the OID request.

    **Note**  The extension should monitor the completion status of this OID request. The extension does this to detect whether the save operation has completed successfully.     

OID method requests of [OID\_SWITCH\_NIC\_SAVE\_COMPLETE](./oid-switch-nic-save-complete.md) are ultimately handled by the underlying miniport edge of the extensible switch. Once this OID method request has been received by the miniport edge, it completes the OID request with NDIS\_STATUS\_SUCCESS. This notifies the protocol edge of the extensible switch that all extensions in the extensible switch driver stack have completed the save operation.

## Restoring Hyper-V Extensible Switch Run-Time Data

When a Hyper-V child partition that has a network adapter connection to an extensible switch port is resumed from a pause, the Hyper-V extensible switch interface is notified. This causes the protocol edge of the extensible switch to issue an object identifier (OID) set request of [OID\_SWITCH\_NIC\_RESTORE](./oid-switch-nic-restore.md) down the extensible switch driver stack. When an extension receives this OID request, it can restore its run-time data for the extensible switch port that is used by the child partition.

The **InformationBuffer** member of the [**NDIS\_OID\_REQUEST**](/windows-hardware/drivers/ddi/oidrequest/ns-oidrequest-ndis_oid_request) structure for the [OID\_SWITCH\_NIC\_RESTORE](./oid-switch-nic-save.md) request contains a pointer to an [**NDIS\_SWITCH\_NIC\_SAVE\_STATE**](/windows-hardware/drivers/ddi/ntddndis/ns-ntddndis-_ndis_switch_nic_save_state) structure. This structure is allocated by the protocol edge of the extensible switch.

When it receives the OID set request of [OID\_SWITCH\_NIC\_RESTORE](./oid-switch-nic-restore.md), the extensible switch extension must first determine whether it owns the run-time data. The extension does this by comparing the value of the **ExtensionId** member of the [**NDIS\_SWITCH\_NIC\_SAVE\_STATE**](/windows-hardware/drivers/ddi/ntddndis/ns-ntddndis-_ndis_switch_nic_save_state) structure to the GUID value that the extension uses to identify itself.

If the extension owns the run-time data for an extensible switch NIC, it restores this data in the following way:

1.  The extension copies the run-time data in the **SaveData** member to driver-allocated storage.

    **Note**  The value of the **PortId** member of the [**NDIS\_SWITCH\_NIC\_SAVE\_STATE**](/windows-hardware/drivers/ddi/ntddndis/ns-ntddndis-_ndis_switch_nic_save_state) structure may be different from the **PortId** value at the time that the run-time data was saved. This can occur if run-time data was saved during a Live Migration from one host to another. However, the configuration of the extensible switch NIC is retained during the Live Migration. This enables the extension to restore the run-time data to the extensible switch NIC by using the new **PortId** value.     

2.  The extension completes the OID set request with NDIS\_STATUS\_SUCCESS.

If the extension does not own the specified run-time data to save, the extension calls [**NdisFOidRequest**](/windows-hardware/drivers/ddi/ndis/nf-ndis-ndisfoidrequest). This forwards the OID set request to underlying drivers in the extensible switch driver stack. In this case, the extension must not modify the [**NDIS\_SWITCH\_NIC\_SAVE\_STATE**](/windows-hardware/drivers/ddi/ntddndis/ns-ntddndis-_ndis_switch_nic_save_state) structure that is associated with the OID request. For more information on how to forward OID requests, see [Filtering OID Requests in an NDIS Filter Driver](filtering-oid-requests-in-an-ndis-filter-driver.md).

If the OID set request of [OID\_SWITCH\_NIC\_RESTORE](./oid-switch-nic-restore.md) is completed with NDIS\_STATUS\_SUCCESS, the protocol edge of the extensible switch issues another OID set request. When it receives this new OID set request, the extension can do one of the following:

-   If it owns the run-time data in the new OID request, the extension restores the additional run-time data within the [**NDIS\_SWITCH\_NIC\_SAVE\_STATE**](/windows-hardware/drivers/ddi/ntddndis/ns-ntddndis-_ndis_switch_nic_save_state) structure. The extension then completes the OID request with NDIS\_STATUS\_SUCCESS.

-   If it does not own the run-time data in the new OID request, the extension calls [**NdisFOidRequest**](/windows-hardware/drivers/ddi/ndis/nf-ndis-ndisfoidrequest) to forward this OID set request to underlying drivers.

<a href="" id="oid-switch-nic-restore-complete"></a>[OID\_SWITCH\_NIC\_RESTORE\_COMPLETE](./oid-switch-nic-restore-complete.md)  
The extensible switch interface signals the protocol edge of the extensible switch to issue this OID at the completion of the restore operation of run-time data for an extensible switchnetwork adapter.

This OID request notifies the extension that the restore operation has completed only for a specified extensible switch NIC.

For more information about this OID request, see [OID\_SWITCH\_NIC\_RESTORE\_COMPLETE](./oid-switch-nic-restore-complete.md).

**Note**  If the [OID\_SWITCH\_NIC\_RESTORE](./oid-switch-nic-restore.md) set request is received by the miniport edge of the extensible switch, it completes the OID request with NDIS\_STATUS\_SUCCESS. This notifies the protocol edge of the extensible switch that no extension owns the run-time data. If this happens, the extensible switch interface logs an event that documents the **ExtensionId** and **PortId** member values for the extension that originally saved the run-time port data.
