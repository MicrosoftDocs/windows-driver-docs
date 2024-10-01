---
title: Publish a driver to Windows Update
description: To publish a driver to Windows Update, create a hardware submission and follow these steps.
ms.topic: article
ms.date: 09/11/2024
---

# Publish a driver to Windows Update

To publish a driver to Windows Update:

1. [Create a hardware submission](hardware-submission-create.md).

1. [Search for the hardware submission](hardware-submissions-view.md) that contains the driver you want to distribute.

1. Go to the **Distribution** section of the hardware submission and select **New shipping label**.

   ![screenshot that shows new shipping label button.](images/publish-new-shipping-label.png)

1. On the shipping label page, go to the **Details** section and enter a name for the shipping label in the **Shipping label name** field. This name allows you to organize and search for your shipping labels.

1. In the **Properties** section, complete the following information:

| Field | Description |
|--|--|
| **Destination** | Select **Publish to Windows Update** to publish your driver to Windows Update. If you want to create a shared shipping label that allows you to share your driver with a partner, see [Share a driver with a partner](sharing-drivers-with-your-partners.md). **Note** Shared drivers can only be shared by the organization that originally created it. An organization that receives a shared driver can't share it again. |
| **Specify any partner that is allowed visibility into this request** | Enter a partner that you want to have read-only permissions to your driver and shipping label. Use this field when you want a partner to be aware of this shipping label request, such as when you publish a driver on their behalf. |
| **Driver Delivery Options** | When the destination is Windows Update, the default is **Automatic**, which means that the driver is delivered automatically on upgrades and for every applicable system. If you select only the **Automatically delivered during Windows Upgrades**, the driver is defined as a Dynamic Driver and is delivered only during OS upgrades. If you select only **Automatically delivered to all applicable systems**, Windows Update delivers the driver immediately to all applicable systems once it's released.<br/><br/>If you select **Manual** in Windows 10, version 1909 or earlier, the driver is automatically delivered only if the device doesn't have a driver installed already or only has a generic driver.<br/><br/>Starting in Windows 10, version 2004, drivers with a **Manual** shipping label isn't automatically delivered. To access the best matching **Optional/Manual** driver, the user must go to **Settings > Update & Security > Windows Update > View optional updates > Driver updates**. |

:::image type="content" source="images/label-name-and-properties-windows-update.png" alt-text="Screenshot that shows label name and publishing properties.":::

1. In the **Targeting** section, select the driver package that you want to publish.

1. After you select your driver package, **Select PNPs** becomes available. Select the hardware IDs you want to target. You can search for a specific hardware ID or operating system by using the search boxes above the list of hardware IDs.

   To target all listed hardware IDs, select **Publish All**.

   To target specific hardware IDs, find each desired hardware ID and select **Publish**.

   If you targeted all hardware IDs and want to remove them, select **Expire All**.

   To remove targeting for specific hardware IDs, find each hardware ID and select **Expire**.

      :::image type="content" source="images/publish-targeting-windows-update.png" alt-text="Screenshot that shows targeting section and pnps.":::

1. If you want to add Computer Hardware IDs (CHIDs), enter each CHID into the text box and select **Add CHID(s)**. To bulk add multiple CHIDs, ensure that each CHID is separated by a newline, select **Add multiple CHIDs**, and paste your CHIDs into the text box. You can view all added CHIDs in the list below the text box. To remove a CHID from the list, select **Remove**

1. If you wish to limit public disclosure of your Shipping Label in the Windows Update Catalog and Windows Server Update Services (WSUS) Catalog, check the **Limit Public Disclosure of this Shipping Label information.** box.  

      :::image type="content" source="images/limit-public-disclosure.png" alt-text="Screenshot that shows limit public disclosure.":::

   Your driver is still published and downloadable from Windows Update but it doesn't show up in either of the public catalog lists.

1. If your driver targets Windows 10 in S mode, you must select both boxes, confirming:

   - Your driver is compatible with and follows the driver policies outlined in the [Windows 10 in S mode Driver Requirements](../install/windows10sdriverrequirements.md).
   - You verify that your driver follows the extra code integrity policies outlined in the Windows 10 in S mode guidelines.
   - Your driver doesn't contain any non-Microsoft UI components or applications in the driver package.

      :::image type="content" source="images/win-cloud-checkboxes.png" alt-text="A screenshot of the two checkboxes you must select when submitting a driver for Windows 10 S.":::

1. Select **Publish** to send your request to Windows Update. If you don't want to publish the shipping label right now, you can select **Save**. You can publish the shipping label later by either opening the shipping label and selecting **Publish**, or you can select **Publish all pending** from the hardware submission page. Selecting **Publish all pending** publishes all unpublished shipping labels.
