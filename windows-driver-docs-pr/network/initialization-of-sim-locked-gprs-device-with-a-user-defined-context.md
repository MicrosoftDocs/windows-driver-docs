---
title: Initializing a SIM-locked GPRS device (user-defined context)
description: Initialization of SIM-Locked GPRS Device with a User-Defined Context
ms.assetid: 655b7789-ffea-459c-9489-5c2f565b77ee
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# Initialization of SIM-Locked GPRS Device with a User-Defined Context


The following diagram illustrates the scenario in which the user enters a SIM PIN and manually configures an access point name string. The labels in bold are OID identifiers or transactional flow control, and the labels in regular text are the important flags within the OID structure.

![diagram illustrating the scenario in which the user enters a sim pin and manually configures an access-point name string](images/wwanlockedgsmdevinitseq.png)

To initialize a GSM-based device with PIN1 locked, implement the following steps:

1.  The MB Service sends an asynchronous (non-blocking) [OID\_WWAN\_READY\_INFO](https://docs.microsoft.com/windows-hardware/drivers/network/oid-wwan-ready-info) query request to the miniport driver to identify the ready state of the device. The miniport driver responds with a provisional acknowledgment (NDIS\_STATUS\_INDICATION\_REQUIRED) that it has received the request, and that it will send a notification with the requested information in the future.

2.  The miniport driver sends an NDIS\_STATUS\_WWAN\_FAILURE notification to the MB Service to indicate to the MB Service that the subscriber identity module (SIM) is locked.

3.  The MB Service sends an asynchronous (non-blocking) [OID\_WWAN\_PIN](https://docs.microsoft.com/windows-hardware/drivers/network/oid-wwan-pin) query request to the miniport driver. The miniport driver responds with a provisional acknowledgment (NDIS\_STATUS\_INDICATION\_REQUIRED) that it has received the request, and that it will send a notification with the requested information in the future.

4.  The miniport driver sends an NDIS\_STATUS\_WWAN\_SUCCESS notification to the MB Service.

5.  The MB Service sends an asynchronous (non-blocking) [OID\_WWAN\_PIN](https://docs.microsoft.com/windows-hardware/drivers/network/oid-wwan-pin) set request to the miniport driver. The miniport driver responds with a provisional acknowledgment (NDIS\_STATUS\_INDICATION\_REQUIRED) that it has received the request, and that it will send a notification with the requested information in the future.

6.  The miniport driver sends an NDIS\_STATUS\_WWAN\_SUCCESS notification to the MB Service.

7.  The miniport driver sends an [**NDIS\_STATUS\_WWAN\_READY\_INFO**](https://docs.microsoft.com/windows-hardware/drivers/network/ndis-status-wwan-ready-info) notification to the MB Service that indicates to the MB Service that the state of the MB device is **WwanReadyStateInitialized**.

8.  The MB Service sends an asynchronous (non-blocking) [OID\_WWAN\_REGISTER\_STATE](https://docs.microsoft.com/windows-hardware/drivers/network/oid-wwan-register-state) query request to the miniport driver. The miniport driver responds with a provisional acknowledgment (NDIS\_STATUS\_INDICATION\_REQUIRED) that it has received the request, and it will send a notification with the requested information in the future.

9.  The miniport driver sends an NDIS\_STATUS\_WWAN\_SUCCESS notification to the MB Service.

10. The miniport driver sends an [**NDIS\_STATUS\_WWAN\_REGISTER\_STATE**](https://docs.microsoft.com/windows-hardware/drivers/network/ndis-status-wwan-register-state) notification to the MB Service.

11. The MB Service sends an asynchronous (non-blocking) [OID\_WWAN\_HOME\_PROVIDER](https://docs.microsoft.com/windows-hardware/drivers/network/oid-wwan-home-provider) query request to the miniport driver. The miniport driver responds with a provisional acknowledgment (NDIS\_STATUS\_INDICATION\_REQUIRED) that it has received the request, and it will send a notification with the requested information in the future.

12. The miniport driver sends an NDIS\_STATUS\_WWAN\_SUCCESS notification to the MB Service.

13. The miniport driver sends an [**NDIS\_STATUS\_WWAN\_REGISTER\_STATE**](https://docs.microsoft.com/windows-hardware/drivers/network/ndis-status-wwan-register-state) notification to the MB Service.

14. The MB Service sends an asynchronous (non-blocking) [OID\_WWAN\_PACKET\_SERVICE](https://docs.microsoft.com/windows-hardware/drivers/network/oid-wwan-packet-service) request to the miniport driver. The miniport driver responds with a provisional acknowledgment (NDIS\_STATUS\_INDICATION\_REQUIRED) that it has received the request, and that it will send a notification with the requested information in the future.

15. The miniport driver sends an [**NDIS\_STATUS\_WWAN\_PACKET\_SERVICE**](https://docs.microsoft.com/windows-hardware/drivers/network/ndis-status-wwan-packet-service) notification to the MB Service.

16. The MB Service sends an asynchronous (non-blocking) [OID\_WWAN\_PROVISIONED\_CONTEXTS](https://docs.microsoft.com/windows-hardware/drivers/network/oid-wwan-provisioned-contexts) query request to the miniport driver. The miniport driver responds with a provisional acknowledgment (NDIS\_STATUS\_INDICATION\_REQUIRED) that it has received the request, and it will send a notification with the requested information in the future.

17. The miniport driver sends [**NDIS\_STATUS\_WWAN\_PROVISIONED\_CONTEXTS**](https://docs.microsoft.com/windows-hardware/drivers/network/ndis-status-wwan-provisioned-contexts) to the MB Service.

18. The MB Service sends an asynchronous (non-blocking) [OID\_WWAN\_PROVISIONED\_CONTEXTS](https://docs.microsoft.com/windows-hardware/drivers/network/oid-wwan-provisioned-contexts) set request to the MB Service. The miniport driver responds with a provisional acknowledgment (NDIS\_STATUS\_INDICATION\_REQUIRED) that it has received the request, and it will send a notification with the requested information in the future.

19. The miniport driver sends NDIS\_STATUS\_WWAN\_SUCCESS to the MB Service.

 

 





