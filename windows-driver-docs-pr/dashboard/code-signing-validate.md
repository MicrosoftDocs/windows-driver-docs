---
title: Validate the Microsoft Signature
description: This article shows you how to validate the Microsoft signature for a submission.
ms.date: 09/12/2024
ms.topic: how-to
ms.custom: sfi-image-nochange
---

# Validate the Microsoft signature

This article shows you how to validate the Microsoft signature for a submission.

There are a couple cases where you might want to validate the Microsoft signature for a submission:

- You aren't sure if a driver is Microsoft signed or not, and you want to check.

- You have two drivers. You need to determine which one is attestation signed. The other driver is signed after submission of Windows Hardware Lab Kit (HLK) or Windows Hardware Certification Kit (HCK) results to the dashboard.

## Download signed driver files

The first step is to download the signed files that you need to validate the Microsoft signature.

> [!NOTE]
> The driver submission folder is located in the package files. Microsoft signs these files. The partner doesn't have to sign the returned payload. Microsoft always returns a .cat file with an approved submission. If a partner includes its own .cat file, Microsoft discards it and returns its own signed .cat file.

To download the driver signed files:

1. [Find the hardware submission](hardware-submissions-view.md) that contains the drivers for which you want to download signed files.

1. To open the driver details, select the **Private Product ID**.

1. On the driver details page, under **Packages and signing properties**, select **More**.

1. Select **Download signed files**.

## Check the Enhanced Key Usage (EKU)

After you download the signed files, you validate the Microsoft signature by checking the Enhanced Key Usage (EKU) extension. The EKU belongs to the certificate that Microsoft uses to sign the submission.

To check the EKU:

1. Right-click the .cat file.

1. Select **Properties**, and then select the **Digital Signatures** tab.

1. Select the name of the certificate, and then select **Details**.

1. On the **Details** tab, select **Enhanced Key Usage**. There, see the EKUs and corresponding object identifier (OID) values for the certificate. In this case, the Windows Hardware Driver Verification OID ends with a 5, which means that driver isn't attestation signed.

    :::image type="content" source="./images/code-signing-validate/certificate-details-tab-no-attestation.png" alt-text="Screenshot of EKU details pane for driver not signed for attestation. OID ends with 5.":::

1. If the driver is attestation signed, the OID ends with a 1.

    :::image type="content" source="./images/code-signing-validate/certificate-details-tab-attestation.png" alt-text="Screenshot of EKU details pane for driver signed for attestation. OID ends with 1.":::
