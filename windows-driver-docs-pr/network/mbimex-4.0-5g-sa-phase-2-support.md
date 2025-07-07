---
title: MBIMEx 4.0 – 5G SA Phase 2 Support
description: MBIMEx 4.0 5G SA Phase 2 supports end-to-end URSP handling and multiple concurrent eMBB network slices. Learn how these features enhance Windows 11 cellular connectivity. 
keywords:
- MBIMEx 4.0 – 5G SA Phase 2 support
ms.date: 05/23/2025
ms.custom: UpdateFrequency3
---

# MBIMEx 4.0 – 5G SA Phase 2 support

> [!NOTE]
> The release of MBIMEx 4.0, which includes 5G network slicing using URSP rules on Windows laptops, is still on hold. This hold also applies to IHV, OEM, and other partner testing involving the special capability mentioned in Microsoft documentation. We welcome signals, use cases, and opportunities from our partners and keep reevaluating this decision.

Windows 11, version 22H2 introduces the MBIMEx 4.0 – 5G SA Phase 2 feature set, supporting end-to-end URSP handling and multiple concurrent eMBB network slices. This article explains these new capabilities and their benefits for Windows 11 cellular connectivity.

MBIM Extensions Release number 4.0 adds support for 5G SA Phase 2 features. This release is commonly called MBIMEx 4.0. URSP handling and multiple concurrent eMBB network slices are the main additions in MBIMEx 4.0. All valid slice types (SST) are supported at the MBIM interface level in MBIMEx 4.0, but non-eMBB slice functionality isn't included in Windows 11, version 22H2 and depends on additional host and device-level support and features. [Download the MBIMEx 4.0 specification here](https://download.microsoft.com/download/d/8/a/d8ad97b9-83bd-4ab2-bcea-7500dfaf22b4/MBIMEx%204.0%20spec%20and%20Errata%20to%20MBIMEx%203.0%20Rev%201.46%2020220426.docx). Section 4 “MBIM Interface Extensions for 5G NGC – Phase 2” contains the MBIMEx 4.0 specification.

## New CIDs in MBIMEx 4.0

:::image type="content" source="images/MBIMEx-4.0-new-CIDs.png" alt-text="Screenshot of a table that shows new CIDs added in MBIMEx 4.0.":::

## Modified CIDs in MBIMEx 4.0

:::image type="content" source="images/MBIMEx-4.0-modified-CIDs.png" alt-text="Screenshot of a table that shows modified CIDs in MBIMEx 4.0.":::

By default, Windows 11, version 22H2 announces MBIMEx 3.0 as the highest supported MBIMEx version for the host.
