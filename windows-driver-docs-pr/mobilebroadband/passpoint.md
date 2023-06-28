---
title: Passpoint
description: Overview of Passpoint (Hotspot 2.0) in Windows
ms.date: 06/19/2023
---

# Passpoint

Passpoint (sometimes referred to as Hotspot 2.0) is a standard for seamless authentication to hotspots. Passpoint offers an encrypted connection between the client and the access point. It uses IEEE 802.11u to communicate with the provider before it establishes a connection. Authentication and encryption are provided by using WPA2-Enterprise or WPA3-Enterprise, together with one of several EAP methods.

The following table describes common credential types and EAP method combinations used for Passpoint, along with the corresponding support per provisioning method in Windows 10 and 11.

| **Credential type** | **EAP Method** | **Provisioning from a website or app** | **Provisioned by MDM or Group Policy** | **Provisioned from COSA by a Mobile Operator** | **Online Sign-Up** |
|----|----|----|----|----|----|
| Username and password | EAP-TTLS with MS-CHAP-V2 | Yes | Yes | No | Yes (Windows 11 only) |
| Username and password | PEAP with MS-CHAP-V2 | Yes | Yes | No | No |
| Username and password | TEAP with MS-CHAP-V2 | Yes | Yes | No | No |
| Certificate | EAP-TLS | Partial\* | Yes | No | No |
| Certificate | PEAP with EAP-TLS | Partial\* | Yes | No | No |
| Certificate | EAP-TTLS with EAP-TLS | Partial\* | Yes | No | No |
| Certificate | TEAP with EAP-TLS | Partial\* | Yes | No | No |
| SIM | EAP-SIM | Yes | Yes | Yes (Windows 11 only) | No |
| SIM | EAP-AKA | Yes | Yes | Yes (Windows 11 only) | No |
| SIM | EAP-AKA' | Yes | Yes | Yes (Windows 11 only) | No |

> [!NOTE]
> If using certificate-based credentials, the certificates can’t be directly associated with the Wi-Fi profile and installed directly from a website or from a UWP app. However, the profile can still be provisioned, and the scenario will work if the certificates are installed through a different mechanism. For example, the certificates could be directly downloaded and installed by the user or installed through a Win32 app.

## Provisioning methods

  - [**From a website**](/windows/win32/nativewifi/prov-wifi-profile-via-website)
  - [**From an app**](./account-provisioning.md#wi-fi-information)
  - [**From COSA, for Mobile Operator SIM based authentication**](./cosa-apn-database.md)
  - **From** [**MDM**](/windows/client-management/mdm/wifi-csp) **,** [**Group Policy**](/previous-versions/windows/it-pro/windows-server-2012-R2-and-2012/hh994701(v=ws.11)) **,**  **or using** [**provisioning packages**](/windows/configuration/provisioning-packages/provisioning-packages)**.**
  - **Using Online Sign-up (OSU)**

    Windows 11 supports OSU as defined in the Wi-Fi Alliance Passpoint specification with certain constraints:

    - Open sign-up SSID (OSEN isn't supported)
    - Username and password credentials using EAP-TTLS (no other authentication methods or credential types are supported).
    - Subscription remediation and policy updates aren't supported.

## Profile format

Except for Online Sign-up, which follows the standard PPS-MO format, all other provisioning methods rely on the [WLANProfile XML](/windows/win32/nativewifi/wireless-profile-samples) format. The Passpoint specific details are specified in the [Hotspot2](/windows/win32/nativewifi/wlan-profileschema-hotspot2-element) element.

## Older releases

Windows 8 and Windows 8.1 don't support the discovery or online sign-up portions of Passpoint, but they do support WPA2-Enterprise and all EAP methods that are required by the Passpoint specification. Therefore, Windows 8 and Windows 8.1 can connect to a Passpoint network when the user already has credentials. Because Windows 8 and Windows 8.1 don't support 802.11u discovery, operators must provision Windows 8 or Windows 8.1 with wireless profiles that contain the applicable SSIDs for their networks.

Windows 10 fully supports Passpoint Release 1, including discovery and profile creation, but doesn't support Online Sign-Up.

## Additional resources

- [Extensible Authentication Protocol (EAP) for network access](/windows-server/networking/technologies/extensible-authentication-protocol/network-access)
