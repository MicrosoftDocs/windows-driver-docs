---
title: Extended Blt Flags
description: Extended Blt Flags
ms.assetid: 9c2f7013-dd58-4a61-b452-d263f5caf0d0
keywords:
- extended blt flags WDK DirectX 9.0
- DDBLT_EXTENDED_FLAGS
- blt flag extensions WDK DirectX 9.0
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# Extended Blt Flags


## <span id="ddk_extended_blt_flags_gg"></span><span id="DDK_EXTENDED_BLT_FLAGS_GG"></span>


DirectX 9.0 uses the DDBLT\_EXTENDED\_FLAGS blt flag to extend use of DDBLT\_*Xxx* blt flags that are available in the **dwFlags** member of the [**DD\_BLTDATA**](https://msdn.microsoft.com/library/windows/hardware/ff550474) structure. When the DirectX 9.0 runtime calls the display driver's [*DdBlt*](https://msdn.microsoft.com/library/windows/hardware/ff549205) function to perform a blt operation, the runtime can combine DDBLT\_EXTENDED\_FLAGS with DDBLT\_*Xxx* flags using a bitwise OR to create new meanings for the flags. The driver then determines the presence of DDBLT\_EXTENDED\_FLAGS, reinterprets the meaning of flags, and performs the blt operation accordingly. The driver uses this mechanism when it determines if it should [perform gamma correction](performing-gamma-correction-on-swap-chains.md) on a linear color space during a blt from a back buffer to the desktop. The driver also uses extended blt flags to determine if [stretch-blit operations](supporting-stretch-blit-operations.md) are requested.

 

 





