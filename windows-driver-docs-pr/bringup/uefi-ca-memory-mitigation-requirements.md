---
title: UEFI CA Memory Mitigation Requirements for Signing
description: Provides background and guidance on the signing requirements for UEFI memory mitigations.
ms.date: 12/05/2022
---

# UEFI memory mitigations

The Microsoft 3rd Party UEFI Certificate Authority (CA) requirements are being updated to mandate that UEFI images
include memory mitigations - these changes will be reflected in [UEFI Signing Requirements - Microsoft Tech Community](https://techcommunity.microsoft.com/t5/hardware-dev-center/updated-uefi-signing-requirements/ba-p/1062916).

The [Cybersecurity & Infrastructure Security Agency](https://static.rainfocus.com/rsac/us21/sess/1602603692582001zuMc/finalwebsite/2021_US21_TECH-W13_01_DHS-CISA-Strategy-to-Fix-Vulnerabilities-Below-the-OS-Among-Worst-Offenders_1620749389851001CH5E.pdf)
recently found that firmware vulnerabilities, as a whole, continue to rise. Meanwhile, firmware mitigation techniques
being deployed are insufficient to prevent modern attacks and mitigations aren't being applied uniformly across vendor
firmware implementations.

These findings are consistent with calls to action from the [Tianocore community](https://edk2-docs.gitbook.io/a-tour-beyond-bios-memory-protection-in-uefi-bios/memory-protection-in-uefi#call-for-action), the
[security research community](https://i.blackhat.com/USA21/Wednesday-Handouts/us-21-Safeguarding-UEFI-Ecosystem-Firmware-Supply-Chain-Is-Hardcoded.pdf),
and the [UEFI community](https://uefi.org/sites/default/files/resources/UEFI_Plugfest_May_2015%20Firmware%20-%20Securing%20SMM.pdf).
A baseline of fundamental mitigation techniques are needed across the ecosystem to improve the platform security
of Windows devices.

To realize this goal, Microsoft is introducing the following Microsoft 3rd Party UEFI CA signing requirements.

## Memory mitigation signing requirements

### PE/COFF metadata

1. Section Alignment of the submitted PE file must be aligned with page size. This must be 4 KB, or a larger power
   of 2 (for example, 64 KB).

1. Section Flags must not combine `IMAGE_SCN_MEM_WRITE` and `IMAGE_SCN_MEM_EXECUTE` for any given section.

### If-implemented: PE/COFF DLL attestation

- DLL Characteristics must include `IMAGE_DLLCHARACTERISTICS_NX_COMPAT`

Since No Execute (NX) compliance can't be detected statically, firmware that sets `IMAGE_DLLCHARACTERISTICS_NX_COMPAT`
should follow these steps to ensure that the firmware image can operate correctly with NX protections applied.

1. The code module must not execute self-modifying code; meaning that the code sections of the application must not have
   the write attribute. Any attempt to change values within the memory range will cause an execution fault.

1. If the code module attempts to load any internal code into memory for execution, or if it provides support for
   an external loader, then it must use the `EFI_MEMORY_ATTRIBUTE_PROTOCOL` appropriately.  This optional protocol
   allows the caller to get, set, and clear the read, write, and execute attributes of a well-defined memory range.

   - Internal code loaded into memory must maintain `WRITE` and `EXECUTE` exclusivity. The attributes must also be
     changed after loading the code to allow execution.
   - External loaders must support `EFI_MEMORY_ATTRIBUTE_PROTOCOL` if available on the system. The loader must not
     assume newly allocated memory allows code execution (even of code types).

1. The application must not assume all memory ranges are valid; specifically, page 0 (typically at physical address
   0 to 4 KB).

1. Stack space can't be used for code execution.

A [PE/COFF Image Validation Tool](https://github.com/tianocore/edk2-pytool-extensions/blob/master/docs/user/tools/using_image_validation_tool.md) is available to test that an image meets the metadata requirements (static image PE/COFF requirements) for setting
the DLL Characteristic bit.

## Application of memory mitigation requirements

Image section alignment enables the UEFI/Platform Initialization (PI) firmware environment to protect the section with
page table attributes. In addition, firmware components should assume page table attributes will be applied to a
firmware image to enable the following features:

- No Execute (NX) memory protection - Any non-code sections will be marked as NX and code sections will be
  marked read-only (RO) to prevent execution outside code sections and overwriting of code sections.

- Page guards - A guard page may be added before and after the corresponding page allocated. Any attempt to access
  the guard page will result in a page fault (#PF).

- Pool guards - A head guard page and a tail guard page will be placed before and after the portion of memory, which the
  allocated pool occupies. It's recommended that vendor firmware tests for both underflow (using a head guard page)
  and overflow (using a tail guard page).

- CPU stack guard - A guard page is set to Not Present in the page table and placed onto the bottom of the stack to
  detect stack overflow.

- Null pointer protection - No accesses to the first page (at address zero). While legacy BIOS implementations placed
  the Interrupt Vector Table (IVT) at this location, UEFI firmware should expect that this page is marked as Not Present
  to catch null pointer dereferences.

## File alignment vs section alignment

Linkers such as [MSVC](/cpp/build/reference/linker-options), typically offer
several alignment options. For example, in MSVC, `/FILEALIGN` affects alignment within the binary file layout that
can have a relatively larger impact on the overall file size. `/ALIGN` controls how various sections will be aligned
in memory once loaded. This section alignment (`/ALIGN`) is what is important for these changes.

## Backward compatibility

A platform firmware can preserve backward compatibility while attempting to enable `IMAGE_DLLCHARACTERISTICS_NX_COMPAT`
by restoring RWX memory allocations when a module is loaded that doesn't have the `IMAGE_DLLCHARACTERISTICS_NX_COMPAT`
bit set. It's expected that this policy will be removed over time ecosystem adopts this change.

## Related resources

[/ALIGN (section alignment)](/cpp/build/reference/align-section-alignment)

[/FILEALIGN (align sections in files)](/cpp/build/reference/filealign)

[A tour beyond BIOS - Memory protection in UEFI BIOS](https://edk2-docs.gitbook.io/a-tour-beyond-bios-memory-protection-in-uefi-bios/)

[DHS CISA strategy to fix vulnerabilities below the OS among worst offenders](https://static.rainfocus.com/rsac/us21/sess/1602603692582001zuMc/finalwebsite/2021_US21_TECH-W13_01_DHS-CISA-Strategy-to-Fix-Vulnerabilities-Below-the-OS-Among-Worst-Offenders_1620749389851001CH5E.pdf)

[Project Mu: Memory Protections Feature](https://github.com/microsoft/mu_basecore/blob/release/202202/Docs/feature_memory_protection.md)

[PE/COFF image validation tool](https://github.com/tianocore/edk2-pytool-extensions/blob/master/docs/user/tools/using_image_validation_tool.md)

[Safeguarding UEFI ecosystem: Firmware supply chain is hard(coded)](https://i.blackhat.com/USA21/Wednesday-Handouts/us-21-Safeguarding-UEFI-Ecosystem-Firmware-Supply-Chain-Is-Hardcoded.pdf)

[UEFI firmware - Securing SMM](https://uefi.org/sites/default/files/resources/UEFI_Plugfest_May_2015%20Firmware%20-%20Securing%20SMM.pdf)

[UEFI signing requirements - Microsoft Tech Community](https://techcommunity.microsoft.com/t5/hardware-dev-center/updated-uefi-signing-requirements/ba-p/1062916)
