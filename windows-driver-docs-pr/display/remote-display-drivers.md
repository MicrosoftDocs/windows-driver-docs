---
title: Remote Display Drivers
description: A remote display driver is based on the Windows 2000 Mirror Driver model and is used to render the desktop in a remote session.
ms.assetid: 249528D3-B5F1-41D8-86BF-B9DC623FB480
ms.author: windowsdriverdev
ms.date: 04/20/2017
ms.topic: article
ms.prod: windows-hardware
ms.technology: windows-devices
---

# Remote Display Drivers


A *remote display driver* is based on the Windows 2000 [Mirror Driver](mirror-drivers.md) model and is used to render the desktop in a remote session.

To successfully install and run starting with Windows 8, a remote display driver must implement only the following device driver interfaces (DDIs) and no more.

-   [**DrvAssertMode**](https://msdn.microsoft.com/library/windows/hardware/ff556178)
-   [**DrvBitBlt**](https://msdn.microsoft.com/library/windows/hardware/ff556180)
-   [**DrvCompletePDEV**](https://msdn.microsoft.com/library/windows/hardware/ff556181)
-   [**DrvCopyBits**](https://msdn.microsoft.com/library/windows/hardware/ff556182)
-   [**DrvDisableDriver**](https://msdn.microsoft.com/library/windows/hardware/ff556196)
-   [**DrvDisablePDEV**](https://msdn.microsoft.com/library/windows/hardware/ff556198)
-   [**DrvDisableSurface**](https://msdn.microsoft.com/library/windows/hardware/ff556200)
-   [**DrvEnablePDEV**](https://msdn.microsoft.com/library/windows/hardware/ff556211)
-   [**DrvEnableSurface**](https://msdn.microsoft.com/library/windows/hardware/ff556214)
-   [**DrvEscape**](https://msdn.microsoft.com/library/windows/hardware/ff556217)
-   [**DrvGetModes**](https://msdn.microsoft.com/library/windows/hardware/ff556233)
-   [**DrvMovePointer**](https://msdn.microsoft.com/library/windows/hardware/ff556248)
-   [**DrvResetPDEV**](https://msdn.microsoft.com/library/windows/hardware/ff556276)
-   [**DrvSetPointerShape**](https://msdn.microsoft.com/library/windows/hardware/ff556289)

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20[display\display]:%20Remote%20Display%20Drivers%20%20RELEASE:%20%282/10/2017%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")




