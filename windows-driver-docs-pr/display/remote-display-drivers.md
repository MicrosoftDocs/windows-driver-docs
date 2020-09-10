---
title: Remote Display Drivers
description: A remote display driver is based on the Windows 2000 Mirror Driver model and is used to render the desktop in a remote session.
ms.assetid: 249528D3-B5F1-41D8-86BF-B9DC623FB480
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# Remote Display Drivers

> [!NOTE]
>
> Support for GDI remote display drivers has been removed in Windows 10, version 2004. However, creating a remote display solution is still possible by building a custom [Remote Protocol Provider](/windows/win32/termserv/creating-a-custom-remote-protocol) and an [Indirect Display Driver](indirect-display-driver-model-overview.md).

A *remote display driver* is based on the Windows 2000 [Mirror Driver](mirror-drivers.md) model and is used to render the desktop in a remote session.

To successfully install and run starting with Windows 8, a remote display driver must implement only the following device driver interfaces (DDIs) and no more.

-   [**DrvAssertMode**](/windows/desktop/api/winddi/nf-winddi-drvassertmode)
-   [**DrvBitBlt**](/windows/desktop/api/winddi/nf-winddi-drvbitblt)
-   [**DrvCompletePDEV**](/windows/desktop/api/winddi/nf-winddi-drvcompletepdev)
-   [**DrvCopyBits**](/windows/desktop/api/winddi/nf-winddi-drvcopybits)
-   [**DrvDisableDriver**](/windows/desktop/api/winddi/nf-winddi-drvdisabledriver)
-   [**DrvDisablePDEV**](/windows/desktop/api/winddi/nf-winddi-drvdisablepdev)
-   [**DrvDisableSurface**](/windows/desktop/api/winddi/nf-winddi-drvdisablesurface)
-   [**DrvEnablePDEV**](/windows/desktop/api/winddi/nf-winddi-drvenablepdev)
-   [**DrvEnableSurface**](/windows/desktop/api/winddi/nf-winddi-drvenablesurface)
-   [**DrvEscape**](/windows/desktop/api/winddi/nf-winddi-drvescape)
-   [**DrvGetModes**](/windows/desktop/api/winddi/nf-winddi-drvgetmodes)
-   [**DrvMovePointer**](/windows/desktop/api/winddi/nf-winddi-drvmovepointer)
-   [**DrvResetPDEV**](/windows/desktop/api/winddi/nf-winddi-drvresetpdev)
-   [**DrvSetPointerShape**](/windows/desktop/api/winddi/nf-winddi-drvsetpointershape)