---
title: Share a driver with a partner
description: To share a driver with one of your partners, create a hardware submission and follow the steps in this article.
ms.topic: article
ms.date: 09/18/2024
---

# Share a driver with a partner

To share a driver with one of your partners, [create a hardware submission](hardware-submission-create.md) and follow the steps in this article.

> [!NOTE]
> Drivers can only be shared by the organization that originally created them. An organization that receives a shared driver cannot share it again.

## Share a driver

1. [Search the hardware submission](hardware-submissions-view.md) that contains the driver you want to share.

1. Go to the **Distribution** section of the hardware submission and select **New shipping label**.

   :::image type="content" source="images/publish-new-shipping-label.png" alt-text="Screenshot that shows new shipping label button.":::

1. On the shipping label page, go to the **Details** section and enter a name for the shipping label in the **Shipping label name** field. This name is private and isn't visible to your partner. The name allows you to organize and search for your shipping labels.

   :::image type="content" source="images/publish-label-name-share-new.png" alt-text="screenshot that shows label name and properties.":::

1. In the **Properties** section, complete the following information:

   | Field | Description |
   |--|--|
   | **Destination** | Select **Send to another Partner** to share your driver with a partner. If you want to create a shipping label for Windows Update, see [Publish a driver to Windows Update](publish-a-driver-to-windows-update.md). |
   | **Who is publishing?** | Search for the company name of your partner, and select it. |
   | **Required CHID targeting by receiver** | This option forces your partner to apply Computer Hardware IDs (CHIDs) to any publication requests they create based on your driver. This option allows you to protect your users when a Hardware ID might be shared among many partner companies. |

1. In the **Targeting** section, select the driver package that you want to share.

   :::image type="content" source="images/publish-targeting-new.png" alt-text="screenshot that shows publish targeting settings.":::

1. After you select your driver package, the **Select PNPs** grid becomes available. You can search for a specific hardware ID or operating system by using the search box above the list of hardware IDs. Your partner is limited to the hardware ID values you share for any publications they create.

   - To target all listed hardware IDs, select **Share All**.
   - To target specific hardware IDs, find each desired hardware ID and select **Share**.
   - If you targeted all hardware IDs and want to remove them, select **Revoke All**.
   - To remove targeting for specific hardware IDs, find each hardware ID and select **Revoke**.

1. Select **Publish** at the bottom to finalize the sharing of the driver. If you don't want to publish the shipping label right now, you can select **Save**. You can publish the shipping label later by either opening the shipping label and selecting **Publish**, or you can select **Publish all pending** from the hardware submission page. Selecting **Publish all pending** publishes all unpublished shipping labels.

## Revoke a hardware ID

Revoking a hardware ID from a shared shipping label does the following steps.

1. Deprecates the existing Submission ID on the receiver's end.

1. A new Private Product ID and Submission ID with the adjusted hardware IDs is shared with your partner. This new entity has the same Shared Product ID. If you selected **Revoke All**,  all hardware IDs are removed.

1. When your partner tries to create a **NEW** shipping label for Windows Update, their list of available hardware IDs reflect your changes, and only lists those hardware IDs shared by you. In the **Revoke All** case, their hardware ID grid would be empty.

> [!NOTE]
> If your partner has already published their shared shipping labels to Windows Update, revoking a hardware ID **does not remove** their existing item from the Windows Update Catalog. It remains published until that partner expires it.
>
> Existing shipping labels created by your partner are only allowed to expire content on a deprecated shipping label.
>
> The signed driver and DUA Shell packages from a deprecated shipping label can still be downloaded by your partner.
>
> Sharing and revoking a hardware ID does not modify your original INF.
