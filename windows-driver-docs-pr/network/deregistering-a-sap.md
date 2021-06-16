---
title: Deregistering a SAP
description: Deregistering a SAP
keywords:
- service access points WDK CoNDIS
- SAPs WDK CoNDIS
- deregistering SAPs
- unregistering SAPs
- removing SAPs
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# Deregistering a SAP





A connection-oriented client deregisters a SAP with [**NdisClDeregisterSap**](/windows-hardware/drivers/ddi/ndis/nf-ndis-ndisclderegistersap).

The following figure shows a client of a call manager deregistering a SAP.

![diagram illustrating a client of a call manager deregistering a sap.](images/cm-04.png)

The following figure shows a client of an MCM driver deregistering a SAP.

![diagram illustrating a client of an mcm driver deregistering a sap.](images/fig1-04.png)

The call to **NdisClDeregisterSap** causes NDIS to call the call manager's or MCM driver's [**ProtocolCmDeregisterSap**](/windows-hardware/drivers/ddi/ndis/nc-ndis-protocol_cm_deregister_sap) function. In *ProtocolCmDeregisterSap*, the call manager or MCM driver might communicate with network control devices or other media-specific agents to deregister the SAP on the network. In addition, *ProtocolCmDeregisterSap* must free any resources that it dynamically allocated for the SAP.

*ProtocolCmDeregisterSap* can complete synchronously or asynchronously. To complete asynchronously, the *ProtocolCmDeregisterSap* function of a call manager calls [**NdisCmDeregisterSapComplete**](/windows-hardware/drivers/ddi/ndis/nf-ndis-ndiscmderegistersapcomplete). The *ProtocolCmDeregisterSap* function of an MCM driver calls [**NdisMCmDeregisterSapComplete**](/windows-hardware/drivers/ddi/ndis/nf-ndis-ndismcmderegistersapcomplete). **Ndis(M)CmDegisterSapComplete** notifies both NDIS and the client that the call manager has completed the SAP-deregistration request for which its *ProtocolCmDeregisterSap* function previously returned NDIS\_STATUS\_PENDING.

A call to **Ndis(M)CmDeregisterSapComplete** causes NDIS to call the client's [**ProtocolClDeregisterSapComplete**](/windows-hardware/drivers/ddi/ndis/nc-ndis-protocol_cl_deregister_sap_complete) function. A call to *ProtocolClDeregisterSapComplete* indicates that the client's preceding call to **NdisClDeregisterSap** has been processed by the call manager or MCM driver.

Note that a client can deregister a SAP without affecting an incoming call that has already been received on that SAP and without affecting the VC for that incoming call.

 

