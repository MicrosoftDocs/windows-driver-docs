---
title: Porting Miniport Driver Status Indications to CoNDIS 6.0
description: Porting Miniport Driver Status Indications to CoNDIS 6.0
ms.assetid: 149c0305-d26e-4e40-9304-064396de3a3d
keywords:
- porting status indications WDK networking
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# Porting Miniport Driver Status Indications to CoNDIS 6.0





In CoNDIS 6.0, the [**NdisMCoIndicateStatusEx**](https://msdn.microsoft.com/library/windows/hardware/ff563562) function replaces the NDIS 5.x [**NdisMCoIndicateStatus**](https://msdn.microsoft.com/library/windows/hardware/ff553458) function. Status indication parameters are packaged within an [**NDIS\_STATUS\_INDICATION**](https://msdn.microsoft.com/library/windows/hardware/ff567373) structure that contains the source handle, status code, buffer, and size.

For more information about status indications in CoNDIS miniport drivers, see [CoNDIS Miniport Driver Status Indications](condis-miniport-driver-status-indications.md).

 

 





