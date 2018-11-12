---
title: Issuing Set and Query Requests from an Intermediate Driver
description: Issuing Set and Query Requests from an Intermediate Driver
ms.assetid: bd049639-970c-43c8-8ef9-c5e75cc2d75f
keywords:
- query operations WDK NDIS intermediate
- set operations WDK NDIS intermediate
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# Issuing Set and Query Requests from an Intermediate Driver





The protocol edge of an intermediate driver can issue set and query information requests to the underlying miniport driver. The virtual miniport edge of an intermediate driver can use the information obtained from the underlying driver to determine how to respond to set and query requests.

To cancel an OID request, call the [**NdisCancelOidRequest**](https://msdn.microsoft.com/library/windows/hardware/ff561622) function.

For more information about responding to set and query requests, see [Responding to Sets and Queries in an Intermediate Driver](responding-to-sets-and-queries-in-an-intermediate-driver.md). For more information about issuing OID requests, see [OID Request Operations in a Protocol Driver](oid-request-operations-in-a-protocol-driver.md).

 

 





