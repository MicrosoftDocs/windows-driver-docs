---
title: Monitor Hot Plug Detection
description: Monitor Hot Plug Detection
ms.assetid: 170d2d5d-fd46-431d-9672-61fa048f7dd2
keywords:
- video present networks WDK display , hot plug detection
- VidPN WDK display , hot plug detection
- video output connectors WDK video present networks
- HPD awareness WDK video present networks
- hot plug detection WDK video present networks
- unplugged detection WDK video present networks
- connected monitors WDK video present networks
- not connected monitors WDK video present networks
- unconnected monitors WDK video present networks
- portable computer video output WDK video present networks
- mobile computer video output WDK video present networks
- monitor hot plug detection WDK video present networks
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# Monitor Hot Plug Detection


A video output on a display adapter is considered a child device of the display adapter. A monitor or other external display device that connects to the output is not considered a child device. During initialization, the display miniport driver's [**DxgkDdiQueryChildRelations**](https://msdn.microsoft.com/library/windows/hardware/ff559750) function assigns each child device a type and an HPD awareness value. The type is one of the [**DXGK\_CHILD\_DEVICE\_TYPE**](https://msdn.microsoft.com/library/windows/hardware/ff561008) enumerators:

-   **TypeVideoOutput**

-   **TypeOther**

The HPD awareness value is one of the [**DXGK\_CHILD\_DEVICE\_HPD\_AWARENESS**](https://msdn.microsoft.com/library/windows/hardware/ff561006) enumerators:

-   **HpdAwarenessAlwaysConnected**

-   **HpdAwarenessInterruptible**

-   **HpdAwarenessPolled**

A child device that has a type of **TypeVideoOutput** and any HPD awareness value other than **HpdAwarenessAlwaysConnected** is called a *video output connector*.

If the display miniport driver cannot determine whether a monitor is connected to the video output, the driver should emulate the behavior of an interruptible device, with the HPD awareness value set to **HpdAwarenessInterruptible**. If the display miniport driver needs to indicate that an interruptible monitor should be connected to the video output, such as when a user enters a keyboard shortcut to switch to a television view, the driver should call the [**DxgkCbIndicateChildStatus**](https://msdn.microsoft.com/library/windows/hardware/ff559522) function with *ChildStatus*.**HotPlug**.**Connected** set to **TRUE**.

At certain times, the operating system requests that the display miniport driver report the status of all video output connectors that have an HPD awareness value of **HpdAwarenessPolled**. There is no regular polling interval; rather, the request is made when there is a specific need to update the list of available display devices and modes. For example, when a laptop computer is docked, the operating system needs to know whether a monitor is connected to the video output on the docking station. The operating system makes the request by calling the display miniport driver's [**DxgkDdiQueryChildStatus**](https://msdn.microsoft.com/library/windows/hardware/ff559754) function for each child device that has an HPD awareness value of **HpdAwarenessPolled**.

For video output connectors that have an HPD awareness value of **HpdAwarenessInterruptible**, the display miniport driver is responsible for notifying the operating system whenever an external display device is hot plugged or unplugged. The display miniport driver's interrupt handling code calls the display port driver's [**DxgkCbIndicateChildStatus**](https://msdn.microsoft.com/library/windows/hardware/ff559522) function to report that an external display device has been connected to or disconnected from a particular video output. When a laptop computer is docked, the display miniport driver's [*DxgkDdiNotifyAcpiEvent*](https://msdn.microsoft.com/library/windows/hardware/ff559695) function must call **DxgkCbIndicateChildStatus** for each video output on the docking station that has an HPD awareness value of **HpdAwarenessInterruptible**.

If a connector with an HPD awareness value of **HpdAwarenessPolled** is made unavailable (that is, covered up) when a laptop computer is docked, the display miniport driver's *DxgkDdiNotifyAcpiEvent* function must call **DxgkCbIndicateChildStatus** to report that the connector is disconnected.

The video output associated with an integrated display panel on a portable computer is an unusual case. The operating system needs to know whether the portable computer's lid is open or closed, so the idea of *connected* is used to mean open and the idea of *not connected* is used to mean closed. The video output associated with an integrated display on a portable computer has an HPD awareness value of **HpdAwarenessInterruptible**. That does not mean, however, that the display adapter generates an interrupt when the lid is opened or closed. Rather, the ACPI BIOS generates an interrupt when the lid is opened or closed. That interrupt results in a call to the display miniport driver's [*DxgkDdiNotifyAcpiEvent*](https://msdn.microsoft.com/library/windows/hardware/ff559695) function, which calls **DxgkCbIndicateChildStatus** to report the status (open or closed) of the lid. The display miniport driver reports the status of the lid by setting the **HotPlug.Connected** member of a [**DXGK\_CHILD\_STATUS**](https://msdn.microsoft.com/library/windows/hardware/ff561010) structure to **TRUE** (open) or **FALSE** (closed) and passing the DXGK\_CHILD\_STATUS structure to **DxgkCbIndicateChildStatus**.

The following list describes the steps followed when a monitor is connected to an HD15 connector, assuming that the connector has an HPD awareness value of **HpdAwarenessPolled**.

1.  A monitor is connected to the HD15 connector on the display adapter. The display adapter does not detect this as a hot-plug event.

2.  At some future time, a user-mode application requests a list of display devices.

3.  For each video output connector on the display adapter that has an HPD awareness value of **HpdAwarenessPolled**, the VidPN manager calls the display miniport driver's [**DxgkDdiQueryChildStatus**](https://msdn.microsoft.com/library/windows/hardware/ff559754) function to determine whether an external display device is connected. When *DxgkDdiQueryChildStatus* is called for the HD15 connector, it reports that an external monitor is indeed connected.

The following list describes the steps followed when a monitor is connected to a DVI connector, assuming that the connector has an HPD awareness value of **HpdAwarenessInterruptible**.

1.  A flat panel is connected to the DVI connector on the display adapter.

2.  The display adapter detects a hot-plug event and generates an interrupt.

3.  The interrupt is handled by the display miniport driver's [**DxgkDdiInterruptRoutine**](https://msdn.microsoft.com/library/windows/hardware/ff559680) function, which schedules a deferred procedure call (DPC). Subsequently the display miniport driver's DPC callback function is called.

4.  The DPC callback function passes a DXGK\_CHILD\_STATUS structure to the display port driver's [**DxgkCbIndicateChildStatus**](https://msdn.microsoft.com/library/windows/hardware/ff559522) function to report the status of the DVI connector. The **ChildUid** member of the DXGK\_CHILD\_STATUS structure identifies the DVI connector, and the **HotPlug.Connected** member (set to **TRUE** in this case) indicates that an external display device is connected.

Suppose a DVI connector supports a dongle that has three branches: DVI, HD15, and S-video. In that case, the display miniport driver would have previously enumerated three child devices associated with the one physical DVI connector: DVI-on-DVI, HD15-on-DVI, and S-video-on-DVI. Each of those child devices would have a type of **TypeVideoOutput** and an HPD awareness value of **HpdAwarenessInterruptible**. The following list describes the steps followed when a monitor is connected to the HD15 branch of the dongle.

1.  The display adapter detects a hot-plug event and generates an interrupt.

2.  The interrupt is handled by the display miniport driver's [**DxgkDdiInterruptRoutine**](https://msdn.microsoft.com/library/windows/hardware/ff559680) function, which schedules a deferred procedure call (DPC). Subsequently the display miniport driver's DPC callback function is called.

3.  The DPC callback function determines that the hot-plug event was on the HD15 branch of the dongle (HD15-on-DVI).

4.  The DPC callback functions passes a DXGK\_CHILD\_STATUS structure to [**DxgkCbIndicateChildStatus**](https://msdn.microsoft.com/library/windows/hardware/ff559522) to report the status of the HD15-on-DVI video output. The **ChildUid** member of the DXGK\_CHILD\_STATUS structure identifies the video output, and the **HotPlug.Connected** member (set to **TRUE** in this case) indicates that an external display device is connected.

The following list describes the steps followed when the lid is closed on a laptop computer.

1.  The lid is closed on a portable computer, which generates an ACPI event. Subsequently, the display miniport driver's [*DxgkDdiNotifyAcpiEvent*](https://msdn.microsoft.com/library/windows/hardware/ff559695) function is called.

2.  *DxgkDdiNotifyAcpiEvent* passes a DXGK\_CHILD\_STATUS structure to the display port driver's **DxgkCbIndicateChildStatus** function to report the status of the child device associated with the built-in display panel. Specifically, *DxgkDdiNotifyAcpiEvent* sets the **HotPlug.Connected** member of the DXGK\_CHILD\_STATUS structure to **FALSE**.

 

 





