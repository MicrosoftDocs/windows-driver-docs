---
title: IddCx 1.4 Updates for Remote IDDs
description: IddCx version 1.4 updates for remote indirect display drivers
ms.date: 09/28/2020
keywords:
- Remote indirect display driver, IddCx versions 1.4 and later
- Remote IDD, IddCx versions 1.4 and later
- Remote indirect display driver
- Remote IDD
---

# IddCx 1.4 updates for remote IDDs

The following updates to IddCx version 1.4 apply to remote indirect display drivers (IDDs) only.

Remote IDD developers should also see [IddCx 1.4 updates for console and remote IDDs](iddcx1.4-updates-for-console-and-remote-idds.md) for additional updates.

## Declare a remote IDD for remote sessions

An IDD declares it wants to create a remote ID adapter by setting the **IDDCX_ADAPTER_FLAGS_REMOTE_SESSION_DRIVER** bit in the [**IDDCX_ADAPTER_CAPS**](/windows-hardware/drivers/ddi/iddcx/ns-iddcx-iddcx_adapter_caps)**.Flags** field when calling [**IddCxAdapterInitAsync**](/windows-hardware/drivers/ddi/iddcx/nf-iddcx-iddcxadapterinitasync).  The OS tracks whether the IDD is being loaded due the remote desktop stack connecting to a remote session and will fail the **IddCxAdapterInitAsync** call in the following two cases:

1. The IDD did not set **IDDCX_ADAPTER_FLAGS_REMOTE_SESSION_DRIVER** for a device that was create by the OS remote desktop stack for a remote session
2. The IDD set **IDDCX_ADAPTER_FLAGS_REMOTE_SESSION_DRIVER** for a device that was not created by the OS remote desktop stack

### Installation recommendations for remote IDDs

UMDF allows drivers to control the [device pooling option](../wdf/using-device-pooling-in-umdf-drivers.md) in their INF files, using directives such as **UmdfHostProcessSharing** and **DeviceGroupId**. Due to some lock contention issues, it is highly recommended that remote IDDs set the **UmdfHostProcessSharing** directive to **ProcessSharingDisabled** and remove any **DeviceGroupId** directives. This setting will configure the remote IDD for each session to be in its own process.

### Additional restrictions on existing IddCx features for remote IDDs

Remote IDDs are required to set **IDDCX_ADAPTER_FLAGS_USE_SMALLEST_MODE** in the [**IDDCX_ADAPTER_CAPS**](/windows-hardware/drivers/ddi/iddcx/ns-iddcx-iddcx_adapter_caps)**.Flags** field.  This ensures that virtual modes are not used and hence the swapchain size will always match the desktop resolution. [**IddCxAdapterInitAsync**](/windows-hardware/drivers/ddi/iddcx/nf-iddcx-iddcxadapterinitasync)
will fail if this flag is not set.

Only progressive target modes are supported for remote IDDs, so [**IDDCX_TARGET_MODE**](/windows-hardware/drivers/ddi/iddcx/ns-iddcx-iddcx_target_mode)**.TargetVideoSignalInfo.targetVideoSignalInfo.scanLineOrdering** must be set to **DISPLAYCONFIG_SCANLINE_ORDERING_PROGRESSIVE**. [**IddCxMonitorArrival**](/windows-hardware/drivers/ddi/iddcx/nf-iddcx-iddcxmonitorarrival) will fail if this value is not set.

## Set the display configuration for the remote session

As the remote IDDs control all the monitors in a remote session, and the remote session display configuration should mirror that of the client, a remote IDD needs the ability to specify the display configuration that the OS will set in the remote session. This display configuration needs to be set when the session is either created as a remote session or transitioned to a remote session.  

The remote IDD can update the display configuration during a remote session to either:

* Change the setting for current monitors (for example, change desktop position, orientation, physical size or DPI)
* Set the desktop configuration after monitors are added/removed, by calling [**IddCxMonitorArrival**](/windows-hardware/drivers/ddi/iddcx/nf-iddcx-iddcxmonitorarrival)/[**IddCxMonitorDeparture**](/windows-hardware/drivers/ddi/iddcx/nf-iddcx-iddcxmonitordeparture). Remote IDDs use **IddCxMonitorArrival** and **IddCxMonitorDeparture** in the same way as console IDDs to inform the OS about monitor arrivals and departures.

Below is the logic the OS uses to process monitor arrivals, departures, and desktop configuration changes. For each remote session, the OS will store a single current desktop configuration provided by the remote IDD. This desktop configuration will start empty and will be updated every time a remote IDD successfully calls [**IddCxDisplayConfigUpdate**](/windows-hardware/drivers/ddi/iddcx/nf-iddcx-iddcxadapterdisplayconfigupdate).

### When the driver receives a new display configuration

```
If all monitors in the new display configuration are present in the system
    If new display configuration is supported by driver (eg resolutions)
        Store new display configuration
        Set new display configuration (this will disable any active monitors
            that are not part of new configuration)

If all monitors in the new display config are not currently present in the system
    Store new display configuration
    Disable all active paths and wait for the correct set of monitors to arrive
```

### When a monitor is removed

```
If removed monitor is not in the current display configuration
    Remove the monitor and do not change the current desktop configuration

If removed monitor is part of the current display configuration
    Remove the monitor
    Disable all active paths and wait for the correct set of monitors to arrive
```

### When a monitor arrives

```
If added monitor is not part of current display configuration
    Do not change the display configuration

If added monitor is part of the current display configuration
    If now all the monitors in the current display configurations are present
        Set the new display configuration
```

Below are some simple scenarios to illustrate how [**IddCxDisplayConfigUpdate**](/windows-hardware/drivers/ddi/iddcx/nf-iddcx-iddcxadapterdisplayconfigupdate) can be used.

### Scenario 1: A new session starts with two monitors connected

| Driver action | Current display topology | Currently connected monitor| Currently active monitors | Notes |
| ------------------------- | ---------- | ---------- | ---------- | -------------------- |
|                           | None       | None       | None       | Session start configuration |
| IddCxMonitorArrival(Mon1) | None       | Mon1       | None       | No active display configuration, so nothing changes |
| IddCxMonitorArrival(Mon2) | None       | Mon1, Mon2 | None       | Still no change in display config |
| IddCxDisplayConfigUpdate  | Mon1, Mon2 | Mon1, Mon2 | Mon1, Mon2 | As all monitors are connected, set the configuration |

NOTE: The driver could have called **IddCxDisplayConfigUpdate** before adding the monitors for the same result.

### Scenario 2: Add a third monitor to Scenario 1 and make it active

| Driver action | Current display topology | Currently connected monitor| Currently active monitors | Notes |
| ------------------------- | ---------- | ---------- | ---------- | -------------------- |
| IddCxMonitorArrival(Mon3) | Mon1, Mon2       | Mon1, Mon2, Mon3 | Mon1, Mon2       | No change to display configuration |
| IddCxDisplayConfigUpdate  | Mon1, Mon2, Mon3 | Mon1, Mon2, Mon3 | Mon1, Mon2, Mon3 | New configuration set |

### Scenario 3: Remove a monitor from an active configuration

| Driver action | Current display topology | Currently connected monitor| Currently active monitors | Notes |
| --------------------------- | ---------------- | ---------------- | ---------------- | -------------------- |
|                             | Mon1, Mon2       | Mon1, Mon2       | Mon1, Mon2       | Starting configuration |
| IddCxDisplayConfigUpdate()  | Mon1             | Mon1, Mon2       | Mon1             | Change configuration to use Mon1 only first |
| IddCxMonitorDeparture(Mon2) | Mon1             | Mon1             | Mon1             | |

### Scenario 4: Changing the mode of a path when the driver only supports a single mode

| Driver action | Current display topology | Currently connected monitor| Currently active monitors | Notes |
| ------------------------------------------- | ---------------------- | ---------- | ---------- | -------------------- |
|                                             | Mon1 10x7 , Mon2 19x10 | Mon1, Mon2 | Mon1, Mon2 | Starting configuration |
| IddCxMonitorUpdateModes(Mon1 supports 16x9) | None                   | Mon1, Mon2 | None       | Updated mode list for Mon1 to 16x9 |
| IddCxDisplayConfigUpdate()                  | Mon1 16x9, Mon2 19x10  | Mon1, Mon2 | Mon1, Mon2 | Set config for Mon1 to 16x9 |

### Handling IddCxDisplayConfigUpdate errors

The remote driver needs to handle errors from [**IddCxDisplayConfigUpdate**](/windows-hardware/drivers/ddi/iddcx/nf-iddcx-iddcxadapterdisplayconfigupdate). Some errors are expected; for example, when the connection was using a temporary session.

In unexpected cases in the initial configuration, the driver has options such as:

* Call [**IddCxReportCriticalError**](/windows-hardware/drivers/ddi/iddcx/nf-iddcx-iddcxreportcriticalerror) to terminate the driver process and disconnect the user session. It is recommended that the driver use a unique major/minor combination so these cases can be identified in crashes and Watson reports.
* Retry the configuration again in the event that it was a transient error.
* Try a different configuration.

A remote driver might decide that mid-session configuration change failures are not as critical as initial configuration failures, and hence might never call **IddCxReportCriticalError** mid-session.

The driver should not call [**IddCxReportCriticalError**](/windows-hardware/drivers/ddi/iddcx/nf-iddcx-iddcxreportcriticalerror) if [**IddCxDisplayConfigUpdate**](/windows-hardware/drivers/ddi/iddcx/nf-iddcx-iddcxadapterdisplayconfigupdate) returns STATUS_GRAPHICS_INDIRECT_DISPLAY_DEVICE_STOPPED as a result of the OS detecting that the target session is being disconnected or the IddCx adapter for that session is being stopped, because this is expected.

## Display API changes in an indirect display remote session

In a remote XDDM session, the OS display control panel does not provide the user with any controls to change the display configuration. This is primarily because the remote session desktop configuration is controlled by the connecting client system, and not by applications running in the session. For example, supporting the Win+P projection user interface does not make sense in a remote session.

In general for remote ID sessions:

* Display enumeration APIs work, including [**QueryDisplayConfig**](/windows/win32/api/winuser/nf-winuser-querydisplayconfig)
* Display setting APIs do not function. For example, it is not desirable for an application running in the remote session to call [**ChangeDisplaySettings**](/windows/win32/api/winuser/nf-winuser-changedisplaysettingsa)/[**SetDisplayConfig**](/windows/win32/api/winuser/nf-winuser-setdisplayconfig) to change the desktop configuration (for example, change the desktop position or topology).

Interestingly, remote XDDM solutions use **ChangeDisplaySetting** to change modes and desktop positions as that is the only way changes from the client can be applied. Since remote ID solutions have [**IddCxDisplayConfigUpdate**](/windows-hardware/drivers/ddi/iddcx/nf-iddcx-iddcxadapterdisplayconfigupdate) functionality, **ChangeDisplaySetting** is no longer required to function in remote ID sessions.

The following table shows the APIs and display control panel (CPL) functionality in a XDDM remote session and a WDDM remote session.

| API/CPL | XDDM remote session | WDDM remote session |
|-| ------------------- | ------------------- |
| **Display CPL** | No information is displayed and a message saying 'The Display Settings cannot be changed from a remote session' is issued. | Same behavior as an XDDM remote session. |
| **Win+P UI and functionality** | The UI is not shown and API fails. | Same behavior as an XDDM remote session. |
| **Legacy display enum APIs (such as EnumDisplaySettings & EnumDisplayDevices)** | The API works as expected and returns relevant information. | Same behavior as an XDDM remote session. |
| **Legacy ChangeDisplaySetting** | Works and is used to reflect desktop changes from the client. | Returns success for application compatibility reasons, but ignores the call and does not change any display configuration.  The IDD will use **IddCxDisplayConfigUpdate** to change the desktop configuration. |
| **QueryDisplayConfig** | Fails. | Works as expected. |
| **DisplayConfigGetDeviceInfo** | Fails. | Works and reports the expected information. |
| **SetDisplayConfig and DisplayConfigSetDeviceInfo** | Fails. | Same behavior as an XDDM remote session. |

## Monitor idle behavior in an ID remote session

When the protocol stack calls [**IWRdsProtocolConnectionCallback::StopScreenUpdates**](/windows/win32/api/wtsprotocol/nf-wtsprotocol-iwrdsprotocolconnectioncallback-stopscreenupdates) to stop updating the client screen, the OS destroys the swapchains and makes all the paths for that session inactive, resulting in the IDD's [**EVT_IDD_CX_ADAPTER_COMMIT_MODES**](/windows-hardware/drivers/ddi/iddcx/nc-iddcx-evt_idd_cx_adapter_commit_modes) callback being called with **IDDCX_PATH_FLAGS_NONE** set in [**IDDCX_PATH**](/windows-hardware/drivers/ddi/iddcx/ns-iddcx-iddcx_path)**.Flags** for all the paths.

When the protocol stack calls [**IWRdsProtocolConnectionCallback::RedrawWindow**](/windows/win32/api/wtsprotocol/nf-wtsprotocol-iwrdsprotocolconnectioncallback-redrawwindow)
to enable updates again, the OS sets new active paths using the IDD's **EVT_IDD_CX_ADAPTER_COMMIT_MODES** callback, and new swapchains will be created.

## Disconnect behavior in an ID remote session

When the user disconnects from a remote session, the OS destroys the devnode hosting the remote ID device for that session, resulting in the remote ID adapter for that session being PnpStopped. UMDF will call the remote IDD's [**EVT_WDF_DEVICE_D0_EXIT**](/windows-hardware/drivers/ddi/wdfdevice/nc-wdfdevice-evt_wdf_device_d0_exit) callback.

If the session is connected to again remotely, the OS will create a new devnode for the remote IDD for that session. The remote IDD should go through the normal start-up sequence again, initialization the adapter and then adding monitors etc.
