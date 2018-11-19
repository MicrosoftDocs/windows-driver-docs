---
title: Windows Hardware Dev Center Dashboard ID Definitions
description: Windows Hardware Dev Center Dashboard ID Definitions
ms.topic: article 
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# Dashboard ID definitions

This topic defines the identification numbers associated with Windows Hardware Dev Center Dashboard submissions.

Within the Windows Hardware Dev Center, each driver submission is associated with three IDs: A private, shared and submission ID. The relation between these three IDs is illustrated below:

![screenshot that shows the relationship of the three ID types](images/id_relationship.png)

The Windows Hardware Dev Center Dashboard lists each of these IDs on the driver details page of your products:

![screenshot that shows the relationship of the three ID types](images/id_driver_details.png)

## ID definitions

<table>
<thead>
<tr class="header">
<th>ID Name</th>
<th>Description</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><p>Shared product ID</p></td>
<td><p>This identifier is shared across all accounts who have access to a driver. The Shared product ID allows you to easily communicate about specific submissions and track submission updates across multiple organizations. In most cases, this is the ID you will want to track and share with others.</p></td>
</tr>
<tr class="even">
<td><p>Private Product ID</p></td>
<td><p>The private product ID is the top level identifier that is generated with each new product creation. This ID is most useful for personal reference of specific products, and predicting their URLs.
&gt; [!NOTE]
&gt; when you share a driver with someone else, they will be assigned a new private product ID. If you want to communicate about a product, use the Shared Product ID.
</p>

</td>
</tr>
<tr class="odd">
<td><p>Submission ID</p></td>
<td><p>This identifier represents the individual packages you upload to a Product. The initial submission, and all submission updates each have a unique identifier. This ID is most useful for tracking updates using the Driver Update Acceptable (DUA) process within a product. See <a href="https://msdn.microsoft.com/windows/hardware/drivers/dashboard/manage-your-hardware-submissions" data-raw-source="[Manage your hardware submissions](https://msdn.microsoft.com/windows/hardware/drivers/dashboard/manage-your-hardware-submissions)">Manage your hardware submissions</a> for more details. </p></td>
</tr>
</tbody>
</table>

Shipping labels also contain two additional IDs:

ID Name | Description
--- | ---
Shipping Label ID | This identifier is used for internal tracking, and is assigned to any shipping labels that are assigned to a product. In most cases, you will not need to know the Shipping Label ID.
Promotion Request ID | If your Shipping Label requires a manual review from Microsoft, it will be given a Promotion Request ID. This represents your unique shipping label in the Driver Shiproom. You should include this Id in any support inquiry.

## <span id="related_topics"></span>Related topics

- [Manage your hardware submissions](https://msdn.microsoft.com/windows/hardware/drivers/dashboard/manage-your-hardware-submissions)

- [Manage driver distribution with shipping labels](https://msdn.microsoft.com/windows/hardware/drivers/dashboard/manage-driver-distribution-by-submission)
