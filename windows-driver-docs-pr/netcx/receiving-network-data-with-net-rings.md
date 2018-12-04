---
title: Receiving network data using net rings
description: This topic describes how NetAdapterCx client drivers use net rings and net ring iterators to receive network data.
ms.assetid: 78D202E2-4123-4F63-9B86-48400C2CCC38
keywords:
- NetAdapterCx Net rings and net ring iterators, NetCx Net rings and net ring iterators, NetAdapterCx PCI devices net ring, NetAdapterCx asynchronous I/O
ms.date: 12/04/2018
ms.localizationpriority: medium
---

# Receiving network data with net rings

[!include[NetAdapterCx Beta Prerelease](../netcx-beta-prerelease.md)]

> [!NOTE]
> In this animation, the packets owned by the client driver are highlighted in light blue and dark blue, and fragments owned by the client driver are highlighted in yellow and orange. The lighter colors represent the *drain* subsection of the elements the driver owns, while the darker colors represent the *post* subsection of the elements the driver owns.

![Net ring post and drain operations for receive (Rx)](images/net_ring_post_and_drain_operations_rx.gif "Net ring post and drain operations for receive (Rx)")