---
title: How to validate the Microsoft signature
description: How to validate the Microsoft signature
ms.topic: article
ms.date: 09/02/2022
---

# How to validate the Microsoft signature

This article shows you how to validate the Microsoft signature for a submission.

There are a couple cases where you might want to validate the Microsoft signature for a submission:

- You aren’t sure if a driver has been signed by Microsoft or not, and you want to check.
- You have two drivers, and you need to determine which one was signed by attestation and which one was signed after submission of HLK/HCK results to the dashboard.

## Prerequisites

This article assumes that you've already made a Hardware Lab Kit(HLK) dashboard submission for Windows 10 or earlier versions of Windows. For information on how to create dashboard submission, see [Create a new hardware submission](hardware-submission-create.md). Your submission contains the package files needed to determine whether or not the packages has a Microsoft signature.

## Step 1: Download signed driver files

In this step, you'll download the signed files you need to validate the Microsoft signature.

>[!NOTE]
>The driver submission folder is located in the package files. These files are signed by Microsoft. The partner doesn't have to sign the returned payload. Microsoft always returns a .cat file with an approved submission. If a partner includes its own .cat file. Microsoft discards it and returns its own signed .cat file.
>In the past, Microsoft only signed the .cat file. Starting with Windows 10, Microsoft now signs all of the portable executables in the returned payload. For example, the .dll file is also signed by Microsoft:

To download the driver signed files:

1. [Find the hardware submission](hardware-submissions-view.md) that contains the drivers that you want to download signed files for.
1. Select the Private Product ID to open the driver details.
1. On the driver details page, under **Packages and signing properties**, select **More**.
1. Select **Download signed files**.

## Step 2: Check the Enhanced Key Usage (EKU)

Now you that you've downloaded the signed files, you can validate the Microsoft signature by checking the EKU. The EKU belongs to the certificate that Microsoft uses to sign the submission. 

To check the EKU:

1. Select and hold (or right-click) the .cat file.

1. Select **Properties**, and then select the **Digital Signatures** tab.

1. Select the name of the certificate, and then select **Details**.

1. On the **Details** tab, select **Enhanced Key Usage**. There, you will see the EKUs and corresponding OID values for the certificate. In this case, the Windows Hardware Driver Verification OID ends with a 5, which means that driver hasn't been signed by attestation:

    :::image type="content" source="./images/code-signing-validate/certificate-details-tab-no-attestation.png" alt-text="Screenshot of EKU details pane for driver not signed for attestation. OID ends with 5.":::

1. If the driver had been signed by attestation, then the OID would end with a 1:

    :::image type="content" source="./images/code-signing-validate/certificate-details-tab-attestation.png" alt-text="Screenshot of EKU details pane for driver signed for attestation. OID ends with 1.":::