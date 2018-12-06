---
title: Terminating Offload State
description: Terminating Offload State
ms.assetid: fbe24062-415b-4333-a83f-c595a4250f58
keywords:
- TCP chimney offload WDK networking , terminating offload state
- chimney offload WDK networking , terminating offload state
- offload state WDK TCP chimney offload , terminating offload state
- terminating offload state WDK TCP chimney offload
- terminating offload state WDK TCP chimney offload , about terminating offload state
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# Terminating Offload State


\[The TCP chimney offload feature is deprecated and should not be used.\]




The Terminating Offload State section describes the process of terminating the offload of one or more state objects. Terminating the offload of a state object uploads that state object to the host stack, and terminating the offload of a TCP connection uploads that connection.

Note that terminating the offload of a TCP connection is not the same as closing the connection. The host stack can upload a TCP connection and later close it, or it can close a connection and later upload it.

Only the host stack can initiate a terminate offload operation. An offload target can, however, request that the host stack terminate the offload of a single TCP connection or all TCP connections that have been offloaded to the offload target.

This section includes:

[Terminate Offload Requested by an Offload Target](terminate-offload-requested-by-an-offload-target.md)

[Terminate Offload Initiated by the Host Stack](terminate-offload-initiated-by-the-host-stack.md)

[Terminate Offload Sequence](terminate-offload-sequence.md)

[Handling Segments Received During a Terminate Offload Operation](handling-segments-received-during-a-terminate-offload-operation.md)

[Handling Buffered Receive Data During a Terminate Offload Operation](handling-buffered-receive-data-during-a-terminate-offload-operation.md)

[Handling Send Requests During a Terminate Offload Operation](handling-send-requests-during-a-terminate-offload-operation.md)

[Handling Outstanding Send Data During a Terminate Offload Operation](handling-outstanding-send-data-during-a-terminate-offload-operation.md)

[Returning the Completion Status of a Terminate Offload Operation](returning-the-completion-status-of-a-terminate-offload-operation.md)

 

 





