---
title: Asynchronous Rendering
description: Asynchronous Rendering
ms.assetid: f291e416-aaee-4639-9410-6d01b3b02097
keywords:
- display drivers WDK Windows 2000 , asynchronous rendering
- asynchronous rendering WDK Windows 2000 display
- rendering asynchronously WDK Windows 2000 display
- synchronization WDK Windows 2000 display
- batching DirectDraw drawing calls WDK Windows 2000 display
- DirectDraw WDK Windows 2000 display , call batches
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# Asynchronous Rendering


## <span id="ddk_asynchronous_rendering_gg"></span><span id="DDK_ASYNCHRONOUS_RENDERING_GG"></span>


A display driver that handles one or more graphics DDI drawing operations asynchronously and provides GDI access to its bitmaps through the use of [**EngModifySurface**](https://msdn.microsoft.com/library/windows/hardware/ff564976) must implement a [*synchronization routine*](https://msdn.microsoft.com/library/windows/hardware/ff556336#wdkgloss-synchronization-routine). The driver must also provide a synchronization routine in order to avoid drawing errors if it batches graphics DDI drawing operations.

Such a driver has the option of implementing one of [**DrvSynchronizeSurface**](https://msdn.microsoft.com/library/windows/hardware/ff557273) or [**DrvSynchronize**](https://msdn.microsoft.com/library/windows/hardware/ff556323) as the synchronization routine. GDI calls one of these routines only when the driver has hooked them in [**EngAssociateSurface**](https://msdn.microsoft.com/library/windows/hardware/ff564183). GDI will call only **DrvSynchronizeSurface** in drivers that hook both of these synchronization routines.

[**DrvSynchronizeSurface**](https://msdn.microsoft.com/library/windows/hardware/ff557273) provides additional information to the driver regarding synchronization events and why they occur. This enables the driver to reduce performance lag due to synchronization. For example, drivers that track which device bitmaps are in the accelerator's queue might be able to return immediately from **DrvSynchronizeSurface** if the specified surface is not currently in the queue.

In addition to providing a synchronization routine, a driver can also activate a *time-based* or *programmatic*[*flush mechanism*](https://msdn.microsoft.com/library/windows/hardware/ff556280#wdkgloss-flush-mechanism) by setting the following flags in the **flGraphicsCaps2** field of the [**DEVINFO**](https://msdn.microsoft.com/library/windows/hardware/ff552835) structure:

-   GCAPS2\_SYNCTIMER -- Setting this flag causes the driver's synchronization routine to be called periodically. Drivers that batch graphics DDI calls must specify this flag. By doing so, these drivers avoid problems such as lag in a software cursor's movement or in drawing that is performed in bursts.

    GDI passes the DSS\_TIMER\_EVENT flag to [**DrvSynchronizeSurface**](https://msdn.microsoft.com/library/windows/hardware/ff557273) when this synchronization routine is called due to a periodic event.

-   GCAPS2\_SYNCFLUSH -- Setting this flag causes the driver's synchronization routine to be called whenever the Microsoft Win32 **GdiFlush** API is called. Drivers that perform asynchronous rendering must specify this flag and provide a synchronization routine.

    GDI passes the DSS\_FLUSH\_EVENT flag to [**DrvSynchronizeSurface**](https://msdn.microsoft.com/library/windows/hardware/ff557273) when this synchronization routine is called due to a flush-based event. See the Microsoft Windows SDK documentation for more information about **GdiFlush**.

### <span id="Limitations_on_Batching_DirectDraw_Drawing_Calls"></span><span id="limitations_on_batching_directdraw_drawing_calls"></span><span id="LIMITATIONS_ON_BATCHING_DIRECTDRAW_DRAWING_CALLS"></span>Limitations on Batching DirectDraw Drawing Calls

The driver must never batch DirectDraw drawing calls when the destination surface is the visible screen. Such a situation occurs in a windowed DirectX application where the completed frame is updated to the screen via [*DdBlt*](https://msdn.microsoft.com/library/windows/hardware/ff549205) and should thus be displayed immediately. This restriction also applies to DirectDraw video port surfaces, which might be flipped asynchronously.

 

 





