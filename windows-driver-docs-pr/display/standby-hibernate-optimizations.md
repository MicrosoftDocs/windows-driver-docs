---
title: Standby hibernate optimizations
description: Windows 8 offers optimizations to the graphics stack that your driver can optionally take advantage of to improve system performance on sleep and resume.
ms.assetid: 1E71BFDF-3C67-41F6-968A-8AE54B54CCCB
ms.author: windows-driver-content
ms.date: 04/20/2017
ms.topic: article
ms.prod: windows-hardware
ms.technology: windows-devices
---

# Standby hibernate optimizations


Windows 8 offers optimizations to the graphics stack that your driver can optionally take advantage of to improve system performance on sleep and resume.

|                                                                                   |                                             |
|-----------------------------------------------------------------------------------|---------------------------------------------|
| Minimum Windows Display Driver Model (WDDM) version                               | 1.2                                         |
| Minimum Windows version                                                           | 8                                           |
| Driver implementation—Full graphics and Render only                               | Optional                                    |
| [WHCK]( http://go.microsoft.com/fwlink/p/?linkid=258342) requirements and tests | **Device.Graphicsâ€¦StandbyHibernateFlags** |

 

## <span id="Standby_hibernate_device_driver_interface__DDI_"></span><span id="standby_hibernate_device_driver_interface__ddi_"></span><span id="STANDBY_HIBERNATE_DEVICE_DRIVER_INTERFACE__DDI_"></span>Standby hibernate device driver interface (DDI)


These structures are new or updated starting with Windows 8 to support standby hibernation.

-   [**DXGK\_QUERYADAPTERINFOTYPE**](https://msdn.microsoft.com/library/windows/hardware/ff562010)
-   [**DXGK\_SEGMENTDESCRIPTOR3**](https://msdn.microsoft.com/library/windows/hardware/hh464086)
-   [**DXGK\_SEGMENTFLAGS**](https://msdn.microsoft.com/library/windows/hardware/ff562039)

Every device that can support this feature should take advantage of these hibernate optimizations. When a WDDM 1.2 or later driver enumerates segment capabilities, it must also set one or more of the standby hibernate flags **PreservedDuringStandby**, **PreservedDuringHibernate**, and **PartiallyPreservedDuringHibernate**. See Remarks of the [**DXGK\_SEGMENTFLAGS**](https://msdn.microsoft.com/library/windows/hardware/ff562039) topic for more details.

## <span id="standbyopt"></span><span id="STANDBYOPT"></span>Using standby hibernate optimizations


When a PC transitions to sleep or resumes from sleep, several operations occur to make sure that video memory content is properly preserved and restored. Some of these operations are unnecessary and can be avoided:

-   An integrated graphics adapter uses system memory as video memory. Because system memory is always refreshed when a computer goes to sleep, no eviction is necessary. Therefore, the delays that are introduced by the graphics stack can be brought down to zero delay or to the order of few milliseconds.
-   The total time to purge memory on discrete adapters equals the amount of memory that is purged, divided by the rate of purge. Thus the time can be reduced by reducing the amount of memory to purge.

The goal of these operations is to make sure that the only data that is discarded is data that can be re-created.

WDDM 1.2 drivers can take advantage of these optimizations by specifying which allocations should be preserved during power state transitions.

Newer generations of discrete graphics adapters can be designed to refresh their memory when in standby (self refreshing VRAM). These adapters will benefit from these optimizations.

Eviction will still be relevant for discrete graphics adapters that donâ€™t have the self-refreshing VRAM feature. In these cases, the performance optimization is to minimize the amount of data that is preserved. For example, unused data in video memory such as offered allocations, discarded allocations, and unused direct memory access (DMA) buffers can be discarded.

This feature can yield these benefits:

-   Doing no work: On integrated and discrete graphics adapters (with self-refresh VRAM feature), the delay that is introduced by the graphics stack can be brought down to zero delay or to the order of few milliseconds.
-   Doing less work: On discrete graphics adapters, the performance improvement is mostly dependent on how much unused data in video memory is discarded.
-   Reduced memory trashing: The larger the amount of memory evicted, the greater the effect of memory trashing. This has a bigger impact on discrete graphics adapters because they require a large amount of system memory to evict.

## <span id="Hardware_certification_requirements"></span><span id="hardware_certification_requirements"></span><span id="HARDWARE_CERTIFICATION_REQUIREMENTS"></span>Hardware certification requirements


For info on requirements that hardware devices must meet when they implement this feature, refer to the relevant [WHCK documentation]( http://go.microsoft.com/fwlink/p/?linkid=258342) on **Device.Graphicsâ€¦StandbyHibernateFlags**.

See [WDDM 1.2 features](wddm-v1-2-features.md) for a review of features added with Windows 8.

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20[display\display]:%20Standby%20hibernate%20optimizations%20%20RELEASE:%20%282/10/2017%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")




