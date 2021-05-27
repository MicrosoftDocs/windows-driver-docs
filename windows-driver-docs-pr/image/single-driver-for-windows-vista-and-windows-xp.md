---
title: Single Driver for Windows Vista and Windows XP
description: Single Driver for Windows Vista and Windows XP
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# Single Driver for Windows Vista and Windows XP


You might want to have a single driver for both Windows Vista and Windows XP. In such situations, the driver handles data transfers by checking the flags. When [**IWiaMiniDrv::drvAcquireItemData**](/windows-hardware/drivers/ddi/wiamindr_lh/nf-wiamindr_lh-iwiaminidrv-drvacquireitemdata) is called for stream-based transfers, the *lFlags* parameter is set to either WIA\_MINIDRV\_TRANSFER\_DOWNLOAD or WIA\_MINIDRV\_TRANSFER\_UPLOAD. If neither of these bits is set, the transfer is a *legacy* transfer and the driver should follow the behavior that is outlined for Windows XP data transfers.

 

