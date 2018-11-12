---
title: Enumerating Child Devices of a Display Adapter
description: Enumerating Child Devices of a Display Adapter
ms.assetid: 3bec2117-aef4-41fc-b88a-0081c7c9fe3d
keywords:
- video present networks WDK display , display adapter child devices
- VidPN WDK display , display adapter child devices
- child devices WDK video present network
- display adapter child devices WDK video present network
- enumerating child devices WDK video present network
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# Enumerating Child Devices of a Display Adapter


The following sequence of steps describes how the display port driver, display miniport driver, and video present network (VidPN) manager collaborate at initialization time to enumerate child devices of a display adapter.

1.  The display port driver calls the display miniport driver's [**DxgkDdiStartDevice**](https://msdn.microsoft.com/library/windows/hardware/ff560775) function. *DxgkDdiStartDevice* returns (in the *NumberOfChildren* parameter) the number of devices that are (or could become by docking) children of the display adapter. *DxgkDdiStartDevice* also returns (in the *NumberOfVideoPresentSources* parameter) the number N of video present sources supported by the display adapter. Those video present sources will subsequently be identified by the numbers 0, 1, ... N -1.

2.  The display port driver calls the display miniport driver's [**DxgkDdiQueryChildRelations**](https://msdn.microsoft.com/library/windows/hardware/ff559750) function, which enumerates child devices of the display adapter. *DxgkDdiQueryChildRelations* fills in an array of [**DXGK\_CHILD\_DESCRIPTOR**](https://msdn.microsoft.com/library/windows/hardware/ff561001) structures: one for each child device. Note that all child devices of the display adapter are on-board: monitors and other external devices that connect to the display adapter are not considered child devices. For more information, see [Child Devices of the Display Adapter](child-devices-of-the-display-adapter.md). *DxgkDdiQueryChildRelations* must enumerate potential child devices as well as the child devices that are physically present at initialization time. For example, if connecting a laptop computer to a docking station will result in the appearance of a new video output, *DxgkDdiQueryChildRelations* must enumerate that video output regardless of whether the computer is docked at initialization time. Also, if connecting a dongle to a video output connector will allow several monitors to share the connector, *DxgkDdiQueryChildRelations* must enumerate a child device for each branch of the dongle, regardless of whether the dongle is connected at initialization time.

3.  For each child device (enumerated as described in Step 1) that has an HPD awareness value of **HpdAwarenessInterruptible** or **HpdAwarenessPolled**, the display port driver calls the display miniport driver's [**DxgkDdiQueryChildStatus**](https://msdn.microsoft.com/library/windows/hardware/ff559754) function to determine whether the child device has an external device connected to it.

4.  The display port driver creates a PDO for each child device that satisfies one of the following conditions:
    -   The child device has an HPD awareness value of **HpdAwarenessAlwaysConnected**.
    -   The child device has an HPD awareness value of **HpdAwarenessPolled** or **HpdAwarenessInterruptible**, and the operating system knows from a previous query or notification that the child device has an external device connected.

5.  The display port driver calls the display miniport driver's [**DxgkDdiQueryDeviceDescriptor**](https://msdn.microsoft.com/library/windows/hardware/ff559761) function for each child device that satisfies one of the following conditions:

    -   The child device is known to have an external device connected.
    -   The child device is assumed to have an external device connected.
    -   The child device has a type of **TypeOther**.

    *DxgkDdiQueryDeviceDescriptor* returns an Extended Display Information Data (EDID) block if the connected monitor (or other display device) supports EDID descriptors.

    Note: During initialization, the display port driver calls *DxgkDdiQueryDeviceDescriptor* for each monitor to obtain the first 128-byte block of the monitor's EDID. That gives the display port driver what it needs at initialization time: PnP hardware ID, instance ID, compatible IDs, and device text. At a later time, the monitor class function driver (Monitor.sys) calls *DxgkDdiQueryDeviceDescriptor* for each monitor to obtain the first 128-byte EDID block and additional 128-byte EDID extension blocks. This means that the display miniport driver will be called twice to provide the first 128-byte block of each monitor's EDID.

6.  The VidPN manager obtains identifiers for all of the video present sources and video present targets supported by the display adapter. The video present sources are identified by the numbers 0, 1, ... N - 1, where N is the number of sources returned by the display miniport driver's *DxgkDdiStartDevice* function. The video present targets have unique integer identifiers that were previously created by the display miniport driver during *DxgkDdiQueryChildRelations*. Each child device of type **TypeVideoOutput** is associated with a video present target, and the **ChildUid** member of the child device's DXGK\_CHILD\_DESCRIPTOR structure is used as the identifier for the video present target.

7.  The VidPN manager uses the following procedure to build an initial VidPN.
    -   If a last known good VidPN is recorded in the registry, use it as the initial VidPN.

    -   Otherwise, call the display miniport driver's [**DxgkDdiRecommendFunctionalVidPn**](https://msdn.microsoft.com/library/windows/hardware/ff559775) function to obtain an initial VidPN.

    -   If *DxgkDdiRecommendFunctionalVidPn* fails to return a functional VidPN that is acceptable, create a simple VidPN that contains one video present path; that is, one (source, target) pair. Call the display miniport driver's [**DxgkDdiIsSupportedVidPn**](https://msdn.microsoft.com/library/windows/hardware/ff559684) function to verify that the proposed VidPN will work. If *DxgkDdiIsSupportedVidPn* reports that the proposed VidPN will not work, keep trying until a suitable VidPN is found.

    -   Call the display miniport driver's [**DxgkDdiEnumVidPnCofuncModality**](https://msdn.microsoft.com/library/windows/hardware/ff559649) function to determine the source and target modes that are available for the VidPN.

 

 





