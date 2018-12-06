---
title: Support for Named VCs
description: Support for Named VCs
ms.assetid: 797f737c-91e7-410b-91d5-5575d5b19e86
keywords:
- WMI WDK networking , virtual connections
- call managers WDK networking , naming virtual connections
- virtual connections WDK NDIS WMI
- VCs WDK NDIS WMI
- miniport call managers WDK networking , naming virtual connections
- MCMs WDK networking , namin
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# Support for Named VCs





NDIS allows WMI clients to query and set information on a per-virtual connection (VC) basis for connection-oriented miniport adapters. WMI clients can also enumerate VCs. Before a WMI client can query or set information that is associated with a particular VC, a stand-alone call manager or connection-oriented client must name the VC by calling the [**NdisCoAssignInstanceName**](https://msdn.microsoft.com/library/windows/hardware/ff561692) function.

After a stand-alone call manager or connection-oriented client initiates the setup of a VC by calling the [**NdisCoCreateVC**](https://msdn.microsoft.com/library/windows/hardware/ff561696) function, the stand-alone call manager or connection-oriented client can name the VC with **NdisCoAssignInstanceName**. NDIS assigns the VC an instance name and registers the instance name with WMI. WMI clients can then enumerate the VC and query or set OIDs that are relative to the VC.

A miniport call manager (MCM) cannot use [**NdisCoAssignInstanceName**](https://msdn.microsoft.com/library/windows/hardware/ff561692) to name its VCs. Instead, an MCM should create a custom GUID and OID for the VC and register the GUID-to-OID mapping with NDIS. For more information about registering custom OIDs, see [Customized OIDs and Status Indications](customized-oids-and-status-indications.md).

 

 





