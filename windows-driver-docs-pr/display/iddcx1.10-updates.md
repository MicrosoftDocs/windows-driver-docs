---
title: Updates for IddCx versions 1.10 and later
description: Version 1.10 updates to the Indirect Display Driver Class eXtension for console and remote indirect display drivers
ms.date: 08/22/2023
keywords:
- IddCx version 1.10
- Console and remote indirect display driver, IddCx versions 1.10 and later
- Console and remote IDD, IddCx versions 1.10 and later
- Console indirect display driver
- Console IDD
- Remote indirect display driver
- Remote IDD
- HDR support, IddCx
- SDR support, IddCx
---

# Updates for IddCx versions 1.10 and later

This page describes the changes made in IddCx 1.10. A single indirect display driver (IDD) binary built against IddCx 1.10 can run on Windows 10, version 1803 and above using runtime checks to verify whether DDI changes in IddCx 1.10 are available on that system. See [Building a WDF driver for multiple versions of Windows](../wdf/building-a-wdf-driver-for-multiple-versions-of-windows.md) for more info.

The IddCx 1.10 changes fall into the following categories:

* Update the [**IddCxGetVersion**](/windows-hardware/drivers/ddi/iddcx/nf-iddcx-iddcxgetversion) version (console and remote). See [IddCx versions](iddcx-versions.md) for a complete list of IddCx-related version information.
* Add HDR10 (high dynamic range) and SDR (standard dynamic range) Wide Color Gamut (WCG) support to Indirect Displays.

## Updated IddCxGetVersion version

[**IddCxGetVersion**](/windows-hardware/drivers/ddi/iddcx/nf-iddcx-iddcxgetversion) returns IDDCX_VERSION_SV3 (0x1A00) on Windows 11 version 22H2's September Moment release.

## HDR and SDR wide color gamut support

For some introductory information about color on Windows, including SDR WCG, see [DirectX with advanced color on HDR and SDR displays](/windows/win32/direct3darticles/high-dynamic-range).

Where possible, drivers can use existing DDIs that were extended to allow them to report support for:

* HDR10
* SDR WCG
* Receiving data describing any HDR frames sent to an IDD

New variants of existing DDIs were added when existing DDIs couldn't be extended. In most cases these changes are applicable to both console and remote drivers but a few details specific to remote drivers are also defined.

New drivers that support HDR must use the new DDI variants. Older drivers or drivers that don't support HDR can continue to use the existing functions. An overview of the changes is given in the following sections.

### Reporting Adapter HDR support

Version 1.10 and above drivers should set the flag added to [**IDDCX_ADAPTER_FLAGS**] to report support for FP16 surfaces. FP16 surfaces can be used for HDR10 or just SDR WCG. Setting this flag implies that a driver does everything required to enable HDR10 or SDR WCG, including:

* Report target capabilities via [**EVT_IDD_CX_ADAPTER_QUERY_TARGET_INFO**]
* Report extended mode information via the following introduced functions: [**EVT_IDD_CX_PARSE_MONITOR_DESCRIPTION2**] and [**EVT_IDD_CX_MONITOR_QUERY_TARGET_MODES2**]
* Only update target modes via [**IddCxMonitorUpdateModes2**] and no longer call**IddCxMonitorUpdateModes**
* Only query cursor details via [**IddCxMonitorQueryHardwareCursor3**] and no longer call **IddCxMonitorQueryHardwareCursor2** or **IddCxMonitorQueryHardwareCursor**
* Process FP16 desktop surfaces provided by IddCxSwapChainReleaseAndAcquireBuffer2
* Use the HDR 3x4 matrix transform received from EVT_IDD_CX_MONITOR_SET_GAMMA_RAMP
* Send HDR metadata to the display. This is sent either in EVT_IDD_CX_MONITOR_SET_DEFAULT_DATA or IddCxSwapChainReleaseAndAcquireBuffer2
* Apply SDR white level where appropriate, e.g. mouse cursors. The SDR white level is included in IddCxSwapChainReleaseAndAcquireBuffer2 and IddCxMonitorQueryHardwareCursor3

### Reporting target HDR capabilities

If a driver wishes to enable HDR for an adapter, it must call the [**EVT_IDD_CX_ADAPTER_QUERY_TARGET_INFO**] function to provide additional information about each target connector, as some aspects of HDR may only be supported on some of the available targets.

### HDR metadata

When the OS detects an HDR-capable monitor, the driver is given default HDR metadata. The driver must keep this data and use it when sending HDR10 information frames (SMPTE ST.2086) to the monitor. When frames are provided to the driver, HDR metadata information is also provided. When this later metadata indicates that the default should be used, it is the default data that is being referred to.

The OS will send HDR metadata state with every frame that tells the driver which HDR metadata to use. This is part of a new IDDCX_METADATA2 structure. The metadata will either be a new metadata block or an indication that either the default metadata the OS provides to the driver, or the same metadata as the previous frame should be used.

Note: HDR metadata isn't made available to remote drivers as any HDR10 metadata should come from the display subsystem on the client.

### Reporting HDR modes

When a display is connected to a target the driver is queried by the OS for monitor and target modes currently supported. To correctly advertise HDR capabilities, extra information is needed for each of these modes so new Ddis have been added which an HDR driver must expose. EVT_IDD_CX_PARSE_MONITOR_DESCRIPTION2 returns a list of IDDCX_MONITOR_MODE2 structures and EVT_IDD_CX_MONITOR_QUERY_TARGET_MODES2 returns a list of IDDCX_TARGET_MODE2 structures. These extended modes will indicate the possible bit depths and surface formats that can be used. A driver can also update a target mode list using IddCxMonitorUpdateModes2.

Note: The OS will infer variations of modes for HDR and SDR WCG based on the information returned in a call to EVT_IDD_CX_ADAPTER_QUERY_TARGET_INFO prior to any modes being reported.

Note: The OS will validate the modes to try and detect repeated modes that should be combined and reported as a single mode. For example if the target supports 1080p at 60Hz in both 8 and 10 bits per channel this should be a single mode. However if the target supports these modes but they require different amounts of bandwidth it is still OK for these to be reported separately.

### New gamma type
The existing EVT_IDD_CX_MONITOR_SET_GAMMA_RAMP Ddi has been extended so new 3x4 matrix transform needed to support HDR displays can be provided to drivers that advertise HDR support. <Insert doc link when available>

### SDR white level
The white level to be applied to mouse cursors, which are always supplied as SDR, when the monitor is in HDR mode, it is provided in two places. It has been added to the per frame metadata received by a driver when calling IddCxSwapChainReleaseAndAcquireBuffer2. It is also part of a new cursor Ddi, IddCxMonitorQueryHardwareCursor3, so a driver can render cursor updates at the correct white level without needing to receive a new frame. The default SDR white level is 80 nits.

### Surface color space
Even though the driver reported color space as part of mode information the actual color space used by a specific frame is reported in the new IDDCX_METADATA2 struct.

### HDR with remote drivers
Where possible OS and driver behavior should be the same for a remote driver as with a console driver. The exceptions are:

* HDR metadata is not provided to remote drivers. This metadata is expected to be provided by the client system based on the physically connected display, it is meaningless to use metadata determined by the server.
* The 3x4 color matrix transform is also not sent as again the equivalent data from the client is expected to be used.
* Remote drivers can provide the colorimetry data and SDR white level to be used on the server.
* Monitor modes are also optional for remote drivers. If a remote driver sets the IDDCX_ADAPTER_FLAGS_ALL_TARGET_MODES_MONITOR_COMPATIBLE adapter flag the OS will not ask it for monitor modes and instead just use the target modes. This allows a driver to specify unusual modes, for example based on a client window size rather than a monitor size, without needing to report the equivalent monitor mode.

### Supporting a 1.10 driver running down level
If a 1.10 driver is to run on older Windows releases there are steps they need to take to ensure compatibility.

* The driver must continue to export all existing functions such as EVT_IDD_CX_PARSE_MONITOR_DESCRIPTION, EVT_IDD_CX_MONITOR_QUERY_TARGET_MODES, and EVT_IDD_CX_ADAPTER_COMMIT_MODES.
* The size of the IDD_CX_CLIENT_CONFIG structure must be set using the IDD_CX_CLIENT_CONFIG_INIT() macro.
* The driver must not try and call any new functions provided by the OS as they will not be available, IDD_IS_FUNCTION_AVAILABLE can be used to check.
* None of the new functions can be exported, drivers can use the IDD_IS_FIELD_AVAILABLE macro to check if the EvtIddXxx callback should be written to the the IDD_CX_CLIENT_CONFIG structure.
* IDD_IS_FIELD_AVAILABLE can also help a driver determine if it is safe to set IDDCX_ADAPTER_FLAGS_CAN_PROCESS_FP16 or IDDCX_ADAPTER_FLAGS_ALL_TARGET_MODES_MONITOR_COMPATIBLE. If one of the 1.10 DDIs is not available the driver should not set the flag.

An example of how IDD_IS_FIELD_AVAILABLE can be used:

``` cpp
    if (IDD_IS_FIELD_AVAILABLE(IDD_CX_CLIENT_CONFIG, EvtIddCxParseMonitorDescription2))
    {
        IddCxClientConfig.EvtIddCxParseMonitorDescription2 = ParseMonitorDescription2;
    }
```

See [Building IddCx 1.4 drivers](building-iddcx1.4-drivers.md) for more information.
