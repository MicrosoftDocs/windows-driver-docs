---
title: Sending network data using net rings
description: This topic describes how NetAdapterCx client drivers use net rings and net ring iterators to send network data.
ms.assetid: 2F3DA1A5-D0C1-4928-80B2-AF41F949FF14
keywords:
- NetAdapterCx Net rings and net ring iterators, NetCx Net rings and net ring iterators, NetAdapterCx PCI devices net ring, NetAdapterCx asynchronous I/O
ms.date: 12/04/2018
ms.localizationpriority: medium
---

# Sending network data with net rings

[!include[NetAdapterCx Beta Prerelease](../netcx-beta-prerelease.md)]


> [!NOTE]
> In this animation, the packets owned by the client driver are highlighted in light blue and dark blue, and fragments owned by the client driver are highlighted in yellow and orange. The lighter colors represent the *drain* subsection of the elements the driver owns, while the darker colors represent the *post* subsection of the elements the driver owns.

![Net ring post and drain operations for transmit (Tx)](images/net_ring_post_and_drain_operations_tx.gif "Net ring post and drain operations for transmit (Tx)")
