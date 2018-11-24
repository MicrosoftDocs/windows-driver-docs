---
title: Linking to the NDIS Library
description: Linking to the NDIS Library
ms.assetid: eac33c9e-ff70-4a6c-b391-833a81faa079
keywords:
- NDIS.sys WDK networking
- NDIS library WDK networking
- linking NDIS library WDK networking
- library WDK NDIS
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# Linking to the NDIS Library





The NDIS Library is packaged in Ndis.sys, a kernel-mode export library, as a set of functions, with emphasis on macros for maximum performance. (An export library is a .sys file that functions similarly to a dynamic-link library.) All NDIS drivers link themselves to the NDIS Library. The NDIS Library functions are described in the Network Reference sections of the Microsoft Windows Driver Kit (WDK) documentation.

The WDK provides Ndis.h as the main header file for miniport drivers. This file defines the entry points for the miniport driver, the NDIS Library functions, and common data structures. The Network Reference section describes the miniport driver, protocol driver, and **Ndis*Xxx*** functions and the common data structures and OIDs.

 

 





