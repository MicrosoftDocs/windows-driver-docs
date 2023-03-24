---
title: UEFI requirements for Windows 10 Mobile
description: In addition to UEFI requirements that apply to all Windows editions, Windows 10 Mobile devices must meet additional requirements described in this topic.
ms.date: 03/23/2023
---

# UEFI requirements for Windows 10 Mobile

In addition to the UEFI requirements listed in [UEFI requirements that apply to all Windows editions](uefi-requirements-that-apply-to-all-windows-platforms.md), devices that run Windows 10 Mobile must also meet the additional requirements described in this topic.

## Requirements that expand on the general UEFI requirements for all Windows editions

The following table describes the UEFI requirements for Windows 10 Mobile that expand on those requirements described in [UEFI requirements that apply to all Windows editions](uefi-requirements-that-apply-to-all-windows-platforms.md).

| Requirement | Description |
|--|--|
| GPT | The device must be able to boot from the GUID Partition Table (GPT). Additionally, the device must include both a primary and backup GPT as described in section 5.3 titled "GUID Partition Table Disk Layout" of the UEFI specification |
| Variable services | Variable services must provide at least 64 KB of non-volatile storage for use by Microsoft. Additionally, these variable services must be implemented in a marked location of storage. This requirement is necessary to have sufficient space to store keys and other parameters for secure boot, to allow for flashing the entire storage with new variables, and to allow for the exclusion of these variables when flashing the entire storage. To reduce BOM cost and hardware complexity, Microsoft requires that variable services must not be implemented through the addition of an extra flash part to the device. |
| Simple text input protocol | The following physical keys shall map to the following functions:<br><br>Volume up: Up arrow<br>Volume up: Down arrow<br>Camera: Enter<br>Power button: Suspend |
| Memory services | The GetMemoryMap() function must return the full range of physical memory for the platform, as specified by section 6.2 "Memory Services" of the UEFI specification. |
| EFI block I/O protocol | The EFI block I/O protocol must report a storage devices size based on its native sector size. For example, a 4-KB sector device should not report itself as a 512-byte sector device. |

## Requirements specific to Windows 10 Mobile

The following table describes the requirements that are specific to Windows 10 Mobile.

| Requirement | Description |
|--|--|
| UEFI drivers | UEFI drivers must be embedded in the UEFI firmware. |
| USB function protocol | The UEFI firmware must include a driver that adheres to the UEFI USB function protocol. For more information, see [UEFI USB function protocol](uefi-usb-function-protocol.md). USB enumeration in UEFI shall only be handled by Microsoft code. |
| Battery charging protocol | If the device uses the Microsoft UEFI battery charging application, the UEFI firmware must include a driver that implements the UEFI battery charging protocol. Before the device hands off to the Microsoft UEFI battery charging software, the device must comply with the *USB Battery Charging v1.2 Specification*. For more information, see [UEFI battery charging protocol](uefi-battery-charging-protocol.md) and [Battery charging in the boot environment](battery-charging-in-the-boot-environment.md).<br><br>**Important:**  This requirement applies only if the device uses the Microsoft UEFI battery charging application. If the device uses a custom UEFI battery charging application instead of the Microsoft-provided application, the UEFI battery charging driver must not implement the UEFI battery charging protocol. |
| Display power state protocol | If the device uses the Microsoft UEFI battery charging application, the UEFI firmware must include a driver that implements the UEFI display power state protocol. This protocol is used to turn the screen and backlight off and on again while charging in the UEFI environment. For more information about this protocol, see [UEFI display power state protocol](uefi-display-power-state-protocol.md). For more information about how this protocol is used by the UEFI battery charging application, see [Architecture of the UEFI battery charging application](architecture-of-the-uefi-battery-charging-application.md).<br><br>**Important:** This requirement applies only if the device uses the Microsoft UEFI battery charging application. If the device uses a custom UEFI battery charging application instead of the Microsoft-provided application, the UEFI battery charging driver must not implement the UEFI display power state protocol. |
| Power optimization | It is recommended that the UEFI environment be power-optimized to not use excessive power. This allows the device to use as little power as possible while booting, and to charge as quickly as possible (when charging in UEFI). |
| Reserved hardware buttons | During the boot process, Microsoft defines standalone presses of the power, volume up and volume down buttons as triggers that can be used to start several Microsoft-provided UEFI applications. OEMs must not overload the power, volume up or volume down button during boot to perform custom actions or start other UEFI applications.<br><br>The following list shows which Microsoft-provided UEFI applications are started by these buttons.<br><br>Volume up: Microsoft-provided UEFI flashing application.<br>Volume down: Microsoft-provided UEFI device reset application.<br>Power: Microsoft-provided developer boot menu application.<br><br>**Note:** OEMs must also ensure that the volume up and volume down buttons function as up arrow and down arrow keys, respectively, in the UEFI environment. |
| OEM UEFI applications | OEMs can add UEFI applications that aid in manufacturing and servicing the device. These applications have the following restrictions:<br><br>UEFI applications should not affect boot time.<br>UEFI applications must be signed with a certificate that is in the allowed signature database (db) UEFI variable.<br>UEFI applications must behave in one of the following ways:  They must *never* run during a boot to the main OS or update OS or they must *always* run during the boot to the main OS or update OS.<br><br>UEFI applications *must not* sometimes run and sometimes not run during boot to the main OS or update OS. When device encryption is enabled, the trusted platform module (TPM) stores the boot sequence, and it cannot be changed after device encryption is enabled. For example, if the boot sequence is *UEFI firmware* &gt; *application A* &gt; bootarm.efi, then removing *application A* from the boot sequence will cause the TPM to fail to unseal.<br><br>In addition, if there are multiple UEFI applications, the firmware should ensure a consistent ordering of the applications. For example, if the boot sequence is *UEFI firmware* &gt; *application A* &gt; *application B* &gt; bootarm.efi, then changing the boot sequence to *UEFI firmware* &gt; *application B* &gt; *application A* &gt; bootarm.efi could cause the TPM to fail to unseal if applications A and B chain to different entries in the db.<br><br>Updating the signing certificates of boot applications will not cause a problem with the TPM. However, if UEFI applications are resigned so that they chain to a different entry in the db, then this will also cause the TPM to fail to unseal. |

## Related topics

[Minimum UEFI requirements for Windows on SoC platforms](minimum-uefi-requirements-for-windows-on-soc-platforms.md)  

[UEFI requirements that apply to all Windows editions](uefi-requirements-that-apply-to-all-windows-platforms.md)  

[UEFI requirements for USB flashing support](uefi-requirements-for-usb-flashing-support.md)  
