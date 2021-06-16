---
title: Publish a driver to Windows Update
description: To publish a driver to Windows Update, create a hardware submission and then follow the steps below.
ms.topic: article
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# Publish a driver to Windows Update


To publish a driver to Windows Update, [create a hardware submission](create-a-new-hardware-submission.md) and then follow the steps below.

1. [Find the hardware submission](manage-your-hardware-submissions.md) that contains the driver you want to distribute.

2. Go to the **Distribution** section of the hardware submission and select **New shipping label**.

   ![screenshot that shows new shipping label button.](images/publish-new-shipping-label.png)

3. On the shipping label page, go to the **Details** section and enter a name for the shipping label in the **Shipping label name** field. This name allows you to organize and search for your shipping labels.

4. In the **Properties** section, complete the following information:

|Field|Description|
|--- |--- |
|**Destination**|Select **Publish to Windows Update** to publish your driver to Windows Update. If you want to create a shared shipping label that allows you to share your driver with a partner, see [Share a driver with a partner](sharing-drivers-with-your-partners.md). **Note** Shared drivers can only be shared by the organization that originally created it. An organization that receives a shared driver cannot share it again.|
|**Specify the partner (if any) that is allowed visibility into this request**|Enter a partner that you want to have read-only permissions to your driver and shipping label. Use this field when you want a partner to be aware of this shipping label request, such as when you publish a driver on their behalf. For more information, see [Publish a driver on behalf of a partner](/previous-versions/mt786462(v=vs.85)).|
|**Driver Delivery Options**|When the destination is Windows Update, the default is **Automatic**, which means that the driver is delivered automatically on upgrades and for every applicable system. If you select only the **Automatically delivered during Windows Upgrades** the driver is defined as a Dynamic Driver and is delivered only during OS upgrades. If you select only **Automatically delivered to all applicable systems**, Windows Update delivers the driver immediately to all applicable systems once it is released.<br/><br/>If you select **Manual** in Windows 10, version 1909 or earlier, the driver is automatically delivered only if the device does not have a driver installed already or only has a generic driver.<br/><br/>Starting in Windows 10, version 2004, drivers with a **Manual** shipping label is not automatically delivered. To access the best matching **Optional/Manual** driver, the user must go to **Settings > Update & Security > Windows Update > View optional updates > Driver updates**.|

![screenshot that shows label name and publishing properties.](images/label-name-and-properties-windows-update.png)

5. In the **Targeting** section, select the driver package that you want to publish.

6. After you select your driver package, **Select PNPs** becomes available. Select the hardware IDs you want to target. You can search for a specific hardware ID or operating system by using the search boxes above the list of hardware IDs.

   To target all listed hardware IDs, select **Publish All**.

   To target specific hardware IDs, find each desired hardware ID and select **Publish**.

   If you targeted all hardware IDs and want to remove them, select **Expire All**.

   To remove targeting for specific hardware IDs, find each hardware ID and select **Expire**.

   ![screenshot that shows targeting section and pnps.](images/publish-targeting-windows-update.png)

7. If you want to add Computer Hardware IDs (CHIDs), enter each CHID into the text box and select **Add CHID(s)**. To bulk add multiple CHIDs, ensure that each CHID is separated by a newline, select **Add multiple CHIDs**, and paste your CHIDs into the text box. You can view all added CHIDs in the list below the text box. To remove a CHID from the list, select **Remove**

>[!IMPORTANT]
> CHIDs are not supported for the following versions of windows:
> * Windows 8.1 or earlier
> * Windows Server 2012 R2 or earlier
>
> If your driver targets either of these operating systems, create two shipping labels: one for Windows 10 (where you can add CHIDs) and one for down-level operating systems (where no CHIDs will be added).



8. If you wish to limit public disclosure of your Shipping Label in the Windows Update Catalog and WSUS Catalog, check the **Limit Public Disclosure of this Shipping Label information.** box.  

   ![screenshot that shows limit public disclosure.](images/limit-public-disclosure.PNG)

   Your driver will still be published and downloadable from Windows Update but will not show up in either of the public catalog lists.

9. If your driver targets Windows 10 in S mode, you must select both boxes, confirming the following:

   * Your driver is compatible with and follows the driver policies outlined in the [Windows 10 in S mode Driver Requirements](../install/windows10sdriverrequirements.md).
   * You verify that your driver follows the additional code integrity policies outlined in the Windows 10 in S mode guidelines.
   * Your driver does not contain any non-Microsoft UI components or applications in the driver package.

   ![A screenshot of the two checkboxes you must select when submitting a driver for Windows 10 S.](images/win-cloud-checkboxes.png)

10. Select **Publish** to send your request to Windows Update. If you do not want to publish the shipping label right now, you can select **Save**. You can publish the shipping label later by either opening the shipping label and selecting **Publish**, or you can select **Publish all pending** from the hardware submission page. Note that selecting **Publish all pending** will publish all unpublished shipping labels.

