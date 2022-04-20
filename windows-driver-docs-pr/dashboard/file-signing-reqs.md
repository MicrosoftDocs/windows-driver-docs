---
title: LSA plugin or UEFI firmware signing requirements
description: LSA plugin or UEFI firmware signing requirements
ms.topic: article
ms.date: 04/19/2022
---

# LSA plugin or UEFI firmware signing requirements

You can use the Partner Center Hardware dashboard to digitally sign [Local Security Authority (LSA)](/windows-server/security/credentials-protection-and-management/configuring-additional-lsa-protection) plugins and [UEFI firmware](/windows-hardware/design/device-experiences/oem-uefi) binaries, to enable them to be installed on windows devices.

## LSA plugins and UEFI firmware

- LSA plugins and UEFI firmware signing requires an [extended validation (EV) code signing certificate](code-signing-req.md#ev-certificate-signed-drivers).
- All LSA and UEFI submissions must be a single, signed CAB library file, and contain all files required for signing.
- This file should contain no folders and only the binaries or .efi files to be signed.
- **UEFI FIRMWARE ONLY** - The CAB file signature must match the [Authenticode certificate](../install/authenticode.md) for your organization.
- Depending on your certificate provider, you may need to use [SignTool](/windows/desktop/SecCrypto/signtool) or an external process.
- EFI ByteCode (EBC) files must be compiled using the /ALIGN:32 flag for processing to succeed.
- **UEFI FIRMWARE ONLY** - If your submission is a shim, you must submit a completed template for review to the shim review board. The shim review process is described at [https://github.com/rhboot/shim-review/](https://github.com/rhboot/shim-review/).
- **LSA PLUGINS ONLY** - The CAB file signature must match the EV code signing certificate for your organization.

## Next Steps

To learn how to file sign an LSA plugin or UEFI firmware in the Hardware dashboard:
> [!div class="nextstepaction"]
>[File sign an LSA plugin or UEFI firmware](file-signing-lsa-uefi)

For more information on Microsoft UEFI signing policies and pre-submission testing see:

> [!div class="nextstepaction"]
> [Microsoft UEFI CA Signing Policy Updates](https://techcommunity.microsoft.com/t5/windows-hardware-certification/microsoft-uefi-ca-signing-policy-updates/ba-p/364828)

> [!div class="nextstepaction"]
>[Pre-Submission Testing for UEFI Submissions](https://techcommunity.microsoft.com/t5/windows-hardware-certification/pre-submission-testing-for-uefi-submissions/ba-p/364829)