---
title: Driver flighting
description: Distribute your driver within defined Windows Insider rings. Driver flighting provides automatic monitoring and evaluation.
ms.date: 09/12/2024
ms.topic: article
---

# Driver flighting

Driver flighting in the Partner Center enables you to distribute your driver within defined Windows Insider rings, while providing automatic monitoring and evaluation. A report of your driver's performance will be generated after the completion of a flight, enabling you to evaluate its critical functionality and update scenarios. Upon a successful flight and approval from Microsoft, the driver is distributed publicly through Windows Update.

## Signing up for driver flighting

To sign up for driver flighting, submit a support ticket to the Partner Center. Support for the Partner Center is accessed in the upper-right corner of the browser window:

:::image type="content" source="images/support.jpg" alt-text="The button for accessing Partner Center Support.":::

> [!NOTE]
> When signing up for driver flighting, make sure you are inside the Partner Center. Clicking the support button from another area of the Partner Center will connect you with a non-dashboard support group.

Within the ticket, specify:

- The estimated number of existing devices that the driver targets
- The estimated volume of promotion requests you make per month
- Your seller and/or publisher ID

After you receive your support ticket, it might take up to five business days for you to receive a response.

Once your account is approved, your organization's administrators are able to configure users for flighting by going to the **Settings** page and selecting **Manage Users**. Make sure the appropriate users have at least one of the following roles selected:

- Shipping label owner
- Shipping label promoter

## How to promote a driver for driver flighting

After being submitted to the Partner Center, you can promote your drivers for flighting with the following steps:

1. Once your driver is submitted and in the **validation** stage of processing, create a new shipping label and fill out the **details** and **properties** sections. For more information, see [Publish a driver to Windows Update](./publish-a-driver-to-windows-update.md).

1. Select one or more driver promotion options to promote your driver for flighting, as described in this table:

   | Promotion Option | Description |
   |--|--|
   | Automatically deliver and install the driver during Windows Upgrade | Marks the driver for delivery via Dynamic Update, enabling it to be delivered to applicable machines during an operating system upgrade. |
   | Automatically deliver and install the driver on all applicable systems. | Marks the driver as a Critical Update (CU), enabling it to be automatically installed via Windows Update. |

1. Complete the other details required for promotion for flighting:

   1. The email address of the Microsoft sponsor you're working with for the promotion
   1. The business justification for promoting the publication request
   1. The process used to validate the quality of the driver
   1. Any OEMs affected by the driver publication

1. Select the appropriate statements that apply to your driver. These answers improve the speed of the evaluation process:

   :::image type="content" source="images/driver-flighting-statements.png" alt-text="An image showing the statements that might apply to a driver being flighted: it's a coengineering driver, it requires a reboot, it deploys UI and/or software, it supports a new or unreleased device, and so on.":::

   > [!IMPORTANT]
   > Please note the following:
   > - It is recommended to avoid requiring a reboot after driver installation.
   > - Drivers that deploy UI and/or software during installation are not Windows 10 in S mode compliant, and cannot be flighted to this operating system.
   > - A co-engineering driver is a driver being developed for an unreleased version of Windows. co-engineering drivers:
   >   - will only be distributed to applicable devices in the Microsoft insider program during the flighting process.
   >   - Will not be distributed to devices that are not a part of the Microsoft insider program after a successful flight.
   >   - will be terminated for flighting after 60 days. A flight bug report will be provided after the flighting process is complete.

1. Complete the shipping label process as usual.

After you promote your driver for shipping, Microsoft will evaluate your driver for approval, and provide a driver flighting report when the evaluation is complete – typically within two weeks from the time of shipping label publication. If a previously created shipping label is reused, its publication date isn't updated.

## Reasons a driver might be rejected

A driver could be rejected for several reasons. Most commonly, improper driver targeting causes rejection. For example:

- Targeting previous versions of Windows while also targeting Windows 10.
- Failing to follow targeting requirements for the device class. Some device classes, like firmware, require CHID. Other classes forbid the use of CHID, such as display. Be sure you enter your information correctly.
- Using hardware IDs that unintentionally targets other OEMs.

## Next Steps

> [!div class="nextstepaction"]
> [Create a hardware submission](hardware-submission-create.md)

> [!div class="nextstepaction"]
> [View hardware submissions](hardware-submissions-view.md)

> [!div class="nextstepaction"]
> [Update a hardware submission](hardware-submission-update.md)

> [!div class="nextstepaction"]
> [Windows HLK Getting Started Guide](/windows-hardware/test/hlk/getstarted/windows-hlk-getting-started)
