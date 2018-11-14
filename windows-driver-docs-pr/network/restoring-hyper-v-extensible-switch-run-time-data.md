---
title: Restoring Hyper-V Extensible Switch Run-Time Data
description: Restoring Hyper-V Extensible Switch Run-Time Data
ms.assetid: 7904FF12-06E9-433F-A0C1-E1FDEF3427B1
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# Restoring Hyper-V Extensible Switch Run-Time Data


When a Hyper-V child partition that has a network adapter connection to an extensible switch port is resumed from a pause, the Hyper-V extensible switch interface is notified. This causes the protocol edge of the extensible switch to issue an object identifier (OID) set request of [OID\_SWITCH\_NIC\_RESTORE](https://msdn.microsoft.com/library/windows/hardware/hh598267) down the extensible switch driver stack. When an extension receives this OID request, it can restore its run-time data for the extensible switch port that is used by the child partition.

The **InformationBuffer** member of the [**NDIS\_OID\_REQUEST**](https://msdn.microsoft.com/library/windows/hardware/ff566710) structure for the [OID\_SWITCH\_NIC\_RESTORE](https://msdn.microsoft.com/library/windows/hardware/hh598268) request contains a pointer to an [**NDIS\_SWITCH\_NIC\_SAVE\_STATE**](https://msdn.microsoft.com/library/windows/hardware/hh598216) structure. This structure is allocated by the protocol edge of the extensible switch.

When it receives the OID set request of [OID\_SWITCH\_NIC\_RESTORE](https://msdn.microsoft.com/library/windows/hardware/hh598267), the extensible switch extension must first determine whether it owns the run-time data. The extension does this by comparing the value of the **ExtensionId** member of the [**NDIS\_SWITCH\_NIC\_SAVE\_STATE**](https://msdn.microsoft.com/library/windows/hardware/hh598216) structure to the GUID value that the extension uses to identify itself.

If the extension owns the run-time data for an extensible switch NIC, it restores this data in the following way:

1.  The extension copies the run-time data in the **SaveData** member to driver-allocated storage.

    **Note**  The value of the **PortId** member of the [**NDIS\_SWITCH\_NIC\_SAVE\_STATE**](https://msdn.microsoft.com/library/windows/hardware/hh598216) structure may be different from the **PortId** value at the time that the run-time data was saved. This can occur if run-time data was saved during a Live Migration from one host to another. However, the configuration of the extensible switch NIC is retained during the Live Migration. This enables the extension to restore the run-time data to the extensible switch NIC by using the new **PortId** value.

     

2.  The extension completes the OID set request with NDIS\_STATUS\_SUCCESS.

If the extension does not own the specified run-time data to save, the extension calls [**NdisFOidRequest**](https://msdn.microsoft.com/library/windows/hardware/ff561830). This forwards the OID set request to underlying drivers in the extensible switch driver stack. In this case, the extension must not modify the [**NDIS\_SWITCH\_NIC\_SAVE\_STATE**](https://msdn.microsoft.com/library/windows/hardware/hh598216) structure that is associated with the OID request. For more information on how to forward OID requests, see [Filtering OID Requests in an NDIS Filter Driver](filtering-oid-requests-in-an-ndis-filter-driver.md).

If the OID set request of [OID\_SWITCH\_NIC\_RESTORE](https://msdn.microsoft.com/library/windows/hardware/hh598267) is completed with NDIS\_STATUS\_SUCCESS, the protocol edge of the extensible switch issues another OID set request. When it receives this new OID set request, the extension can do one of the following:

-   If it owns the run-time data in the new OID request, the extension restores the additional run-time data within the [**NDIS\_SWITCH\_NIC\_SAVE\_STATE**](https://msdn.microsoft.com/library/windows/hardware/hh598216) structure. The extension then completes the OID request with NDIS\_STATUS\_SUCCESS.

-   If it does not own the run-time data in the new OID request, the extension calls [**NdisFOidRequest**](https://msdn.microsoft.com/library/windows/hardware/ff561830) to forward this OID set request to underlying drivers.

<a href="" id="oid-switch-nic-restore-complete"></a>[OID\_SWITCH\_NIC\_RESTORE\_COMPLETE](https://msdn.microsoft.com/library/windows/hardware/hh846215)  
The extensible switch interface signals the protocol edge of the extensible switch to issue this OID at the completion of the restore operation of run-time data for an extensible switchnetwork adapter.

This OID request notifies the extension that the restore operation has completed only for a specified extensible switch NIC.

For more information about this OID request, see [OID\_SWITCH\_NIC\_RESTORE\_COMPLETE](https://msdn.microsoft.com/library/windows/hardware/hh846215).

**Note**  If the [OID\_SWITCH\_NIC\_RESTORE](https://msdn.microsoft.com/library/windows/hardware/hh598267) set request is received by the miniport edge of the extensible switch, it completes the OID request with NDIS\_STATUS\_SUCCESS. This notifies the protocol edge of the extensible switch that no extension owns the run-time data. If this happens, the extensible switch interface logs an event that documents the **ExtensionId** and **PortId** member values for the extension that originally saved the run-time port data.

 

 

 





