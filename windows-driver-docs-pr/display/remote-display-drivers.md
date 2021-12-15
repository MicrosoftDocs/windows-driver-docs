---
title: Remote Display Drivers
description: A remote display driver is based on the Windows 2000 Mirror Driver model and is used to render the desktop in a remote session.
ms.date: 04/20/2017
---

# Remote Display Drivers

> [!NOTE]
>
> Support for GDI remote display drivers has been removed in Windows 10, version 2004. However, creating a remote display solution is still possible by building a custom [Remote Protocol Provider](/windows/win32/termserv/creating-a-custom-remote-protocol) and an [Indirect Display Driver](indirect-display-driver-model-overview.md).

A *remote display driver* is based on the Windows 2000 [Mirror Driver](mirror-drivers.md) model and is used to render the desktop in a remote session.

To successfully install and run starting with Windows 8, a remote display driver must implement only the following device driver interfaces (DDIs) and no more.

-   [**DrvAssertMode**](/windows/win32/api/winddi/nf-winddi-drvassertmode)
-   [**DrvBitBlt**](/windows/win32/api/winddi/nf-winddi-drvbitblt)
-   [**DrvCompletePDEV**](/windows/win32/api/winddi/nf-winddi-drvcompletepdev)
-   [**DrvCopyBits**](/windows/win32/api/winddi/nf-winddi-drvcopybits)
-   [**DrvDisableDriver**](/windows/win32/api/winddi/nf-winddi-drvdisabledriver)
-   [**DrvDisablePDEV**](/windows/win32/api/winddi/nf-winddi-drvdisablepdev)
-   [**DrvDisableSurface**](/windows/win32/api/winddi/nf-winddi-drvdisablesurface)
-   [**DrvEnablePDEV**](/windows/win32/api/winddi/nf-winddi-drvenablepdev)
-   [**DrvEnableSurface**](/windows/win32/api/winddi/nf-winddi-drvenablesurface)
-   [**DrvEscape**](/windows/win32/api/winddi/nf-winddi-drvescape)
-   [**DrvGetModes**](/windows/win32/api/winddi/nf-winddi-drvgetmodes)
-   [**DrvMovePointer**](/windows/win32/api/winddi/nf-winddi-drvmovepointer)
-   [**DrvResetPDEV**](/windows/win32/api/winddi/nf-winddi-drvresetpdev)
-   [**DrvSetPointerShape**](/windows/win32/api/winddi/nf-winddi-drvsetpointershape)
