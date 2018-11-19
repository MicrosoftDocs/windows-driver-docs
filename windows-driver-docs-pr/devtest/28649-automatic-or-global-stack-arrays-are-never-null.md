---
title: C28649
description: Warning C28649 Automatic or Global Stack Arrays are never NULL.
ms.assetid: 5440269b-6deb-4956-973a-201ab6c4c027
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# C28649


warning C28649: Automatic or Global Stack Arrays are never NULL

Stack-based arrays can never be **NULL**. However, most of the time the intention is to check a particular element (mostly the first element) against **NULL** or for a **nul** character. Due to an error of omission, the programmer misses the dereferencing (\*) operator that results in the array being checked instead.

 

 





