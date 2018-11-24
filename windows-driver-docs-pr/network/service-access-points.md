---
title: Service Access Points
description: Service Access Points
ms.assetid: a6fab686-6adb-4d77-8f0d-2b48e2e49f1f
keywords:
- incoming calls WDK CoNDIS
- connection-oriented NDIS WDK , service access points
- CoNDIS WDK networking , service access points
- service access points WDK CoNDIS
- SAPs WDK CoNDIS
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# Service Access Points





A *service access point* (SAP) identifies the characteristics of incoming calls of interest to a connection-oriented client. By registering a SAP with a call manager or MCM driver, a client indicates that the call manager or MCM driver should notify the client of all incoming calls addressed to that SAP.

A client does not always register a SAP, for example, if it does not handle incoming calls. A client can register multiple SAPs with a call manager or MCM driver.

For more information about SAPs, see [Registering a SAP](registering-a-sap.md) and [Deregistering a SAP](deregistering-a-sap.md).

 

 





