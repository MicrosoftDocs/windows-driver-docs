---
title: Network Cameras
description: Describes compatibility with ONVIF Network Cameras in Windows.
ms.date: 12/18/2024
---

# Network cameras

This article describes compatibility with ONVIF Network Cameras in Windows.

## Introduction

Windows 10 and Windows 11 support connecting to and streaming from cameras on a local network that support ONVIF Profile S. When paired to a Windows device, ONVIF cameras appear like any other camera (for example, integrated, USB, and so on) and any camera application may stream from them.

### Terminology and prerequisites

In addition to the terms defined in this table, this document also references terms defined by Windows audio class extensions.

| Term | Definition |
|--|--|
| H.264 | An efficient lossy compressed video format that produces high quality and low bitrate video. Also known as Advanced Video Coding (AVC). |
| H.265 | A highly efficient lossy compressed video format that produces high quality and low bitrate video. Also known as High Efficiency Video Coding (HEVC). |
| MJPEG | Motion Joint Photographic Experts Group, a lossy compressed video format transmitting frames as sequential JPEG images. |
| ONVIF | Open Network Video Interface Forum, an open industry forum that develops standards for interfacing with network-based camera products. |
| WS-Discovery | Web Services Dynamic Discovery, an open standard for multicast-based discovery of services available on a local network. |

## Supported features

Windows supports cameras that are conformant with ONVIF Profile S, using no authentication or digest authentication. Streaming occurs using RTP over UDP, using either MJPEG or H.264 codecs.

## Unsupported features

Windows doesn't support TLS, Profile T features (including H.265), or Audio streaming.

## Network requirements

The ONVIF standard uses WS-Discovery to locate cameras on the local network. This enables easy discovery of cameras, but also imposes some constraints on the network conditions that must exist for successfully discovery:

- The camera and the PC must be on the same network subnet.

- The network must not block local intra-device communications (for example, for WiFi connections, features like Client Isolation must not be turned on).

- The network must not block multicast.

In some commercial or corporate environments, wireless and wired networks may be on different subnets/VLANs, and Ethernet ports throughout the building may also be on different subnets/VLANs. In these cases, camera discovery won't succeed.

## Pairing cameras

ONVIF cameras can be paired either using [**Settings**](ms-settings:camera), or programmatically using the [**Windows.Devices.Enumeration**](/uwp/api/windows.devices.enumeration?view=winrt-22621&preserve-view=true) APIs.

### Windows 11 settings

The camera settings page allows customers to initiate a search of the local network for ONVIF-conformant network/IP cameras and connect them to the system.

To access the camera settings page, go to [**Settings > Bluetooth & devices > Cameras**](ms-settings:camera). To begin searching the local network for available cameras, select **Search for cameras**.

During the connection process, if the camera requires authentication (a username and password), Windows prompts for the credentials.

Network cameras that have been connected to a system can be removed by selecting the camera from the **Connected cameras** list in the camera settings page, and then selecting the **Remove** button.

### Windows 10 settings

Windows 10 doesn't include the camera settings page and is limited in pairing capabilities through **Settings**. On Windows 10, it's only possible to use **Settings** to connect to cameras that don't require authentication.

To connect to an ONVIF camera that doesn't require authentication, go to **Settings > Devices > Bluetooth & other devices**. Select **Add Bluetooth or other device**. In the **Add a device** popup, select **Everything else**. Wait for discovery to complete, and then select the camera you wish to connect to.

Cameras that require authentication can only be paired on Windows 10 by using the [**Windows.Devices.Enumeration**](/uwp/api/windows.devices.enumeration?view=winrt-22621&preserve-view=true) API. A sample application, [Device Enumeration and Pairing](https://apps.microsoft.com/detail/9N7DVKWXKQFC), is available on the Microsoft Store. Select the **Custom Device Pairing** option, and then use **Web Services on Devices (Network Camera)** to discover and pair an ONVIF camera.

### Windows.Devices.Enumeration API

On Windows 10 and Windows 11, the [**Windows.Devices.Enumeration**](/uwp/api/windows.devices.enumeration?view=winrt-22621&preserve-view=true) API can be used to programmatically discover and pair cameras. This API can pair to both cameras that do and don't require authentication.

## Troubleshooting

### Discovery

If a camera isn't able to be discovered, it's usually due to either network configuration, or bugs in the camera's implementation of the WS-Discovery protocol.

Try the following troubleshooting steps:

1. Verify that the camera is listed in the [ONVIF Conformant Products database](https://www.onvif.org/conformant-products/) as a Profile S compatible camera. Some cameras claim ONVIF compatibility even if they haven't gone through the full conformance testing process.

1. Check for camera firmware updates. Some cameras that had bugs in their implementation of the WS-Discovery protocol were known to have fixed these bugs in newer firmware.

1. Ensure your Windows device and your ONVIF camera both have an IPv4 address within the same subnet.

1. If the Windows device or camera is connected using WiFi, ensure that features such as Client Isolation aren't active on the wireless access point.

If the camera is still not discoverable, it's likely that the camera has a flaw in its WS-Discovery implementation. Windows has a strict implementation of WS-Discovery, and some cameras are known to have flaws. While other ONVIF client implementations may implement workarounds for noncompliant WS-Discovery implementations, Windows doesn't do so. Consult the manufacturer of the camera for additional support.

### Pairing

If a discovered camera isn't able to be paired, it's usually due to incorrect credentials.

Try the following troubleshooting steps:

1. On Windows 10, a camera that requires authentication will silently fail the pairing process through **Settings**. Review the **Windows 10 settings** section above for information about a sample app available on the Microsoft Store that can pair these cameras on Windows 10.

1. Ensure you're using the ONVIF credentials for the camera. Many cameras use different credentials to access the camera's web-based configuration interface, and the ONVIF interface. Be sure to configure and use the ONVIF credentials when pairing to the camera.

### Streaming

If a paired camera stops working when apps stream from it, it's likely that the camera was reconfigured by another ONVIF client since it was paired to Windows. Windows configures and uses ONVIF Media Profiles on the camera to support the set of resolutions and video codecs that can be selected by applications. Once a camera is paired to Windows, it's expected that the camera isn't used with other ONVIF clients. To recover, try disconnecting the camera from the system and re-pairing it.

If a camera freezes or drops frames while streaming, it's likely a network bandwidth issue. Streaming at high resolution (for example, 1080p) video in the MJPEG format requires a significant amount of bandwidth. For wireless devices, ensure they're receiving a strong signal to the access point. For wired devices, ensure the network is operating at a high speed (for example, Gigabit Ethernet) and that other applications and devices on the network aren't consuming all available bandwidth.

## See also

[Device Enumeration and Pairing](https://apps.microsoft.com/detail/9N7DVKWXKQFC)

[ONVIF Conformant Products database](https://www.onvif.org/conformant-products)

[**Windows.Devices.Enumeration**](/uwp/api/windows.devices.enumeration?view=winrt-22621&preserve-view=true)
