---
title: LSA and UEFI file signing
description: LSA plug-in and UEFI firmware signing
ms.topic: article
ms.date: 10/17/2018
---

# File signing LSA plugins and UEFI firmware

Use the Partner Center to digitally sign [Local Security Authority (LSA)](/windows-server/security/credentials-protection-and-management/configuring-additional-lsa-protection) plugins and [UEFI firmware](/windows-hardware/design/device-experiences/oem-uefi) binaries, enabling them to be installed on windows devices.

> [!IMPORTANT]
> Use the file-signing technique described in this topic for **UEFI** and **LSA** signing.
> For information about **driver** signing, see [Hardware submissions](./hardware-certification-submissions.md).
>
> * File signing requires an [extended validation (EV) code signing certificate](get-a-code-signing-certificate.md).
> * All LSA and UEFI submissions must be a single, signed CAB library file, and contain all files required for signing.
>   * This file should contain no folders and only the binaries or .efi files to be signed.
> * **UEFI FIRMWARE ONLY** - The CAB file signature must match the [Authenticode certificate](../install/authenticode.md) for your organization.
>   * Depending on your certificate provider, you may need to use [SignTool](/windows/desktop/SecCrypto/signtool) or an external process.
>   * EFI ByteCode (EBC) files must be compiled using the /ALIGN:32 flag for processing to succeed.
> * **UEFI FIRMWARE ONLY** - If your submission is a shim, you must submit a completed template for review to the shim review board. The shim review process is described at [https://github.com/rhboot/shim-review/](https://github.com/rhboot/shim-review/).
> **LSA PLUGINS ONLY** - The CAB file signature must match the EV code signing certificate for your organization.

## Creating a new UEFI or LSA submission

1. Sign in to the dashboard with your Microsoft account and click **Hardware certification**.

2. On the **File Signing Services** page, click **Submit New UEFI** or **Submit New LSA**.
    > [!NOTE]
    > You may be prompted to sign a legal agreement before creating a new file signing submission. Review and complete the agreement to continue. Every organization only needs to sign the agreement once.

3. On the submission page, upload the CAB file you want to submit, and click **Submit**.

4. Once your submission has been processed, you’ll receive a notification with your submission ID.

## Managing your file signing submission

After signing in to the Partner Center, you can [manage your firmware submission](manage-your-hardware-submissions.md) like any other dashboard submission.

## Related topics

* [Microsoft UEFI CA Signing Policy Updates](https://techcommunity.microsoft.com/t5/windows-hardware-certification/microsoft-uefi-ca-signing-policy-updates/ba-p/364828)

* [Pre-Submission Testing for UEFI Submissions](https://techcommunity.microsoft.com/t5/windows-hardware-certification/pre-submission-testing-for-uefi-submissions/ba-p/364829)
