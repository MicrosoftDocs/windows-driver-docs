---
title: Preparing for NDIS Debugging
description: Preparing for NDIS Debugging
ms.assetid: 9a23cc3a-5940-46c3-928f-7fac46dfaba2
keywords: ["NDIS debugging, setup"]
ms.author: domars
ms.date: 05/23/2017
ms.localizationpriority: medium
---

# Preparing for NDIS Debugging


To debug NDIS components, a checked version of Ndis.sys is required on the target computer. However, instead of installing an entire checked-build operating system, you can copy the checked version of Ndis.sys onto an otherwise free-build operating system. Before you copy the checked version of Ndis.sys to the target computer, you must disable Windows File Protection (WFP). To ensure that WFP is disabled, start the operating system in safe mode.

The NDIS symbols are publicly available on the Microsoft symbol store. For details on how to access this, see [Microsoft Public Symbols](microsoft-public-symbols.md).

 

 





