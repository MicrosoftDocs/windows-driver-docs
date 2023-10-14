---
title: Supporting DisplayPort monitors over USB4 in KMD
keywords:
- display drivers, usb4
- display miniport driver, usb4
- displayport, usb4
- kernel-mode driver, usb4
ms.date: 10/13/2023
---

# Supporting DisplayPort monitors over USB4 in KMD

This article describes how a kernel-mode graphics driver (KMD) can support DisplayPort monitors connected over USB4 starting in Windows 11 (WDDM 3.0).

## Requirements

The Windows graphics stack needs to know that a KMD supports USB4 at start time. At start time, the system can verify whether a driver supports all the necessary requirements and fail driver start if it doesn't offer such support rather than find out at hot plug detect time.

The KMD must meet the following requirements:

1. It must be a WDDM 3.0 or above driver.
2. It exposes an added adapter cap to indicate USB4 support.
3. All static VidPn targets exposed by the driver need to be reported as power components.
4. Each USB4 dynamic target connected to the same static target must be connected to the same host router; that is their [**DXGK_CONNECTION_USB4_INFO**](/windows-hardware/drivers/ddi/d3dkmddi/ns-d3dkmddi-dxgk_connection_usb4_info)'s **USB4_Driver_ID** members must have the same value. Currently, connecting a USB4 DisplayPort monitor to Display Only or Indirect Display WDDM drivers is not supported.

### Added USB4 support driver cap

The **SupportUsb4Targets** cap was added to the [**DXGK_DISPLAY_DRIVERCAPS_EXTENSION**](/windows-hardware/drivers/ddi/d3dkmddi/ns-d3dkmddi-_dxgk_display_drivercaps_extension) structure that the system queries from the driver at start time. Only WDDM 3.0 and later drivers should set this value and only if the driver meets all the previously listed requirements.

### Reporting USB4 monitor DisplayPort Configuration Data values

The **[DXGK_CONNECTION_CHANGE](/windows-hardware/drivers/ddi/d3dkmddi/ns-d3dkmddi-_dxgk_connection_change).MonitorConnect.[MonitorConnectFlags](/windows-hardware/drivers/ddi/d3dkmddi/ns-d3dkmddi-dxgk_connection_monitor_connect_flags)** field was added.

The OS calls KMD's [**DXGKDDI_QUERYCONNECTIONCHANGE**](/windows-hardware/drivers/ddi/d3dkmddi/nc-d3dkmddi-dxgkddi_queryconnectionchange) function whenever a connector status change is detected. When a DisplayPort monitor has been connected to a specified VidPn target and is connected to a USB4 DP-IN adapter, the driver should:

1. Set the **[DXGK_CONNECTION_CHANGE](/windows-hardware/drivers/ddi/d3dkmddi/ns-d3dkmddi-_dxgk_connection_change).[MonitorConnectFlags.Usb4DisplayPortMonitor](/windows-hardware/drivers/ddi/d3dkmddi/ns-d3dkmddi-dxgk_connection_monitor_connect_flags)** flag to indicate this monitor is a USB4-connected monitor.
2. Complete the fields in **[DXGKARG_QUERYCONNECTIONCHANGE](/windows-hardware/drivers/ddi/d3dkmddi/ns-d3dkmddi-_dxgkarg_queryconnectionchange).[pUsb4MonitorInfo](/windows-hardware/drivers/ddi/d3dkmddi/ns-d3dkmddi-dxgk_connection_usb4_info)**.

### All static VidPn targets being reported as PoFx components

To enable correct power management between the graphics and USB stacks, the driver must report all static VidPn targets as PoFx components through [**DxgkDdiQueryAdapterInfo**](/windows-hardware/drivers/ddi/d3dkmddi/nc-d3dkmddi-dxgkddi_queryadapterinfo) when **[DXGKARG_QUERYADAPTERINFO](/windows-hardware/drivers/ddi/d3dkmddi/ns-d3dkmddi-_dxgkarg_queryadapterinfo).[Type](/windows-hardware/drivers/ddi/d3dkmddi/ne-d3dkmddi-_dxgk_queryadapterinfotype)** is **DXGKQAITYPE_NUMPOWERCOMPONENTS** or **DXGKQAITYPE_POWERCOMPONENTINFO**.

### All dynamic targets created from same static VidPn target

USB4 monitors connected to dynamic VidPn targets are supported but all USB4 dynamic VidPn targets connected to a static VidPn target must have the same USB4_Driver_ID values, ie connected to the same USB4 host router.

### System HLK test

The driver must pass the [USB4 Systems Graphics Driver Support](/windows-hardware/test/hlk/testref/6ad59683-3b1d-4f90-abae-cd41fd6b250a) test added to the Hardware Lab Kit (HLK). This test verifies that on a laptop with USB4 all graphics drivers (iGPU and dGPU) support USB4 functionality if they expose any targets.
