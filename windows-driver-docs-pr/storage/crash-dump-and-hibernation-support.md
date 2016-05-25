---
title: Crash Dump and Hibernation Support
author: windows-driver-content
description: Crash Dump and Hibernation Support
ms.assetid: 6f5e6f4e-b734-45fe-80d5-fd7b81c9b329
keywords: ["crash dump WDK"]
---

# Crash Dump and Hibernation Support


A Storport virtual miniport driver must support the [**SCSI\_REQUEST\_BLOCK**](https://msdn.microsoft.com/library/windows/hardware/ff565393) (SRB) function code SRB\_FUNCTION\_DUMP\_POINTERS. When a miniport driver receives this type of SRB, the DataBuffer SRB member points to a [**MINIPORT\_DUMP\_POINTERS**](https://msdn.microsoft.com/library/windows/hardware/ff562247) structure. This SRB is sent to a virtual miniport driver that is used to control the disk that holds the crash dump data after the SRB returns from the miniport driver's [**HwStorInitialize**](https://msdn.microsoft.com/library/windows/hardware/ff557396) routine.

 

 


--------------------
[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20[storage\storage]:%20Crash%20Dump%20and%20Hibernation%20Support%20%20RELEASE:%20%285/9/2016%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")


