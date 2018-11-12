---
title: Completing the Transmission of Send Data
description: Completing the Transmission of Send Data
ms.assetid: 63389c7d-8afa-4017-a73a-05f896fd67b2
keywords:
- state offloading process WDK TCP chimney offload , outstanding send data
- offloading state process WDK TCP chimney offload , outstanding send data
- outstanding send data WDK TCP chimney offload
- send data outstanding WDK TCP chimney offload
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# Completing the Transmission of Send Data


\[The TCP chimney offload feature is deprecated and should not be used.\]




The host stack must complete the transmission of all of the send data with one or more calls to the [**NdisTcpOffloadSendComplete**](https://msdn.microsoft.com/library/windows/hardware/ff564609) function.

 

 





