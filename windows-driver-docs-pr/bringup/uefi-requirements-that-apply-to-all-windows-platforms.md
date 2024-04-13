---
title: UEFI Requirements for Windows on SoC Platforms
description: This article describes UEFI requirements that apply to Windows 10 for desktop editions (Home, Pro, Enterprise, and Education) and Windows 10 Mobile.
ms.date: 03/23/2023
---

# UEFI requirements for Windows editions on SoC platforms

This article describes UEFI requirements that apply to Windows 10 for desktop editions (Home, Pro, Enterprise, and Education) and Windows 10 Mobile. For additional requirements that apply only to Windows 10 Mobile, see [UEFI requirements for Windows 10 Mobile](uefi-requirements-specific-to-windows-mobile.md).

## Summary of requirements

The following table lists all current requirements for UEFI compliance as defined in the UEFI specification (Section 2.6 of the UEFI 2.3.1 specification). In this table, the term *Explicit Windows Requirement* identifies any protocol or service that is directly called by a Windows component. Although only these services are explicitly used by Windows, other listed services and protocols may be implicitly or explicitly required by a core firmware implementation, EFI device drivers or by development and deployment tool chains.

Microsoft welcomes feedback and comments from implementers on this set of requirements. For any UEFI compliance requirements that are determined to not be required by either the OS or the firmware, it is our intention to work through UEFI.org to have these compliance requirements relaxed for this class of device.

For more information about specific requirements, see the sections after the table.

| Requirement | UEFI specification section | Notes |
|--|--|--|
| **EFI system table** | 4.3 | Explicit Windows requirement |
| **EFI boot services** | 6.0 |  |
| Event, timer and task services | 6.1 |  |
| Memory services | 6.2 | Explicit Windows requirement\` |
| Protocol handler services | 6.3 | Explicit Windows requirement |
| Image services | 6.4 | Explicit Windows requirement |
| Miscellaneous services | 6.5 | Explicit Windows requirement |
| **EFI runtime services** | 7.0 |  |
| Time services | 7.3 | Explicit Windows requirement |
| Variable services | 7.2 | Explicit Windows requirement |
| Miscellaneous services | 7.5 | Explicit Windows requirement |
| **Required UEFI protocols** |  |  |
| EFI loaded image protocol | 8.1 |  |
| EFI loaded image device path protocol | 8.2 |  |
| EFI device path protocol | 9.2 | Explicit Windows requirement |
| EFI device path utilities protocol | 9.5 |  |
| EFI decompress protocol | 18.5 |  |
| EBC interpreter protocol | 20.11 |  |
| **Conditionally required UEFI protocols** |  |  |
| EFI simple text input protocol | 11.3 | Explicit Windows requirement |
| EFI simple text input EX protocol | 11.2 |  |
| EFI simple text output protocol | 11.4 |  |
| EFI graphics output protocol | 11.9 | Explicit Windows requirement |
| EFI EDID discovered protocol | 11.9.1 |  |
| EFI EDID active protocol | 11.9.1 |  |
| EFI block IO protocol | 12.8 | Explicit Windows requirement |
| EFI disk IO protocol | 12.7 |  |
| EFI simple file system protocol | 12.4 |  |
| EFI Unicode collation protocol | 12.10 |  |
| EFI simple network protocol | 21.1 |  |
| EFI PXE base code protocol | 21.3 |  |
| EFI boot integrity services protocol | 21.5 |  |
| EFI serial IO protocol | 11.8 |  |
| UEFI Arm binding | 2.3.5 | Explicit Windows requirement |
| **Security requirements** |  |  |
| Secure boot | 27.0 | Explicit Windows requirement |
| Boot manager requirements | 3.1, 3.3 | Explicit Windows requirement |

## EFI system table requirements

The EFI System Table must conform to the standard definition at the revision level implemented. The Configuration Table pointed to by the EFI System Table must include the two GUIDs and their associated pointers described in the following table.

| GUID | Description |
|--|--|
| EFI_ACPI_Table GUID | This GUID must point to the ACPI Root System Description Pointer (RSDP) for the platform. |
| SMBIOS_Table GUID | This GUID must point to the SMBIOS Entry Point Structure.<br><br>Windows requires SMBIOS Specification, at the 2.4 or higher revision level. Sections 3.2, "Required Structures and Data", and 4, "Conformance Guidelines", are required. A Windows SMBIOS compatibility test is available. |

## EFI boot services requirements

The following table lists the EFI boot services requirements for Windows.

| EFI boot service | Requirement |
|--|--|
| Memory services | Windows requires all of the memory services. |
| Protocol handler services | Windows requires the following protocol handler services:<br><br>OpenProtocol()<br>CloseProtocol()<br>LocateDevicePath()<br>LocateHandle() |
| Image services | Windows requires the following image services:<br><br>ExitBootServices() |
| Miscellaneous boot services | Windows requires the following miscellaneous boot services:<br><br>Stall()<br><br>**Note:** The Stall() implementation is required to have a deterministic (repeatable) error such that error correction or cancellation can be done reliably. |

## EFI runtime services requirements

The following table lists the EFI runtime services requirements for Windows.

| EFI runtime service | Requirement |
|--|--|
| Time services | Windows requires the following time services:<br><br>GetTime()<br>SetTime()<br><br>**Note:** Time services will only be called during boot (before ExitBootServices()) for accessing platform time-of-day hardware. |
| Variable services | All of the UEFI Variable Services are required for managing multiple boot devices and security variables on the target class of systems. |
| Miscellaneous runtime services | Windows requires the following miscellaneous runtime services:<br><br>ResetSystem()<br><br>**Note:** The ResetSystem() implementation must support both reset and shutdown options. |

## Protocol requirements

The following table describes the UEFI protocols that are required by Windows to accomplish specific functions during boot.

| Protocol | Requirement |
|--|--|
| Graphics output protocol | Windows requires the Graphics Output Protocol (GOP). Specific frame buffer requirements are:<br><br>For integrated displays, *HorizontalResolution* and *VerticalResoluton* must be the native resolution of the panel.<br><br>For External displays, *HorizontalResolution* and *VerticalResoluton* must be the native resolution of the display, or, if this isn't supported, then the highest values supported by both the video adapter and the connected display.<br><br>*PixelsPerScanLine* must be equal to *HorizontalResolution*.<br><br>*PixelFormat* must be *PixelBlueGreenRedReserved8BitPerColor*. A physical frame buffer is required; *PixelBltOnly* isn't supported.<br><br>When execution is handed off to a UEFI boot application, the firmware boot manager and firmware must not use the frame buffer for any purpose. The frame buffer must continue to be scanned out after boot services have exited. |
| Alternate display output | The UEFI firmware must support booting using any display connector supported by the hardware. If an internal panel is connected and visible then the internal panel must be used. All outputs that have physically connected displays must show the boot screen. For connected displays, the UEFI firmware must:<br><br>Initialize the output with the native mode of the display, if the native resolution can be determined.<br><br>If a native mode isn't possible, then it must initialize to the highest compatible mode.<br><br>If the display capabilities can't be determined, then the connected display must be initialized in a mode that is known to be compatible with as many monitors as possible (typically 640x480 or 1024x768, at 60 Hz). |
| Input at boot time | The EFI Simple Text Input Protocol is required for making boot choices or other menu selections on systems that have built-in keyboards or attached keyboards. For keyboard-less systems, three buttons are recommended in the boot environment:<br><br>Start button<br>Volume Up button<br>Volume Down button<br><br>Button presses should be reported through the EFI Simple Text Input Protocol by mapping them to the following keyboard keys, respectively:<br><br>Windows key<br>Up Arrow key<br>Down Arrow key<br> |
| Local storage boot | Windows requires Block I/O Protocol and Device Path Protocol support for the storage solution that contains the EFI system partition and the Windows OS partition. For booting from flash storage that requires wear-leveling or other flash management, this must be implemented in the firmware (not in a UEFI application). |

## Security requirements

Windows has security requirements in the areas of Secure Boot, Measured Boot, Cryptography, and Data Protection. These requirements are detailed in the following table. Additionally, for those areas in which SoC hardware prevents compliance with the existing standard (TPM, RTC, etc.), additional requirements are being developed. These are described at the end of the table.

| Area | Requirement |
|--|--|
| General | <ul><li><p>Requirement 1: MANDATORY. The platform shall be compliant with all requirements specified in this section.</p></li><li><p>Requirement 2: MANDATORY. Platforms shall be UEFI Class Three with no Compatibility Support Module installed or installable. BIOS emulation and legacy PC/AT boot must be disabled.</p></li></ul> |
| UEFI secure boot | <ul><li><p>Requirement 3: MANDATORY. Secure Boot as defined in UEFI v2.3.1 section 27 must ship enabled and with a signature database (EFI_IMAGE_SECURITY_DATABASE) necessary to boot the machine securely pre-provisioned. The initial contents of the signature database is determined by the OEM, based on required 3rd party UEFI drivers, recovery needs and the OS Boot Loader installed on the machine, but a Microsoft-provided EFI_CERT_X509 signature shall be included. No additional signatures shall be present.</p></li><li><p>Requirement 4: MANDATORY. Presence of the UEFI "forbidden" signature database (EFI_IMAGE_SECURITY_DATABASE1) is required.</p></li><li><p>Requirement 5: MANDATORY. A Microsoft-provided UEFI KEK shall be included in the UEFI KEK database. No additional KEKs shall be present. Microsoft provides the KEK in the form of an EFI_CERT_X509 signature.</p></li><li><p>Requirement 6: MANDATORY. A PK<em><sub>pub</sub></em> key shall be present and stored in firmware flash. **Note**: Because PK<em><sub>priv</sub></em> (the private-key counterpart to PK<em><sub>pub</sub></em>) controls Secure Boot policy on all devices provisioned with PK<em><sub>pub</sub></em>, its protection and use must be closely guarded.</p></li><li><p>Requirement 7: MANDATORY. The initial signature databases shall be stored in firmware flash and may be updated only with an OEM-signed firmware update or through UEFI authenticated variable write.</p></li><li><p>Requirement 8: MANDATORY. Images in the boot path that fails signature verification must not be executed, and the reason for the failure shall be added to the EFI_IMAGE_EXECUTION_TABLE. Further, the recommended approach in these situations is that the UEFI boot manager initiates recovery according to an OEM-specific strategy.</p></li><li><p>Requirement 9: MANDATORY. Physically present user override must not be permitted for UEFI images that fail signature verification.</p></li><li><p>Requirement 10: OPTIONAL. An OEM may implement the ability for a physically present user to turn off Secure Boot either with access to the PK<em><sub>priv</sub></em> or with Physical Presence through the firmware setup. Access to the firmware setup may be protected by platform specific means (administrator password, smart card, static configuration, etc.)</p></li><li><p>Requirement 11: MANDATORY if requirement 10 is implemented. If Secure Boot is turned off, then all existing UEFI variables shall not be accessible.</p></li><li><p>Requirement 12: OPTIONAL. An OEM may implement the ability for a physically present user to select between two Secure Boot modes in firmware setup: "Custom" and "Standard". Custom Mode allows for more flexibility as specified in the following.</p></li><li><p>Requirement 13: MANDATORY if requirement 12 is implemented. It shall be possible to re-enable a disabled Secure Boot in Custom Mode by setting an owner specific <em>PK</em>. The administration shall proceed as defined in section 27.5 of the UEFI specification v2.3.1: Firmware/OS Key Exchange. In Custom Mode, the device owner may set their choice of signatures in the signature databases.</p></li><li><p>Requirement 14: MANDATORY if requirement 12 is implemented. The firmware setup shall indicate if Secure Boot is turned on, and if it's operated in Standard or Custom Mode. The firmware setup shall provide an option to return from Custom to Standard Mode.</p></li><li><p>Requirement 15: MANDATORY. If the firmware settings are reset to factory defaults, all custom-set protected variables shall be erased and the original PK<em><sub>pub</sub></em> shall be re-established along with the original, manufacturer-provisioned signature databases.</p></li><li><p>Requirement 16: MANDATORY. Driver signing shall use the Authenticode option (WIN_CERT_TYPE_PKCS_SIGNED_DATA).</p></li><li><p>Requirement 17: MANDATORY. Support for the EFI_IMAGE_EXECUTION_INFO_TABLE (that is, creation and storage of information about images started or not started during boot).</p></li><li><p>Requirement 18: MANDATORY. Supporting GetVariable() for the EFI_IMAGE_SECURITY_DATABASE (both authorized and forbidden signature database).</p></li><li><p>Requirement 19: MANDATORY. Supporting SetVariable() for the EFI_IMAGE_SECURITY_DATABASE (both authorized and forbidden signature database), using the Microsoft KEK for authentication.</p></li><li><p>Requirement 20: MANDATORY. EFI_HASH_SERVICE_BINDING_PROTOCOL: Service support: CreateChild(), DestroyChild().</p></li><li><p>Requirement 21: MANDATORY. EFI_HASH_PROTOCOL. Service support: Hash(). Support for the SHA_1 and SHA-256 hash algorithms. Must support passing a Message at least 10 Mbytes long.</p></li></ul></td> |
| UEFI measured boot | <p>The following requirements don't imply a need for a TCG TPM implementation; they do however imply a need for equivalent functionality for the affected areas.</p><p>The platform support may be provided by a firmware implementation of a TPM executing in the secure execution environment, layering on top of the cryptographic acceleration engine and leveraging the isolated storage. Microsoft may be able to provide reference software for such a TPM implementation for use by the vendor. This is subject to further discussions.</p><ul><li><p>Requirement 22: MANDATORY. The platform shall conform to the EFI protocol specified in the [UEFI Trusted Execution Environment EFI Protocol](/previous-versions/windows/hardware/hck/jj923068(v=vs.85)).</p></li><li><p>Requirement 23: MANDATORY. The platform shall adhere to the TCG EFI Platform Specification with the following additions:</p><ul><li><p>On platforms supporting the interface defined in TrEE EFI Protocol, the digest of PK<em><sub>pub</sub></em> shall be extended to TPM PCR[03] as an EV_EFI_VARIABLE_CONFIG event.</p></li><li><p>The digest of the content of the authorized signature database (see section 27.8 of the UEFI specification v2.3.1) list must be extended in the measured boot as an EV_EFI_VARIABLE_CONFIG event. The extend operation shall be to TPM PCR[03].</p></li><li><p>It shall be possible for a UEFI client to read and parse the list of certificates using the EFI_IMAGE_SECURITY_DATABASE variable and validate the digest against the extended value.</p></li><li><p>TCG_PCR_EVENT digest values shall be SHA-256, not SHA-1.</p></li></ul></li><li><p>Requirement 24: MANDATORY. The platform must implement the MemoryOverwriteRequestControl defined in the [TCG Platform Reset Attack Mitigation Specification](https://trustedcomputinggroup.org/wp-content/uploads/Platform-Reset-Attack-Mitigation-Specification.pdf).</p></li></ul> |
| Cryptography | <ul><li><p>Requirement 25: MANDATORY. The platform shall provide the EFI_HASH_PROTOCOL (UEFI v2.3.1 Section 27.4) for offload of cryptographic hash operations. SHA-256 must be supported.</p></li><li><p>Requirement 26: MANDATORY. The platform shall support the Microsoft-defined [EFI_RNG_PROTOCOL](uefi-entropy-gathering-protocol.md) for pre-OS read of entropy.</p></li></ul> |
| Data protection | <ul><li><p>Requirement 27: MANDATORY. The platform must support EFI variables with any combination of the following UEFI variable attributes set:</p><ul><li><p>EFI_VARIABLE_BOOTSERVICE_ACCESS</p></li><li><p>EFI_VARIABLE_NON_VOLATILE</p></li><li><p>EFI_VARIABLE_AUTHENTICATED_WRITE_ACCESS</p></li></ul></li></ul> |
| Other security requirements | <p>The following additional requirements are required by Windows on SoC platforms.</p><ul><li><p>Microsoft has defined protocol for gathering entropy from a UEFI platform. While not a UEFI requirement, this protocol is required by Windows on SoC platforms. For more information about this protocol, see [UEFI entropy gathering protocol](uefi-entropy-gathering-protocol.md).</p></li><li><p>UEFI Signature Database Updates. A new mechanism for updating Authenticated Variables has been adopted in section 27 of UEFI 2.3.1. This mechanism is required by Windows.</p></li><li><p>Trusted Execution Environment. Microsoft has developed an EFI protocol for interacting with a Trusted Execution Environment (TrEE), similar in functionality to a subset of a Trusted Computing Group (TCG) Trusted Platform Module (TPM). The EFI protocol leverages to a large degree, "TCG EFI Protocol," Version 1.2 Revision 1.00, June 9, 2006, by the Trusted Computing Group.</p><p>For details, refer to [UEFI Trusted Execution Environment EFI Protocol](/previous-versions/windows/hardware/hck/jj923068(v=vs.85)).</p></li></ul> |

## Firmware boot manager requirements

The firmware boot manager must support the default boot behavior defined in section 3.3 of the specification. Additionally, for support of multi-boot, globally-defined variables and the Boot Manager requirements of section 3.1 of the specification are required.

## UEFI Arm binding requirements

The UEFI Arm Binding includes requirements specific to the Arm platform needed in order to be UEFI spec compliant. Windows requires everything in the Arm binding that is applicable to ARMv7. Because Windows doesn't support anything previous to ARMv7, requirements in the binding that are specific to ARMv6k and below are optional.

The binding specifies, for example,  how the MMU should be configured, and how physical memory should be mapped. The binding also specifies that calls made to UEFI protocols and services should be done in only the Arm ISA, meaning that software running in Thumb2 or Thumb would need to switch back to Arm mode before calling UEFI functions.

## UEFI Arm multiprocessor startup requirements

Microsoft has developed a protocol for starting multiple Arm cores on a multi-processor UEFI platform. This protocol is required by Windows on Arm platforms that don't support the [Power State Coordination Interface (PSCI)](https://developer.arm.com/documentation/den0022/latest). Platforms that do support PSCI must not use this protocol. For more information about this protocol, see the [Multiprocessor startup on UEFI Arm-based platforms](https://cdrdv2.intel.com/v1/dl/getContent/772757) document on the ACPI Component Architecture (ACPICA) Web site.

## Platform setup requirements

The firmware is responsible for putting the system hardware into a well-defined state before handing-off to the OS loader. The following table defines the related platform setup requirements.

| Requirement | Description |
|--|--|
| Boot path | The firmware must initialize the platform to the point where Windows is able to access the boot device via UEFI and load the kernel. Any device involved in the hierarchy to read from the boot device must be clocked and powered at a reasonable rate, given performance and power considerations. The base processor core itself should also be clocked and powered at a reasonable rate, so that the system can boot in a timely manner without draining the battery. |
| Core system resources | The Core System Resources that are exposed to the OS through ACPI tables must be powered on and clocked. Core System Resources include Interrupt controllers, Timers and DMA controllers that must be managed by the OS. Additionally, interrupts must be masked by the call to ExitBootServices() until the associated device driver in the OS unmasks and re-enables interrupts on the device. If interrupts are enabled during boot services, it's assumed that the firmware manages them. |
| Debugging | Windows supports debugging via USB 3 Host (XHCI) , USB 2 Host (EHCI)1, IEEE 1394, serial and USB Function interfaces (as well as PCI ethernet adapters). At least one of these must be powered, clocked and initialized by the firmware before OS handoff. Whichever option is provided, it must have an exposed port for debugging purposes, and the controller must be memory-mapped, or be connected via a dedicated (non-shared) peripheral bus. |
| Other platform setup requirements | Any pin-multiplexing and pad configuration must be completed in the firmware prior to handing control to the OS loader. |

## Installation requirements

Windows requires the OS partition to reside on a GPT partitioned storage solution. MBR partitioned storage can be used as data storage. As defined in the UEFI specification, a UEFI platform requires a dedicated system partition. Windows requires this dedicated system partition, referred to as the EFI system partition (ESP).

## Hardware Security Test Interface (HSTI) requirement

The platform must implement the Hardware Security Test Interface, and the platform is required to share documentation and tools as specified in the [Hardware Security Testability Specification](/windows-hardware/test/hlk/testref/hardware-security-testability-specification).

## Related articles

[Minimum UEFI requirements for Windows on SoC platforms](minimum-uefi-requirements-for-windows-on-soc-platforms.md)  

[UEFI requirements for Windows 10 Mobile](uefi-requirements-specific-to-windows-mobile.md)  

[UEFI requirements for USB flashing support](uefi-requirements-for-usb-flashing-support.md)
