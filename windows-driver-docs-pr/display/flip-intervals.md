---
title: Flip Intervals
description: Flip Intervals
ms.assetid: 9372d63c-e2a7-4f70-a4f0-c50df9183f75
keywords:
- drawing page flips WDK DirectDraw , intervals
- DirectDraw flipping WDK Windows 2000 display , intervals
- page flipping WDK DirectDraw , intervals
- flipping WDK DirectDraw , intervals
- posted flips WDK DirectDraw
- retired flips WDK DirectDraw
- DDCAPS2_FLIPNOVSYNC
- DDCAPS2_FLIPINTERVAL
- DDFLIP_NOVSYNC
- DDFLIP_INTERVAL2
- DDFLIP_INTERVAL3
- DDFLIP_INTERVAL4
- DDERR_WASSTILLDRAWING
- pending flips WDK DirectDraw
- drawing page flips WDK DirectDraw , timing
- DirectDraw flipping WDK Windows 2000 display , timing
- page flipping WDK DirectDraw , timing
- flipping WDK DirectDraw , timing
- timing flips WDK DirectDraw
- surfaces WDK DirectDraw , flipping
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# Flip Intervals


## <span id="ddk_flip_intervals_gg"></span><span id="DDK_FLIP_INTERVALS_GG"></span>


Beginning with DirectX 6.0, DirectDraw added the ability for an application to determine when a flip command is performed. Support for these features can be added to an existing driver, depending on the hardware capabilities.

The following terms are used when describing the timing related to the application's call to **Flip**:

<span id="Posted"></span><span id="posted"></span><span id="POSTED"></span>**Posted**  
The time at which the application calls **Flip** and DirectDraw calls the driver's [*DdFlip*](https://msdn.microsoft.com/library/windows/hardware/ff549306) entry point.

<span id="Retired"></span><span id="retired"></span><span id="RETIRED"></span>**Retired**  
The time at which the hardware begins displaying from the new surface.

In previous versions of DirectDraw, flips were always retired on or near the vertical sync following when they were posted. With DirectX 6.0 and later versions, applications can specify that the flip be retired immediately, that is, exactly when posted, or at some set number of vertical syncs after the flip is posted. There are two capability bits (DDCAPS2\_FLIPNOVSYNC and DDCAPS2\_FLIPINTERVAL in the [**DDCORECAPS**](https://msdn.microsoft.com/library/windows/hardware/ff549248) structure) and four flags (DDFLIP\_NOVSYNC, DDFLIP\_INTERVAL2, DDFLIP\_INTERVAL3, and DDFLIP\_INTERVAL4 in the [**DD\_FLIPDATA**](https://msdn.microsoft.com/library/windows/hardware/ff551520) structure) to enable these features.

If your driver sets DDCAPS2\_FLIPNOVSYNC, it receives the DDFLIP\_NOVSYNC flag in the **dwFlags** member of the DD\_FLIPDATA structure. The DDFLIP\_NOVSYNC flag indicates that the flip should be retired as soon as it is posted. However, in this case, your hardware must be able to switch buffers on at least a per-scan line basis. The driver should not specify support for DDCAPS2\_FLIPNOVSYNC if the display does not actually retire the flip until the next vertical sync, even if the driver returns immediately.

The number at the end of the DDFLIP\_INTERVAL2, DDFLIP\_INTERVAL3, and DDFLIP\_INTERVAL4 flags denotes how many vertical syncs the hardware should wait before retiring a posted flip. For example, DDFLIP\_INTERVAL2 means that the hardware should count two vertical syncs, then retire the flip on or near the second vertical sync.

If your driver exposes DDCAPS2\_FLIPINTERVAL, then DirectDraw places the number of vertical syncs to delay a flip by, into the most significant byte of the **dwFlags** member of the [**DD\_FLIPDATA**](https://msdn.microsoft.com/library/windows/hardware/ff551520) structure. Because the DDFLIP\_INTERVAL2, DDFLIP\_INTERVAL3, and DDFLIP\_INTERVAL4 flags are defined to make this true, the driver should not treat these three flags as bit flags. Additionally, if the driver exposes DDCAPS2\_FLIPINTERVAL, DirectDraw ensures that the most significant byte of the **dwFlags** member is set accordingly when the DDFLIP\_INTERVAL2, DDFLIP\_INTERVAL3, and DDFLIP\_INTERVAL4 flags are not set. DDFLIP\_NOVSYNC causes a zero to be placed in the most significant byte, and the default value of the most significant byte becomes one because the default behavior of a flip call is to retire the flip on or near the first vertical sync after it is posted.

Since DirectX 1.0, drivers have been required to return DDERR\_WASSTILLDRAWING whenever a flip was pending (that is, when the flip had been posted but not yet retired). This requirement is extended for flip intervals. Because DDFLIP\_NOVSYNC flips are retired when they are posted and therefore are never pending, the driver should never return DDERR\_WASSTILLDRAWING as a result of such flips. Conversely, using one of the DDFLIP\_INTERVAL2, DDFLIP\_INTERVAL3, or DDFLIP\_INTERVAL4 flags means that the driver needs to return DDERR\_WASSTILLDRAWING for a long period of time, because the period between posting and retiring a flip is extended.

DirectDraw does not preclude the use of these flags with overlay surfaces, but drivers are not required to respect them, even if they do set the DDCAPS2\_FLIPINTERVAL or DDCAPS2\_FLIPNOVSYNC capability bits. Drivers may choose to respect these flags for overlays if they have the capability, but applications are unlikely to exploit this feature.

**Note**   The DDFLIP\_INTERVAL2, DDFLIP\_INTERVAL3, and DDFLIP\_INTERVAL4 flags are intended to exploit hardware capabilities. Drivers should not attempt to emulate these flags by looping in the driver until the flip can be retired as requested. Because important operating system mutexes are held while calling a DirectDraw driver, such an implementation can affect system performance.

 

 

 





