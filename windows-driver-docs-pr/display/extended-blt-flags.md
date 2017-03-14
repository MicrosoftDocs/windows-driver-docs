---
title: Extended Blt Flags
description: Extended Blt Flags
ms.assetid: 9c2f7013-dd58-4a61-b452-d263f5caf0d0
keywords: ["extended blt flags WDK DirectX 9.0", "DDBLT_EXTENDED_FLAGS", "blt flag extensions WDK DirectX 9.0"]
---

# Extended Blt Flags


## <span id="ddk_extended_blt_flags_gg"></span><span id="DDK_EXTENDED_BLT_FLAGS_GG"></span>


DirectX 9.0 uses the DDBLT\_EXTENDED\_FLAGS blt flag to extend use of DDBLT\_*Xxx* blt flags that are available in the **dwFlags** member of the [**DD\_BLTDATA**](https://msdn.microsoft.com/library/windows/hardware/ff550474) structure. When the DirectX 9.0 runtime calls the display driver's [*DdBlt*](https://msdn.microsoft.com/library/windows/hardware/ff549205) function to perform a blt operation, the runtime can combine DDBLT\_EXTENDED\_FLAGS with DDBLT\_*Xxx* flags using a bitwise OR to create new meanings for the flags. The driver then determines the presence of DDBLT\_EXTENDED\_FLAGS, reinterprets the meaning of flags, and performs the blt operation accordingly. The driver uses this mechanism when it determines if it should [perform gamma correction](performing-gamma-correction-on-swap-chains.md) on a linear color space during a blt from a back buffer to the desktop. The driver also uses extended blt flags to determine if [stretch-blit operations](supporting-stretch-blit-operations.md) are requested.

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20[display\display]:%20Extended%20Blt%20Flags%20%20RELEASE:%20%282/10/2017%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")




