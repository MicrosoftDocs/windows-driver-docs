---
title: Registering a SAP
description: Registering a SAP
keywords:
- service access points WDK CoNDIS
- SAPs WDK CoNDIS
- registering SAPs
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# Registering a SAP





If a client accepts incoming calls, its [**ProtocolClOpenAfCompleteEx**](/windows-hardware/drivers/ddi/ndis/nc-ndis-protocol_cl_open_af_complete_ex) function usually registers one or more SAPs with the call manager by calling [**NdisClRegisterSap**](/windows-hardware/drivers/ddi/ndis/nf-ndis-ndisclregistersap).

The following figure shows a client of a call manager registering a SAP.

![diagram illustrating a client of a call manager registering a sap.](images/cm-02.png)

The following figure shows a client of an MCM driver registering a SAP.

![registering a sap with an mcm driver.](images/fig1-02.png)

With the call to **NdisClRegisterSap**, a client requests notifications of incoming calls on a particular SAP. NDIS forwards the SAP information supplied by the client to the call manager's or MCM driver's [**ProtocolCmRegisterSap**](/windows-hardware/drivers/ddi/ndis/nc-ndis-protocol_cm_reg_sap) function for validation. If the given SAP is already in use or if the call manager or MCM driver does not recognize the client-supplied SAP specification, the call manager or MCM driver fails this request.

In *ProtocolCmRegisterSap*, the call manager or MCM driver might communicate with network control devices or other media-specific agents to register the SAP on the network for a connection-oriented client. *ProtocolCmRegisterSap* also stores an NDIS-supplied *NdisSapHandle* that represents the SAP.

*ProtocolCmRegisterSap* can complete synchronously or asynchronously. To complete asynchronously, the *ProtocolCmRegisterSap* function of a call manager calls [**NdisCmRegisterSapComplete**](/windows-hardware/drivers/ddi/ndis/nf-ndis-ndiscmregistersapcomplete). The *ProtocolCmRegisterSap* function of an MCM driver calls [**NdisMCmRegisterSapComplete**](/windows-hardware/drivers/ddi/ndis/nf-ndis-ndismcmregistersapcomplete). The call to **Ndis(M)CmRegisterSapComplete** causes NDIS to call the client's [*ProtocolClRegisterSapComplete*](/windows-hardware/drivers/ddi/ndis/nc-ndis-protocol_cl_register_sap_complete) function.

If the client's call to **NdisClRegisterSap** is successful, NDIS returns to the client an NdisSapHandle that represents the SAP.

After a call manager registers a SAP on behalf of a connection-oriented client, it notifies that client of an incoming call offer directed to that SAP by calling [**NdisCmDispatchIncomingCall**](/windows-hardware/drivers/ddi/ndis/nf-ndis-ndiscmdispatchincomingcall). An MCM driver calls [**NdisMCmDispatchIncomingCall**](/windows-hardware/drivers/ddi/ndis/nf-ndis-ndismcmdispatchincomingcall)(see [Indicating an Incoming Call](indicating-an-incoming-call.md)). A client can receive incoming calls on a SAP even while SAP registration is still pending; that is, before its *ProtocolClRegisterSapComplete* function is called.

 

