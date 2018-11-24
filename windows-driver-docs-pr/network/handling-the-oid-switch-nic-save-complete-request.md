---
title: Handling the OID_SWITCH_NIC_SAVE_COMPLETE Request
description: Handling the OID_SWITCH_NIC_SAVE_COMPLETE Request
ms.assetid: 5EE5F4ED-E0FC-458E-B9E1-23C20B3BC597
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# Handling the OID\_SWITCH\_NIC\_SAVE\_COMPLETE Request


This topic describes the process by which the operation of saving run-time data is completed in the Hyper-V extensible switch interface.

When a Hyper-V child partition that has a network adapter connection to an extensible switch port is paused or its state is being saved, the Hyper-V extensible switch interface is notified. This causes the protocol edge of the extensible switch to issue an object identifier (OID) method request of [OID\_SWITCH\_NIC\_SAVE](https://msdn.microsoft.com/library/windows/hardware/hh598268) down the extensible switch driver stack. For more information about this procedure, see [Handling the OID\_SWITCH\_NIC\_SAVE Request](handling-the-oid-switch-nic-save-request.md).

When every Hyper-V extensible switch extension has saved its run-time data, the protocol edge of the extensible switch notifies underlying extensions that the save operation has completed. The protocol edge does this by issuing an OID set request of [OID\_SWITCH\_NIC\_SAVE\_COMPLETE](https://msdn.microsoft.com/library/windows/hardware/hh598269) down the extensible switch driver stack.

**Note**  When a run-time save operation is started for an extensible switch network adapter connection, another save operation for the same network adapter connection will not be performed until the [OID\_SWITCH\_NIC\_SAVE\_COMPLETE](https://msdn.microsoft.com/library/windows/hardware/hh598269) request is issued. However, save operations for other network adapter connections could occur during this time.

 

The **InformationBuffer** member of the [**NDIS\_OID\_REQUEST**](https://msdn.microsoft.com/library/windows/hardware/ff566710) structure for the [OID\_SWITCH\_NIC\_SAVE\_COMPLETE](https://msdn.microsoft.com/library/windows/hardware/hh598269) request contains a pointer to an [**NDIS\_SWITCH\_NIC\_SAVE\_STATE**](https://msdn.microsoft.com/library/windows/hardware/hh598216) structure. This structure is allocated by the protocol edge of the extensible switch.

When it receives the OID set request of [OID\_SWITCH\_NIC\_SAVE\_COMPLETE](https://msdn.microsoft.com/library/windows/hardware/hh598269), the extension must follow these guidelines:

-   The extension must not modify the [**NDIS\_SWITCH\_NIC\_SAVE\_STATE**](https://msdn.microsoft.com/library/windows/hardware/hh598216) structure that is associated with the OID request.

-   The extension must call [**NdisFOidRequest**](https://msdn.microsoft.com/library/windows/hardware/ff561830) to forward this OID request through the extensible switch extension stack. The extension must not fail the OID request.

    **Note**  The extension should monitor the completion status of this OID request. The extension does this to detect whether the save operation has completed successfully.

     

OID method requests of [OID\_SWITCH\_NIC\_SAVE\_COMPLETE](https://msdn.microsoft.com/library/windows/hardware/hh598269) are ultimately handled by the underlying miniport edge of the extensible switch. Once this OID method request has been received by the miniport edge, it completes the OID request with NDIS\_STATUS\_SUCCESS. This notifies the protocol edge of the extensible switch that all extensions in the extensible switch driver stack have completed the save operation.

 

 





