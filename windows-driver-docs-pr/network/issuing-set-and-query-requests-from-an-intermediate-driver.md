---
title: Issuing Set and Query Requests from an Intermediate Driver
description: Issuing Set and Query Requests from an Intermediate Driver
keywords:
- query operations WDK NDIS intermediate
- set operations WDK NDIS intermediate
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# Issuing Set and Query Requests from an Intermediate Driver





The protocol edge of an intermediate driver can issue set and query information requests to the underlying miniport driver. The virtual miniport edge of an intermediate driver can use the information obtained from the underlying driver to determine how to respond to set and query requests.

To cancel an OID request, call the [**NdisCancelOidRequest**](/windows-hardware/drivers/ddi/ndis/nf-ndis-ndiscanceloidrequest) function.

For more information about responding to set and query requests, see [Responding to Sets and Queries in an Intermediate Driver](responding-to-sets-and-queries-in-an-intermediate-driver.md). For more information about issuing OID requests, see [OID Request Operations in a Protocol Driver](oid-request-operations-in-a-protocol-driver.md).

 

