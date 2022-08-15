---
title: Asynchronous Rendering
description: Asynchronous Rendering
keywords:
- display drivers WDK Windows 2000 , asynchronous rendering
- asynchronous rendering WDK Windows 2000 display
- rendering asynchronously WDK Windows 2000 display
- synchronization WDK Windows 2000 display
- batching DirectDraw drawing calls WDK Windows 2000 display
- DirectDraw WDK Windows 2000 display , call batches
ms.date: 04/20/2017
---

# Asynchronous Rendering

A display driver that handles one or more graphics DDI drawing operations asynchronously provides GDI access to its bitmaps through the use of [**EngModifySurface**](/windows/win32/api/winddi/nf-winddi-engmodifysurface). The driver must also provide a synchronization routine in order to avoid drawing errors if it batches graphics DDI drawing operations.

Such a driver has the option of implementing one of [**DrvSynchronizeSurface**](/windows/win32/api/winddi/nf-winddi-drvsynchronizesurface) or [**DrvSynchronize**](/windows/win32/api/winddi/nf-winddi-drvsynchronize) as the synchronization routine. GDI calls one of these routines only when the driver has hooked them in [**EngAssociateSurface**](/windows/win32/api/winddi/nf-winddi-engassociatesurface). GDI will call only **DrvSynchronizeSurface** in drivers that hook both of these synchronization routines.

[**DrvSynchronizeSurface**](/windows/win32/api/winddi/nf-winddi-drvsynchronizesurface) provides additional information to the driver regarding synchronization events and why they occur. This enables the driver to reduce performance lag due to synchronization. For example, drivers that track which device bitmaps are in the accelerator's queue might be able to return immediately from **DrvSynchronizeSurface** if the specified surface is not currently in the queue.

In addition to providing a synchronization routine, a driver can also activate a *time-based* or *programmatic* flush mechanism by setting the following flags in the **flGraphicsCaps2** field of the [**DEVINFO**](/windows/win32/api/winddi/ns-winddi-devinfo) structure:

* GCAPS2_SYNCTIMER: Setting this flag causes the driver's synchronization routine to be called periodically. Drivers that batch graphics DDI calls must specify this flag. By doing so, these drivers avoid problems such as lag in a software cursor's movement or in drawing that is performed in bursts.

  GDI passes the DSS_TIMER_EVENT flag to [**DrvSynchronizeSurface**](/windows/win32/api/winddi/nf-winddi-drvsynchronizesurface) when this synchronization routine is called due to a periodic event.

* GCAPS2_SYNCFLUSH: Setting this flag causes the driver's synchronization routine to be called whenever the Microsoft Win32 **GdiFlush** API is called. Drivers that perform asynchronous rendering must specify this flag and provide a synchronization routine.

  GDI passes the DSS_FLUSH_EVENT flag to [**DrvSynchronizeSurface**](/windows/win32/api/winddi/nf-winddi-drvsynchronizesurface) when this synchronization routine is called due to a flush-based event. See the Microsoft Windows SDK documentation for more information about **GdiFlush**.

> [!NOTE]
> The driver must never batch DirectDraw drawing calls when the destination surface is the visible screen. Such a situation occurs in a windowed DirectX application where the completed frame is updated to the screen via [*DdBlt*](/windows/win32/api/ddrawint/nc-ddrawint-pdd_surfcb_blt) and should thus be displayed immediately. This restriction also applies to DirectDraw video port surfaces, which might be flipped asynchronously.
