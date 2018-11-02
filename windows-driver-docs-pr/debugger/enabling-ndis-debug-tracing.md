---
title: Enabling NDIS Debug Tracing
description: Enabling NDIS Debug Tracing
ms.assetid: 4ca3c246-3e73-46fb-93a5-ea376788e330
keywords: ["NDIS debugging, debug tracing"]
ms.author: domars
ms.date: 05/23/2017
ms.localizationpriority: medium
---

# Enabling NDIS Debug Tracing


NDIS debug tracing is the primary method for debugging NDIS drivers. When you set up NDIS debug tracing, you are actually enabling one or more levels of DbgPrint statements with NDIS. The resulting information is sufficient for debugging most network driver problems.

You can enable debug tracing by setting appropriate registry values. For details, see [Enabling NDIS Debug Tracing By Setting Registry Values](enabling-ndis-debug-tracing-by-setting-registry-values.md).

Setting registry values to enable debug tracing works even if the host computer does not have the checked version of the Ndis.sys symbols installed.

 

 





