---
title: Updates for IddCx versions 1.7 and later
description: IddCx version 1.7 updates for console and remote indirect display drivers
ms.date: 08/09/2022
keywords:
- IddCx version 1.7
- Console and remote indirect display driver, IddCx versions 1.7 and later
- Console and remote IDD, IddCx versions 1.7 and later
- Console indirect display driver
- Console IDD
- Remote indirect display driver
- Remote IDD
---

# Updates for IddCx versions 1.7 and later

This page describes the changes made in IddCx 1.7. A single indirect display driver (IDD) binary built against IddCx 1.7 can run on Windows 10, version 1803 and above using runtime checks to verify whether DDI changes in IddCx 1.7 are available on that system. See [Building a WDF driver for multiple versions of Windows](/windows-hardware/drivers/wdf/building-a-wdf-driver-for-multiple-versions-of-windows) for more info.

The IddCx 1.7 changes fall into the following categories:

* The [**IddCxGetVersion**](/windows-hardware/drivers/ddi/iddcx/nf-iddcx-iddcxgetversion) version was updated (console and remote). See [IddCx versions](iddcx-versions.md) for a complete list of IddCx-related version information.
* An improved mouse cursor DDI was added (available for console and remote but only useful from remote).
* The **IDDCX_ADAPTER_FLAGS_CAN_USE_MOVE_REGIONS** adapter flag was deprecated (console and remote).

## Updated IddCxGetVersion version

The IddCx version returned by [**IddCxGetVersion**](/windows-hardware/drivers/ddi/iddcx/nf-iddcx-iddcxgetversion) on Windows Server 2022 was updated to IDDCX_VERSION_IRON (0x1700).

## Updated mouse cursor for remote drivers

Remote IDDs in IddCx versions prior to 1.7 only receive mouse updates for *procedural* cursor moves. A procedural cursor move is a position change caused by an API call from an application or the OS on the server, and not by mouse input injected into the remote session from the remote client. This leads to some issues that are unique to remote sessions. For example:

1. In IddCx 1.6 and earlier, the remote driver cannot tell if an API call set a mouse position to the same position twice.
2. A change in cursor shape or visibility cannot be triggered without a valid position. This is not an issue for console IDDs. For remote drivers, however, when there have not been any valid procedural position changes the DDI would have to give a position value that would cause the cursor to jump in the client.

To address these issues the following changes were made starting in IddCx 1.7.

### IDDCX_ADAPTER_FLAGS_REMOTE_ALL_CURSOR_POSITION flag was added

The **IDDCX_ADAPTER_FLAGS_REMOTE_ALL_CURSOR_POSITION** adapter flag was added to [**IDDCX_ADAPTER_FLAGS**](/windows-hardware/drivers/ddi/iddcx/ne-iddcx-iddcx_adapter_flags) to allow remote drivers to receive all mouse position updates. This flag allow a remote driver to indicate on an adapter basis that it wants to receive all cursor position changes and not just procedural moves. This flag is only valid when combined with **IDDCX_ADAPTER_FLAGS_REMOTE_SESSION_DRIVER**. [**IddCxAdapterInitAsync**](/windows-hardware/drivers/ddi/iddcx/nf-iddcx-iddcxadapterinitasync) will fail if **IDDCX_ADAPTER_FLAGS_REMOTE_ALL_CURSOR_POSITION** is set without **IDDCX_ADAPTER_FLAGS_REMOTE_SESSION_DRIVER**.

### IddCxMonitorQueryHardwareCursor2 DDI was added for cursor position

The [**IddCxMonitorQueryHardwareCursor2**](/windows-hardware/drivers/ddi/iddcx/nf-iddcx-iddcxmonitorqueryhardwarecursor2) DDI provides cursor position information. This DDI returns an [**IDARG_OUT_QUERY_HWCURSOR2**](/windows-hardware/drivers/ddi/iddcx/ns-iddcx-idarg_out_query_hwcursor2) structure. Both remote and console drivers can call this DDI but the information in the **IDARG_OUT_QUERY_HWCURSOR2** structure is not very relevant for console drivers.

The [**IDARG_OUT_QUERY_HWCURSOR2**](/windows-hardware/drivers/ddi/iddcx/ns-iddcx-idarg_out_query_hwcursor2) structure returns the following additional cursor information:

* A position ID (**PositionId**)

  Prior to IddCx 1.7, the [cursor DDI](/windows-hardware/drivers/ddi/iddcx/nf-iddcx-iddcxmonitorqueryhardwarecursor) uses a [shape ID](/windows-hardware/drivers/ddi/iddcx/ns-iddcx-idarg_in_query_hwcursor) so the driver can know whether the shape has changed since the last update. Starting in IddCx 1.7, a position ID was added. The position ID value changes if a new cursor position was reported, even if the **X** and **Y** co-ordinates of the new position are the same as the old.

* A position valid flag (**PositionValid**)

  **PositionValid** indicates to the driver whether the cursor position in the cursor information structure is valid. This valid flag covers the **X**, **Y** and **PositionId** fields. If this flag is not set then the **X**, **Y** and **PositionId** fields cannot be used.

## IDDCX_ADAPTER_FLAGS_CAN_USE_MOVE_REGIONS flag deprecated (console and remote)

Due to changes in the way the desktop is rendered, starting in IddCx 1.7 move regions will no longer be provided at acquire frame time. Instead, the dirty rects list provided at acquire frame time contains all the changed regions of the image and [**IDDCX_METADATA**](/windows-hardware/drivers/ddi/iddcx/ns-iddcx-iddcx_metadata).**MoveRegionCount** will always be zero.

Drivers can still set the **IDDCX_ADAPTER_FLAGS_CAN_USE_MOVE_REGIONS** flag for IddCx 1.7 and above but it will have no effect. If a driver is designed to run on pre-IddCx 1.7 and sets the flag, that driver must have the logic to process the moves; otherwise users will see visual issues when running on pre-IddCx 1.7 systems.
