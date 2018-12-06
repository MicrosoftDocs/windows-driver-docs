---
title: Remote Display Drivers
description: A remote display driver is based on the Windows 2000 Mirror Driver model and is used to render the desktop in a remote session.
ms.assetid: 249528D3-B5F1-41D8-86BF-B9DC623FB480
ms.date: 04/20/2017
ms.localizationpriority: medium
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

 

 





