---
title: Crash Dump and Hibernation Support
description: Crash Dump and Hibernation Support
ms.assetid: 6f5e6f4e-b734-45fe-80d5-fd7b81c9b329
keywords:
- crash dump WDK
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# Crash Dump and Hibernation Support


A Storport virtual miniport driver must support the [**SCSI\_REQUEST\_BLOCK**](https://msdn.microsoft.com/library/windows/hardware/ff565393) (SRB) function code SRB\_FUNCTION\_DUMP\_POINTERS. When a miniport driver receives this type of SRB, the DataBuffer SRB member points to a [**MINIPORT\_DUMP\_POINTERS**](https://msdn.microsoft.com/library/windows/hardware/ff562247) structure. This SRB is sent to a virtual miniport driver that is used to control the disk that holds the crash dump data after the SRB returns from the miniport driver's [**HwStorInitialize**](https://msdn.microsoft.com/library/windows/hardware/ff557396) routine.

 

 




