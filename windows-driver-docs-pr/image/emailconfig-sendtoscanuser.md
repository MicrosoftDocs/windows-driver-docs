---
title: EmailConfig.SendToScanUser
description: EmailConfig.SendToScanUser
ms.assetid: fa6dca60-0615-49fe-811a-fdd8aed16bbc
keywords: ["EmailConfig.SendToScanUser"]
ms.author: windowsdriverdev
ms.date: 11/28/2017
ms.topic: article
ms.prod: windows-hardware
ms.technology: windows-devices
ms.localizationpriority: medium
---

# EmailConfig.SendToScanUser


The **SendToScanUser** element contains a Boolean value that indicates whether the scanned images should be sent through an email to the user who initiated the PostScan job. The value **true** indicates the email address of the user who submitted the PostScan job should be added to the list of destination email addresses. The value **false** indicates the list of destination email addresses should not be changed.

The **SendToScanUser** element is an optional child element of an **EmailConfig** element. By default if the **SendToScanUser** element is omitted the list of destination email addresses should not be changed.

This element has no sub-elements.

 

 





