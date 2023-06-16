---
title: Storage silo definitions
description: Definitions
ms.date: 06/15/2023
---

# Storage silo definitions

The following definitions are useful for storage silo driver developers.

| Term | Definition |
| ---- | ---------- |
| IEEE 1667 | A standard protocol for secure authentication and creation of trust between a secure host and a directly attached Transient Storage Device (TSD), such as a USB flash drive, portable hard drive, or cellular phone." For more information, see [IEEE 1667-2018 - IEEE Standard for Discovery, Authentication, and Authorization in Host Attachments of Storage Devices](https://standards.ieee.org/standard/1667-2018.html). |
| 1667 authentication silo | A 1667 silo whose function provides either authentication of host to device, device to host, or both. |
| 1667 standard authentication silo | A standard certificate or password authentication silo defined in the base 1667 specification for which Microsoft is shipping drivers. |
| 1667 USB Flash Device (UFD) | USB flash device implementing the 1667 command set according to the IEEE 1667 specification. |
| Third-party authentication silo | Silo not defined in the base set of 1667 specified standard authentication silos implementing the authentication function. |
| third-party silo | Silo not contained in the set of 1667 specified standard silos. The function is proprietary and not documented in the IEEE 1667 base standard. Sometimes referred to as an "unknown" silo. |
| Addressable command target (ACT) | Independent unit of access that accepts 1667 commands and optionally provides access to user data (see Logical Unit). According to the 1667 specification, an ACT is not required to provide a user data access function. A 1667 device may implement one or more ACTs. |
| Authentication | (As it relates to IEEE 1667) the act of verifying the veracity of the identity claimed by either the host or the device. In the password authentication case, a secret password established by the user of the device is the credential that serves this purpose. In the certificate authentication case, possession of the private key must be proven by successfully decrypting a random stream of bytes encrypted with the paired public key. |
| Authorization | Indication that concomitant access to the governed resource is authorized after a device or host identity has been authenticated. Host-to-device authentication governs authorized access to the user data portion of the associated ACT, whereas successful device-to-host authentication authorizes the connected data channel between the device and the host. |
| Certificate silo (Cert Silo) | Authentication silo that uses certificates and associated public-private key pairs as the basis for authentication. |
| Legacy mass storage (or Legacy UFD) | A USB mass storage (or USB flash device) not implementing the 1667 command set. |
| Logical unit (LUN) | Independent unit of access for user data contained on a device that is exposed as a single disk on the host system. A LUN is synonymous with a data-bearing 1667 ACT currently in the authorized state. Some UFDs are multi-LUN-capable. |
| Password silo (PW Silo) | Authentication silo using pass-phrase matching as the basis for authentication. |
| Removable media bit (RMB) | A bit contained in the device response to the SCSI INQUIRY command (0x12) that indicates whether the media is removable (RMB=1) or fixed (RMB=0). Not to be confused with the Removable field of the DEVICE_CAPABILITIES used to indicate whether a PDO represents a hot-pluggable device, RMB refers to a property of the media rather than the device itself. Media for which RMB=1 is treated differently by the system than show media with RMB=0. |
| Silo | Independent functional unit that responds to 1667 commands. To each ACT one or more silos may be attached. A 1667 silo command may be addressed to a particular ACT index and silo index. |
