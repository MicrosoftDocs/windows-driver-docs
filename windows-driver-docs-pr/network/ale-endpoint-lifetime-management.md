---
title: ALE Endpoint Lifetime Management
description: ALE Endpoint Lifetime Management
ms.assetid: cbf54062-4ced-4cf6-babf-e9e4e1ddf302
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# ALE Endpoint Lifetime Management


A callout driver that supports application layer enforcement (ALE) may need to allocate resources to process indications. This topic describes how to configure a callout driver to release such resources when the associated endpoint is closed. ALE endpoint lifetime management is supported in Windows 7 and later versions of Windows.

To manage resources associated with ALE endpoints, a callout driver can register at the following layers:

-   FWPS\_LAYER\_ALE\_RESOURCE\_RELEASE\_V4 (FWPM\_LAYER\_ALE\_RESOURCE\_RELEASE\_V4)

-   FWPS\_LAYER\_ALE\_RESOURCE\_RELEASE\_V6 (FWPM\_LAYER\_ALE\_RESOURCE\_RELEASE\_V6)

-   FWPS\_LAYER\_ALE\_ENDPOINT\_CLOSURE\_V4 (FWPM\_LAYER\_ALE\_ENDPOINT\_CLOSURE\_V4)

-   FWPS\_LAYER\_ALE\_ENDPOINT\_CLOSURE\_V6 (FWPM\_LAYER\_ALE\_ENDPOINT\_CLOSURE\_V6)

An ALE resource release layer is indicated for every indication at the corresponding ALE resource assignment layer (for example, FWPS\_LAYER\_ALE\_RESOURCE\_ASSIGNMENT\_V4). To ensure that callout drivers can match the release layer to the assignment layer, the FWPS\_METADATA\_FIELD\_TRANSPORT\_ENDPOINT\_HANDLE metadata field is provided at both layers and each endpoint is assigned a unique handle.

ALE endpoint closure layers are invoked differently depending on the type of endpoint. For TCP connections, an ALE endpoint closure is indicated for every ALE authorize connect layer (for example FWPS\_LAYER\_ALE\_AUTH\_CONNECT\_V4) or ALE authorize receive accept layer (for example FWPS\_LAYER\_ALE\_AUTH\_RECV\_ACCEPT\_V4) indication. As with ALE resource release indications, the engine assigns a unique handle for each endpoint and passes it in the FWPS\_METADATA\_FIELD\_TRANSPORT\_ENDPOINT\_HANDLE metadata field. For non-TCP endpoints, an ALE endpoint closure layer is invoked for each endpoint regardless of the number of unique remote peers the socket communicates with. An ALE endpoint closure layer is also invoked for each TCP listening socket.

Callouts registered for an ALE endpoint closure layer can pend classification. This enables the callout to reinject any packets queued for asynchronous processing before the endpoint is shut down. To pend classification, the callout driver must call [**FwpsPendClassify0**](https://msdn.microsoft.com/library/windows/hardware/ff551197) followed by a call to [**FwpsCompleteClassify0**](https://msdn.microsoft.com/library/windows/hardware/ff551150) when processing is complete.

When applicable, the engine will indicate a unique handle for the parent endpoint in the FWPS\_METADATA\_FIELD\_PARENT\_ENDPOINT\_HANDLE metadata field. This enables the callout driver to track parent/child relationships, if required.

 

 





